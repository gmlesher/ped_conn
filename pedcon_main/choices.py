PHONE_TYPE = (
    ('', 'Select...'), 
    ('Mobile', 'Mobile'),
    ('Home', 'Home'), 
    ('Work', 'Work')
    )

IEP = (
    ('', 'Select...'), 
    ('Yes', 'Yes'),
    ('No', 'No')
    )

INSURANCE = (
    ('', 'Select...'),
    ('Blue Cross Blue Shield', 'Blue Cross Blue Shield'),
    ('Kansas Medicaid Aetna Better Health of Kansas', \
        'Kansas Medicaid Aetna Better Health of Kansas'),
    ('Kansas Medicaid Sunflower', 'Kansas Medicaid Sunflower'),
    ('Kansas Medicaid UHC Kancare', 'Kansas Medicaid UHC Kancare'),
    ('Tricare', 'Tricare'),
    ('WWPA', 'WWPA'),
    ('Aetna (Out of Network)', 'Aetna (Out of Network)'),
    ('Blue Cross Blue Shield - Blue Select (Out of Network)', \
        'Blue Cross Blue Shield - Blue Select (Out of Network)'),
    ('Cigna (Out of Network)', 'Cigna (Out of Network)'),
    ('Coventry (Out of Network)', 'Coventry (Out of Network)'),
    ('Humana (Out of Network)', 'Humana (Out of Network)'),
    ('Missouri Health Net (Out of Network)', \
        'Missouri Health Net (Out of Network)'),
    ('Missouri Medicaid (Out of Network)', \
        'Missouri Medicaid (Out of Network)'),
    ('United Health Care Commercial (Out of Network)', \
        'United Health Care Commercial (Out of Network)'),
    ('Private Pay', 'Private Pay'),
    ('Other', 'Other')
    )

CONTACT_VIA = (
    ('Mobile phone voice mail', 'Mobile phone voice mail'),
    ('Mobile phone text messages', 'Mobile phone text messages'),
    ('Home phone voice mail', 'Home phone voice mail'),
    ('Work phone voice mail', 'Work phone voice mail'),
    ('Email', 'Email'),
    )

INFO_RELEASE = (
    ('Medical Records', 'Medical Records'),
    ('Physical/Occupational Therapy Records', 'Physical/Occupational Therapy Records'),
    ('Speech Therapy Records', 'Speech Therapy Records'),
    ('School Records', 'School Records'),
    ('Other', 'Other'),
    )

GENDER = (
    ('', 'Select...'), 
    ('Boy', 'Boy'),
    ('Girl', 'Girl')
    )

ADULT_HX_GENDER = (
    ('', 'Select...'), 
    ('Male', 'Male'),
    ('Female', 'Female')
    )

CHILD_IS = (
    ('', 'Select...'), 
    ('Adopted', 'Adopted'),
    ('Biological Child', 'Biological Child'),
    ('Foster child', 'Foster Child')
    )

BORN_PREMATURE = (
    ('', 'Select...'), 
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Unknown', 'Unknown')
    )

