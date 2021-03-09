""" django file imports:"""
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core import validators
from django.core.mail import EmailMessage # for sending email in contact page
from django.conf import settings # for sending email in contact page
from django.http import Http404 # allows me to force 404 page when needed
from django.views.generic import View # for class based views 

""" my file imports: """
from .forms import *
from .models import *
from .utils import *


# # Practice form processing (see .utils for Mixin)
# class PracticeFormView(ProcessFormMixin, View):
#     form_class = PracticeForm
#     initial = {'key': 'value'}
#     template_name = 'pedcon_main/practice_form.html'
#     to_url = '/pdf_view/'

# # renders practice information to PDF & sends email of PDF
# class ViewPDF(CreatePdfMixin, EmailPdfMixin, View):
#     model = PracticeInformation
#     template = 'pedcon_main/practice_pdf_template.html'




# Client info form processing (see .utils for Mixin)
class CIFormView(ProcessFormMixin, View):
    form_class = ClientInformationForm
    initial = {'key': 'value'}
    template_name = 'pedcon_main/ci_form.html'
    to_url = '/ci_pdf_view/'

# renders client information to PDF & sends email of PDF
class ViewCIPDF(CreatePdfMixin, EmailPdfMixin, View):
    model = ClientInformation
    template = 'pedcon_main/client_info_pdf_template.html'




# Payment policy form processing (see .utils for Mixin)
class PaymentPolicyFormView(ProcessFormMixin, View):
    form_class = PaymentPolicyForm
    initial = {'key': 'value'}
    template_name = 'pedcon_main/pp_form.html'
    to_url = '/pp_pdf_view/'

# renders payment policy information to PDF & sends email of PDF
class ViewPPPDF(CreatePdfMixin, EmailPdfMixin, View):
    model = PaymentPolicyInformation
    template = 'pedcon_main/payment_policy_pdf_template.html'




# Cancellation policy form processing (see .utils for Mixin)
class CancellationPolicyFormView(ProcessFormMixin, View):
    form_class = CancellationPolicyForm
    initial = {'key': 'value'}
    template_name = 'pedcon_main/can_pol_form.html'
    to_url = '/cancel_pdf_view/'

# renders cancellation policy information to PDF & sends email of PDF
class ViewCancelPDF(CreatePdfMixin, EmailPdfMixin, View):
    model = CancellationPolicyInformation
    template = 'pedcon_main/cancellation_pdf_template.html'




# Pediatric history form processing (see .utils for Mixin)
class PediatricHxFormView(ProcessFormMixin, View):
    form_class = PedHxForm
    initial = {'key': 'value'}
    template_name = 'pedcon_main/pediatric_hx_form.html'
    to_url = '/pediatric_hx_pdf_view/'

# renders pediatric history information to PDF & sends email of PDF
class ViewPedHxPDF(CreatePdfMixin, EmailPdfMixin, View):
    model = PediatricHistoryInformation
    template = 'pedcon_main/pediatric_hx_pdf_template.html'




# Adult history form processing (see .utils for Mixin)
class AdultHxFormView(ProcessFormMixin, View):
    form_class = AdultHxForm
    initial = {'key': 'value'}
    template_name = 'pedcon_main/adult_hx_form.html'
    to_url = '/adult_hx_pdf_view/'

# renders adult history information to PDF & sends email of PDF
class ViewAdultHxPDF(CreatePdfMixin, EmailPdfMixin, View):
    model = AdultHistoryInformation
    template = 'pedcon_main/adult_hx_pdf_template.html'




# Speech language history form processing (see .utils for Mixin)
class SpeechLanguageHxFormView(ProcessFormMixin, View):
    form_class = SpeechLanguageHxForm
    initial = {'key': 'value'}
    template_name = 'pedcon_main/speech_language_hx_form.html'
    to_url = '/speech_lang_hx_pdf_view/'

# renders speech language history information to PDF & sends email of PDF
class ViewSpeechLangHxPDF(CreatePdfMixin, EmailPdfMixin, View):
    model = SpeechLanguageHxInformation
    template = 'pedcon_main/speech_lang_hx_pdf_template.html'




# Release of information form processing (see .utils for Mixin)
class ROIFormView(ProcessFormMixin, View):
    form_class = ROIForm
    initial = {'key': 'value'}
    template_name = 'pedcon_main/roi_form.html'
    to_url = '/roi_pdf_view/'

# renders release of information to PDF & sends email of PDF
class ViewROIPDF(CreatePdfMixin, EmailPdfMixin, View):
    model = ReleaseOfInformation
    template = 'pedcon_main/roi_pdf_template.html'




