var wrapper = document.getElementById("signature-pad");
var clearButton = wrapper.querySelector("[data-action=clear]");
var changeColorButton = wrapper.querySelector("[data-action=change-color]");
var undoButton = wrapper.querySelector("[data-action=undo]");
var savePNGButton = wrapper.querySelector("[data-action=save-png]");
var saveJPGButton = wrapper.querySelector("[data-action=save-jpg]");
var saveSVGButton = wrapper.querySelector("[data-action=save-svg]");
var canvas = wrapper.querySelector("canvas");
var signaturePad = new SignaturePad(canvas, {
  // It's Necessary to use an opaque color when saving image as JPEG;
  // this option can be omitted if only saving as PNG or SVG
  backgroundColor: 'rgb(255, 255, 255)'
});

// Adjust canvas coordinate space taking into account pixel ratio,
// to make it look crisp on mobile devices.
// This also causes canvas to be cleared.
function resizeCanvas() {
  // When zoomed out to less than 100%, for some very strange reason,
  // some browsers report devicePixelRatio as less than 1
  // and only part of the canvas is cleared then.
  var ratio =  Math.max(window.devicePixelRatio || 1, 1);

  // This part causes the canvas to be cleared
  canvas.width = canvas.offsetWidth * ratio;
  canvas.height = canvas.offsetHeight * ratio;
  canvas.getContext("2d").scale(ratio, ratio);

  // This library does not listen for canvas changes, so after the canvas is automatically
  // cleared by the browser, SignaturePad#isEmpty might still return false, even though the
  // canvas looks empty, because the internal data of this library wasn't cleared. To make sure
  // that the state of this library is consistent with visual state of the canvas, you
  // have to clear it manually.
  signaturePad.clear();
}

// On mobile devices it might make more sense to listen to orientation change,
// rather than window resize events.

// Garrett's notes - commented out below window.onresize to prevent signature 
// from being cleared when resizing window on desktop and when scrolling on mobile
// window.onresize = resizeCanvas;
resizeCanvas();

function download(dataURL, filename) {
  if (navigator.userAgent.indexOf("Safari") > -1 && navigator.userAgent.indexOf("Chrome") === -1) {
    window.open(dataURL);
  } else {
    var blob = dataURLToBlob(dataURL);
    var url = window.URL.createObjectURL(blob);

    var a = document.createElement("a");
    a.style = "display: none";
    a.href = url;
    a.download = filename;

    document.body.appendChild(a);
    a.click();

    window.URL.revokeObjectURL(url);
  }
}

// One could simply use Canvas#toBlob method instead, but it's just to show
// that it can be done using result of SignaturePad#toDataURL.
function dataURLToBlob(dataURL) {
  // Code taken from https://github.com/ebidel/filer.js
  var parts = dataURL.split(';base64,');
  var contentType = parts[0].split(":")[1];
  var raw = window.atob(parts[1]);
  var rawLength = raw.length;
  var uInt8Array = new Uint8Array(rawLength);

  for (var i = 0; i < rawLength; ++i) {
    uInt8Array[i] = raw.charCodeAt(i);
  }

  return new Blob([uInt8Array], { type: contentType });
}

clearButton.addEventListener("click", function (event) {
  signaturePad.clear();
});

undoButton.addEventListener("click", function (event) {
  var data = signaturePad.toData();

  if (data) {
    data.pop(); // remove the last dot or line
    signaturePad.fromData(data);
  }
});

// changeColorButton.addEventListener("click", function (event) {
//   var r = Math.round(Math.random() * 255);
//   var g = Math.round(Math.random() * 255);
//   var b = Math.round(Math.random() * 255);
//   var color = "rgb(" + r + "," + g + "," + b +")";

//   signaturePad.penColor = color;
// });

savePNGButton.addEventListener("click", function (event) {
  if (signaturePad.isEmpty()) {
    alert("Please provide a signature first.");
  } else {
    var dataURL = signaturePad.toDataURL();
    // download(dataURL, "signature.png");
  }
});


// saveJPGButton.addEventListener("click", function (event) {
//   if (signaturePad.isEmpty()) {
//     alert("Please provide a signature first.");
//   } else {
//     var dataURL = signaturePad.toDataURL("image/jpeg");
//     // download(dataURL, "signature.jpg");
//   }
// });

// saveSVGButton.addEventListener("click", function (event) {
//   if (signaturePad.isEmpty()) {
//     alert("Please provide a signature first.");
//   } else {
//     var dataURL = signaturePad.toDataURL('image/svg+xml');
//     // download(dataURL, "signature.svg");
//   }
// });

// ********** Saves signature field to dataurl and adds red border and message if error. had to be moved from "script.js" for functionality reasons (threw errors that I couldn't figure out) **********
// save signaturePad url data to form field on form submission
// also adds validation message for signature field if empty
// prevents multiple error messages upon multiple invalid submissions for signature pads
if (signaturePad) {
  $('.PracticeForm, .paymentPolicyForm, .cancellationPolicyForm, .roiForm').submit(function(e){
    e.preventDefault();
    var errorExists = false;
    if(signaturePad.isEmpty()){
      $('#id_sig_data_URL').val("");
      if (errorExists === false){
        if(!$(".error")[0]){
          $(".signature-pad").append( "<div class='error' id='sig-error'><small>Please provide a signature</small></div>");
          $('.error').css("color", "#dc3545");
          $('.signature-pad--body > canvas').css('border-color', '#dc3545');
          errorExists = true;
        }; 
      };
    } else if(!signaturePad.isEmpty()) {
      if (errorExists === true){
        $('#sig-error').remove();
        errorExists = false;
      };
      // Loading animation
      $('.loaderDiv, .loader, .loading_msg').css('visibility', 'visible');
      $("[name='savePNG']")[0].click();
      var dataURL = signaturePad.toDataURL();
      $('#id_sig_data_URL').val(dataURL);
      $(this).unbind();
      $(this).submit();
    };
  });
};