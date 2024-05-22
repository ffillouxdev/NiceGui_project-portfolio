from nicegui import ui
from pages.ContactPage import contactPage

def create() -> None:
    ui.page('/Contact/')(contactPage)
    
if __name__ == '__main__':
    create()
    