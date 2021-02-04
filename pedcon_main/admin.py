from django.contrib import admin
from django.forms import CheckboxSelectMultiple, RadioSelect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
from django.core.mail import EmailMessage
from django.conf import settings
import re

from .models import *
from .m2m import *
from .utils import render_to_pdf

"""VERY IMPORTANT!!! Registering models with admin takes place in for loop below PdfAdmin class with the try/except block. m2m models are commented out. If m2m classes are needed, uncomment, save admin.py file, and they will show up in Django admin."""

# retrieves all model names from 'pedcon_main' models.py
app_models = apps.get_app_config('pedcon_main').get_models()

class PdfAdmin(admin.ModelAdmin):
    ''' This model allows for opening of PDF documents for each submitted form. Only called when admin user selects desired object and clicks "go" button as "open PDF" is selected '''
    '''Side note: the reason "paired_dict" is available in the function below is because it is already created when admin.py is saved. This goes back to the fact that this class in only called on user request.'''

    # turns all m2m  multiple select fields into checkboxes in django admin
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def open_pdf(self, request, queryset, *args, **kwargs):
        for obj in queryset:
            # gets name and id of object 
            obj = get_object_or_404(self.model, pk=obj.id)

            # creates title for form
            unfinished_title = f"{obj.__class__.__name__} Form"

            # regex creates space before the second capitalized letter in 
            # object name for use in PDF title
            almost_finished_title = re.sub(r"(\w)([A-Z])", r"\1 \2", unfinished_title)

            # keeps "information" in title of 'ClientInformation' and
            # 'ReleaseOfInformation' form, else removes "information" in title
            if obj.__class__.__name__ == 'ClientInformation' or  obj.__class__.__name__ == 'ReleaseOfInformation':
                finished_title = almost_finished_title
            else:
                finished_title = almost_finished_title.replace("Information", "")

            # sets data to be rendered in PDF
            data = {
                    'form_title': finished_title,
                    'object': obj,
                }

            # takes request object name and checks whether in "paired_dict" keys.
            # If so, executes render to pdf, else throws error on screen
            if obj.__class__.__name__ in paired_dict.keys():
                # f string is value of associated object name in "paired_dict" 
                # dictionary which is template name associated with key in "paired_dict"  
                pdf = render_to_pdf(f'{paired_dict.get(obj.__class__.__name__)}', data)
                pdf_file = pdf.getvalue()

                if pdf:
                    return HttpResponse(pdf, content_type="application/pdf")
            else:
                return HttpResponse(f'{obj.__class__.__name__} not found in "paired_dict" dictionary in admin.py')

    def email_pdf(open_pdf, request, queryset):
        for obj in queryset:
            obj = get_object_or_404(obj.__class__, pk=obj.id)

            # creates title for form
            unfinished_title = f"{obj.__class__.__name__} Form"

            # regex creates space before the second capitalized letter in 
            # object name for use in PDF title
            almost_finished_title = re.sub(r"(\w)([A-Z])", r"\1 \2", unfinished_title)

            # keeps "information" in title of 'ClientInformation' and
            # 'ReleaseOfInformation' form, else removes "information" in title
            if obj.__class__.__name__ == 'ClientInformation' or  obj.__class__.__name__ == 'ReleaseOfInformation':
                finished_title = almost_finished_title
            else:
                finished_title = almost_finished_title.replace("Information", "")

            # sets data to be rendered in PDF
            data = {
                    'form_title': finished_title,
                    'object': obj,
                }

            # takes request object name and checks whether in "paired_dict" keys.
            # If so, executes render to pdf, else throws error on screen
            if obj.__class__.__name__ in paired_dict.keys():
                # f string is value of associated object name in "paired_dict" 
                # dictionary which is template name associated with key in "paired_dict"  
                pdf = render_to_pdf(f'{paired_dict.get(obj.__class__.__name__)}', data)
                pdf_file = pdf.getvalue()

                if pdf:
                    # names file
                    filename = f'{data["form_title"].lower().replace(" ","_")}_'\
                    f'{obj.id}.pdf'
                    # send email of pdf 
                    subject = f'New {data["form_title"]} submission'
                    message = f'See attached file: \n\n'
                    recipients = ['gmlesher@gmail.com',]


                    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, recipients)

                    email.attach(filename, pdf_file, 'application/pdf')
                    email.send(fail_silently=False)
                    return HttpResponse(f'{obj.__class__.__name__} form has been emailed successfully.')

            else:
                return HttpResponse(f'{obj.__class__.__name__} not found in "paired_dict" dictionary in admin.py')


        


    actions = [open_pdf, email_pdf]

    open_pdf.short_description = "Open PDF"
    email_pdf.short_description = "Email PDF"


# list of all m2m.py classes
m2m_classes = []

# list of all models.py classes
model_names = []

# loops over all model names in 'app_models' variable
# and appends each model to either "model_name" list or "m2m_classes"
for models in app_models:
    if models.__module__ == 'pedcon_main.m2m':
        m2m_classes.append(f'{models.__name__}')

        # # registers m2m.py classes in admin
        # try:
        #     admin.site.register(models, PdfAdmin)

        # except AlreadyRegistered:
        #     pass

    elif models.__module__ == 'pedcon_main.models':
        model_names.append(f'{models.__name__}')

        # registers models.py classes in admin
        try:
            admin.site.register(models, PdfAdmin)

        except AlreadyRegistered:
            pass

# alphabetizes items in "model_names" list for purpose of matching with 
# alphabetized "template_names" list so they match in "paired_dict" list below.
model_names.sort()


# PDF template names for each associated model
template_names = ['pedcon_main/practice_pdf_template.html', 'pedcon_main/client_info_pdf_template.html', 'pedcon_main/payment_policy_pdf_template.html', 'pedcon_main/cancellation_pdf_template.html', 'pedcon_main/pediatric_hx_pdf_template.html', 'pedcon_main/adult_hx_pdf_template.html', 'pedcon_main/speech_lang_hx_pdf_template.html', 'pedcon_main/roi_pdf_template.html', 'pedcon_main/safe_and_sound_pdf_template.html']

# alphabetizes items in "template_names" list for purpose of matching 
# with alphabetized "model_names" list so they match in "paired_dict" list below.
template_names.sort()

# stores dictionary of model names and template names
paired_dict = {}

# loop pairs model_name items as key with template_name items as 
# value in "paired_dict" dictionary.
for item in range(min(len(model_names), len(template_names))):
    paired_dict[model_names[item]] = template_names[item]
