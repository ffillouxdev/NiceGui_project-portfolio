from nicegui import ui
import theme

def yourWebsite():
    with theme.frame('YourWebsite') as frame:
        ui.page_title('YourWebsite')
        with ui.row().classes("w-full h-screen bg-gray-200 flex justify-between"):
            with ui.column().classes("bg-red-200 w-4/5 h-full") as screenEditor:   
                pass 
            with ui.column().classes("bg-white w-1/6 h-full"):
                ui.markdown("#### Components").classes("text-center w-full")
                ui.separator().classes("bg-black w-1/3 mx-auto lessTopGap")
                ui.tree([
                    {'id': 'navbar', 'children': [{'id': 'navbar1'}, {'id': 'navbar2'}]},
                    {'id': 'footer', 'children': [{'id': 'footer1'}, {'id': 'footer2'}]},
                    {'id': 'buttons', 'children': [{'id': 'button1'}, {'id': 'button2'}]},
                    {'id': 'contenteditable', 'children': [{'id': 'choice1'}, {'id': 'choice2'}]},
                    {'id': 'containers', 'children': [{'id': 'grid'}, {'id': 'card'}]},
                    {'id': 'media', 'children': [{'id': 'video'}, {'id': 'img'}]},
                ], label_key='id', tick_strategy='leaf', on_tick=lambda e: ui.notify(e.value))
                ui.button("page informations", color='none').classes("mx-auto bg-gray-300")
                with ui.card().tight().classes("mx-auto bg-gray-300 w-2/3"):
                    with ui.card_section():
                        ui.label(" Element selected :").classes("ml-1")
                    with ui.card_section():
                        ui.label("setColor").classes("ml-2")
                        ui.label("setColor").classes("ml-2")
                        ui.label("setForeground").classes("ml-2")
                ui.button("export my website").classes("mx-auto")
            



#ui.code