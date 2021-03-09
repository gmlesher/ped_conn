from django import forms
from .models import *
from localflavor.us.models import USStateField
from django.core.validators import RegexValidator

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3 

class PracticeForm(forms.ModelForm):
    required_css_class = 'required'
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    class Meta:
        model = PracticeInformation
        fields = '__all__'
        labels = {
        'sig_data_URL': '',
        }
        widgets = {
        'options': forms.CheckboxSelectMultiple(),
        'first_name': forms.TextInput(attrs={'placeholder': 'First name'}), 
        'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
        'date': forms.DateTimeInput(attrs={'placeholder': 'MM/DD/YYY', 'type': 'date'}),
        'sig_data_URL': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix','')
        super(PracticeForm, self).__init__(*args, **kwargs)

        # adds field name to all error messages
        for field in self.fields.values():
            field.error_messages = {'required':'{fieldname} is required'.format(
                fieldname=field.label)}

class ClientInformationForm(forms.ModelForm):
    required_css_class = 'required'
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    class Meta:
        model = ClientInformation
        fields = '__all__'
        widgets = {
        'dob': forms.DateInput(attrs={'placeholder': 'MM/DD/YYY', 'type': 'date'}),
        'pol_hold_dob': forms.DateInput(attrs={'placeholder': 'MM/DD/YYY', 'type': 'date'}),
        'sec_pol_hold_dob': forms.DateInput(attrs={'placeholder': 'MM/DD/YYY', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix','')
        super(ClientInformationForm, self).__init__(*args, **kwargs)

        # adds field name to all error messages
        for field in self.fields.values():
            field.error_messages = {'required':'{fieldname} is required'.format(
                fieldname=field.label)}

class PaymentPolicyForm(forms.ModelForm):
    required_css_class = 'required'
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    class Meta:
        model = PaymentPolicyInformation
        fields = '__all__'
        labels = {
        'initial_1': 'Initial',
        'initial_2': 'Initial',
        'initial_3': 'Initial',
        'initial_4': 'Initial',
        'initial_5': 'Initial',
        'initial_6': 'Initial',
        'initial_7': 'Initial',
        'initial_8': 'Initial',
        'initial_9': 'Initial',
        'initial_10': 'Initial',
        'sig_data_URL': '',
        }
        widgets = {
        'contact_via': forms.CheckboxSelectMultiple(),
        'client_first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
        'client_last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
        'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
        'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
        'date': forms.DateInput(attrs={'placeholder': 'MM/DD/YYY', 'type': 'date'}),
        'initial_1': forms.TextInput(attrs={'placeholder': 'Initials'}),
        'initial_2': forms.TextInput(attrs={'placeholder': 'Initials'}),
        'initial_3': forms.TextInput(attrs={'placeholder': 'Initials'}),
        'initial_4': forms.TextInput(attrs={'placeholder': 'Initials'}),
        'initial_5': forms.TextInput(attrs={'placeholder': 'Initials'}),
        'initial_6': forms.TextInput(attrs={'placeholder': 'Initials'}),
        'initial_7': forms.TextInput(attrs={'placeholder': 'Initials'}),
        'initial_8': forms.TextInput(attrs={'placeholder': 'Initials'}),
        'initial_9': forms.TextInput(attrs={'placeholder': 'Initials'}),
        'initial_10': forms.TextInput(attrs={'placeholder': 'Initials'}),
        'sig_data_URL': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix','')
        super(PaymentPolicyForm, self).__init__(*args, **kwargs)

        # adds field name to all error messages
        for field in self.fields.values():
            field.error_messages = {'required':'{fieldname} is required'.format(
                fieldname=field.label)}

class CancellationPolicyForm(forms.ModelForm):
    required_css_class = 'required'
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    class Meta:
        model = CancellationPolicyInformation
        fields = '__all__'
        labels = {
        'sig_data_URL': '',
        }
        widgets = {
        'client_first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
        'client_last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
        'parent_first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
        'parent_last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
        'sig_data_URL': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix','')
        super(CancellationPolicyForm, self).__init__(*args, **kwargs)

        # adds field name to all error messages
        for field in self.fields.values():
            field.error_messages = {'required':'{fieldname} is required'.format(
                fieldname=field.label)}

class PedHxForm(forms.ModelForm):
    required_css_class = 'required'
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    class Meta:
        model = PediatricHistoryInformation
        fields = '__all__'
        labels = {
        'adopted_age': 'Adopted at what age?',
        'pre_adoption_hx': 'If international adoption, explain setting of \
            pre-adoption history.',
        'how_long_foster': 'How long in foster care?',
        'trauma_hx': 'Please give a brief explanation of known trauma history \
            (abuse, neglect, sexual trauma, etc.):', 
        'born_premature': 'Was client born premature?', 
        'gest_wk': 'Gestational week', 
        'birth_hx': 'Describe birth history, including complications:',
        'med_conditions': 'Medical conditions/allergies',
        'diagnosis': 'Diagnosis (as given by MD)',
        'hearing_vision': 'Hearing/Vision Concerns',
        'diff_at_school': 'Is client having difficulties at school? \
            Please list areas of concern.',
        'diff_at_home': 'Is client having difficulties at home? \
            Please list areas of concern.',
        'type_of_discipline': 'Type of discipline used at home.',
        'diff_in_community': 'Is client having difficulties within the community (stores, unfamiliar places, etc)? Please list concerns.', 
        'ftg': 'Foot Tendon Guard', 
        'lcfe': 'Legs Cross Flexion Extension', 
        'atnr': 'ATNR', 
        'trunk_ext': 'Trunk Extension', 
        'hands_grasp': 'Hands Grasp', 
        'hands_supp': 'Hands Supporting', 
        'hands_pulling':'Hands Pulling',  
        'fear_paral': 'Fear Paralysis', 
        'spinal_perez': 'Spinal Perez', 
        'tlr': 'TLR',
        'bauer_crawl': 'Bauer Crawling', 
        'spinal_galant': 'Spinal Galant', 
        'stnr': 'STNR', 
        'fly_land': 'Flying and Landing',
        'goal_1': 'Goal #1',
        'goal_2': 'Goal #2',
        'goal_3': 'Goal #3',
        'goal_4': 'Goal #4',
        'childs_strengths': "Your Child's Strengths:",
        'childs_challenges': "Your Child's Challenges:",
        'other_comm': 'Any other comments/concerns not addressed above?',

        }
        widgets = {
        'client_first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
        'client_last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
        'dob': forms.DateInput(attrs={'placeholder': 'MM/DD/YYY', 'type': 'date'}),
        'serv_received': forms.CheckboxSelectMultiple(),
        'type_of_discipline': forms.CheckboxSelectMultiple(),
        'muscle_tone': forms.CheckboxSelectMultiple(),
        'babinski': forms.CheckboxSelectMultiple(),
        'ftg': forms.CheckboxSelectMultiple(),
        'lcfe': forms.CheckboxSelectMultiple(),
        'atnr': forms.CheckboxSelectMultiple(),
        'trunk_ext': forms.CheckboxSelectMultiple(),
        'hands_grasp': forms.CheckboxSelectMultiple(),
        'hands_supp': forms.CheckboxSelectMultiple(),
        'hands_pulling': forms.CheckboxSelectMultiple(),
        'babkin': forms.CheckboxSelectMultiple(),
        'moro': forms.CheckboxSelectMultiple(),
        'fear_paral': forms.CheckboxSelectMultiple(),
        'spinal_perez': forms.CheckboxSelectMultiple(),
        'tlr': forms.CheckboxSelectMultiple(),
        'landau': forms.CheckboxSelectMultiple(),
        'bauer_crawl': forms.CheckboxSelectMultiple(),
        'spinal_galant': forms.CheckboxSelectMultiple(),
        'stnr': forms.CheckboxSelectMultiple(),
        'fly_land': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix','')
        super(PedHxForm, self).__init__(*args, **kwargs)

        # adds field name to all error messages
        for field in self.fields.values():
            field.error_messages = {'required':'{fieldname} is required'.format(
                fieldname=field.label)}


class AdultHxForm(forms.ModelForm):
    required_css_class = 'required'
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    class Meta:
        model = AdultHistoryInformation
        fields = '__all__'
        labels = {
        'medical_hx': 'Describe Medical History',
        'rel_sig_other': 'Relationship with significant other',
        'rel_children': 'Relationship with children',
        'rel_peers': 'Relationship with peers',
        'rel_colleagues': 'Relationship with colleagues',
        'clar_of_thought': 'Clarity of thought',
        'clar_of_speech': 'Clarity of speech',
        'focus': 'Ability to focus',
        'comp_of_task': 'Completion of task',
        'resp_to_stress': 'Response to stress',
        'goal_1': 'Goal #1',
        'goal_2': 'Goal #2',
        'goal_3': 'Goal #3',
        'goal_4': 'Goal #4',
        'other_comm': 'Any other comments/concerns not addressed above?',
        }
        widgets = {
        'client_first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
        'client_last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
        'dob': forms.DateInput(attrs={'placeholder': 'MM/DD/YYY', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix','')
        super(AdultHxForm, self).__init__(*args, **kwargs)

        # adds field name to all error messages
        for field in self.fields.values():
            field.error_messages = {'required':'{fieldname} is required'.format(
                fieldname=field.label)}


class SpeechLanguageHxForm(forms.ModelForm):
    required_css_class = 'required'
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    class Meta:
        model = SpeechLanguageHxInformation
        fields = '__all__'
        labels = {
        'prim_lang': "Child's primary language spoken at home",
        'other_lang': 'Is there a language other than English spoken at home?',
        'born_premature': 'Was client born premature?',
        'gest_wk': 'Gestational Week',
        'birth_hx': 'Describe birth history, including complications:',
        'hearing_vision': 'Hearing/Vision Concerns',
        'conditions': 'Has your child had any of the following:',
        'other_conditions': 'Other serious injury/surgery/hospitalizations (age & reason)',
        'current_care': 'Is client currently under the care of:',
        'grasped_pencil': 'Grasped Crayon/Pencil',
        'first_word': 'Said 1st word',
        'two_words': 'Put 2 words together',
        'sentences': 'Spoke in short sentences',
        'latex_allergy': 'Does the client have a latex allergy?',
        'comm_format': 'Your child currently communicates using the primary format of:',
        'childs_strengths': "What are your child's strengths? What does your child like to do in his/her spare time?",
        'speech_ther_hx': 'Has your child ever had speech therapy/screening?',
        'where_when': 'Where and when?',
        'dismissed': 'Was he/she dismissed?',
        'freq_last_service': 'List frequency and length of last service',
        'frustrated': 'Is your child aware of or frustrated by any speech/language challenges?',
        'school_name': 'Name of School',
        'grade': 'Grade Level',
        'grade_repeated': 'Has your child repeated a grade?',
        'goal_1': 'Goal #1',
        'goal_2': 'Goal #2',
        'goal_3': 'Goal #3',
        'goal_4': 'Goal #4',
        'other_comm': "Please state any additional information or comments you feel would be helpful in learning about your child's speech/language behavior:",
        }
        widgets = {
        'client_first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
        'client_last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
        'dob': forms.DateInput(attrs={'placeholder': 'MM/DD/YYY', 'type': 'date'}),
        'other_lang': forms.RadioSelect(),
        'date_of_tubes': forms.DateInput(attrs={'placeholder': 'MM/DD/YYY', 'type': 'date'}),
        'last_hearing_exam': forms.DateInput(attrs={'placeholder': 'MM/DD/YYY', 'type': 'date'}),
        'latex_allergy': forms.RadioSelect(),
        'comm_format': forms.RadioSelect(),
        'speech_ther_hx': forms.RadioSelect(),
        'grade_repeated': forms.RadioSelect(),
        'conditions': forms.CheckboxSelectMultiple(),
        'current_care': forms.CheckboxSelectMultiple(),
        'does_client': forms.CheckboxSelectMultiple(),
        'does_your_child': forms.CheckboxSelectMultiple(),
        'social_char': forms.CheckboxSelectMultiple(),
        'behavioral_char': forms.CheckboxSelectMultiple(),
        'dismissed': forms.RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix','')
        super(SpeechLanguageHxForm, self).__init__(*args, **kwargs)

        # adds field name to all error messages
        for field in self.fields.values():
            field.error_messages = {'required':'{fieldname} is required'.format(
                fieldname=field.label)}

        radio_fields = ['other_lang', 'latex_allergy', 'comm_format', 'speech_ther_hx', 'grade_repeated', 'dismissed' ]

        # removes first blank "-----" choice on radio buttons
        for field_name in radio_fields:
            field = self.fields.get(field_name)
            if field and isinstance(field , forms.TypedChoiceField):
                field.choices = field.choices[1:]


class ROIForm(forms.ModelForm):
    required_css_class = 'required'
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    class Meta:
        model = ReleaseOfInformation
        fields = '__all__'
        labels = {
        'other': 'Other (specifics)',
        'second_address': 'Address',
        'second_address_2': 'Address 2',
        'second_city': 'City',
        'second_state': 'State',
        'second_zip': 'Zip',
        'sig_data_URL': '',
        }
        widgets = {
        'info_released': forms.CheckboxSelectMultiple(),
        'dob': forms.DateInput(attrs={'placeholder': 'MM/DD/YYY', 'type': 'date'}),
        'date': forms.DateInput(attrs={'placeholder': 'MM/DD/YYY', 'type': 'date'}),
        
        # 'client_first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
        # 'client_last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
        # 'parent_first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
        # 'parent_last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
        'sig_data_URL': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix','')
        super(ROIForm, self).__init__(*args, **kwargs)

        # adds field name to all error messages
        for field in self.fields.values():
            field.error_messages = {'required':'{fieldname} is required'.format(
                fieldname=field.label)}

class SSPForm(forms.ModelForm):
    required_css_class = 'required'
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    class Meta:
        model = SafeAndSoundInformation
        fields = '__all__'
        labels = {
        'form_completed_by': 'Form Completed By:',
        'pre_or_post': 'Please select whether you are filling out this form before or after SSP treatment:',
        'sound_sensitivity': 'Sound Sensitivity:',
        'general_sensitivity': 'General Nervous System Function:',
        'ss_other': 'Other',
        'gs_other': 'Other',
        'prior_listen_ther': 'Prior Listening Therapies (i.e. Interactive Metronome, iLs Focus)',
        'symp_other': 'Other',
        'dv_other': 'Other',
        'for_children': 'For children: Will a reliable, caring adult be able to support their experience with SSP?',
        'for_adults': 'For adults: Do you have a reliable, caring person at or close to home who could support you during your SSP journey?',
        'quiet_space': 'Will you have access to the same quiet space for your SSP listening sessions during remote delivery, and will your privacy in these sessions be respected?',
        'peaceful_env': 'Will you have access to a peaceful supportive environment to practice self-regulation between sessions and after completing SSP?',
        'how_music_affect': 'How does music affect you generally?',
        'reaction_to_stress': 'When reacting to distressing events I tend more towards:',
        'general_feeling_home': 'General feeling at home',
        'people_in_home': 'People in your home',
        'sympathetic': 'In sympathetic hyper-arousal (activation/mobilization), you might feel:',
        'dorsal_vagal': 'In dorsal vagal hypo-arousal (shutdown/immobilization), you might feel:',
        'ss_other': 'If other, please specify:',
        'gs_other': 'If other, please specify:',
        'symp_other': 'If other, please specify:',
        'dv_other': 'If other, please specify:',
        'life_comfy': 'Does your life and world feel comfortable?',
        'willingness': 'Do you have a willingness to engage and participate fully in the process with us as your provider, and understand that the SSP is not a quick fix, or a stand-alone therapy?',
        }
        widgets = {
        'dob': forms.DateInput(attrs={'placeholder': 'MM/DD/YYY', 'type': 'date'}),
        'date': forms.DateInput(attrs={'placeholder': 'MM/DD/YYY', 'type': 'date'}),
        'form_completed_by': forms.RadioSelect(),
        'pre_or_post': forms.RadioSelect(),
        'prior_listen_ther': forms.RadioSelect(),
        'for_children': forms.RadioSelect(),
        'for_adults': forms.RadioSelect(),
        'quiet_space': forms.RadioSelect(),
        'peaceful_env': forms.RadioSelect(),
        'sound_sensitivity': forms.CheckboxSelectMultiple(),
        'general_sensitivity': forms.CheckboxSelectMultiple(),
        'sympathetic': forms.CheckboxSelectMultiple(),
        'dorsal_vagal': forms.CheckboxSelectMultiple(),

        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix','')
        super(SSPForm, self).__init__(*args, **kwargs)

        # adds field name to all error messages
        for field in self.fields.values():
            field.error_messages = {'required':'{fieldname} is required'.format(
                fieldname=field.label)}



        
        radio_fields = ['form_completed_by', 'pre_or_post', 'prior_listen_ther', 'for_children', 'for_adults', 'quiet_space', 'peaceful_env' ]

        # removes first blank "-----" choice on radio buttons
        for field_name in radio_fields:
            field = self.fields.get(field_name)
            if field and isinstance(field , forms.TypedChoiceField):
                field.choices = field.choices[1:]
    
class ContactForm(forms.Form):
    required_css_class  = 'required'
    captcha             = ReCaptchaField(widget=ReCaptchaV3)
    first_name          = forms.CharField(label='First Name', max_length=50)
    last_name           = forms.CharField(label='Last Name', max_length=50)
    email               = forms.EmailField(label='Email', max_length=50)
    phone_regex         = RegexValidator(regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?' \
                            r'[\s.-]?\d{3}[\s.-]?\d{4}$')
    phone               = forms.CharField(label='Phone', validators=[phone_regex])
    subject             = forms.CharField(label='Subject', max_length=50)
    message             = forms.CharField(label='Message', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix','')
        super(ContactForm, self).__init__(*args, **kwargs)

        # adds field name to all error messages
        for field in self.fields.values():
            field.error_messages = {'required':'{fieldname} is required'.format(
                fieldname=field.label)}
