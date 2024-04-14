import theme
from nicegui import ui


def aboutPage():
    with theme.frame('About'):
        ui.page_title('About Us')
        yield
        