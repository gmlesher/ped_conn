// Functionality for navigation bar & directions for dropdown inside toggle button. Clicking anywhere in window when "resources" dropdown is open closes dropdown. If "resourses" is open, clicking anywhere in window collapses entire navbar. Also adds slide effect to dropdown instead of abrupt appearance. 
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

// fading "home-tiles" images and text on home page
// can be used on other tiles in different function. 
// just change ".home-tiles" to another class & change "find('')" calls for appropriate html markup.
$(function () {
  $(".home-tiles").hover(function () {
    var img_id = $(this).find('img').attr("id"); //finds img id attribute
    var img_class = $(this).find('img').attr("class"); //finds img class attribute
    var div_id = $(this).find('div:eq(1)').attr("id"); //second "div" under "home-tiles" id attribute
    var div_class = $(this).find('div:eq(1)').attr("class"); //second "div" under "home-tiles" class attribute
    $("." + img_class + "#" + img_id).fadeOut(); //fades out image 
    $("." + div_class + "#" + div_id).fadeIn(); //fades in text
  }, function () {
    var img_id = $(this).find('img').attr("id"); //finds img id attribute
    var img_class = $(this).find('img').attr("class"); //finds img class attribute
    var div_id = $(this).find('div:eq(1)').attr("id"); //second "div" under "home-tiles" id attribute
    var div_class = $(this).find('div:eq(1)').attr("class"); //second "div" under "home-tiles" class attribute
    $("." + img_class + "#" + img_id).fadeIn(); //fades in image
    $("." + div_class + "#" + div_id).fadeOut(); //fades out text
  });
});

// On safari, services page background images set to "scroll" from "fixed". Safari has bad jitter with "fixed". 
var ua = navigator.userAgent.toLowerCase(); 
if (ua.indexOf('safari') != -1) { 
  if (ua.indexOf('chrome') > -1) {
     // Chrome
  } else {
    $(".bgimg-1, .bgimg-2, .bgimg-3, .bgimg-4").css("backgroundAttachment", "scroll") // Safari
  }
};

// validation for forms before submission
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
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();

// Conditional logic for IEP file upload option on client info form
$(".clientInfoForm").ready(function(){
  $(".IEPUpload").hide();
  $("#patientIEP").on('change',function(){
    var selectedValue = $("#patientIEP").val();
    if (selectedValue == "Yes") {
      $(".IEPUpload").slideDown();
    }
    else {
      $(".IEPUpload").slideUp();
    }
  });  
});

// Displays the user file input name when selected for the client info form in the IEP file upload section
$('.custom-file-input').change(function(){
  var fileName = $(this).val().replace("C:\\fakepath\\", "");
  $(this).next('.custom-file-label').html(fileName);
});

// Conditional logic for Pediatric History Form child relationship to parent/guardian
$(".pediatricHxForm").ready(function(){
  $(".childInfo").hide();
  $("#childIs").on('change',function(){
    var selectedValue = $("#childIs").val();
    if (selectedValue == "adopted") {
      $(".adoptedInfo").slideDown();
    } else {
      $(".adoptedInfo").slideUp();
    }
    if (selectedValue == "fosterChild") {
      $(".fosterInfo").slideDown();
    } else {
      $(".fosterInfo").slideUp()
    }
  });  
});

// Conditional logic for Pediatric History Form client born premature relationship to gestational week section
$(".pediatricHxForm").ready(function(){
  $(".gestWeek").hide();
  $("#premature").on('change',function(){
    var selectedValue = $("#premature").val();
    if (selectedValue == "yes") {
      $(".gestWeek").slideDown();
    }
    else {
      $(".gestWeek").slideUp();
    }
  });  
});


// 

// (function (global) {

// var dc = {};

