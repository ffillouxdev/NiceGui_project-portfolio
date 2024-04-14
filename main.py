from nicegui import ui
import home_page, all_pages, theme


# homepage   
@ui.page("/")
def index_page() -> None:
    with theme.frame('Homepage'):
        home_page.content()
       

all_pages.create()

ui.run(title='Getting Started with NiceGUI')


