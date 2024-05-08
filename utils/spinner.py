import asyncio
from nicegui import ui

async def simulate_loading(dialog):
    await asyncio.sleep(1)
    dialog.close()
    
    
    
    with ui.dialog() as dialog:
            ui.spinner(size='lg', color='blue')
            dialog.open()
            asyncio.create_task(simulate_loading(dialog))     
""""          
https://nicegui.io/documentation/section_data_elements
https://nicegui.io/documentation/spinner
https://nicegui.io/documentation/log
https://nicegui.io/documentation/section_configuration_deployment#server_hosting"""