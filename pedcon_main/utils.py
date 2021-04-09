""" django file imports:"""
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template # for "render_to_pdf" function
from django.core.mail import EmailMessage # for sending email of PDFs
from django.conf import settings # for sending email of PDFs
from django.http import Http404 # allows me to force 404 page when needed
from io import BytesIO 
from base64 import b64decode # allows decoding of encoded items
from django.core.files import File # for saving signature images
import re # for regular expressions

# 3rd party imports
from django.contrib.gis.geoip2 import GeoIP2
from xhtml2pdf import pisa
from user_agents import parse

# my file imports
from .models import *

# gets ip of user 
def get_ip(request):
    address = request.META.get("HTTP_X_FORWARDED_FOR")
    if address:
        ip = address.split(',')[-1].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip

# gets browser info of user
def get_device_info(request):
    info = request.META.get("HTTP_USER_AGENT")
    user_agent = parse(info)
    return user_agent

# gets country of user
def get_country(request):
    g = GeoIP2()
    try:
        # use below line of code for production
        country = g.country_name(get_ip(request))
        # country = g.country_name('2.63.235.215') # Russia
        # country = g.country_name('3.99.25.5') # Canada
        # country = g.country_name('2.56.114.0') # United States
        return country
    except: 
        country = "n/a"
        return country

# renders pdf
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding='UTF-8')
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

# Mixin for processing each form
class ProcessFormMixin:
    form_class = None
    initial = None
    template_name = None
    to_url = None

    # get request for blank form
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    # post request for complted form
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.cleaned_data
            new_form = form.save()
            pk_value = new_form.pk
            # sets session to "form-submitted" in this view. To be processed in the view below
            request.session['form-submitted'] = True
            return HttpResponseRedirect(f'{self.to_url}{pk_value}')
        return render(request, self.template_name, {'form': form})


"""It's possible that this "CreatePdfMixin" is doing too much and needs to be broken up. Works fine as-is for now."""
""" Mixin for creating PDF and saving object info to database. Also processes signature images. DON'T BE TEMPTED TO EXCLUDE THIS MIXIN IN VIEWS. VERY IMPORTANT FOR SAVING DATA! """
class CreatePdfMixin:
    model = None
    template = None

    def get(self, request, pk, *args, **kwargs):

        # If form has been submitted, run below code. If not, raise 404
        if "form-submitted" in request.session:
            # deletes "form-submitted" in request.session to prevent manual url access to "pdf_view" url
            del request.session["form-submitted"]

            # gets object model from specified model name in view and model object from form submission based on pk value
            obj = get_object_or_404(self.model, pk=pk)

            obj.ip_address = get_ip(request)
            obj.device_info = get_device_info(request)
            obj.country = get_country(request)

            # if form has signature field, process signature image
            if hasattr(obj, "sig_data_URL"):
                # takes image string, splits header and string, decodes string, reads sting, writes to file 
                img_string = obj.sig_data_URL
                header, encoded = img_string.split(",", 1)
                d = b64decode(encoded)

                from urllib import request
                with request.urlopen(img_string) as response:
                    d = response.read()

                """try to get 'client_last_name'. if exception, get 'first_name',  
                'last_name' in Hipaa form"""
                try:
                    file_name = f'{obj.client_last_name.lower()}_{obj.client_first_name.lower()}_sig_pf_{pk}.png'
                # only Hipaa form has first_name and last_name, so I know the exception will work for that form
                except:
                    file_name = f'{obj.last_name.lower()}_{obj.first_name.lower()}_sig_pf_{pk}.png'

                obj.filename = file_name.replace("'","").replace(" ","_")
                with open(file_name, "wb") as f:
                    f.write(d)

                # saves image to "sig_img" model variable
                obj.sig_img.save(file_name, File(open(file_name, 'rb')))

                # save all above info in database
                obj.save()

                # delete image from root directory
                if os.path.exists(file_name):
                    os.remove(file_name)
            else: 
                pass

            # save all above info in database
            obj.save()

            # creates title for form
            unfinished_title = f"{obj.__class__.__name__} Form"
            # replaces "Hx" in Speech Language History form with "history" in title
            if "Hx" in unfinished_title:
                unfinished_title = unfinished_title.replace("Hx", "History")

            # keeps "information" in title of 'ClientInformation' and
            # 'ReleaseOfInformation' form, else removes "information" in title
            if obj.__class__.__name__ == 'ClientInformation' or  obj.__class__.__name__ == 'ReleaseOfInformation':
                # regex creates space before the second capitalized letter in 
                # object name for use in PDF title
                almost_finished_title = re.sub(r"(\w)([A-Z])", r"\1 \2", unfinished_title)
                finished_title = almost_finished_title
            else:
                almost_finished_title = unfinished_title.replace("Information", "")
                finished_title = re.sub(r"(\w)([A-Z])", r"\1 \2", almost_finished_title)

            data = {
                'form_title': finished_title,
                'object': obj,
            }

            pdf = render_to_pdf(self.template, data)
            pdf_file = pdf.getvalue()

            if pdf:

                response = HttpResponse(pdf, content_type="application/pdf")

                # names pdf file 
                pdf_name = f'{data["form_title"].lower().replace(" ","_")}_'\
                        f'{pk}.pdf'
                content = f'inline; filename={pdf_name}'
                response['Content-Disposition'] = content

                return super(CreatePdfMixin, self).get(request, pk, *args, **kwargs)

                # uncomment line below to render pdf on screen and comment line above to make it work
                # return response

        else:
            # raises 404 error if someone tries to access a pdf_view after form submission
            raise Http404('Page not found')

        return HttpResponseRedirect("/forms")

