from nicegui import ui

is_enabled = False
current_page = "/"
button_submit = None

def set_style():
    global is_enabled
    # General styles
    if is_enabled:
        background = ui.query("body").style("background-color: black")
        foreground = ui.query("a").classes("text-white")
    else:
        background = ui.query("body").style("background-color: lightblue")
        foreground = ui.query("a").classes("text-white")

    dark = ui.dark_mode()
    style = ui.add_head_html(
        """
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
    """
    )


def create_navbar():
    global current_page
    with ui.header().classes(
        "flex justify-between items-center transparent no-shadow"
    ) as tabs:
        with ui.row().classes("flex justify-center items-center w-full"):
            home = ui.link("Home", "/").classes(
                "text-lg font-bold no-underline hover:underline"
                + (" text-red" if current_page == "/" else "")
            )
            about = ui.link("About", "/About").classes(
                "text-lg font-bold no-underline hover:underline"
                + (" text-red" if current_page == "/About" else "")
            )
            contact = ui.link("Contact", "/Contact").classes(
                "text-lg font-bold no-underline hover:underline"
                + (" text-red" if current_page == "/Contact" else "")
            )
            dark_button1 = ui.button("Dark", on_click=dark_mode)
        with ui.row().classes("flex justify-center items-center w-full"):
            separator1 = ui.separator().classes("w-1/3 bg-white")


def create_footer():
    with ui.footer().classes(
        "flex justify-center items-center w-full h-16 bg-gray-800 text-white fixed bottom-0"
    ) as footer:
        footerLabel = ui.label("© 2024 All rights reserved")
        with ui.row().classes("flex justify-center items-center w-full"):
            separator2 = ui.separator().classes("w-1/3 bg-white")



def main_section():
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


def contactForm():
    with ui.row().classes(
        "flex justify-center items-center w-full h-2/3 animate__slideInUp"
    ):
        with ui.column().classes("bg-white w-1/2 p-4 shadow-lg") as col1:
            welcomeLabel = ui.markdown("### Get in touch").classes(
                "text-lg font-semibold mx-auto"
            )
            separator = ui.separator().classes("w-2/3 bg-gray-800 mb-4 mx-auto")
            input_name = ui.input(label="Your Name", placeholder="John Doe").classes(
                "w-full mb-4 px-4 py-2 focus:outline-none focus:border-green-500 rounded-lg"
            )
            input_email = ui.input(
                label="Your Email", placeholder="example@example.com"
            ).classes(
                "w-full mb-4 px-4 py-2 focus:outline-none focus:border-green-500 rounded-lg"
            )
            subject = ui.input(label="Subject", placeholder="Subject").classes(
                "w-full px-4 py-2 focus:outline-none focus:border-green-500 rounded-lg"
            )
            textarea_message = ui.textarea(label="Your Message").classes(
                "w-full mb-4 px-4 py-2 focus:outline-none focus:border-green-500 resize-none h-32 rounded-lg"
            )
            button_submit = ui.button("Send Message", color="green").classes(
                "w-full px-4 py-2 bg-green-500 text-white hover:bg-green-600 focus:outline-none focus:bg-green-600 rounded-lg mx-auto"
            )
            button_submit.on_click(on_click)

        with ui.column().classes(
            "bg-blue-400 w-1/3 h-1/2 p-8 shadow-lg text-white"
        ) as col2:
            contactLabel = ui.markdown("### Contact Us").classes(
                "text-lg font-semibold mb-4"
            )
            separator = ui.separator().classes("w-2/3 bg-white mb-4")
            with ui.row().classes("flex items-center mb-4"):
                icon = ui.icon("phone").classes("text-5xl text-blue-500 mr-4")
                phoneLabel = ui.label("Phone : +1 234 567 890").classes("text-lg")
            with ui.row().classes("flex items-center mb-4"):
                icon = ui.icon("email").classes("text-5xl text-blue-500 mr-4")
                emailLabel = ui.label("Email : example@email.com").classes("text-lg")
            with ui.row().classes("flex items-center mb-4"):
                icon = (
                    ui.icon("o_home")
                    .classes("text-4xl text-blue-500 mr-4")
                    .classes("ml-1")
                )
                locationLabel = ui.label("Loc : 123 Street, City, Country").classes(
                    "text-lg"
                )


def dark_mode():
    global is_enabled
    if not is_enabled:
        is_enabled = True
        print(is_enabled)
        background = ui.query("body").style("background-color: black")

    else:
        is_enabled = False
        print(is_enabled)
        background = ui.query("body").style("background-color: lightblue")


def on_click():
    ui.notify("Button clicked")
    button_submit.text = "Clicked"


def home_page():
    global current_page
    current_page = "/"
    set_style()
    create_navbar()
    main_section()
    create_footer()


    

# Define pages
@ui.page("/About")
def about():
    global current_page
    current_page = "/About"
    set_style()
    create_navbar()
    create_footer()



@ui.page("/Contact")
def contact():
    global current_page
    current_page = "/Contact"
    set_style()
    create_navbar()
    contactForm()
    create_footer()



# Run website
home_page()
ui.run()
