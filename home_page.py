from nicegui import ui
from animationJs import slide_left, slide_right, all_gsap


def content() -> None:
    ui.page_title("Home")
    #ici met moi une fonction qui appelle gsap 
    slide_left('.animate_slideInLeft')
    slide_right('.animate_slideInRight')
    all_gsap()
    with ui.row().classes(
        "flex justify-bottom items-left w-full h-screen"
    ) as first_section:
        ui.html(
            """
                <div class="mt- animate_slideInRight title_section">
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
        "w-full h-2/3 bg-blue-500 text-white flex justify-center section2"
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
        "w-full h-screen text-white flex justify-center items-center bg-white hover_section2"   
    ) as third_section:
        with ui.row().classes("w-1/4 flex flex-row shadow-lg h-1/2 rounded-lg bg-blue-500 animate_slideInRight el1") as col1:
            with ui.row() as row2:
                with ui.column().classes("p-4") as col1:
                    ui.label("Why choose us").classes("text-2xl font-bold mb-2 w-full text-center")
                    ui.label("""lorem ipsum dolor sit amet, consectetur
                            adipiscing elit, sed do eiusmod tempor 
                            incididunt ut labore et dolore magna aliqua
                            """).classes("w-full text-mg")
                    ui.label("""lorem ipsum dolor sit amet, consectetur sit amet, consectetur, elit, sed do eiusmod tempor""").classes("w-full text-mg")
                    ui.button("Read More", on_click=lambda: ui.navigate.to("/About/")).classes("bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mx-auto")
        with ui.row().classes("w-1/3 h-1/3 bg-white flex justify-center items-center animate_slideInLeft el2") as col2:
            ui.image(source="assets/img3.png").classes("img-spe")
        
            
            
   