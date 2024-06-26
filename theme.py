from contextlib import contextmanager
from nicegui import ui, app
from assets.style import setupStyle


app.add_static_files("/static", "assets/")
# Ajoute le fichier gsap.js comme fichier statique


is_enabled = False
current_page = "/"
button_submit = None
have_checked = False


def dark_mode():
    global is_enabled
    global current_page
    if not is_enabled:
        is_enabled = True
        print(is_enabled)

    else:
        is_enabled = False
        print(is_enabled)


@contextmanager
def frame(navtitle: str):
    """Custom page frame to share the same styling and behavior across all pages"""
    # Set style
    global is_enabled
    global have_checked
    global current_page
    current_page = navtitle
    setupStyle()
    # General styles
    if is_enabled:
        background = ui.query("body").classes("bg-black")
        foreground = ui.query("a").classes("text-white")
    else:
        background = ui.query("body").style("""margin: 0; padding: 0; width: 100%; background: url('static/parallax/montainsss.jpg') no-repeat center center fixed; background-size: cover""")
        foreground = ui.query("a").classes("text-white")

    dark = ui.dark_mode()
    style = ui.add_head_html(
        """
        <script src="/static/js/gsap.js"></script>
        <link rel="stylesheet" type="text/css" href="/static/css/style.css">
        <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/ScrollTrigger.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/ScrambleTextPlugin.min.js"></script>
        """
    )

    # Create a welcome cookies dialog
    if not have_checked:
        with ui.dialog() as dialog:
            with ui.column().classes("text-blue-500 bg-white p-4 rounded-lg shadow-lg"):
                ui.label("Welcome to our website!").classes(
                    "text-lg font-semibold mb-2 text-center w-full"
                )
                ui.html(
                    """
                    <p class="text-black text-center">We use cookies to improve user experience on our website.</p>
                    <p class="text-black text-center">By clicking "Accept", you consent to the use of all cookies.</p>
                """
                )
                ui.button("Accept", on_click=dialog.close).classes(
                    "mt-4 mx-auto bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 focus:outline-none focus:bg-blue-600"
                )
                have_checked = True
            dialog.open()

    # Create navbar
    with ui.header().classes(
        "flex justify-between items-center transparent no-shadow navbar"
    ) as tabs:
        with ui.row().classes("flex justify-between items-center w-full h-10"):
            with ui.row().classes():
                ui.label("FFillouxdev").classes("text-lg font-bold no-underline")
                ui.separator().classes("w-3/4 mt-[-15px] ml-0.5 mr-0.5 bg-blue h-0.5")
            with ui.row().classes("flex items-center"):
                home = ui.link("Home", "/").classes(
                    "text-lg font-bold no-underline hover:underline"
                    + (" text-blue" if navtitle == "Homepage" else "")
                )
                contact = ui.link("Contact", "/Contact").classes(
                    "text-lg font-bold no-underline hover:underline"
                    + (" text-blue" if navtitle == "Contact" else "")
                )
                dark_button1 = ui.button("Dark", on_click=dark_mode, color="blue")
    yield


"""
  # Create footer
    with ui.footer().classes(
        "flex justify-center items-center w-full h-16 text-white fixed bottom-0 bg-blue"
    ) as footer:
        footerLabel = ui.label("© 2024 All rights reserved")
        logo = ui.image(source="assets/logo.jpg").classes("w-6 h-6")
        with ui.row().classes("flex justify-center items-center w-full"):
            separator2 = ui.separator().classes("w-1/3 bg-white")
"""
