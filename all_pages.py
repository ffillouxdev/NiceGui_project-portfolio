from nicegui import ui
from pages.AboutPage import aboutPage
from pages.ContactPage import contactPage

def create() -> None:
    ui.page('/Contact/')(contactPage)
    ui.page('/About/')(aboutPage)
    
if __name__ == '__main__':
    create()