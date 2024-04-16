from nicegui import ui
import theme

def yourWebsite():
    with theme.frame('YourWebsite') as frame:
        ui.page_title('YourWebsite')
        with ui.grid(columns=2).classes("w-full h-screen bg-gray-200 flex justify-between"):
            with ui.column().classes():
                ui.label("Yo").classes("")
            with ui.column().classes("bg-white w-1/5"):
                ui.markdown("#### Components").classes("text-center w-full")
                ui.separator().classes("bg-black w-1/3 mx-auto lessTopGap")
                ui.tree([
                    {'id': 'navbar', 'children': [{'id': 'choice1'}, {'id': 'choice2'}]},
                    {'id': 'footer', 'children': [{'id': 'A'}, {'id': 'B'}]},
                    {'id': 'buttons', 'children': [{'id': 'A'}, {'id': 'B'}]},
                    {'id': 'contenteditable', 'children': [{'id': 'A'}, {'id': 'B'}]},
                    {'id': 'containers', 'children': [{'id': 'grid'}, {'id': 'card'}]},
                    {'id': 'media', 'children': [{'id': 'video'}, {'id': 'img'}]},
                ], label_key='id', on_select=lambda e: ui.notify(e.value))
                ui.button("page informations").classes("mx-auto")
                with ui.card().tight().classes("mx-auto bg-gray-300 w-2/3"):
                    with ui.card_section():
                        ui.label(" Element selected :").classes("ml-1")
                    with ui.card_section():
                        ui.label("setColor").classes("ml-2")
                        ui.label("setColor").classes("ml-2")
                        ui.label("setForeground").classes("ml-2")
                ui.button("export my website").classes("mx-auto")
                