# Emails pdf of submitted form 
class EmailPdfMixin:
    model = None
    template = None

    def get(self, request, pk, *args, **kwargs):
        obj = get_object_or_404(self.model, pk=pk)

        # creates title for form
        unfinished_title = f"{obj.__class__.__name__} Form"
        # replaces "Hx" in Speech Language History form with "history" in title
        if "Hx" in unfinished_title:
            unfinished_title = unfinished_title.replace("Hx", "History")

        # keeps "information" in title of 'ClientInformation' and
        # 'ReleaseOfInformation' form, else removes "information" in title
        if obj.__class__.__name__ == 'ClientInformation' or  obj.__class__.__name__ == 'ReleaseOfInformation':
            # regex creates space before the second capitalized letter in 
            # object name for use in PDF title
            almost_finished_title = re.sub(r"(\w)([A-Z])", r"\1 \2", unfinished_title)
            finished_title = almost_finished_title
        else:
            almost_finished_title = unfinished_title.replace("Information", "")
            finished_title = re.sub(r"(\w)([A-Z])", r"\1 \2", almost_finished_title)

        data = {
            'form_title': finished_title,
            'object': obj,
        }

        pdf = render_to_pdf(self.template, data)
        pdf_file = pdf.getvalue()

        # names pdf file for email 
        email_filename = f'{data["form_title"].lower().replace(" ","_")}_{pk}.pdf'

        # send email of pdf 
        subject = f'New {data["form_title"]} Submission'
        message = f'See attached file: \n\n'
        recipients = ['info@pediatricconnectionsot.com',]
        # recipients = ['gmlesher@gmail.com',]
        email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, recipients)
        email.attach(email_filename, pdf_file, 'application/pdf')
        email.send(fail_silently=True)

        '''Use below code for sending to multiple recipients with sendgrid 
        unless sendgrid has a better solution'''
        # recipients = ['info@pediatricconnectionsot.com', 'glesher@garrettlesher.com',]
        # Bcc not supported by sendgrid. Workaround is to loop through
        # list of recipients and send them an individual email
        # for recipient in recipients:
        #     email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [recipient])
        #     email.attach(email_filename, pdf_file, 'application/pdf')
        #     email.send(fail_silently=True)

        # takes user to success page after form has been emailed 
        return HttpResponseRedirect("/success")

