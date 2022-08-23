from django.db import models
from django import forms
from django.core.validators import RegexValidator
from django.core.files import File
from django.urls import reverse, reverse_lazy
import os
import urllib

# Wagtail
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from localflavor.us.models import USStateField
from multiselectfield import MultiSelectField

# my files
from .choices import *
from .m2m import * 



# models for form data
class PracticeInformation(models.Model):
    # User information
    device_info     = models.CharField(max_length=100, blank=True, null=True)
    ip_address      = models.GenericIPAddressField(null=True, blank=True)
    country         = models.CharField(max_length=100, blank=True, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)

    # First section
    client_first_name      = models.CharField(max_length=100)
    client_last_name       = models.CharField(max_length=100)
    text            = models.TextField(blank=True, null=True)
    options         = models.ManyToManyField(Options)
    sig_data_URL    = models.TextField(blank=True)
    sig_img         = models.ImageField(blank=True, upload_to='sig_images/practice_form_sigs')
    filename        = models.CharField(max_length=255, blank=True, null=True)
    

class ClientInformation(models.Model):    
    # User information
    device_info         = models.CharField(max_length=100, blank=True, null=True)
    ip_address          = models.GenericIPAddressField(null=True, blank=True)
    country             = models.CharField(max_length=100, blank=True, null=True)
    created_at          = models.DateTimeField(auto_now_add=True, editable=False)

    # First section
    client_first_name   = models.CharField(max_length=100)
    client_last_name    = models.CharField(max_length=100)
    parent_first_name   = models.CharField(max_length=100, \
                            blank=True, null=True)
    parent_last_name    = models.CharField(max_length=100, \
                            blank=True, null=True)
    dob                 = models.DateField(auto_now=False, auto_now_add=False, \
                            verbose_name='Date of birth')
    address             = models.CharField(max_length=100)
    address_2           = models.CharField(max_length=100, blank=True, null=True)
    city                = models.CharField(max_length=100)
    state               = USStateField(default="KS")
    zip_code            = models.CharField(max_length=10, verbose_name='Zip')
    phone_regex         = RegexValidator(regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?' \
                            r'[\s.-]?\d{3}[\s.-]?\d{4}$')
    prim_phone          = models.CharField(validators=[phone_regex], \
                            max_length=17, verbose_name='Primary Phone')
    prim_phone_type     = models.CharField(max_length=10, choices=PHONE_TYPE, \
                            verbose_name='Primary phone type', default='')
    sec_phone           = models.CharField(validators=[phone_regex], \
                            max_length=17, verbose_name='Secondary Phone', \
                            blank=True, null=True)
    sec_phone_type      = models.CharField(max_length=10, choices=PHONE_TYPE, \
                            blank=True, null=True, \
                            verbose_name='Secondary phone type', default='')
    email               = models.EmailField(max_length=75)
    physician           = models.CharField(max_length=100)
    physician_fax       = models.CharField(max_length=17)
    pt_dx               = models.CharField(max_length=200, \
                            verbose_name='Patient Diagnosis', blank=True, null=True)
    iep                 = models.CharField(max_length=10, choices=IEP, \
                            verbose_name='Does your child have an IEP?', default='')
    ref_source          = models.CharField(max_length=100, \
                            verbose_name='How did you hear about us?')

    # Responsible Financial Party section
    rfp_first_name      = models.CharField(max_length=100, verbose_name='First Name')
    rfp_last_name       = models.CharField(max_length=100, verbose_name='Last Name')
    rfp_address         = models.CharField(max_length=100, verbose_name='Address', \
                            blank=True, null=True)
    rfp_address_2       = models.CharField(max_length=100, blank=True, null=True, \
                            verbose_name='Address 2')
    rfp_city            = models.CharField(max_length=100, verbose_name='City', \
                            blank=True, null=True)
    rfp_state           = USStateField(default="", verbose_name="State", \
                            blank=True, null=True)
    rfp_zip_code        = models.CharField(max_length=10, verbose_name='Zip', \
                            blank=True, null=True)
    rfp_prim_phone      = models.CharField(validators=[phone_regex], \
                            max_length=17, verbose_name='Primary Phone')
    rfp_prim_phone_type = models.CharField(max_length=10, choices=PHONE_TYPE, \
                            verbose_name='Primary phone type', default='')
    rfp_sec_phone       = models.CharField(validators=[phone_regex], \
                            max_length=17, verbose_name='Secondary Phone', \
                            blank=True, null=True)
    rfp_sec_phone_type  = models.CharField(max_length=10, choices=PHONE_TYPE, \
                            blank=True, null=True, \
                            verbose_name='Secondary phone type', default='')
    rfp_employer        = models.CharField(max_length=100, verbose_name='Employer')

    # Insurance Section
    prim_insurance          = models.CharField(max_length=100, choices=INSURANCE, \
                                verbose_name='Primary insurance', default='')
    ins_id                  = models.CharField(max_length=100, verbose_name='ID #')
    ins_group_id            = models.CharField(max_length=100, verbose_name='Group #')
    pol_hold_first_name     = models.CharField(max_length=100, \
                                verbose_name='Policy holder first name')
    pol_hold_last_name      = models.CharField(max_length=100, \
                                verbose_name='Policy holder last name')
    pol_hold_dob            = models.DateField(auto_now=False, auto_now_add=False, \
                                verbose_name='Policy holder date of birth')
    pol_hold_employer       = models.CharField(max_length=100, \
                                verbose_name='Policy holder employer')
    sec_insurance           = models.CharField(max_length=100, choices=INSURANCE, \
                                verbose_name='Secondary insurance', \
                                blank=True, null=True, default='')
    sec_ins_id              = models.CharField(max_length=100, \
                                verbose_name='ID #', \
                                blank=True, null=True)
    sec_ins_group_id        = models.CharField(max_length=100, \
                                verbose_name='Group #', \
                                blank=True, null=True)
    sec_pol_hold_first_name = models.CharField(max_length=100, \
                                verbose_name='Policy holder first name', \
                                blank=True, null=True)
    sec_pol_hold_last_name  = models.CharField(max_length=100, \
                                verbose_name='Policy holder last name', \
                                blank=True, null=True)
    sec_pol_hold_dob        = models.DateField(auto_now=False, auto_now_add=False, \
                                verbose_name='Policy holder date of birth', \
                                blank=True, null=True)
    sec_pol_hold_employer   = models.CharField(max_length=100, \
                                verbose_name='Policy holder employer', \
                                blank=True, null=True)

    
class PaymentPolicyInformation(models.Model):
    # User information
    device_info         = models.CharField(max_length=100, blank=True, null=True)
    ip_address          = models.GenericIPAddressField(null=True, blank=True)
    country             = models.CharField(max_length=100, blank=True, null=True)
    created_at          = models.DateTimeField(auto_now_add=True, editable=False)

    # Initials Section
    client_first_name   = models.CharField(max_length=100, verbose_name="Child's first name")
    client_last_name    = models.CharField(max_length=100, verbose_name="Child's last name")
    initial_1           = models.CharField(max_length=4)
    initial_2           = models.CharField(max_length=4)
    initial_3           = models.CharField(max_length=4)
    initial_4           = models.CharField(max_length=4)
    initial_5           = models.CharField(max_length=4)
    initial_6           = models.CharField(max_length=4)
    initial_7           = models.CharField(max_length=4)
    initial_8           = models.CharField(max_length=4)
    initial_9           = models.CharField(max_length=4)

    # Select multiple checkbox
    contact_via         = models.ManyToManyField(ContactVia, verbose_name="Communication preference")

    # Payment authorization section
    initial_10          = models.CharField(max_length=4)
    first_name          = models.CharField(max_length=100)
    last_name           = models.CharField(max_length=100)
    date                = models.DateField(auto_now=False, auto_now_add=False)

    # Signature Field data
    sig_data_URL    = models.TextField(blank=True)
    sig_img         = models.ImageField(blank=True, upload_to='sig_images/payment_policy_form_sigs')
    filename        = models.CharField(max_length=255, blank=True, null=True)


class CancellationPolicyInformation(models.Model):
    # User information
    device_info         = models.CharField(max_length=100, blank=True, null=True)
    ip_address          = models.GenericIPAddressField(null=True, blank=True)
    country             = models.CharField(max_length=100, blank=True, null=True)
    created_at          = models.DateTimeField(auto_now_add=True, editable=False)

    # Only Section
    client_first_name   = models.CharField(max_length=100)
    client_last_name    = models.CharField(max_length=100)
    parent_first_name   = models.CharField(max_length=100)
    parent_last_name    = models.CharField(max_length=100)
    
    # Signature Field data
    sig_data_URL    = models.TextField(blank=True)
    sig_img         = models.ImageField(blank=True, upload_to='sig_images/cancellation_policy_form_sigs')
    filename        = models.CharField(max_length=255, blank=True, null=True)


class PediatricHistoryInformation(models.Model):
    # User information
    device_info         = models.CharField(max_length=100, blank=True, null=True)
    ip_address          = models.GenericIPAddressField(null=True, blank=True)
    country             = models.CharField(max_length=100, blank=True, null=True)
    created_at          = models.DateTimeField(auto_now_add=True, editable=False)

    # First Section
    client_first_name   = models.CharField(max_length=100)
    client_last_name    = models.CharField(max_length=100)
    parent_email        = models.EmailField(max_length=75, \
        verbose_name="Parent/Guardian email")
    dob                 = models.DateField(auto_now=False, auto_now_add=False, \
                            verbose_name='Date of birth')
    gender              = models.CharField(max_length=100, choices=GENDER, \
                            default='')
    child_is            = models.CharField(max_length=100, choices=CHILD_IS, \
                            default='', \
                            verbose_name="Child is...")
    adopted_age         = models.CharField(max_length=100, blank=True, null=True)
    pre_adoption_hx     = models.TextField(blank=True, null=True)
    how_long_foster     = models.CharField(max_length=100, blank=True, null=True)   
    trauma_hx           = models.TextField(blank=True, null=True)
    ref_source          = models.CharField(max_length=100, \
                            blank=True, null=True, \
                            verbose_name='Who referred you to Pediatric Connections?')
    ref_reason          = models.CharField(max_length=100, \
                            blank=True, null=True, \
                            verbose_name='Why were you referred?')

    # Family Info Section
    client_lives_with   = models.TextField()
    parent_1_occ        = models.CharField(max_length=100, \
                            blank=True, null=True, \
                            verbose_name="Parent #1 Occupation")
    parent_2_occ        = models.CharField(max_length=100, \
                            blank=True, null=True, \
                            verbose_name="Parent #2 Occupation")

    # Medical History Section
    born_premature      = models.CharField(max_length=100, \
                            choices=BORN_PREMATURE, \
                            default='')
    gest_wk             = models.CharField(max_length=100, blank=True, null=True)
    birth_hx            = models.TextField()
    med_conditions      = models.TextField()
    diagnosis           = models.CharField(max_length=100, blank=True, null=True)
    medications         = models.CharField(max_length=100, blank=True, null=True)
    hearing_vision      = models.CharField(max_length=100, blank=True, null=True)

    # School/Home/Family
    school_name         = models.CharField(max_length=100, blank=True, null=True)
    school_dist         = models.CharField(max_length=100, blank=True, null=True)
    grade               = models.CharField(max_length=25, blank=True, null=True)
    serv_received       = models.ManyToManyField(ServicesReceived, \
                            verbose_name="Services received at school", \
                            blank=True)
    diff_at_school      = models.TextField(blank=True, null=True)
    diff_at_home        = models.TextField(blank=True, null=True)
    type_of_discipline  = models.ManyToManyField(TypeOfDiscipline, \
                            verbose_name="Type of discipline used at home", \
                            blank=True)
    diff_in_community   = models.TextField(blank=True, null=True)
    muscle_tone         = models.ManyToManyField(MuscleTone)
    muscle_tone_comm    = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    babinski            = models.ManyToManyField(Babinski)
    babinski_comm       = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    ftg                 = models.ManyToManyField(FootTendonGuard)
    ftg_comm            = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    lcfe                = models.ManyToManyField(LegsCrossedFlexionExtension)
    lcfe_comm           = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    atnr                = models.ManyToManyField(ATNR)
    atnr_comm           = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    trunk_ext           = models.ManyToManyField(TrunkExtension)
    trunk_ext_comm      = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    hands_grasp         = models.ManyToManyField(HandsGrasp)
    hands_grasp_comm    = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    hands_supp          = models.ManyToManyField(HandsSupporting)
    hands_supp_comm     = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    hands_pulling       = models.ManyToManyField(HandsPulling)
    hands_pulling_comm  = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    babkin              = models.ManyToManyField(Babkin)
    babkin_comm         = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    moro                = models.ManyToManyField(Moro)
    moro_comm           = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    fear_paral          = models.ManyToManyField(FearParalysis)
    fear_paral_comm     = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    spinal_perez        = models.ManyToManyField(SpinalPerez)
    spinal_perez_comm   = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    tlr                 = models.ManyToManyField(TLR)
    tlr_comm            = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    landau              = models.ManyToManyField(Landau)
    landau_comm         = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    bauer_crawl         = models.ManyToManyField(BauerCrawling)
    bauer_crawl_comm    = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    spinal_galant       = models.ManyToManyField(SpinalGalant)
    spinal_galant_comm  = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    stnr                = models.ManyToManyField(STNR)
    stnr_comm           = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")
    fly_land            = models.ManyToManyField(FlyingAndLanding)
    fly_land_comm       = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")

    # Goals Section
    goal_1              = models.CharField(max_length=100)
    goal_2              = models.CharField(max_length=100, blank=True, null=True)
    goal_3              = models.CharField(max_length=100, blank=True, null=True)
    goal_4              = models.CharField(max_length=100, blank=True, null=True)
    childs_strengths    = models.TextField()
    childs_challenges   = models.TextField()
    other_comm          = models.TextField(blank=True, null=True)


class AdultHistoryInformation(models.Model):
    # User information
    device_info         = models.CharField(max_length=100, blank=True, null=True)
    ip_address          = models.GenericIPAddressField(null=True, blank=True)
    country             = models.CharField(max_length=100, blank=True, null=True)
    created_at          = models.DateTimeField(auto_now_add=True, editable=False)

    # First Section
    client_first_name   = models.CharField(max_length=100)
    client_last_name    = models.CharField(max_length=100)
    client_email        = models.EmailField(max_length=75)
    dob                 = models.DateField(auto_now=False, auto_now_add=False, \
                            verbose_name='Date of birth')
    gender              = models.CharField(max_length=100, \
                            choices=ADULT_HX_GENDER, default='')
    ref_source          = models.CharField(max_length=100, \
                            blank=True, null=True, \
                            verbose_name='Who referred you to Pediatric Connections?')
    ref_reason          = models.CharField(max_length=100, \
                            blank=True, null=True, \
                            verbose_name='Why were you referred?')

    # Family Info Section
    client_lives_with   = models.TextField()
    client_occ          = models.CharField(max_length=100, \
                            blank=True, null=True, \
                            verbose_name="client Occupation")

    # Medical History Section
    medical_hx          = models.TextField()
    medications         = models.CharField(max_length=100, blank=True, null=True)

    # Emotional Section
    calm                = models.CharField(max_length=100, \
                            choices=CALM, default='')
    happy               = models.CharField(max_length=100, \
                            choices=HAPPY, default='')
    safe                = models.CharField(max_length=100, \
                            choices=SAFE, default='')
    hopeful             = models.CharField(max_length=100, \
                            choices=HOPEFUL, default='')
    peaceful            = models.CharField(max_length=100, \
                            choices=PEACEFUL, default='')
    emotional_comm      = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")

    # Physical Section
    appetite           = models.CharField(max_length=100, \
                            choices=APPETITE, default='')
    sleep_quality       = models.CharField(max_length=100, \
                            choices=SLEEP_QUALITY, default='')
    sleep_quantity      = models.CharField(max_length=100, \
                            choices=SLEEP_QUANTITY, default='')
    pain                = models.CharField(max_length=100, \
                            choices=PAIN, default='')
    health              = models.CharField(max_length=100, \
                            choices=HEALTH, default='')
    physical_comm       = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")

    # Social Section
    rel_sig_other       = models.CharField(max_length=100, \
                            choices=SOCIAL, default='', blank=True, null=True)
    rel_children        = models.CharField(max_length=100, \
                            choices=SOCIAL, default='', blank=True, null=True)
    rel_peers           = models.CharField(max_length=100, \
                            choices=SOCIAL, default='')
    rel_colleagues      = models.CharField(max_length=100, \
                            choices=SOCIAL, default='')
    social_comm         = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")

    # Mental Health Section
    clar_of_thought     = models.CharField(max_length=100, \
                            choices=THOUGHT, default='')
    clar_of_speech      = models.CharField(max_length=100, \
                            choices=SPEECH, default='')
    focus               = models.CharField(max_length=100, \
                            choices=FOCUS, default='')
    comp_of_task        = models.CharField(max_length=100, \
                            choices=TASK, default='')
    mental_health_comm  = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")

    # Daily Functioning Section
    daily_tasks         = models.CharField(max_length=100, \
                            choices=DAILY_TASKS, default='')
    daily_tasks_comm    = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")

    # Stress Resiliency Section
    resp_to_stress      = models.CharField(max_length=100, \
                            choices=RESP_TO_STRESS, default='')
    resp_to_stress_comm = models.TextField(blank=True, null=True, \
                            verbose_name="Comments")

    # Goals Section
    goal_1              = models.CharField(max_length=100)
    goal_2              = models.CharField(max_length=100, blank=True, null=True)
    goal_3              = models.CharField(max_length=100, blank=True, null=True)
    goal_4              = models.CharField(max_length=100, blank=True, null=True)
    other_comm          = models.TextField(blank=True, null=True)


class SpeechLanguageHxInformation(models.Model):
    # User information
    device_info         = models.CharField(max_length=100, blank=True, null=True)
    ip_address          = models.GenericIPAddressField(null=True, blank=True)
    country             = models.CharField(max_length=100, blank=True, null=True)
    created_at          = models.DateTimeField(auto_now_add=True, editable=False)

    # First Section
    client_first_name   = models.CharField(max_length=100)
    client_last_name    = models.CharField(max_length=100)
    dob                 = models.DateField(auto_now=False, auto_now_add=False, \
                            verbose_name='Date of birth')
    gender              = models.CharField(max_length=100, \
                            choices=ADULT_HX_GENDER, default='')
    parent_email        = models.EmailField(max_length=75, verbose_name="Parent/Guardian Email")
    ref_source          = models.CharField(max_length=100, \
                            blank=True, null=True, \
                            verbose_name='Who referred you to Pediatric Connections?')
    ref_reason          = models.CharField(max_length=100, \
                            blank=True, null=True, \
                            verbose_name='Why were you referred?')

    # Family Info Section
    client_lives_with   = models.TextField()
    parent_1_occ        = models.CharField(max_length=100, \
                            verbose_name="Parent #1 Occupation")
    parent_2_occ        = models.CharField(max_length=100, \
                            blank=True, null=True, \
                            verbose_name="Parent #2 Occupation")
    prim_lang           = models.CharField(max_length=100, \
                            blank=True, null=True)
    other_lang          = models.CharField(max_length=100, blank=True, null=True, \
                            choices=YES_NO, )

    # Medical History Section
    born_premature      = models.CharField(max_length=100, \
                            choices=BORN_PREMATURE, default='', \
                            blank=True, null=True)
    gest_wk             = models.CharField(max_length=100, blank=True, null=True)
    birth_hx            = models.TextField(blank=True, null=True)
    medications         = models.CharField(max_length=100, blank=True, null=True)
    hearing_vision      = models.CharField(max_length=100, blank=True, null=True)
    conditions          = models.ManyToManyField(Conditions, blank=True)
    date_of_tubes       = models.DateField(auto_now=False, auto_now_add=False, \
                            verbose_name='Date of ear tubes', \
                            blank=True, null=True)
    tonsillitis_freq    = models.CharField(max_length=100, \
                            verbose_name='Tonsillitis: How Often?', \
                            blank=True, null=True)
    other_conditions    = models.CharField(max_length=100, blank=True, null=True)
    last_hearing_exam   = models.DateField(auto_now=False, auto_now_add=False, \
                            blank=True, null=True)
    exam_results        = models.CharField(max_length=100, blank=True, null=True, \
                            verbose_name='Results of hearing exam')
    current_care        = models.ManyToManyField(CurrentCare)
    other_specialist    = models.CharField(max_length=100, blank=True, null=True)
    does_client         = models.ManyToManyField(DoesClient)
    sat_alone           = models.CharField(max_length=100, blank=True, null=True)
    grasped_pencil      = models.CharField(max_length=100, \
                            blank=True, null=True)
    babbled             = models.CharField(max_length=100, blank=True, null=True)
    first_word          = models.CharField(max_length=100, blank=True, null=True)
    two_words           = models.CharField(max_length=100, blank=True, null=True)
    sentences           = models.CharField(max_length=100, blank=True, null=True)
    walked              = models.CharField(max_length=100, blank=True, null=True)
    toilet_trained      = models.CharField(max_length=100, blank=True, null=True)

    # Speech-Language Hearing Section
    latex_allergy       = models.CharField(max_length=100, blank=True, null=True, \
                            choices=YES_NO)
    comm_format         = models.CharField(max_length=100, blank=True, null=True, \
                            choices=COMM_FORMAT)
    childs_strengths    = models.TextField(blank=True, null=True)
    speech_ther_hx      = models.CharField(max_length=100, blank=True, null=True, \
                            choices=YES_NO)
    where_when          = models.CharField(max_length=100, blank=True, null=True)
    dismissed           = models.CharField(max_length=100, blank=True, null=True, \
                            choices=YES_NO)
    freq_last_service   = models.CharField(max_length=100, blank=True, null=True)
    frustrated          = models.TextField(blank=True, null=True)
    does_your_child     = models.ManyToManyField(DoesYourChild, blank=True)
    social_char         = models.ManyToManyField(SocialChar, blank=True)
    behavioral_char     = models.ManyToManyField(BehavioralChar, blank=True)
    school_name         = models.CharField(max_length=100, blank=True, null=True)
    teacher_name        = models.CharField(max_length=100, blank=True, null=True)
    grade               = models.CharField(max_length=25, blank=True, null=True)
    grade_repeated      = models.CharField(max_length=100, blank=True, null=True, \
                            choices=YES_NO)

    # Goals Section
    goal_1              = models.CharField(max_length=100)
    goal_2              = models.CharField(max_length=100, blank=True, null=True)
    goal_3              = models.CharField(max_length=100, blank=True, null=True)
    goal_4              = models.CharField(max_length=100, blank=True, null=True)
    other_comm          = models.TextField(blank=True, null=True)


class ReleaseOfInformation(models.Model):
    # User information
    device_info             = models.CharField(max_length=100, blank=True, null=True)
    ip_address              = models.GenericIPAddressField(null=True, blank=True)
    country                 = models.CharField(max_length=100, blank=True, null=True)
    created_at              = models.DateTimeField(auto_now_add=True, editable=False)

    # Only Section
    client_first_name       = models.CharField(max_length=100)
    client_last_name        = models.CharField(max_length=100)
    dob                     = models.DateField(auto_now=False, auto_now_add=False, \
                            verbose_name='Date of birth')
    person_agency_name      = models.CharField(max_length=100, verbose_name='Name of person/agency')

    address                 = models.CharField(max_length=100)
    address_2               = models.CharField(max_length=100, blank=True, null=True)
    city                    = models.CharField(max_length=100)
    state                   = USStateField(default="KS")
    zip_code                = models.CharField(max_length=10, verbose_name='Zip')
    phone_regex             = RegexValidator(regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?' \
                            r'[\s.-]?\d{3}[\s.-]?\d{4}$')
    phone                   = models.CharField(validators=[phone_regex], \
                            max_length=17)
    fax                     = models.CharField(max_length=17, blank=True, null=True)
    info_released           = models.ManyToManyField(ReleasedInfo, verbose_name="Information to be released/exchanged")
    other                   = models.CharField(max_length=200, blank=True, null=True)
    printed_first_name      = models.CharField(max_length=100, verbose_name="Printed client/legal guardian first name")
    printed_last_name       = models.CharField(max_length=100, verbose_name="Printed client/legal guardian last name")
    date                    = models.DateField(auto_now=False, auto_now_add=False)
    second_address          = models.CharField(max_length=100)
    second_address_2        = models.CharField(max_length=100, blank=True, null=True)
    second_city             = models.CharField(max_length=100)
    second_state            = USStateField(default="KS")
    second_zip_code         = models.CharField(max_length=10, verbose_name='Zip')

    # Signature Field data
    sig_data_URL    = models.TextField(blank=True)
    sig_img         = models.ImageField(blank=True, upload_to='sig_images/roi_form_sigs')
    filename        = models.CharField(max_length=255, blank=True, null=True)


class SafeAndSoundInformation(models.Model):
    # User information
    device_info             = models.CharField(max_length=100, blank=True, null=True)
    ip_address              = models.GenericIPAddressField(null=True, blank=True)
    country                 = models.CharField(max_length=100, blank=True, null=True)
    created_at              = models.DateTimeField(auto_now_add=True, editable=False)

    # First Section (client information)
    client_first_name       = models.CharField(max_length=100)
    client_last_name        = models.CharField(max_length=100)
    dob                     = models.DateField(auto_now=False, auto_now_add=False, \
                                verbose_name='Date of birth')
    form_completed_by       = models.CharField(max_length=100, choices=PARENT_SELF, default="abc")
    pre_or_post             = models.CharField(max_length=100, choices=PRE_POST, default="abc")

    # Client Experience Section
    # sound sensitivity
    sound_sensitivity       = models.ManyToManyField(SoundSensitivity)
    ss_other                = models.CharField(max_length=200, blank=True, null=True)
    # general sensitivity
    general_sensitivity     = models.ManyToManyField(GeneralSensitivity)
    gs_other                = models.CharField(max_length=200, blank=True, null=True)
    # prior listening experiences
    prior_listen_ther       = models.CharField(max_length=100, choices=YES_NO, default="abc")  
    prior_listen_ther_comm  = models.TextField(blank=True, null=True, \
                                verbose_name="Comments")
    how_music_affect        = models.CharField(max_length=100, choices=HOW_MUSIC_AFFECT, default="abc")
    how_music_affect_comm   = models.TextField(blank=True, null=True, \
                                verbose_name="Comments")
    # nervous system tendency
    sympathetic             = models.ManyToManyField(Sympathetic)
    symp_other              = models.CharField(max_length=200, blank=True, null=True)
    dorsal_vagal            = models.ManyToManyField(DorsalVagal)
    dv_other                = models.CharField(max_length=200, blank=True, null=True)
    reaction_to_stress      = models.CharField(max_length=100, choices=REACT_TO_STRESS, default="abc")

    # Client resources Section
    # home environment
    general_feeling_home    = models.CharField(max_length=100, choices=GEN_FEEL_HOME, default="abc")
    noise                   = models.CharField(max_length=100, choices=NOISE, default="abc")
    people_in_home          = models.CharField(max_length=100, choices=PEOPLE_IN_HOME, default="abc")
    home_comm               = models.TextField(blank=True, null=True, \
                                verbose_name="Comments") 
    # access to support
    for_children            = models.CharField(max_length=100, blank=True, \
                                null=True, choices=YES_NO)
    for_children_comm       = models.TextField(blank=True, null=True, \
                                verbose_name="Comments")
    for_adults              = models.CharField(max_length=100, blank=True, \
                                null=True, choices=YES_NO)
    for_adults_comm         = models.TextField(blank=True, null=True, \
                                verbose_name="Comments")
    quiet_space             = models.CharField(max_length=100, choices=YES_NO, default="abc")
    quiet_space_comm        = models.TextField(blank=True, null=True, \
                                verbose_name="Comments")
    peaceful_env            = models.CharField(max_length=100, choices=YES_NO, default="abc")
    peaceful_env_comm       = models.TextField(blank=True, null=True, \
                                verbose_name="Comments")
    # unforeseen circumstances
    life_comfy              = models.CharField(max_length=100, choices=LIFE_COMFY, default="abc")
    life_comfy_comm         = models.TextField(blank=True, null=True, \
                                verbose_name="Comments")
    # commitment to program
    willingness             = models.CharField(max_length=100, choices=WILLINGNESS, default="abc")
    willingness_comm        = models.TextField(blank=True, null=True, \
                                verbose_name="Comments")   


class HipaaInformation(models.Model):
    # User information
    device_info     = models.CharField(max_length=100, blank=True, null=True)
    ip_address      = models.GenericIPAddressField(null=True, blank=True)
    country         = models.CharField(max_length=100, blank=True, null=True)
    created_at      = models.DateTimeField(auto_now_add=True, editable=False)

    # First Section (client information)
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    date            = models.DateField(auto_now=False, auto_now_add=False)

    # Signature Field data
    sig_data_URL    = models.TextField(blank=True)
    sig_img         = models.ImageField(blank=True, upload_to='sig_images/hipaa_form_sigs')
    filename        = models.CharField(max_length=255, blank=True, null=True)

class AboutPage(Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    occupation = models.CharField(max_length=50)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\d{3}-\d{3}-\d{4}$', 
        message="Phone number must be entered in the format: '999-999-9999'. Up to 12 digits allowed."
        )
    phone = models.CharField(validators=[phone_regex], 
        max_length=12, 
        blank=True,
        default="913-257-5808"
        )
    phone_ext = models.CharField(max_length=4, blank=True)
    bio = StreamField([
        ('paragraph', blocks.RichTextBlock()),
    ], blank=True)
    about_me = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
    ])
    other = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        MultiFieldPanel([
            FieldPanel('occupation'),
            FieldPanel('email'),
            FieldPanel('phone'),
            FieldPanel('phone_ext'),

        ], heading="Personal information"),
        StreamFieldPanel('bio'),
        StreamFieldPanel('about_me'),
        StreamFieldPanel('other'),
    ]

    def __init__(self, *args, **kwargs):
        super(AboutPage, self).__init__(*args, **kwargs)
        self._meta.get_field('title').verbose_name = 'Name'

class AboutIndexPage(Page):

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        aboutpages = AboutPage.objects.live().public()
        context["aboutpages"] = aboutpages

        return context