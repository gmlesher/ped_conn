"""Defines URL patterns for pedcon."""

from django.urls import path
from . import views

app_name = 'pedcon_main'
urlpatterns = [
    
    # Home Page
    path('', views.index, name='index'),
    # About us
    path('about_us/', views.about_us, name='about_us'),
    # About Deana page
    path('about_us_deana', views.about_us_deana, name='about_us_deana'),
    # Services page
    path('services/', views.services, name='services'),
    # Forms page
    path('forms/', views.forms, name='forms'),
    # Faq page
    path('faq/', views.faq, name='faq'),
    # Local professionals page
    path('local_professionals/', views.local_professionals, name='local_professionals'),
    # Helpful links page
    path('helpful_links/', views.helpful_links, name='helpful_links'),
    # Recommended product page
    path('recommended_products/', views.recommended_products, name='recommended_products'),
    # Contact page
    path('contact/', views.contact, name='contact'),
    # Privacy policy page
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    # Success page
    path('success/', views.success, name='success'),



    # *************** urls for form pages ***************

    # Practice form page
    path('practice_form/', views.PracticeFormView.as_view(), name='practice_form'),
    # Client information form page
    path('client_info_form/', views.CIFormView.as_view(), name='client_info_form'),
    # Payment policy form page
    path('payment_policy_form/', views.PaymentPolicyFormView.as_view(), name='payment_policy_form'),
    # Cancellation policy form page
    path('cancellation_policy_form/', views.CancellationPolicyFormView.as_view(), name='cancellation_policy_form'),
    # Pediatric history form page
    path('pediatric_hx_form/', views.PediatricHxFormView.as_view(), name='pediatric_hx_form'),
    # Adult history form page
    path('adult_hx_form/', views.AdultHxFormView.as_view(), name='adult_hx_form'),
    # Speech Language history form page
    path('speech_language_hx_form/', views.SpeechLanguageHxFormView.as_view(), name='speech_language_hx_form'),
    # Release of information history form page
    path('roi_form/', views.ROIFormView.as_view(), name='roi_form'),
    # SSP form page
    path('ssp_form/', views.SSPFormView.as_view(), name='ssp_form'),



    # *************** urls for PDF views ***************

    # Practice PDF view
    path('pdf_view/<int:pk>/', views.ViewPDF.as_view(), name='pdf_view'),
    # Client info PDF view
    path('ci_pdf_view/<int:pk>/', views.ViewCIPDF.as_view(), name='ci_pdf_view'),
    # Payment policy PDF view
    path('pp_pdf_view/<int:pk>/', views.ViewPPPDF.as_view(), name='pp_pdf_view'),
    # Cancellation Policy PDF view
    path('cancel_pdf_view/<int:pk>/', views.ViewCancelPDF.as_view(), name='cancel_pdf_view'),
    # ROI PDF view
    path('roi_pdf_view/<int:pk>/', views.ViewROIPDF.as_view(), name='roi_pdf_view'),
    # Pediatric History PDF view
    path('pediatric_hx_pdf_view/<int:pk>/', views.ViewPedHxPDF.as_view(), name='pediatric_hx_pdf_view'),
    # Adult History PDF view
    path('adult_hx_pdf_view/<int:pk>/', views.ViewAdultHxPDF.as_view(), name='adult_hx_pdf_view'),
    # Speech Language History PDF view
    path('speech_lang_hx_pdf_view/<int:pk>/', views.ViewSpeechLangHxPDF.as_view(), name='speech_lang_hx_pdf_view'),
    # Safe and Sound PDF view
    path('ssp_pdf_view/<int:pk>/', views.ViewSSPPDF.as_view(), name='ssp_pdf_view'),
    
]