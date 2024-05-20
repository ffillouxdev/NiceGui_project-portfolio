function animateSection1() {
    gsap.from('.title_section', { opacity: 0, x: "-50%", duration: 1.5, ease: "power2.out" });
}

function animateSection5() {
    gsap.from('.el1', { opacity: 0, x: "-50%", duration: 1, ease: "power2.out" });
    gsap.from('.el2', { opacity: 0, x: "50%", duration: 1, ease: "power2.out"});
    setNavbarBlack();
}

function animateSection3() {
    gsap.from('.title1', { opacity: 0, y: "50%", duration: 1.5, ease: "power2.out" });
}

function animateSection4() {
    // slideRight
    gsap.from('.title2', { opacity: 0, x: "-50%", duration: 2.2, ease: "power2.out" });
}

function setNavbarBlack() {
    var navbar = document.querySelector('.navbar');
    var navbarHr = document.querySelector('.navbar_hr');
    var navbarA = document.querySelectorAll('.navbar a');
    navbarA.forEach((a) => {
        a.classList.remove('text-white');
        a.classList.add('text-black');
    });
    navbar.classList.add('set_navbar_el_black');
    navbarHr.classList.add('set_navbar_hr_black');
}

function removeSetNavbarBlack() {
    var navbar = document.querySelector('.navbar');
    var navbarHr = document.querySelector('.navbar_hr');
    var navbarA = document.querySelectorAll('.navbar a');
    navbarA.forEach((a) => {
        a.classList.remove('text-black');
        a.classList.add('text-white');
    });
    navbar.classList.remove('set_navbar_el_black');
    navbarHr.classList.remove('set_navbar_hr_black');
}

// Initialisation des animations
document.addEventListener('DOMContentLoaded', function () {
    var section1 = document.querySelector('.parallax_group');
    var section2 = document.querySelector('.second');
    var section3 = document.querySelector('.third');
    var section4 = document.querySelector('.fourth');
    var section5 = document.querySelector('.fifth');
    var animationsTriggered = { section1: false, section2: false, section3: false, section4: false, section5: false };

    gsap.to(section1, {
        scrollTrigger: {
            trigger: section1,
            start: "top top",
            onEnter: () => {
                if (!animationsTriggered.section1) {
                    animateSection1();
                    animationsTriggered.section1 = true;
                }
            },
            onLeaveBack: () => {
                animationsTriggered.section1 = false;
            }
        }
    });

    gsap.to(section5, {
        scrollTrigger: {
            trigger: section5,
            start: "top 80%",
            onEnter: () => {
                if (!animationsTriggered.section2) {
                    animateSection5();
                    animationsTriggered.section2 = true;
                }
            },
            onLeaveBack: () => {
                animationsTriggered.section2 = false;
                removeSetNavbarBlack();
            }
        }
    });

    gsap.to(section3, {
        scrollTrigger: {
            trigger: section3,
            start: "top 80%",
            onEnter: () => {
                if (!animationsTriggered.section3) {
                    animateSection3();
                    animationsTriggered.section3 = true;
                }
            },
            onLeaveBack: () => {
                animationsTriggered.section3 = false;
            }
        }
    });

    gsap.to(section4, {
        scrollTrigger: {
            trigger: section4,
            start: "top 80%",
            onEnter: () => {
                if (!animationsTriggered.section4) {
                    animateSection4();
                    animationsTriggered.section4 = true;
                }
            },
            onLeaveBack: () => {
                animationsTriggered.section4 = false;
            }
        }
    });

    gsap.to(window, {
        scrollTrigger: {
            trigger: "body",
            start: "top top",
            onEnter: () => {
                animationsTriggered = false;
            }
        }
    });

    setTimeout(function () {
        gsap.to(".title_section", {
            y: 20,
            duration: 1,
            ease: "power1.inOut",
            yoyo: true,
            repeat: -1
        });
    }, 1000);
});