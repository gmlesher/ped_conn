""" django file imports:"""
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core import validators
from django.core.mail import EmailMessage # for sending email in contact page
from django.conf import settings # for sending email in contact page
from django.views.generic import View # for class based views
# from django.urls import reverse, reverse_lazy # form processing in CBV (maybe) 
# from django.views.generic.edit import FormView # form processing in CBV (maybe) 

""" my file imports: """
from .forms import *
from .models import *
from .utils import *

    
# class ProcessView(FormView):
#     form_class = PracticeForm
#     template_name = 'pedcon_main/practice_form.html'
#     pk = None
    # success_url = reverse_lazy(f'pedcon_main:pdf_view{pk}')

    # def get_success_url(self):
    #     print(self.pk)
    #     return reverse('pdf_view', kwargs={'pk': self.pk})
    
    # def form_valid(self, form):
    #     # self.request.session['form-submitted'] = True
    #     form = form.save()
    #     self.pk = form.pk
    #     print(self.pk)
    #     return super().form_valid(form)

   

        # # x = request.__name__
        # # print(x)

# processes and saves practice form
def practice_form(request):
    form = PracticeForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.cleaned_data
            new_form = form.save()

            pk_value = new_form.pk
            # sets session to "form-submitted" in this view. To be processed in the view below
            request.session['form-submitted'] = True
            return HttpResponseRedirect(f'/pdf_view/{pk_value}')

    context = {'form': form}

    return render(request, 'pedcon_main/practice_form.html', context)


# renders practice information to PDF & sends email of PDF
class ViewPDF(CreatePdfMixin, EmailPdfMixin, View):
    model = PracticeInformation
    template = 'pedcon_main/practice_pdf_template.html'


# processes and saves client information form
def client_info_form(request):

    form = ClientInformationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.cleaned_data
            new_form = form.save()
            pk_value = new_form.pk

            # sets session to "form-submitted" in this view. To be processed in the view below
            request.session['form-submitted'] = True
            return HttpResponseRedirect(f'/ci_pdf_view/{pk_value}')

    context = {'form': form}

    return render(request, 'pedcon_main/ci_form.html', context)


# renders client information to PDF & sends email of PDF
class ViewCIPDF(CreatePdfMixin, EmailPdfMixin, View):
    model = ClientInformation
    template = 'pedcon_main/client_info_pdf_template.html'


# processes and saves payment policy form
def payment_policy_form(request):

    form = PaymentPolicyForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.cleaned_data
            new_form = form.save()
            pk_value = new_form.pk

            # sets session to "form-submitted" in this view. To be processed in the view below
            request.session['form-submitted'] = True
            return HttpResponseRedirect(f'/pp_pdf_view/{pk_value}')

    context = {'form': form}

    return render(request, 'pedcon_main/pp_form.html', context)


# renders payment policy information to PDF & sends email of PDF
class ViewPPPDF(CreatePdfMixin, EmailPdfMixin, View):
    model = PaymentPolicyInformation
    template = 'pedcon_main/payment_policy_pdf_template.html'


# processes and saves cancellation policy form
def cancellation_policy_form(request):

    form = CancellationPolicyForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.cleaned_data
            new_form = form.save()
            pk_value = new_form.pk

            # sets session to "form-submitted" in this view. To be processed in the view below
            request.session['form-submitted'] = True
            return HttpResponseRedirect(f'/cancel_pdf_view/{pk_value}')

    context = {'form': form}

    return render(request, 'pedcon_main/can_pol_form.html', context)


# renders cancellation policy information to PDF & sends email of PDF
class ViewCancelPDF(CreatePdfMixin, EmailPdfMixin, View):
    model = CancellationPolicyInformation
    template = 'pedcon_main/cancellation_pdf_template.html'


# processes and saves pediatric history form
def pediatric_hx_form(request):

    form = PedHxForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.cleaned_data
            new_form = form.save()
            pk_value = new_form.pk

            # sets session to "form-submitted" in this view. To be processed in the view below
            request.session['form-submitted'] = True
            return HttpResponseRedirect(f'/pediatric_hx_pdf_view/{pk_value}')

    context = {'form': form}

    return render(request, 'pedcon_main/pediatric_hx_form.html', context)


