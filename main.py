from nicegui import ui

class MyWebsite:
    def __init__(self):
        # General styles
        self.background = ui.query('body').style("background-color: lightblue")
        self.foreground = ui.query('body').style("color: black")
        self.est_enabled = False
        self.dark = ui.dark_mode()
        
        # Create the navbar
        self.current_page = "/"
        self.create_navbar()

    def create_navbar(self):
        with ui.header().classes("w-full flex justify-between items-center shadow-md") as tabs:
            with ui.row().classes("flex justify-center items-center w-full"):
                self.home = ui.link("Home", "/").classes("text-lg font-bold no-underline hover:underline" + (" text-red" if self.current_page == "/" else " text-black"))
                self.about = ui.link("About", "/About").classes("text-lg font-bold no-underline hover:underline" + (" text-red" if self.current_page == "/About" else " text-black"))
                self.contact = ui.link("Contact", "/Contact").classes("text-lg font-bold no-underline hover:underline" + (" text-red" if self.current_page == "/Contact" else " text-black"))
                self.dark_button1 = ui.button("Dark", on_click=self.dark_mode)
            with ui.row().classes("flex justify-center items-center w-full"):
                self.separator1 = ui.separator().classes("w-1/3 bg-gray-800")
        
        # pages
        @ui.page("/Contact")
        def contact_page():
            self.current_page = "/Contact"
            self.create_navbar()
            self.contactForm()
                
        @ui.page("/About")
        def about_page():
            self.current_page = "/About"
            self.create_navbar()
            
        self.header = tabs
        
    def contactForm(self):
        with ui.row().classes("w-full flex justify-center items-center") as section:
            with ui.column().classes("w-full md:w-1/2 bg-gray-200 rounded-lg shadow-md p-6 custom-contact-form"):
                self.welcomeLabel = ui.markdown("### Contact us").classes("mb-4 text-lg font-semibold")
                self.input1 = ui.input(label="Name", placeholder="Put your name here").classes("mt-2 w-full px-4 py-2 focus:outline-none focus:border-green-500")
                self.textarea1 = ui.textarea(label="Message").classes("mt-4 w-full px-4 py-2 focus:outline-none focus:border-green-500 resize-none h-32")
                self.button1 = ui.button("Click me", color="green").classes("mt-4 w-full px-4 py-2 bg-green-500 text-white hover:bg-green-600 focus:outline-none focus:bg-green-600")
                self.button1.on_click(self.on_click)


                
               

    def dark_mode(self):
        if not self.est_enabled:
            self.est_enabled = True
            self.background = ui.query('body').style("background-color: lightblue")
            self.dark.disable()
        else:
            self.est_enabled = False
            self.background = ui.query('body').style("background-color: black")
            self.dark.enable()

        
    # Methods                    
    def on_click(self):
        ui.notify("Button clicked")
        self.button1.text = "Clicked"
       
    def change_bg(self, color):
        self.background = ui.query('body').style("background-color: " + color)

# Example component    
def create_card():
    with ui.card().tight() as card:
        ui.image(source="assets/image1.png")
        with ui.card_section():
            ui.label("This is a card")
        with ui.card_section():
            ui.button("Click me")
    return card       

def run():
    ui.run()

website = MyWebsite()
run()


"""composants
        self.welcomeLabel = ui.markdown("### Welcome to my website")
        self.input1 = ui.input(label="Name", placeholder="Put your name here")
        self.button1 = ui.button("Click me", color="green")
        self.button1.on_click(self.on_click)
        self.fname = ui.label()
        self.textarea1 = ui.textarea(label="Message", on_change= lambda e : self.fname.set_text(e.value))
        self.date1 = ui.date(value="2004-02-07")
        self.numberCounter = ui.number(label="Counter", min=0, max=99)
        self.timeCounter = ui.time(value="12:00")
        self.colorInput = ui.color_input(value="#ff0000", on_change= lambda e : self.change_bg(e.value))
        self.button2 = ui.button(text="Click me", color="green", on_click=lambda e: ui.notify("Button clicked"))
        self.radio1 = ui.radio(["Option 1", "Option 2", "Option 3"], value="Option 1").props("inline")
        self.genderLabel = ui.label(text="Gender:")
        self.genderSelect = ui.select(["Male", "Female"])
        self.simpleCheckbox = ui.checkbox("Simple checkbox")
        self.switch_btn = ui.switch("Switch")
        self.salarytSlider = ui.slider(min=0, max=10, step=1, value=5)
        #self.picture1 = ui.image(source="assets/img3.png")
        #self.video1 = ui.video(source="assets/video1.mp4")
        #possiblite de mettre un tab avec un csv
        self.code1 = ui.code("print('Hello world')", language="python")
        self.editor1 = ui.editor()
        self.chatMessage = ui.chat_message("Hello World")
         self.mermaid = ui.mermaid(graph TD;
                                    A --> B;
                                    A --> C;
                                    B --> D;
                                    C --> D;
                                  )
        
        self.card1 = create_card()
        self.card2 = create_card()

        
         #self.contact_link = ui.link("Contact", self.contact_page)
        self.contact_link = ui.link("Contact", contact_page)
        
        self.upload1 = ui.upload(label="Upload file")
        self.download1 = ui.download(src="assets/download/README.md")
        
        self.dark = ui.dark_mode()
        self.button3 = ui.button("Black", color="black", on_click=self.dark.enable)
        self.button4 = ui.button("White", color="white", on_click=self.dark.disable)
         self.date1 = ui.date(value="2004-02-07")
                self.numberCounter = ui.number(label="Counter", min=0, max=99)
                self.timeCounter = ui.time(value="12:00")
                self.colorInput = ui.color_input(value="#ff0000", on_change= lambda e : self.change_bg(e.value))
                self.radio1 = ui.radio(["Option 1", "Option 2", "Option 3"], value="Option 1").props("inline")""" 