import theme
from nicegui import ui


def aboutPage():
    with theme.frame("About"):
        ui.page_title("About me")
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

