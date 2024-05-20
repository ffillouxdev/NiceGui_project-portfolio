from nicegui import ui, app
import home_page, all_pages, theme
from utils.recupData import init_db, close_db


# homepage
@ui.page("/")
def index_page() -> None:
    with theme.frame("Homepage"):
        home_page.content()


all_pages.create()

ui.run(title="Getting Started with NiceGUI", port=5000)
