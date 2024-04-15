import asyncio

async def simulate_loading(dialog):
    await asyncio.sleep(1)
    dialog.close()
    
    
    
    with ui.dialog() as dialog:
            ui.spinner(size='lg', color='blue')
            dialog.open()
            asyncio.create_task(simulate_loading(dialog))     