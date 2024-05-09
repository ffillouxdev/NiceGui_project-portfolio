from nicegui import ui

class MyWebsite:
    def __init__(self):
        self.is_enabled = False
        self.current_page = "/"

    def set_style(self):
    # General styles
        if self.is_enabled:
            self.background = ui.query("body").style("background-color: black")
            self.foreground = ui.query("a").classes("text-white")
        else:
            self.background = ui.query("body").style("background-color: lightblue")
            self.foreground = ui.query("a").classes("text-white")
            
            
        self.dark = ui.dark_mode()
        self.style = ui.add_head_html("""
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    width: 100%;
                }
                .card-plus {
                    background-color: white;
                    margin: 1rem;
                    padding: 1rem;
                }
                .card-plus img {
                    width: 100%;
                    height: auto;
                }
                @keyframes slideleft {
                    from {
                        opacity: 0;
                        transform: translateX(50%);
                    }
                    to {
                        transform: translateX(0);
                        opacity: 1;
                    }
                }

                @keyframes slideright {
                    from {
                        opacity: 0;
                        transform: translateX(-50%);
                    }
                    to {
                        opacity: 1;
                        transform: translateX(0);
                    }
                }
                
                
                @keyframes slideup {
                    from {
                        opacity: 0;
                        transform: translateY(8%);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }

                @keyframes slidedown {
                    from {
                        opacity: 0;
                        transform: translateY(0);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(-10%);
                    }
                }

                .animate__slideInLeft {
                    animation: slideleft 0.5s;
                }

                .animate__slideInRight {
                    animation: slideright 0.5s;
                }
                .animate__slideInRight1 {
                    animation: slideright 1.2s;
                }
                .animate__slideInUp {
                    animation: slideup 1.2s;
                }

                .animate__slideInDown {
                    animation: slidedown 1.2s;
                }
            </style>
        """)       


    def create_navbar(self):
        with ui.header().classes(
            "flex justify-between items-center transparent no-shadow"
        ) as tabs:
            with ui.row().classes("flex justify-center items-center w-full"):
                self.home = ui.link("Home", "/").classes(
                    "text-lg font-bold no-underline hover:underline"
                    + (" text-red" if self.current_page == "/" else "")
                )
                self.about = ui.link("About", "/About").classes(
                    "text-lg font-bold no-underline hover:underline"
                    + (" text-red" if self.current_page == "/About" else "")
                )
                self.contact = ui.link("Contact", "/Contact").classes(
                    "text-lg font-bold no-underline hover:underline"
                    + (" text-red" if self.current_page == "/Contact" else "")
                )
                self.dark_button1 = ui.button("Dark", on_click=self.dark_mode)
            with ui.row().classes("flex justify-center items-center w-full"):
                self.separator1 = ui.separator().classes("w-1/3 bg-white")

    def create_footer(self):
        with ui.footer().classes(
            "flex justify-center items-center w-full h-16 bg-gray-800 text-white fixed bottom-0" 
        ) as footer:
            self.footerLabel = ui.label("© 2024 All rights reserved")
            with ui.row().classes("flex justify-center items-center w-full"):
                self.separator2 = ui.separator().classes("w-1/3 bg-white")
                


    def main_section(self):
        with ui.row().classes(
            "flex justify-bottom items-left w-full h-screen"
        ) as first_section:
            ui.html(
                """
                    <div class="mt-8 animate__slideInRight1">
                        <h1 class="text-6xl font-bold text-white text-left pl-8 pt-8 pr-8">Welcome to my website</h1>
                        <p class="text-white text-left pl-9">This is a simple website created using nicegui !</p>
                    </div>
                    """
            ).classes("w-1/2 ml-8 mt-8")
            with ui.column().classes() as container:
                with ui.column().classes("r") as box1:
                    with ui.card().tight().classes(
                        "border rounded-lg shadow-md card-plus"
                    ) as card1:
                        ui.image(source="assets/image1.png")
                        with ui.card_section():
                            ui.label("This is a card").classes("text-lg font-semibold")
                        with ui.card_section():
                            ui.button("Click me").classes(
                                "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                            )
                with ui.column().classes("") as box2:
                    with ui.card().tight().classes(
                        "border rounded-lg shadow-md card-plus"
                    ) as card2:
                        ui.image(source="assets/image1.png")
                        with ui.card_section():
                            ui.label("This is a card").classes("text-lg font-semibold")
                        with ui.card_section():
                            ui.button("Click me").classes(
                                "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                            )
            with ui.row().classes("") as row:
                with ui.column().classes("") as box3:
                    with ui.card().tight().classes(
                        "border rounded-lg shadow-md card-plus"
                    ) as card3:
                        ui.image(source="assets/image1.png")
                        with ui.card_section():
                            ui.label("This is a card").classes("text-lg font-semibold")
                        with ui.card_section():
                            ui.button("Click me").classes("")
                    with ui.card().tight().classes(
                        "border rounded-lg shadow-md card-plus"
                    ) as card4:
                        ui.image(source="assets/image1.png")
                        with ui.card_section():
                            ui.label("This is a card").classes("text-lg font-semibold")
                        with ui.card_section():
                            ui.button("Click me").classes(
                                "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                            )
        with ui.row().classes(
            "w-full h-2/3 bg-blue-500 text-white flex justify-center"
        ) as second_section:
            with ui.column().classes(
                "bg-blue-500 w-full p-4 text-white text-center mb-10"
            ) as col1:
                ui.label("We create amazing websites only with python").classes(
                    "text-center text-5xl font-bold w-full mb-2 mt-2" 
                )
                ui.label(
                    """lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                         ut labore et dolore magna aliqua lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"""
                )
                with ui.column().classes("w-full flex justify-center items-center") as container:
                    with ui.row().classes("w-full flex justify-center items-center") as row:
                        with ui.card().tight().classes(
                            "card-plus"
                        ) as card1:
                                with ui.card_section():
                                    with ui.row().classes("") as row:
                                        ui.icon("done").classes("text-5xl bg-blue-500 text-white rounded-full mr-4")
                                        
                                        with ui.column().classes(""):
                                            ui.label("Python").classes(" font-semibold text-black")
                                            ui.label("nicegui is a python web gui library").classes("text-gray-500")
                                        
                                    #ui.icon("done").classes("text-5xl bg-blue-500 text-white rounded-full mr-4")

                        with ui.column().classes(""):
                           with ui.card().tight().classes(
                            "card-plus"
                            ) as card2:
                                with ui.card_section():
                                    with ui.row().classes("") as row:
                                        ui.icon("done").classes("text-5xl bg-blue-500 text-white rounded-full mr-4")
                                        
                                        with ui.column().classes(""):
                                            ui.label("Python").classes(" font-semibold text-black")
                                            ui.label("nicegui is a python web gui library").classes("text-gray-500")
                        
                    with ui.row().classes(""):
                        with ui.card().tight().classes(
                            "card-plus"
                            ) as card3:
                                with ui.card_section():
                                    with ui.row().classes("") as row:
                                        ui.icon("done").classes("text-5xl bg-blue-500 text-white rounded-full mr-4")
                                        
                                        with ui.column().classes(""):
                                            ui.label("Python").classes(" font-semibold text-black")
                                            ui.label("nicegui is a python web gui library").classes("text-gray-500")
                        with ui.column().classes(""):
                            with ui.card().tight().classes(
                            "card-plus"
                            ) as card4:
                                with ui.card_section():
                                    with ui.row().classes("") as row:
                                        ui.icon("done").classes("text-5xl bg-blue-500 text-white rounded-full mr-4")
                                        
                                        with ui.column().classes(""):
                                            ui.label("Python").classes(" font-semibold text-black")
                                            ui.label("nicegui is a python web gui library").classes("text-gray-500")
                                   
      
        with ui.row().classes(
            "w-full h-screen text-white flex justify-center items-center bg-white"   
        ) as third_section:
            with ui.row().classes("w-1/4 flex flex-row shadow-lg h-1/2 rounded-lg bg-blue-500 animate__slideInRight") as col1:
                with ui.row() as row2:
                    with ui.column().classes("p-4") as col1:
                        ui.label("Why choose us").classes("text-2xl font-bold mb-2 w-full text-center")
                        ui.label("""lorem ipsum dolor sit amet, consectetur
                                adipiscing elit, sed do eiusmod tempor 
                                incididunt ut labore et dolore magna aliqua
                                """).classes("w-full text-mg")
                        ui.label("""lorem ipsum dolor sit amet, consectetur sit amet, consectetur, elit, sed do eiusmod tempor""").classes("w-full text-mg")
                        ui.button("Read More").classes("bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mx-auto")
            with ui.row().classes("w-1/3 h-1/3 bg-white flex justify-center items-center animate__slideInLeft") as col2:
                ui.image(source="assets/img3.png").classes("img-spe")

       
                
                """with ui.column().classes(
                    "flex flex-col bg-blue-800 w-1/2 p-4 text-white text-center"  
                ) as col1:
                    ui.label("Why choose us").classes("text-xl font-bold mb-2")
                    ui.label(lorem ipsum dolor sit amet, consectetur
                            adipiscing elit, sed do eiusmod tempor 
                            incididunt ut labore et dolore magna aliqua
                            ).classes("w-1/4 text-mg")
                    ui.button("Read More").classes("bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded")"""
                    
                

    def contactForm(self):
        with ui.row().classes("flex justify-center items-center w-full h-2/3 animate__slideInUp"):
            with ui.column().classes("bg-white w-1/2 p-4 shadow-lg") as col1:
                self.welcomeLabel = ui.markdown("### Get in touch").classes(
                    "text-lg font-semibold mx-auto"
                )
                self.separator = ui.separator().classes("w-2/3 bg-gray-800 mb-4 mx-auto")
                self.input_name = ui.input(
                    label="Your Name", placeholder="John Doe"
                ).classes(
                    "w-full mb-4 px-4 py-2 focus:outline-none focus:border-green-500 rounded-lg"
                )
                self.input_email = ui.input(
                    label="Your Email", placeholder="example@example.com"
                ).classes(
                    "w-full mb-4 px-4 py-2 focus:outline-none focus:border-green-500 rounded-lg"
                )
                self.subject = ui.input(label="Subject", placeholder="Subject").classes(
                    "w-full px-4 py-2 focus:outline-none focus:border-green-500 rounded-lg"
                )
                self.textarea_message = ui.textarea(label="Your Message").classes(
                    "w-full mb-4 px-4 py-2 focus:outline-none focus:border-green-500 resize-none h-32 rounded-lg"
                )
                self.button_submit = ui.button("Send Message", color="green").classes(
                    "w-full px-4 py-2 bg-green-500 text-white hover:bg-green-600 focus:outline-none focus:bg-green-600 rounded-lg mx-auto"
                )
                self.button_submit.on_click(self.on_click)

            with ui.column().classes("bg-blue-400 w-1/3 h-1/2 p-8 shadow-lg text-white") as col2:
                self.contactLabel = ui.markdown("### Contact Us").classes(
                    "text-lg font-semibold mb-4"
                )
                self.separator = ui.separator().classes("w-2/3 bg-white mb-4")
                with ui.row().classes("flex items-center mb-4"):
                    self.icon = ui.icon("phone").classes("text-5xl text-blue-500 mr-4")
                    self.phoneLabel = ui.label("Phone : +1 234 567 890").classes(
                        "text-lg"
                    )
                with ui.row().classes("flex items-center mb-4"):
                    self.icon = ui.icon("email").classes("text-5xl text-blue-500 mr-4")
                    self.emailLabel = ui.label("Email : example@email.com").classes(
                        "text-lg"
                    )
                with ui.row().classes("flex items-center mb-4"):
                    self.icon = ui.icon("o_home").classes("text-4xl text-blue-500 mr-4").classes("ml-1")
                    self.locationLabel = ui.label(
                        "Loc : 123 Street, City, Country"
                    ).classes("text-lg")

    # Methods
    def runWebsite(self):
        self.home_page()
        ui.run()

    def dark_mode(self):
        if not self.is_enabled:
            self.is_enabled = True
            print(self.is_enabled)
            self.background = ui.query("body").style("background-color: black")

        else:
            self.is_enabled = False
            print(self.is_enabled)
            self.background = ui.query("body").style("background-color: lightblue")

    def on_click(self):
        ui.notify("Button clicked")
        self.button_submit.text = "Clicked"

    def change_bg(self, style):
        self.query("body").style(f"background: {style};")

    def contact_page(self):
        self.current_page = "/Contact"
        self.set_style()
        self.create_navbar()
        self.contactForm()
        self.create_footer()

    def about_page(self):
        self.current_page = "/About"
        self.set_style()
        self.create_navbar()
        self.create_footer()

    def home_page(self):
        self.current_page = "/"
        self.set_style()
        self.create_navbar()
        self.main_section()
        self.create_footer()




"""
@ui.page("/About")
def about():
    website.about_page()
@ui.page("/Contact")
def contact():
    website.contact_page()  

website = MyWebsite()
website.runWebsite()
"""








