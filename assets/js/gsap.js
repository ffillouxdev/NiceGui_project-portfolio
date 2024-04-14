function slideLeft(element) {
    gsap.from(element, { opacity: 0, x: "50%", duration: 0.5 });
}

function slideRight(element) {
    gsap.from(element, { opacity: 0, x: "-50%", duration: 0.5 });
}

function slideUp(element) {
    gsap.from(element, { opacity: 0, y: "8%", duration: 1.2 });
}

function slideDown(element) {
    gsap.from(element, { opacity: 0, y: "-10%", duration: 1.2 });
}

var animationsTriggered = false;

document.addEventListener('DOMContentLoaded', function() {
    var sections = document.querySelectorAll('.hover_section2');
    sections.forEach((section) => {
        gsap.to(section, {
            scrollTrigger: {
                trigger: section,
                start: "top 50%", 
                onEnter: () => {
                    if (!animationsTriggered) {
                        slideRight('.el1');
                        slideLeft('.el2');
                        animationsTriggered = true;
                    }
                }
            }
        });
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
    
    setTimeout(function() {
        gsap.to(".title_section", {
            y: 20, 
            duration: 1,
            ease: "power1.inOut", 
            yoyo: true, 
            repeat: -1 
        });
    }, 1000);
});

