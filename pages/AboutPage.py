import theme
import numpy as np
from nicegui import ui
from matplotlib import pyplot as plt
from utils.recupData import refresh_CounterForWebsiteTrafic, init_db, close_db, refresh_CounterFoProjectsNumber, recup_CounterOfCommits


async def aboutPage():
    await init_db()
    val = await recup_CounterOfCommits()
    print(val)
    try:
        with theme.frame("About"):
            ui.page_title("About me")
            ui.context.client.content.classes("p-0 gap-0")
            with ui.row() as first_section:
                with ui.grid(columns=2).classes("first_section"):
                    with ui.column().classes("ml-8"):
                        ui.image(source="assets/about.png").classes("img1")
                    with ui.column().classes("w-2/3 p-4"):
                        ui.label("A propos de moi").classes(
                            "text-center text-white text-4xl font-semibold pt-4"
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
            with ui.row().classes("h-screen w-[100%] bg-blue-500") as second_section:
                ui.html(
                    """
                    <div class="w-[98vw]">
                        <h2 class="text-5xl font-bold text-white w-full text-center mt-8">Quelques données sur mon activité</h2>
                        <hr class="w-1/4 bg-white h-1 mt-2 mb-2 mx-auto">
                    </div>
                    """
                )
                with ui.grid(columns=3).classes("flex justify-center h-full w-full"):
                    with ui.column().classes("bg-gray-200 p-4 h-1/3 w-[400px] ml-7"):
                        ui.label("Mon compteur de contributions Github :").classes("")
                        with ui.pyplot(figsize=(3, 2)).classes(
                            "flex justify-center w-full"
                        ):
                            x = np.linspace(0.0, 5.0)
                            y = np.cos(2 * np.pi * x) * np.exp(-x)
                            plt.plot(x, y, "-")
                    with ui.column().classes("bg-gray-200 p-4 h-1/3 w-[400px]"):
                        ui.label("Nombre de projets réalisés :").classes("")
                        with ui.row().classes(
                            "border-2 border-black rounded-lg w-full mx-auto  flex justify-center items-center h-full"
                        ):
                            counterForLabel1 = await refresh_CounterFoProjectsNumber()
                            ui.label(f"{counterForLabel1}").classes(
                                "text-7xl text-center w-full"
                            )
                    with ui.column().classes("bg-gray-200 p-4 h-1/3 w-[400px]"):
                        ui.label("Nombre de visites sur mon site web :").classes("")
                        with ui.row().classes(
                            "border-2 border-black rounded-lg w-full mx-auto  flex justify-center items-center h-full"
                        ):
                            counterForLabel2 = await refresh_CounterForWebsiteTrafic()
                            ui.label(f"{counterForLabel2}").classes(
                                "text-7xl text-center w-full"
                            )
    finally:
        await close_db()
