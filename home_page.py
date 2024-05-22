from nicegui import ui
from animationJs import slide_left, slide_right, all_gsap, fadeIn
from matplotlib import pyplot as plt
import numpy as np
from utils.recupData import (
    refresh_CounterForWebsiteTrafic,
    init_db,
    close_db,
    refresh_CounterFoProjectsNumber,
    recup_CounterOfCommits,
)


def create_card_tech(icon, text):
    with ui.card().tight().classes("cardLang hover:bg-blue-200") as card:
        with ui.row().classes("flex justify-center items-center") as row:
            ui.image(source=f"assets/{icon}").classes("w-1/2 p-6")
            # ui.label(text).classes("text-xs font-semibold text-black text-center")


async def content() -> None:
    await init_db()
    try:
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
                                            ui.image(
                                                source="assets/logdm.webp"
                                            ).classes("w-1/2")
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
                                            ui.image(
                                                source="assets/image1.png"
                                            ).classes("w-1/2")
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
                                            ui.image(
                                                source="assets/nicegui.png"
                                            ).classes("w-1/2")
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
                "third section h-[100vh]"
            ) as third_section:
                with ui.row().classes(""):
                    ui.markdown("# Mes technologies actuelles").classes(
                        "text-5xl font-bold text-white w-full text-center mt-8 title1"
                    )
                    ui.separator().classes("w-1/4 bg-white h-1 mt-2 mb-2 mx-auto")

                    with ui.row().classes(
                        "flex justify-center items-center mb-2 w-full mt-8"
                    ) as row2:
                        ui.label("software languages").classes("text-white")
                        create_card_tech("python.png", "Python")
                        create_card_tech("cpp.png", "C++")
                        create_card_tech("c.png", "C")
                        create_card_tech("java.png", "Java")
                    with ui.row().classes(
                        "flex justify-center items-center mb-2 w-full"
                    ) as row3:
                        ui.label("Développement web").classes("text-white")
                        create_card_tech("django.png", "Django")
                        create_card_tech("js.png", "Javascript")
                        create_card_tech("node.png", "Node.js")
                        create_card_tech("react.png", "React")

            with ui.element("section").classes(
                "w-full h-2/3 text-white flex justify-center section2 hover_title_2 fourth section"
            ) as fourth_section:
                with ui.row().classes(""):
                    ui.html(
                        """
                        <div class="w-[98vw]">
                            <h2 class="text-5xl font-bold text-white w-full text-center mt-8 title2">Quelques données sur mon activité</h2>
                            <hr class="w-1/4 bg-white h-1 mt-2 mb-2 mx-auto">
                        </div>
                        """
                    )
                    with ui.grid(columns=3).classes(
                        "flex justify-center h-full w-full"
                    ):
                        with ui.column().classes(
                            "bg-white p-4 h-1/3 w-[300px] ml-7 h-[150px]"
                        ):
                            ui.label("Mon compteur de contributions Github :").classes(
                                "text-black"
                            )
                            """with ui.pyplot(figsize=(3, 2)).classes(
                                "flex justify-center w-full"
                            ):
                                x = np.linspace(0.0, 5.0)
                                y = np.cos(2 * np.pi * x) * np.exp(-x)
                                plt.plot(x, y, "-")"""
                        with ui.column().classes(
                            "bg-white p-4 h-1/3 w-[300px] h-[150px]"
                        ):
                            ui.label("Nombre de projets github réalisés :").classes(
                                "text-black"
                            )
                            with ui.row().classes(
                                "border-2 border-black rounded-lg w-full mx-auto flex justify-center items-center h-full"
                            ):
                                counterForLabel1 = (
                                    await refresh_CounterFoProjectsNumber()
                                )
                                ui.label(f"{counterForLabel1}").classes(
                                    "text-7xl text-center w-full text-black"
                                )
                        with ui.column().classes(
                            "bg-white p-4 h-1/3 w-[300px]  h-[150px]"
                        ):
                            ui.label("Nombre de visites sur mon site web :").classes(
                                "text-black"
                            )
                            with ui.row().classes(
                                "border-2 border-black rounded-lg w-full mx-auto flex justify-center items-center h-full"
                            ):
                                counterForLabel2 = (
                                    await refresh_CounterForWebsiteTrafic()
                                )
                                ui.label(f"{counterForLabel2}").classes(
                                    "text-7xl text-center w-full text-black"
                                )
            with ui.element("section").classes(
                "w-full h-screen hover_section2 fifth section"
            ) as fifth_section:
                with ui.row().classes("flex justify-center items-center text-white"):
                    with ui.row().classes(
                        "w-1/4 flex flex-row shadow-lg h-1/2 rounded-lg bg-blue-500 animate_slideInRight el1"
                    ) as col1:
                        with ui.row() as row2:
                            with ui.column().classes(
                                "h-[420px] w-[300px] pl-4 pr-6"
                            ) as col1:
                                ui.label("A propos de moi").classes(
                                    "text-center text-white text-4xl font-semibold pt-4 title3"
                                )
                                ui.label("Bienvenue sur mon portfolio !").classes(
                                    "text-bold text-white text-lg"
                                )
                                ui.label(
                                    """
                                        Chaque jour, je m'efforce de progresser pour pouvoir un jour combiner mes passions avec mon travail. Actuellement à la recherche d'opportunités professionnelles, je suis particulièrement intéressé par les domaines de l'aéronautique, de la finance et du spatial, tout en cherchant à les fusionner avec le monde de l'informatique.
                                        """
                                ).classes("text-white w-full")

                                ui.button(
                                    "Mon CV",
                                    on_click=lambda: ui.run_javascript(
                                        """
                                        console.log('downloadCV')
                                        function downloadCV(){
                                            let boutonDownload = document.querySelectorAll('.downloadCV');
                                            boutonDownload.forEach((bouton) => {
                                                bouton.addEventListener('click', () => {
                                                    window.open('/static/downloads/version1.pdf'); 
                                                });
                                            });
                                        }
                                        downloadCV();
                                    """
                                    ),
                                ).classes(
                                    "bg-blue-500 text-white text-md px-8 py-3 rounded-lg hover:bg-blue-600 focus:outline-none focus:bg-blue-600 downloadCV"
                                )
                    with ui.row().classes(
                        "w-1/3 h-1/3 flex justify-center items-center animate_slideInLeft el2"
                    ) as col2:
                        ui.image(source="assets/imageAboutME.jpg").classes("img-spe")
    finally:
        await close_db()
