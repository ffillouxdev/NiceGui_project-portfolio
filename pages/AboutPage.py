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
                ui.button('Get Started').classes('bg-blue-500 text-white text-md px-6 py-3 rounded-lg hover:bg-blue-600 focus:outline-none focus:bg-blue-600')
        
                                
                        
                        
                        
                
"""ui.label('https://nicepage.com/t/2880966/about-digital-agency-template').classes('text-white')
  ui.separator().classes('bg-white w-1/2 mx-auto')
            with ui.grid(columns=3).classes('w-full p-4'):
            
                    
                ui.label('Start your website').classes('text-center text-white text-4xl font-semibold pt-4')
                ui.separator().classes('bg-white w-1/2 mx-auto')
                with ui.grid(columns=3).classes('w-full p-4'):
                    with ui.column().classes('w-full ml-8'):
                        ui.label('Get started by creating an account.').classes('text-center text-white text-3xl font-semibold')
                        ui.label('Choose a theme and start building your website.').classes('text-white')
                    with ui.column().classes('w-px h-full bg-white mx-auto'):
                        pass
                    with ui.column().classes('w-full mr-8 mt-4 text-left'):
                        ui.label('Our platform offers a variety of themes to choose from.').classes('text-white')
"""