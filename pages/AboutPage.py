import theme
from nicegui import ui


def aboutPage():
    with theme.frame('About'):
        ui.page_title('About Us')
        with ui.grid():
            ui.label('Welcome to Our Website!')
            ui.label('We are dedicated to providing high-quality services and products.')

        with ui.grid(columns=2):
            ui.label('Contact Information:')
            ui.label('Address:')
            ui.label('1234 Example Street')
            ui.label('City, Country')
            ui.label('Email:')
            ui.label('info@example.com')
            ui.label('Phone:')
            ui.label('+123 456 789')

        ui.link('Visit Our Website', 'https://www.example.com')


        ui.button('Back')