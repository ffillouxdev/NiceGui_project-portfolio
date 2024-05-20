from nicegui import ui

# fait apparaitre une alerte
def alert():
    ui.run_javascript('alert("Hello!")')
    
# fait une animation de slide vers la gauche
def slide_left(element):
    ui.run_javascript(f'gsap.from("{element}", {{ opacity: 0, x: "50%", duration: 0.5 }});')

# fait une animation de slide vers la droite
def slide_right(element):
    ui.run_javascript(f'gsap.from("{element}", {{ opacity: 0, x: "-50%", duration: 0.5 }});')

# fait une animation de slide vers le haut
def slide_up(element):
    ui.run_javascript(f'gsap.from("{element}", {{ opacity: 0, y: "16%", duration: 1.2 }});')

# fait une animation de slide vers le bas
def slide_down(element):
    ui.run_javascript(f'gsap.from("{element}", {{ opacity: 0, y: "-10%", duration: 1.2 }});')
    
# c'est quoi fade in et fade out ?

def fadeIn(element):
    ui.run_javascript(f'gsap.from("{element}", {{ opacity: 0, duration: 4.5, ease: "power2.out" }});')

def fadeOut(element):
    ui.run_javascript(f'gsap.to("{element}", {{ opacity: 0, duration: 0.5, ease: "power2.out" }});')

def slideLeftOut(element):
    ui.run_javascript(f'gsap.to("{element}", {{ opacity: 0, x: "-50%", duration: 0.5, ease: "power2.out" }});')
    

def slideLeftOut(element):
    ui.run_javascript(f'gsap.to("{element}", {{ opacity: 0, x: "-50%", duration: 0.5, ease: "power2.out" }});')


def slideRightOut(element):
    ui.run_javascript(f'gsap.to("{element}", {{ opacity: 0, x: "50%", duration: 0.5, ease: "power2.out" }});')
    

def slideUpOut(element):
    ui.run_javascript(f'gsap.to("{element}", {{ opacity: 0, y: "-66%", duration: 0.5, ease: "power2.out" }});')

def slideDownOut(element):
    ui.run_javascript(f'gsap.to("{element}", {{ opacity: 0, y: "66%", duration: 0.5, ease: "power2.out" }});')
    

#class_list = ["animate_slideInUp", "animate_slideInDown", "animate_slideInLeft", "animate_slideInRight"]

def all_gsap():
    ui.run_javascript("""
                var parallax = gsap.timeline({
                scrollTrigger: {
                        trigger: ".parallax_group",
                        start: "top top",
                        end: "+=200%",
                        scrub: true
                    }
                });

                parallax.to('.montains2', {
                    scale:1.1,
                    duration: 1,
                    ease: "none",
                    y : '-20vh',
                });

                parallax.to('.montains4', {
                    scale: 1.1,
                    duration: 1,
                    ease: "none",
                    y: '-5vh'
                }, "-=1");

                parallax.to('.dune1', {
                    scale: 1.1,
                    duration: 1,
                    ease: "none",
                    y: '-5vh'
                }, "-=1");

                parallax.to('.moon', {
                    scale: 1.2,
                    duration: .3,
                    ease: "none",
                    y: '20vh'                
                    }, "-=1");


                parallax.to('.parallax_group h1', {
                    opacity: 0,
                    duration: 0.5,
                    ease: "none",
                    y: '-50vh'
                }, "-=1");
                

                gsap.from('.star1', {
                    duration: 2.5,
                    x: '106%',
                    y: '-150%',
                    opacity: 0,
                    ease: "power1.inOut"
                });

                gsap.from('.star2', {
                    duration: 3.5,
                    x: '106%',
                    y: '-100%',
                    opacity: 0,
                    ease: "power1.inOut",
                    delay: 0.3
                });
                
                parallax.to('.star1', {
                    scale: 1.2,
                    duration: .3,
                    ease: "none",
                    y: '50vh'                
                }, "-=1");
                
                parallax.to('.star2', {
                     scale: 1.2,
                    duration: .3,
                    ease: "none",
                    y: '50vh'                
                }, "-=1");
                        """)


#https://bepatrickdavid.com/
#https://brittanychiang.com/