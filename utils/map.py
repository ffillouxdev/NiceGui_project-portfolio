"""
        MAP
        with ui.row().classes("w-full"):  
            m = ui.leaflet(center=(51.505, -0.09))
            ui.label().bind_text_from(m, 'center', lambda center: f'Center: {center[0]:.3f}, {center[1]:.3f}')
            ui.label().bind_text_from(m, 'zoom', lambda zoom: f'Zoom: {zoom}')

            with ui.grid(columns=2):
                ui.button('London', on_click=lambda: m.set_center((51.505, -0.090)))
                ui.button('Berlin', on_click=lambda: m.set_center((52.520, 13.405)))
                ui.button(icon='zoom_in', on_click=lambda: m.set_zoom(m.zoom + 1))
                ui.button(icon='zoom_out', on_click=lambda: m.set_zoom(m.zoom - 1))  
"""      