# Adult hx form 
# Emotional section
CALM = (
    ('', 'Select...'), 
    ('1 - Calm', '1 - Calm'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Anger', '10 - Anger')
    )

HAPPY = (
    ('', 'Select...'), 
    ('1 - Happy', '1 - Happy'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Sad', '10 - Sad')
    )

SAFE = (
    ('', 'Select...'), 
    ('1 - Safe', '1 - Safe'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Fearful', '10 - Fearful')
    )

HOPEFUL = (
    ('', 'Select...'), 
    ('1 - Hopeful', '1 - Hopeful'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Hopeless', '10 - Hopeless')
    )

PEACEFUL = (
    ('', 'Select...'), 
    ('1 - Peaceful', '1 - Peaceful'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Frustrated', '10 - Frustrated')
    )

# Physical section
APPETITE = (
    ('', 'Select...'), 
    ('1 - Healthy', '1 - Healthy'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Irregular', '10 - Irregular')
    )

SLEEP_QUALITY = (
    ('', 'Select...'), 
    ('1 - Restful', '1 - Restful'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Restless', '10 - Restless')
    )

SLEEP_QUANTITY = (
    ('', 'Select...'), 
    ('1 - Ideal', '1 - Ideal'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Irregular', '10 - Irregular')
    )

PAIN = (
    ('', 'Select...'), 
    ('1 - No Discomfort', '1 - No Discomfort'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Extreme Pain', '10 - Extreme Pain')
    )

HEALTH = (
    ('', 'Select...'), 
    ('1 - Healthy', '1 - Healthy'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Unhealthy', '10 - Unhealthy')
    )

# Social section (all options are the same)
SOCIAL = (
    ('', 'Select...'), 
    ('1 - Thriving', '1 - Thriving'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Stressful', '10 - Stressful')
    )

# Mental Health section
THOUGHT = (
    ('', 'Select...'), 
    ('1 - Clear', '1 - Clear'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Brain Fog', '10 - Brain Fog')
    )

SPEECH = (
    ('', 'Select...'), 
    ('1 - I make total sense', '1 - I make total sense'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - I make no sense', '10 - I make no sense')
    )

FOCUS = (
    ('', 'Select...'), 
    ('1 - Laser Focus', '1 - Laser Focus'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Distracted', '10 - Distracted')
    )

TASK = (
    ('', 'Select...'), 
    ('1 - Completed all tasks', '1 - Completed all tasks'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Completed no tasks', '10 - Completed no tasks')
    )

# Daily Functioning section (all options are the same)
DAILY_TASKS = (
    ('', 'Select...'), 
    ('1 - Completes all daily tasks with ease', '1 - Completes all daily tasks with ease'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Unable to do any daily tasks', '10 - Unable to do any daily tasks')
    )

# Stress Resiliency section (all options are the same)
RESP_TO_STRESS = (
    ('', 'Select...'), 
    ('1 - Able to address and move on', '1 - Able to address and move on'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Stressors derail', '10 - Stressors derail')
    )

# Speech Language Hx form
YES_NO = (
    ('',''),
    ('Yes', 'Yes'), 
    ('No', 'No'),
    )

COMM_FORMAT = (
    ('Body Language (pointing, gesturing)', 'Body Language (pointing, gesturing)'), 
    ('Sounds', 'Sounds'),
    ('Words (shoe, doggy, up)', 'Words (shoe, doggy, up)'),
    ('2-4 word sentences', '2-4 word sentences'),
    ('Sentences longer than 4 words', 'Sentences longer than 4 words'),
    ('Other (sign language)', 'Other (sign language)')
    )

# SSP form
PARENT_SELF = (
    ('',''),
    ('Parent', 'Parent'), 
    ('Self', 'Self'),
    )

PRE_POST = (
    ('',''),
    ('Pre-treatment', 'Pre-treatment'), 
    ('Post-treatment', 'Post-treatment'),
    )

HOW_MUSIC_AFFECT = (
    ('', 'Select...'), 
    ('1 - Calming, Grounding', '1 - Calming, Grounding'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Aggravating, Irritating', '10 - Aggravating, Irritating')
    )

REACT_TO_STRESS = (
    ('', 'Select...'), 
    ('1 - Sympathetic hyper-arousal (activation/mobilization)', '1 - Sympathetic hyper-arousal (activation/mobilization)'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Dorsal vagal hypo-arousal (shutdown/immobilization)', '10 - Dorsal vagal hypo-arousal (shutdown/immobilization)')
    )

GEN_FEEL_HOME = (
    ('', 'Select...'), 
    ('1 - Calm', '1 - Calm'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Chaotic', '10 - Chaotic')
    )

NOISE = (
    ('', 'Select...'), 
    ('1 - Peaceful, Quiet', '1 - Peaceful, Quiet'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Frenzied, Loud', '10 - Frenzied, Loud')
    )

PEOPLE_IN_HOME = (
    ('', 'Select...'), 
    ('1 - Supportive', '1 - Supportive'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Unpredictable', '10 - Unpredictable')
    )

LIFE_COMFY = (
    ('', 'Select...'), 
    ('1 - Comfortable', '1 - Comfortable'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10 - Unsettled', '10 - Unsettled')
    )

WILLINGNESS = (
    ('', 'Select...'), 
    ("1 - I'm all in", "1 - I'm all in"),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ("10 - I'm skeptical", "10 - I'm skeptical")
    )