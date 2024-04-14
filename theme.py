from contextlib import contextmanager
from nicegui import ui

is_enabled = False
current_page = "/"
button_submit = None
have_checked = False

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

@contextmanager
def frame(navtitle: str):
    """Custom page frame to share the same styling and behavior across all pages"""
    # Set style
    global is_enabled
    global have_checked
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
    
    #Create a welcome cookies dialog 
    if not have_checked:
        with ui.dialog() as dialog:
            with ui.column().classes("text-blue-500 bg-white p-4 rounded-lg shadow-lg"):
                ui.label("Welcome to our website!").classes("text-lg font-semibold mb-2 text-center w-full")
                ui.html("""
                    <p class="text-black text-center">We use cookies to improve user experience on our website.</p>
                    <p class="text-black text-center">By clicking "Accept", you consent to the use of all cookies.</p>
                """)
                ui.button("Accept", on_click=dialog.close).classes("mt-4 mx-auto bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 focus:outline-none focus:bg-blue-600")
                have_checked = True
            dialog.open()  
    
    # Create navbar
    with ui.header().classes(
        "flex justify-between items-center transparent no-shadow"
    ) as tabs:
        with ui.row().classes("flex justify-center items-center w-full"):
            home = ui.link("Home", "/").classes(
                "text-lg font-bold no-underline hover:underline"
                + (" text-red" if navtitle == "Homepage" else "")
            )
            about = ui.link("About", "/About").classes(
                "text-lg font-bold no-underline hover:underline"
                + (" text-red" if navtitle == "About" else "")
            )
            contact = ui.link("Contact", "/Contact").classes(
                "text-lg font-bold no-underline hover:underline"
                + (" text-red" if navtitle == "Contact" else "")
            )
            dark_button1 = ui.button("Dark", on_click=dark_mode)
        with ui.row().classes("flex justify-center items-center w-full"):
            separator1 = ui.separator().classes("w-1/3 bg-white")

    # Create footer
    with ui.footer().classes(
        "flex justify-center items-center w-full h-16 bg-gray-800 text-white fixed bottom-0"
    ) as footer:
        footerLabel = ui.label("© 2024 All rights reserved")
        with ui.row().classes("flex justify-center items-center w-full"):
            separator2 = ui.separator().classes("w-1/3 bg-white")
    yield

    
"""
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
    )


def create_navbar(navtitle: str):
    with ui.header().classes(
        "flex justify-between items-center transparent no-shadow"
    ) as tabs:
        with ui.row().classes("flex justify-center items-center w-full"):
            home = ui.link("Home", "/").classes(
                "text-lg font-bold no-underline hover:underline"
                + (" text-red" if navtitle == "/" else "")
            )
            about = ui.link("About", "/About").classes(
                "text-lg font-bold no-underline hover:underline"
                + (" text-red" if navtitle == "/About" else "")
            )
            contact = ui.link("Contact", "/Contact").classes(
                "text-lg font-bold no-underline hover:underline"
                + (" text-red" if navtitle == "/Contact" else "")
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
"""
