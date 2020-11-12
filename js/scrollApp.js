if ($(window).innerWidth() > 991) {

    function splitScroll (){
      const controller = new ScrollMagic.Controller();
      new ScrollMagic.Scene({
        duration: "200%", 
        triggerElement: ".aboutPicture", 
        triggerHook: 0,
      })
      .setPin(".aboutPicture")
      .addTo(controller);
    }

    splitScroll();
} 