// var homeHtml = "snippets/home-snippet.html";
// var allCategoriesUrl =
//   "https://davids-restaurant.herokuapp.com/categories.json";
// var categoriesTitleHtml = "snippets/categories-title-snippet.html";
// var categoryHtml = "snippets/category-snippet.html";
// var menuItemsUrl =
//   "https://davids-restaurant.herokuapp.com/menu_items.json?category=";
// var menuItemsTitleHtml = "snippets/menu-items-title.html";
// var menuItemHtml = "snippets/menu-item.html";

// // Convenience function for inserting innerHTML for 'select'
// var insertHtml = function (selector, html) {
//   var targetElem = document.querySelector(selector);
//   targetElem.innerHTML = html;
// };

// // Show loading icon inside element identified by 'selector'.
// var showLoading = function (selector) {
//   var html = "<div class='text-center'>";
//   html += "<img src='images/ajax-loader.gif'></div>";
//   insertHtml(selector, html);
// };

// // Return substitute of '{{propName}}'
// // with propValue in given 'string'
// var insertProperty = function (string, propName, propValue) {
//   var propToReplace = "{{" + propName + "}}";
//   string = string
//     .replace(new RegExp(propToReplace, "g"), propValue);
//   return string;
// }

// // Remove the class 'active' from home and switch to Menu button
// var switchMenuToActive = function () {
//   // Remove 'active' from home button
//   var classes = document.querySelector("#navHomeButton").className;
//   classes = classes.replace(new RegExp("active", "g"), "");
//   document.querySelector("#navHomeButton").className = classes;

//   // Add 'active' to menu button if not already there
//   classes = document.querySelector("#navMenuButton").className;
//   if (classes.indexOf("active") == -1) {
//     classes += " active";
//     document.querySelector("#navMenuButton").className = classes;
//   }
// };

// // On page load (before images or CSS)
// document.addEventListener("DOMContentLoaded", function (event) {

// // On first load, show home view
// showLoading("#main-content");
// $ajaxUtils.sendGetRequest(
//   homeHtml,
//   function (responseText) {
//     document.querySelector("#main-content")
//       .innerHTML = responseText;
//   },
//   false);
// });

// // Load the menu categories view
// dc.loadMenuCategories = function () {
//   showLoading("#main-content");
//   $ajaxUtils.sendGetRequest(
//     allCategoriesUrl,
//     buildAndShowCategoriesHTML);
// };


// // Load the menu items view
// // 'categoryShort' is a short_name for a category
// dc.loadMenuItems = function (categoryShort) {
//   showLoading("#main-content");
//   $ajaxUtils.sendGetRequest(
//     menuItemsUrl + categoryShort,
//     buildAndShowMenuItemsHTML);
// };


// // Builds HTML for the categories page based on the data
// // from the server
// function buildAndShowCategoriesHTML (categories) {
//   // Load title snippet of categories page
//   $ajaxUtils.sendGetRequest(
//     categoriesTitleHtml,
//     function (categoriesTitleHtml) {
//       // Retrieve single category snippet
//       $ajaxUtils.sendGetRequest(
//         categoryHtml,
//         function (categoryHtml) {
//           // Switch CSS class active to menu button
//           switchMenuToActive();

//           var categoriesViewHtml =
//             buildCategoriesViewHtml(categories,
//                                     categoriesTitleHtml,
//                                     categoryHtml);
//           insertHtml("#main-content", categoriesViewHtml);
//         },
//         false);
//     },
//     false);
// }


// // Using categories data and snippets html
// // build categories view HTML to be inserted into page
// function buildCategoriesViewHtml(categories,
//                                  categoriesTitleHtml,
//                                  categoryHtml) {

//   var finalHtml = categoriesTitleHtml;
//   finalHtml += "<section class='row'>";

//   // Loop over categories
//   for (var i = 0; i < categories.length; i++) {
//     // Insert category values
//     var html = categoryHtml;
//     var name = "" + categories[i].name;
//     var short_name = categories[i].short_name;
//     html =
//       insertProperty(html, "name", name);
//     html =
//       insertProperty(html,
//                      "short_name",
//                      short_name);
//     finalHtml += html;
//   }