# renders pediatric history information to PDF & sends email of PDF
class ViewPedHxPDF(CreatePdfMixin, EmailPdfMixin, View):
    model = PediatricHistoryInformation
    template = 'pedcon_main/pediatric_hx_pdf_template.html'


# processes and saves pediatric history form
def adult_hx_form(request):

    form = AdultHxForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.cleaned_data
            new_form = form.save()
            pk_value = new_form.pk

            # sets session to "form-submitted" in this view. To be processed in the view below
            request.session['form-submitted'] = True
            return HttpResponseRedirect(f'/adult_hx_pdf_view/{pk_value}')

    context = {'form': form}

    return render(request, 'pedcon_main/adult_hx_form.html', context)


# renders adult history information to PDF & sends email of PDF
class ViewAdultHxPDF(CreatePdfMixin, EmailPdfMixin, View):
    model = AdultHistoryInformation
    template = 'pedcon_main/adult_hx_pdf_template.html'


# processes and saves speech language history form
def speech_language_hx_form(request):

    form = SpeechLanguageHxForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.cleaned_data
            new_form = form.save()
            pk_value = new_form.pk

            # sets session to "form-submitted" in this view. To be processed in the view below
            request.session['form-submitted'] = True
            return HttpResponseRedirect(f'/speech_lang_hx_pdf_view/{pk_value}')

    context = {'form': form}

    return render(request, 'pedcon_main/speech_language_hx_form.html', context)


# renders speech language history information to PDF & sends email of PDF
class ViewSpeechLangHxPDF(CreatePdfMixin, EmailPdfMixin, View):
    model = SpeechLanguageHxInformation
    template = 'pedcon_main/speech_lang_hx_pdf_template.html'


# processes and saves client information form
def roi_form(request):

    form = ROIForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.cleaned_data
            new_form = form.save()
            pk_value = new_form.pk

            # sets session to "form-submitted" in this view. To be processed in the view below
            request.session['form-submitted'] = True
            return HttpResponseRedirect(f'/roi_pdf_view/{pk_value}')

    context = {'form': form}

    return render(request, 'pedcon_main/roi_form.html', context)


# renders release of information to PDF & sends email of PDF
class ViewROIPDF(CreatePdfMixin, EmailPdfMixin, View):
    model = ReleaseOfInformation
    template = 'pedcon_main/roi_pdf_template.html'


# processes and saves client information form
def ssp_form(request):

    form = SSPForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.cleaned_data
            new_form = form.save()
            pk_value = new_form.pk

            # sets session to "form-submitted" in this view. To be processed in the view below
            request.session['form-submitted'] = True
            return HttpResponseRedirect(f'/ssp_pdf_view/{pk_value}')

    context = {'form': form}

    return render(request, 'pedcon_main/ssp_form.html', context)


# renders SSP information to PDF & sends email of PDF
class ViewSSPPDF(CreatePdfMixin, EmailPdfMixin, View):
    model = SafeAndSoundInformation
    template = 'pedcon_main/safe_and_sound_pdf_template.html'


# Contact form view. Processes and sends content of contact form
def contact(request):
    """The contact page for pedcon."""
    if request.method == 'POST':
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
              f'Message: {message}'

        recipients = ['gmlesher@gmail.com',]

        email = EmailMessage(subject, msg, settings.EMAIL_HOST_USER, recipients)
        email.send(fail_silently=False)
        
        return render(request, 'pedcon_main/contact.html', {'message_first_name': message_first_name})

    else:

        return render(request, 'pedcon_main/contact.html')

def index(request):
    """The home page for pedcon."""
    return render(request, 'pedcon_main/index.html')

def about_us(request):
    """The about us page for pedcon."""
    return render(request, 'pedcon_main/about_us.html')

def about_us_deana(request):
    """The about us Deana page for pedcon."""
    return render(request, 'pedcon_main/about_us_deana.html')

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
    """The release of information form page for pedcon."""
    return render(request, 'pedcon_main/success.html')

