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
            "flex justify-center items-center w-full h-16 bg-gray-800 text-white fixed"
        ) as footer:
            self.footerLabel = ui.label("© 2024 All rights reserved")

    def main_section(self):
        with ui.row().classes(
            "flex justify-bottom items-left w-full h-screen"
        ) as first_section:
            ui.html(
                """
                    <div class="mt-8">
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
            "w-full h-screen bg-blue-500 text-white flex justify-center"
        ) as second_section:
            with ui.column().classes(
                "bg-blue-500 w-1/2 p-4 text-white text-center"
            ) as col1:
                ui.label("We create amazing websites only with python").classes(
                    "text-center text-4xl font-bold"
                )
                ui.label(
                    """lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                         ut labore et dolore magna aliqua lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"""
                )
                with ui.card().tight().classes(
                    "border rounded-lg shadow-md w-full flex flex-row items-center p-2"
                ) as card1:
                        ui.icon("done").classes("text-5xl bg-blue-500 text-white rounded-full mr-4")
                        ui.label("This is a card").classes("text-lg font-semibold text-blue-500")
                with ui.card().tight().classes(
                    "border rounded-lg shadow-md w-full flex flex-row items-center p-2"
                ) as card1:
                        ui.icon("done").classes("text-5xl bg-blue-500 text-white rounded-full mr-4")
                        ui.label("This is a card").classes("text-lg font-semibold text-blue-500")
                with ui.card().tight().classes(
                    "border rounded-lg shadow-md w-full flex flex-row items-center p-2"
                ) as card1:
                        ui.icon("done").classes("text-5xl bg-blue-500 text-white rounded-full mr-4")
                        ui.label("This is a card").classes("text-lg font-semibold text-blue-500")
                with ui.card().tight().classes(
                    "border rounded-lg shadow-md w-full flex flex-row items-center p-2"
                ) as card1:
                        ui.icon("done").classes("text-5xl bg-blue-500 text-white rounded-full mr-4")
                        ui.label("This is a card").classes("text-lg font-semibold text-blue-500")
                

        with ui.row().classes(
            "w-full h-screen bg-yellow-500 text-white"
        ) as third_section:
            with ui.column().classes(
                "bg-yellow-500 w-1/2 p-4 text-white text-center"
            ) as col1:
                ui.label("We create amazing websites only with python").classes(
                    "text-center text-4xl font-bold"
                )
                ui.label(
                    """lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                         ut labore et dolore magna aliqua lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"""
                )

    def contactForm(self):
        with ui.row().classes("flex justify-center items-center w-full h-screen"):
            with ui.column().classes("bg-blue-500 w-1/2 p-4 shadow-lg") as col1:
                self.welcomeLabel = ui.markdown("### Get in touch").classes(
                    "text-lg font-semibold mb-4"
                )
                self.separator = ui.separator().classes("w-full bg-gray-800 mb-4")
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
                    "w-full mb-4 px-4 py-2 focus:outline-none focus:border-green-500 rounded-lg"
                )
                self.textarea_message = ui.textarea(label="Your Message").classes(
                    "w-full mb-4 px-4 py-2 focus:outline-none focus:border-green-500 resize-none h-32 rounded-lg"
                )
                self.button_submit = ui.button("Send Message", color="green").classes(
                    "w-full px-4 py-2 bg-green-500 text-white hover:bg-green-600 focus:outline-none focus:bg-green-600 rounded-lg"
                )
                self.button_submit.on_click(self.on_click)

            with ui.column().classes("bg-yellow-500 w-1/3 h-1/2 p-8 shadow-lg") as col2:
                self.contactLabel = ui.markdown("### Contact Us").classes(
                    "text-lg font-semibold mb-4"
                )
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
                    self.icon = ui.icon("o_home").classes("text-5xl text-blue-500 mr-4")
                    self.locationLabel = ui.label(
                        "Location : 123 Street, City, Country"
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


# Pages     
@ui.page("/About")
def about():
    website.about_page()
@ui.page("/Contact")
def contact():
    website.contact_page()  



website = MyWebsite()
website.runWebsite()
 

        

"""
# Example component
def create_card():
    with ui.card().tight() as card:
        ui.image(source="assets/image1.png")
        with ui.card_section():
            ui.label("This is a card")
        with ui.card_section():
            ui.button("Click me")
    return card

"""