# Safe and sound form processing (see .utils for Mixin)
class SSPFormView(ProcessFormMixin, View):
    form_class = SSPForm
    initial = {'key': 'value'}
    template_name = 'pedcon_main/ssp_form.html'
    to_url = '/ssp_pdf_view/'

# renders SSP information to PDF & sends email of PDF
class ViewSSPPDF(CreatePdfMixin, EmailPdfMixin, View):
    model = SafeAndSoundInformation
    template = 'pedcon_main/safe_and_sound_pdf_template.html'


# Contact form view. Processes and sends content of contact form
def contact(request):
    """The contact page for pedcon."""
    form = ContactForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():

            subject = 'Contact Form Submission'
            message_first_name = request.POST['first_name']
            message_last_name = request.POST['last_name']
            message_email = request.POST['email']
            message_phone = request.POST['phone']
            message_subject = request.POST['subject']
            message = request.POST['message']
            msg = f'Name: {message_first_name} {message_last_name} \n' \
                  f'Email: {message_email} \n'\
                  f'Phone: {message_phone} \n'\
                  f'Subject: {message_subject} \n'\
                  f'Message: {message} \n'
            recipients = ['info@pediatricconnectionsot.com',] 
            email = EmailMessage(subject, msg, settings.EMAIL_HOST_USER, recipients)
            email.send(fail_silently=True)

            '''Use below code for sending to multiple recipients with sendgrid 
            unless sendgrid has a better solution'''
            # recipients = ['info@pediatricconnectionsot.com', 'glesher@garrettlesher.com',]
            '''# Bcc not supported by sendgrid. Workaround is to loop through list 
            of recipients and send them an individual email. Not efficient with 
            large # of recipients, ok for this use case.'''
            # for recipient in recipients:
            #     email = EmailMessage(subject, msg, settings.EMAIL_HOST_USER, [recipient])
            #     email.send(fail_silently=True)
            return render(request, 'pedcon_main/contact.html', {'message_first_name': message_first_name})
    else:
        form = ContactForm()
    return render(request, 'pedcon_main/contact.html', {'form': form})

def index(request):
    """The home page for pedcon."""
    return render(request, 'pedcon_main/index.html')

def about_us(request):
    """The about us page for pedcon."""
    return render(request, 'pedcon_main/about_us.html')

def about_us_deana(request):
    """The about us Deana page for pedcon."""
    return render(request, 'pedcon_main/about_us_deana.html')

def andrea_arlotti(request):
    """The about us Andrea Arlotti page for pedcon."""
    return render(request, 'pedcon_main/andrea-arlotti.html')

def lisa_berry(request):
    """The about us Lisa berry page for pedcon."""
    return render(request, 'pedcon_main/lisa-berry.html')

def briana_picht(request):
    """The about us Briana Picht page for pedcon."""
    return render(request, 'pedcon_main/briana-picht.html')

def lisa_bergeson(request):
    """The about us Lisa bergeson page for pedcon."""
    return render(request, 'pedcon_main/lisa-bergeson.html')

def jennifer_shrum(request):
    """The about us Jennifer Shrum page for pedcon."""
    return render(request, 'pedcon_main/jennifer-shrum.html')

def paula_worley(request):
    """The about us Paula Worley page for pedcon."""
    return render(request, 'pedcon_main/paula-worley.html')

def trisha_morris(request):
    """The about us Trisha Morris page for pedcon."""
    return render(request, 'pedcon_main/trisha-morris.html')

def cathy_pickert(request):
    """The about us Cathy Pickert page for pedcon."""
    return render(request, 'pedcon_main/cathy-pickert.html')

def suzanne_remy(request):
    """The about us Suzanne Remy page for pedcon."""
    return render(request, 'pedcon_main/suzanne-remy.html')

def jennifer_vennart(request):
    """The about us Jennifer Vennart page for pedcon."""
    return render(request, 'pedcon_main/jennifer-vennart.html')

def services(request):
    """The services page for pedcon."""
    return render(request, 'pedcon_main/services.html')

def forms(request):
    """The forms page for pedcon."""
    return render(request, 'pedcon_main/forms.html')

def faq(request):
    """The faq page for pedcon."""
    return render(request, 'pedcon_main/faq.html')

def local_professionals(request):
    """The local_professionals page for pedcon."""
    return render(request, 'pedcon_main/local_professionals.html')

def helpful_links(request):
    """The helpful_links page for pedcon."""
    return render(request, 'pedcon_main/helpful_links.html')

def recommended_products(request):
    """The recommended_products page for pedcon."""
    return render(request, 'pedcon_main/recommended_products.html')

def privacy_policy(request):
    """The privacy policy page for pedcon."""
    return render(request, 'pedcon_main/privacy_policy.html')

def success(request):
    """The success page for pedcon."""
    return render(request, 'pedcon_main/success.html')