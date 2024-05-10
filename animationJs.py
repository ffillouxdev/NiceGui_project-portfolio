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
    ui.run_javascript("")


#https://bepatrickdavid.com/
#https://brittanychiang.com/