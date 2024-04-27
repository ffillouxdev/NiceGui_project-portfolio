from nicegui import ui
from components.default_button import defaultBut1, defaultBut2
from components.default_footer import defaultFoo1, defaultFoo2
from components.default_navbar import defaultNav1, defaultNav2
from components.media.defaut_size_picture import defaultImg1, defaultImg2
from components.media.defaut_size_video import defaultVid1, defaultVid2
import theme

list_of_components = []


def setComponentOnScreen(component):
    list_of_components.append(component)
    if component is "button1":
        defaultBut1()
    elif component is "button2":
        defaultBut2()
    elif component is "footer1":
        defaultFoo1()
    elif component is "footer2":
        defaultFoo2()
    elif component is "navbar1":
        defaultNav1()
    elif component is "navbar2":
        defaultNav2()
    elif component is "img1":
        defaultImg1()
    elif component is "img2":
        defaultImg2()
    elif component is "img2":
        defaultVid1()
    elif component is "img2":
        defaultVid1()
    else:
        with ui.dialog():
            with ui.card():
                ui.label("components doesn't exist.")


def removeComponent(component):
    list_of_components.remove(component)


def editComponent(component):
    pass


def selectComponent(component):
    pass


def exportWebsite():
    pass


def setColor(color):
    pass


def setForeground(color):
    pass


def setFont(font):
    pass


def setFontSize(size):
    pass


def setFontStyle(style):
    pass


def setFontWeight(weight):
    pass


def setFontDecoration(decoration):
    pass


def setFontAlign(align):
    pass


def dragComponent(component):
    pass


def dropComponent(component):
    pass


def yourWebsite():
    with theme.frame("YourWebsite") as frame:
        ui.page_title("YourWebsite")
        with ui.row().classes("w-full h-screen bg-gray-200 flex justify-between"):
            with ui.column().classes("bg-red-200 w-4/5 h-full") as screenEditor:
                pass
            with ui.column().classes("bg-white w-1/6 h-full"):
                ui.markdown("#### Components").classes("text-center w-full")
                ui.separator().classes("bg-black w-1/3 mx-auto lessTopGap")
                ui.tree(
                    [
                        {
                            "id": "navbar",
                            "children": [{"id": "navbar1"}, {"id": "navbar2"}],
                        },
                        {
                            "id": "footer",
                            "children": [{"id": "footer1"}, {"id": "footer2"}],
                        },
                        {
                            "id": "buttons",
                            "children": [{"id": "button1"}, {"id": "button2"}],
                        },
                        {
                            "id": "contenteditable",
                            "children": [{"id": "choice1"}, {"id": "choice2"}],
                        },
                        {
                            "id": "containers",
                            "children": [{"id": "grid"}, {"id": "card"}],
                        },
                        {"id": "media", "children": [{"id": "video"}, {"id": "img"}]},
                    ],
                    label_key="id",
                    tick_strategy="leaf",   
                    on_tick=lambda e: ui.notify(e.value),
                )
                ui.button("page informations", color="none").classes(
                    "mx-auto bg-gray-300"
                )
                with ui.card().tight().classes("mx-auto bg-gray-300 w-2/3"):
                    with ui.card_section():
                        ui.label(" Element selected :").classes("ml-1")
                    with ui.card_section():
                        ui.label("setColor").classes("ml-2")
                        ui.label("setColor").classes("ml-2")
                        ui.label("setForeground").classes("ml-2")
                ui.button("export my website").classes("mx-auto")


# ui.code
