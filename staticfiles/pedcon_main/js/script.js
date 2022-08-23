// Functionality for navigation bar & directions for dropdown inside toggle button.
// Clicking anywhere in window when "resources" dropdown is open closes dropdown. 
// If "resourses" is open, clicking anywhere in window collapses entire navbar. 
// Also adds slide effect to dropdown instead of abrupt appearance. 
$(function () { // Same as document.addEventListener("DOMContentLoaded"...
  $(function() {
    $('#navbarDropdown').on('click', function(event) {
      $('.dropdown-menu').slideToggle();
      event.stopPropagation();
    });
    $('.dropdown-menu').on('click', function(event) {
      event.stopPropagation();
    });
    $(window).on('click', function() {
      if ($("#header-items").is(":visible")) {
        $("#toggler").blur();
        $('.dropdown-menu').slideUp();
      } 
      if ($('.dropdown-menu').is(":hidden")) {
        $('#header-items').collapse("hide");
        $("#toggler").blur();
      }
    }); 
  });
});

// On safari, services page background images set to "scroll" from "fixed". 
// Safari has bad jitter with "fixed". 
var ua = navigator.userAgent.toLowerCase(); 
if (ua.indexOf('safari') != -1) { 
  if (ua.indexOf('chrome') > -1) {
     // Chrome
  } else {
    $(".bgimg-1, .bgimg-2, .bgimg-4").css("backgroundAttachment", "scroll") // Safari
  }
};

// validation for contact form before submission. Loading animation for 
// contact form here too
(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        } else if (form.checkValidity() === true) {
          // Loading animation for contact form. Same as other forms
          $('.loaderDiv, .loader, .loading_msg').css('visibility', 'visible');
        } 
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();

// Displays the user file input name when selected for the client info form 
// in the IEP file upload section
$('.custom-file-input').change(function(){
  var fileName = $(this).val().replace("C:\\fakepath\\", "");
  $(this).next('.custom-file-label').html(fileName);
});

// Conditional logic for Pediatric History Form child 
// relationship to parent/guardian
$(".pediatricHxForm").ready(function(){
  $("#id_adopted_age, #id_pre_adoption_hx, #id_how_long_foster").parent().hide();
  $("#id_child_is").on('change',function(){
    var selectedValue = $("#id_child_is").val();
    if (selectedValue == "Adopted") {
      $("#id_adopted_age, #id_pre_adoption_hx").parent().slideDown();
    } else {
      $("#id_adopted_age, #id_pre_adoption_hx").parent().slideUp();
    }
    if (selectedValue == "Foster child") {
      $("#id_how_long_foster").parent().slideDown();
    } else {
      $("#id_how_long_foster").parent().slideUp();
    }
  });  
});

// Conditional logic for Pediatric History Form client born premature
// relationship to gestational week section
$(".pediatricHxForm, .speechLangHxForm").ready(function(){
  $("#id_gest_wk").parent().hide();
  $("#id_born_premature").on('change',function(){
    var selectedValue = $("#id_born_premature").val();
    if (selectedValue == "Yes") {
      $("#id_gest_wk").parent().slideDown();
    }
    else {
      $("#id_gest_wk").parent().slideUp();
    }
  });  
});

// Conditional logic for Speech Language History Form ear tubes and 
// tonsillitis drop downs
$(".speechLangHxForm").ready(function(){
  $("#id_date_of_tubes").parent().hide();
  $("#id_tonsillitis_freq").parent().hide();
  // ear Tubes
  $("#id_conditions_7").click(function(){
    if ($(this).is(":checked")) {
      $("#id_date_of_tubes").parent().slideDown();
    }
    else {
      $("#id_date_of_tubes").parent().slideUp();
    }
  });  
  // tonsillitis
  $("#id_conditions_21").click(function(){
    if ($(this).is(":checked")) {
      $("#id_tonsillitis_freq").parent().slideDown();
    }
    else {
      $("#id_tonsillitis_freq").parent().slideUp();
    }
  });
});

// Conditional logic for Speech Language History Form previous speech 
// therapy/screening, leading to when and where, dismissed and dismissed info 
$(".speechLangHxForm").ready(function(){
  $("#id_where_when").parent().hide();
  $("#id_freq_last_service").parent().hide();
  $("#id_dismissed_0").parent().parent().parent().hide();
  // When and Where/Was he/she dismissed dropdown
  $("#id_speech_ther_hx_0").click(function(){
    // if "yes" radio button is toggled:
    if ($("#id_speech_ther_hx_0").is(":checked")) {
      $("#id_where_when").parent().slideDown();
      $("#id_dismissed_0").parent().parent().parent().slideDown();
      // reopens "list frequency and length..." if "was he/she..." is selected as yes before user returns to "yes" on "has your child ever..." from a "no" selection on that section
      if ($("#id_dismissed_0").is(":checked")) {
        $("#id_freq_last_service").parent().slideDown();
      }
    } 
  });
  $("#id_speech_ther_hx_1").click(function(){
    // if "no" radio button is toggled:
    if ($("#id_speech_ther_hx_1").is(":checked")) {
      $("#id_where_when").val(""); //clears text field
      $("#id_freq_last_service").val(""); //clears text field
      $("#id_dismissed_0").prop('checked', false); //clears toggled "yes" icon
      $("#id_dismissed_1").prop('checked', false); //clears toggled "no" icon
      $("#id_dismissed_0").parent().parent().parent().slideUp(); //slides up field
      $("#id_where_when").parent().slideUp(); //slides up field
      $("#id_freq_last_service").parent().slideUp(); //slides up field
    }
  });
  // List frequency and length of last service dropdown
  $("#id_dismissed_0").click(function(){
    if ($("#id_dismissed_0").is(":checked")) {
      $("#id_freq_last_service").parent().slideDown();//slides down field
    }
  });
  $("#id_dismissed_1").click(function(){
    if ($("#id_dismissed_1").is(":checked")) {
      $("#id_freq_last_service").val(""); //clears text field
      $("#id_freq_last_service").parent().slideUp();//slides up field
    }
  });
});

// makes all text area fields 3 rows tall
$('form').ready(function() {
  $('textarea').attr({'rows': "3"})
});

// Makes text red for multiple choice fields if error
$('form').ready(function() {
  if($('.errorlist')[0]){
    $('.errorlist').parent().parent('.form-row').css('color', '#dc3545');
    // $('.errorlist').parent().parent().css('color', '#dc3545');
  }
});

// loader animation for non-signature pad forms. Contact form animation is 
// the same, just above in contact form validation section.
$('.clientInfoForm, .pediatricHxForm, .adultHxForm, .speechLangHxForm, .sspForm').submit(function() {
  $('.loaderDiv, .loader, .loading_msg').css('visibility', 'visible');
});

// Moved processing of signature pad data to "app.js" for functionality 
// and specificity reasons. would get errors on pages without signature 
// pad when loading app.js 