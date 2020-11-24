const welcome = document.querySelector('.homeTitle');
const logo = document.querySelector('#logo');

//home page animations for welcome text and logo
window.onload = function () {
    const tl = new TimelineMax();
    tl
    .fromTo(welcome, 3, {opacity: 0, y: -100}, {background: "linear-gradient(45deg, rgba(21, 173, 226, 0.75), rgba(94, 191, 156, 0.75))", opacity: 1, y: 0})
    .fromTo("#logo", 3, {x: "-100%", opacity: 0}, {x: 0, ease: Back.easeOut, opacity: 1}, "-=3")
}

//home page animations for scroll
let tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".identify",
    start: "top 80%"
  }
});

tl
.fromTo(".identify_img, .identify_text", 1.2, {y: 50, opacity: 0}, {y: 0, opacity: 1}, "+=0.4");

let tl1 = gsap.timeline({
  scrollTrigger: {
    trigger: ".lightbulb",
    start: "top 80%"
  }
});

tl1
.fromTo(".lightbulb_img, .lightbulb_text", 1.2, {y: 50, opacity: 0}, {backgroundColor: "#FED000", y: 0, opacity: 1}, "+=0.4")

let tl2 = gsap.timeline({
  scrollTrigger: {
    trigger: ".empower",
    start: "top 80%"
  }
});

tl2
.fromTo(".empower_img, .empower_text", 1.2, {y: 50, opacity: 0}, {y: 0, opacity: 1}, "+=0.4");
tl2
// .to(".empower")

let tl3 = gsap.timeline({
  scrollTrigger: {
    trigger: ".wwd",
    start: "top 80%"
  }
});

tl3
.fromTo(".wwd_img, .wwd_text", 1.2, {y: 50, opacity: 0}, {backgroundColor: "#ffffff", y: 0, opacity: 1}, "+=0.4")


