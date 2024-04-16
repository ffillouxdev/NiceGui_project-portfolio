import theme
from nicegui import ui
import asyncio

    
def aboutPage():
    with theme.frame('About'):
        ui.page_title('About Us')
        with ui.grid(columns=2).classes('w-full pl-8 first_section'):
            with ui.column().classes('ml-8'):
                ui.image(source='assets/about.png').classes('img1')  
            with ui.column().classes('w-2/3 p-4'):
                ui.label('About Us').classes('text-center text-white text-4xl font-semibold pt-4')
                ui.label('Welcome to Our Website!').classes('text-bold text-white text-lg')
                ui.label("""
                        We are a team of developers who are passionate about creating websites,
                        we are dedicated to providing high-quality services and products, our 
                        platform aims to empower users to create websites easily, similar to WordPress,
                        we provide intuitive tools and customizable themes to suit your needs.
                        """).classes('text-white w-full')
                ui.button('Get Started', on_click=lambda: ui.navigate.to("/Create-your-website/")).classes('bg-blue-500 text-white text-md px-6 py-3 rounded-lg hover:bg-blue-600 focus:outline-none focus:bg-blue-600')
        
                                
                        
                        
 