//   finalHtml += "</section>";
//   return finalHtml;
// }



// // Builds HTML for the single category page based on the data
// // from the server
// function buildAndShowMenuItemsHTML (categoryMenuItems) {
//   // Load title snippet of menu items page
//   $ajaxUtils.sendGetRequest(
//     menuItemsTitleHtml,
//     function (menuItemsTitleHtml) {
//       // Retrieve single menu item snippet
//       $ajaxUtils.sendGetRequest(
//         menuItemHtml,
//         function (menuItemHtml) {
//           // Switch CSS class active to menu button
//           switchMenuToActive();

//           var menuItemsViewHtml =
//             buildMenuItemsViewHtml(categoryMenuItems,
//                                    menuItemsTitleHtml,
//                                    menuItemHtml);
//           insertHtml("#main-content", menuItemsViewHtml);
//         },
//         false);
//     },
//     false);
// }


// // Using category and menu items data and snippets html
// // build menu items view HTML to be inserted into page
// function buildMenuItemsViewHtml(categoryMenuItems,
//                                 menuItemsTitleHtml,
//                                 menuItemHtml) {

//   menuItemsTitleHtml =
//     insertProperty(menuItemsTitleHtml,
//                    "name",
//                    categoryMenuItems.category.name);
//   menuItemsTitleHtml =
//     insertProperty(menuItemsTitleHtml,
//                    "special_instructions",
//                    categoryMenuItems.category.special_instructions);

//   var finalHtml = menuItemsTitleHtml;
//   finalHtml += "<section class='row'>";

//   // Loop over menu items
//   var menuItems = categoryMenuItems.menu_items;
//   var catShortName = categoryMenuItems.category.short_name;
//   for (var i = 0; i < menuItems.length; i++) {
//     // Insert menu item values
//     var html = menuItemHtml;
//     html =
//       insertProperty(html, "short_name", menuItems[i].short_name);
//     html =
//       insertProperty(html,
//                      "catShortName",
//                      catShortName);
//     html =
//       insertItemPrice(html,
//                       "price_small",
//                       menuItems[i].price_small);
//     html =
//       insertItemPortionName(html,
//                             "small_portion_name",
//                             menuItems[i].small_portion_name);
//     html =
//       insertItemPrice(html,
//                       "price_large",
//                       menuItems[i].price_large);
//     html =
//       insertItemPortionName(html,
//                             "large_portion_name",
//                             menuItems[i].large_portion_name);
//     html =
//       insertProperty(html,
//                      "name",
//                      menuItems[i].name);
//     html =
//       insertProperty(html,
//                      "description",
//                      menuItems[i].description);

//     // Add clearfix after every second menu item
//     if (i % 2 != 0) {
//       html +=
//         "<div class='clearfix visible-lg-block visible-md-block'></div>";
//     }

//     finalHtml += html;
//   }

//   finalHtml += "</section>";
//   return finalHtml;
// }


// // Appends price with '$' if price exists
// function insertItemPrice(html,
//                          pricePropName,
//                          priceValue) {
//   // If not specified, replace with empty string
//   if (!priceValue) {
//     return insertProperty(html, pricePropName, "");;
//   }

//   priceValue = "$" + priceValue.toFixed(2);
//   html = insertProperty(html, pricePropName, priceValue);
//   return html;
// }


// // Appends portion name in parens if it exists
// function insertItemPortionName(html,
//                                portionPropName,
//                                portionValue) {
//   // If not specified, return original string
//   if (!portionValue) {
//     return insertProperty(html, portionPropName, "");
//   }

//   portionValue = "(" + portionValue + ")";
//   html = insertProperty(html, portionPropName, portionValue);
//   return html;
// }


// global.$dc = dc;

// })(window);
