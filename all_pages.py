from nicegui import ui
from pages.AboutPage import aboutPage
from pages.ContactPage import contactPage
from pages.YourWebsite import yourWebsite

def create() -> None:
    ui.page('/Contact/')(contactPage)
    ui.page('/About/')(aboutPage)
    ui.page('/Create-your-website')(yourWebsite)
    
if __name__ == '__main__':
    create()
    
#https://github.com/zauberzeug/nicegui/wiki/fly.io-Deployment