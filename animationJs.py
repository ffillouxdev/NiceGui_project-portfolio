from nicegui import ui

def alert():
    ui.run_javascript('alert("Hello!")')
    
def slide_left(element):
    ui.run_javascript(f'gsap.from("{element}", {{ opacity: 0, x: "50%", duration: 0.5 }});')

def slide_right(element):
    ui.run_javascript(f'gsap.from("{element}", {{ opacity: 0, x: "-50%", duration: 0.5 }});')

def slide_up(element):
    ui.run_javascript(f'gsap.from("{element}", {{ opacity: 0, y: "16%", duration: 1.2 }});')

def slide_down(element):
    ui.run_javascript(f'gsap.from("{element}", {{ opacity: 0, y: "-10%", duration: 1.2 }});')

#class_list = ["animate_slideInUp", "animate_slideInDown", "animate_slideInLeft", "animate_slideInRight"]

def all_gsap():
    ui.run_javascript("")
