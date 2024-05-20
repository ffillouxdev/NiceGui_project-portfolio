from nicegui import ui
from animationJs import slide_left, slide_right, all_gsap, fadeIn


def create_card_tech(icon, text):
    with ui.card().tight().classes("cardLang hover:bg-blue-200") as card:
        with ui.row().classes("flex justify-center items-center") as row:
            ui.image(source=f"assets/{icon}").classes("w-1/2 p-6")
            # ui.label(text).classes("text-xs font-semibold text-black text-center")


def content() -> None:
    ui.page_title("Home")
    ui.context.client.content.classes("p-0 gap-0")
    # ici met moi une fonction qui appelle gsap
    # slide_left(".animate_slideInLeft")
    # slide_right(".animate_slideInRight")
    # fadeIn(".textfade")
    all_gsap()
    with ui.element("div").classes(
        "container w-full h-full p-0 gap-0"
    ) as section_container:
        ui.html(
            """
                        <section class="parallax_group w-[98.5vw] h-[100vh]">
                            <img src="static/parallax/montainss2.png" class="w-[98vw] h-[100vh] montains2" alt="montains2">
                            <img src="static/parallax/montainss3.png" class="w-[98vw] h-[100vh]" alt="montains3">
                            <img src="static/parallax/montainss4.png" class="w-full h-[100vh] montains4" alt="montains4">
                            <img src="static/parallax/dune-bottom.png" class="w-full h-[100vh] dune1 absolute z-20" alt="dune1">
                            <img src="static/parallax/moon.png" class="moon absolute top-40 z-10" alt="moon" style="transform: translateY(-20vh);">
                            <img src="static/parallax/star1.png" class="star1 ml-[40%]" alt="star1">
                            <img src="static/parallax/star2.png" class="star2 ml-[45%]" alt="star2">
                            <h1 class="font-bold text-white text-center text-6xl mt-[25vh] md:text-6xl relative z-10">Florian Filloux</h1>
                        </section>
                        """
        )
        with ui.element("section").classes(
            "second section w-full h-[100vh]"
        ) as second_section:
            with ui.row().classes("w-full h-[100vh]"):
                with ui.grid(columns=2).classes("w-full h-full FKIRUABB pt-[5%] ]"):
                    with ui.column().classes(
                        "animate_slideInRight title_section"
                    ) as col1:
                        ui.html(
                            "<h1 class='text-6xl font-bold text-white text-left pl-8 pt-8 pr-8'>Bienvenue sur <br> mon site</h1>"
                        )
                        ui.html(
                            "<p class='text-white text-left pl-9'>c'est un site simple utilisant nicegui ! <br> 'mettre ma tete en fond'</p>"
                        )

                    with ui.column().classes("mt-[7%] ml-[35%]") as col2:
                        with ui.grid(columns=2).classes():
                            with ui.column().classes("card-container1") as col_2_1:
                                with ui.row().classes("flex flex-col"):
                                    with ui.card().tight().classes(
                                        "border rounded-lg shadow-md card-plus flex flex-col justify-center items-center pt-6"
                                    ) as card1:
                                        ui.image(source="assets/logdm.webp").classes(
                                            "w-1/2"
                                        )
                                        with ui.card_section():
                                            ui.label("DouceMob'").classes(
                                                "text-lg font-semibold text-center ml-2"
                                            )
                                        with ui.card_section().classes(""):
                                            ui.button(
                                                "Click me",
                                                on_click=lambda e: ui.navigate.to(
                                                    "http://p2203403.pages.univ-lyon1.fr/sae-webs1/",
                                                    new_tab=True,
                                                ),
                                            ).classes(
                                                "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4"
                                            )

                                    with ui.card().tight().classes(
                                        "border rounded-lg shadow-md card-plus flex flex-col justify-center items-center pt-6"
                                    ) as card2:
                                        ui.image(
                                            source="assets/logo_logiCompta.png"
                                        ).classes("w-2/3")
                                        with ui.card_section():
                                            ui.label("LogiCompta").classes(
                                                "text-lg font-semibold text-center"
                                            )
                                        with ui.card_section().classes(""):
                                            ui.button(
                                                "Click me",
                                                on_click=lambda e: ui.navigate.to(
                                                    "https://ffillouxdev.github.io/logicompta-website/",
                                                    new_tab=True,
                                                ),
                                            ).classes(
                                                "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4"
                                            )
                            with ui.column().classes("card-container2") as col_2_2:
                                with ui.row().classes("flex flex-col"):
                                    with ui.card().tight().classes(
                                        "border rounded-lg shadow-md card-plus flex flex-col justify-center items-center pt-6"
                                    ) as card3:
                                        ui.image(source="assets/image1.png").classes(
                                            "w-1/2"
                                        )
                                        with ui.card_section():
                                            ui.label("GestionAir").classes(
                                                "text-lg font-semibold w-[120px] text-center gestionair"
                                            )
                                        with ui.card_section().classes(""):
                                            ui.button(
                                                "Click me",
                                                on_click=lambda e: ui.navigate.to(
                                                    "https://github.com/ffillouxdev/GESTIONAIR",
                                                    new_tab=True,
                                                ),
                                            ).classes(
                                                "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4"
                                            )

                                    with ui.card().tight().classes(
                                        "border rounded-lg shadow-md card-plus flex flex-col justify-center items-center pt-6"
                                    ) as card4:
                                        ui.image(source="assets/nicegui.png").classes(
                                            "w-1/2"
                                        )
                                        with ui.card_section():
                                            ui.label("NiceGui").classes(
                                                "text-lg font-semibold w-[120px] text-center"
                                            )
                                        with ui.card_section().classes():
                                            ui.button(
                                                "Click me",
                                                on_click=lambda e: ui.navigate.to(
                                                    "https://github.com/ffillouxdev/NiceGui_project",
                                                    new_tab=True,
                                                ),
                                            ).classes(
                                                "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded nicegui"
                                            )
        with ui.element("section").classes(
            "third section h-screen w-screen"
        ) as third_section:
            with ui.row().classes(""):
                ui.markdown("# Mes technologies actuelles").classes("text-5xl font-bold text-white w-full text-center mt-8 title1")
                ui.separator().classes("w-1/4 bg-white h-1 mt-2 mb-2 mx-auto")

                with ui.row().classes(
                    "flex justify-center items-center mb-2 slideUp"
                ) as row2:
                    create_card_tech("windows.png", "Windows")
                    create_card_tech("python.png", "Python")
                    create_card_tech("cpp.png", "C++")
                    create_card_tech("c.png", "C")
                    create_card_tech("java.png", "Java")
                    create_card_tech("django.png", "Django")
                    create_card_tech("node.png", "Node.js")
                    create_card_tech("react.png", "React")
                    create_card_tech("js.png", "Javascript")

        with ui.element("section").classes(
            "w-full h-2/3 text-white flex justify-center section2 hover_title_2 fourth section"
        ) as fourth_section:
            with ui.row().classes(""):
                with ui.column().classes(
                    " w-full p-4 text-white text-center mb-10"
                ) as col1:
                    ui.label("Qui suis-je ?").classes(
                        "text-center text-5xl font-bold w-full mb-2 mt-2 title2"
                    )
                    ui.label(
                        """je suis un jeune en but informatique qui aimerait lié mes passions au domaine de la technologie innovante, tel 
                            que l'aéronatique et le spatial, les banques, la recherche et d'autres. Je suis un touche à tout, j'aime apprendre 
                            et j'aime savoir comment les choses fonctionnent. J'ai 4 centres d'intéréts prédominants qui sont les suivants :
                            """
                    ).classes("textfade")
                    with ui.column().classes(
                        "w-full flex justify-center items-center"
                    ) as container:
                        with ui.row().classes(
                            "w-full flex justify-center items-center"
                        ) as row:
                            with ui.card().tight().classes("card-plus1") as card1:
                                with ui.card_section():
                                    with ui.row().classes("") as row:
                                        ui.icon("done").classes(
                                            "text-5xl bg-blue-500 text-white rounded-full mr-4"
                                        )

                                        with ui.column().classes(""):
                                            ui.label("Python").classes(
                                                " font-semibold text-black"
                                            )
                                            ui.label(
                                                "Pour la simplicité et sa communauté"
                                            ).classes("text-gray-500")

                            with ui.column().classes(""):
                                with ui.card().tight().classes("card-plus1") as card2:
                                    with ui.card_section():
                                        with ui.row().classes("") as row:
                                            ui.icon("done").classes(
                                                "text-5xl bg-blue-500 text-white rounded-full mr-4"
                                            )

                                            with ui.column().classes(""):
                                                ui.label("C++").classes(
                                                    " font-semibold text-black"
                                                )
                                                ui.label(
                                                    "Pour la performance et l'architecture"
                                                ).classes("text-gray-500")

                        with ui.row().classes(""):
                            with ui.card().tight().classes("card-plus1") as card3:
                                with ui.card_section():
                                    with ui.row().classes("") as row:
                                        ui.icon("done").classes(
                                            "text-5xl bg-blue-500 text-white rounded-full mr-4"
                                        )

                                        with ui.column().classes(""):
                                            ui.label("Aéronautique").classes(
                                                " font-semibold text-black"
                                            )
                                            ui.label(
                                                "C'est une passion qui me tient à coeur"
                                            ).classes("text-gray-500")
                            with ui.column().classes(""):
                                with ui.card().tight().classes("card-plus1") as card4:
                                    with ui.card_section():
                                        with ui.row().classes("") as row:
                                            ui.icon("done").classes(
                                                "text-5xl bg-blue-500 text-white rounded-full mr-4"
                                            )

                                            with ui.column().classes(""):
                                                ui.label("Informatique").classes(
                                                    " font-semibold text-black"
                                                )
                                                ui.label(
                                                    "Je veux en faire mon métier plus tard"
                                                ).classes("text-gray-500")
        with ui.element("section").classes(
            "w-full h-screen hover_section2 fifth section"
        ) as fifth_section:
            with ui.row().classes("flex justify-center items-center text-white"):
                with ui.row().classes(
                    "w-1/4 flex flex-row shadow-lg h-1/2 rounded-lg bg-blue-500 animate_slideInRight el1"
                ) as col1:
                    with ui.row() as row2:
                        with ui.column().classes("h-[400px] p-2") as col1:
                            ui.label("Pourquoi me choisir ?").classes(
                                "text-2xl font-bold mb-2 w-full text-center"
                            )
                            ui.label(
                                """
                                Je suis passionné par la création et l'innovation dans le domaine de la technologie. 
                                Mon parcours est façonné par une curiosité insatiable et un désir constant d'apprendre. 
                            
                                """
                            ).classes("w-full text-mg")
                            ui.label(
                                """
                                J'explore des horizons variés, de l'aéronautique à la finance, de la recherche à la programmation. 
                                """
                            ).classes("w-full text-mg")

                            ui.button(
                                "Read More", on_click=lambda: ui.navigate.to("/About/")
                            ).classes(
                                "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mx-auto"
                            )
                with ui.row().classes(
                    "w-1/3 h-1/3 bg-white flex justify-center items-center animate_slideInLeft el2"
                ) as col2:
                    ui.image(source="assets/image3.png").classes("img-spe")
