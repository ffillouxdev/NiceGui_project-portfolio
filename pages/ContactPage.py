import theme
from nicegui import ui, app
from animationJs import slide_up

app.add_static_files("/Contact/static", "assets/")

def on_click(button_submit):    
    ui.notify("Button clicked")
    button_submit.text = "Clicked"
    

    
def contactPage():
    with theme.frame('Contact') as frame:
        ui.page_title('Contact Me')   
        ui.context.client.content.classes('p-0 gap-0')
        slide_up('.animate_slideInUp')  
        with ui.row().classes(
        "flex justify-center items-center w-full h-2/3 animate_slideInUp gap-0"
        ):
            with ui.column().classes("bg-white w-1/2 p-4 shadow-lg rounded-xl") as col1:
                welcomeLabel = ui.markdown("### Get in touch").classes( 
                    "text-lg font-semibold mx-auto"
                )
                separator = ui.separator().classes("w-2/3 bg-gray-800 mb-4 mx-auto")
                input_name = ui.input(label="Your Name", placeholder="John Doe").classes(
                    "w-full mb-4 px-4 py-2 focus:outline-none focus:border-green-500 rounded-lg"
                )
                input_email = ui.input(
                    label="Your Email", placeholder="example@example.com"
                ).classes(
                    "w-full mb-4 px-4 py-2 focus:outline-none focus:border-green-500 rounded-lg"
                )
                subject = ui.input(label="Subject", placeholder="Subject").classes(
                    "w-full px-4 py-2 focus:outline-none focus:border-green-500 rounded-lg"
                )
                textarea_message = ui.textarea(label="Your Message").classes(
                    "w-full mb-4 px-4 py-2 focus:outline-none focus:border-green-500 resize-none h-32 rounded-lg"
                )
                button_submit = ui.button("Send Message", color="blue").classes(
                    "w-full px-4 py-2 bg-blue-500 text-white hover:bg-blue-600 focus:outline-none focus:bg-blue-600 rounded-lg mx-auto"
                )
                button_submit.on_click(lambda: on_click(button_submit))


            with ui.column().classes(
                "bg-blue-400 w-1/3 h-1/2 p-8 shadow-lg text-white"
            ) as col2:
                contactLabel = ui.markdown("### Contact Me").classes(
                    "text-lg font-semibold mb-4"
                )
                separator = ui.separator().classes("w-2/3 bg-white mb-4")
                with ui.row().classes("flex items-center mb-4"):
                    icon = ui.icon("phone").classes("text-5xl text-blue-500 mr-4")
                    phoneLabel = ui.label("Phone : +1 234 567 890").classes("text-lg")
                with ui.row().classes("flex items-center mb-4"):
                    icon = ui.icon("email").classes("text-5xl text-blue-500 mr-4")
                    emailLabel = ui.label("Email : example@email.com").classes("text-lg")
                with ui.row().classes("flex items-center mb-4"):
                    icon = (
                        ui.icon("o_home")
                        .classes("text-4xl text-blue-500 mr-4")
                        .classes("ml-1")
                    )
                    locationLabel = ui.label("Loc : 123 Street, City, Country").classes(
                        "text-lg"
                    )
                    


#rajouter un ui.spinner dans une dialog pour faire patienter l'utilisateur avant le demarrage de la page et eviter les bugs avec gsap
"""
https://nicegui.io/documentation/section_data_elements
https://nicegui.io/documentation/spinner
https://nicegui.io/documentation/log
https://nicegui.io/documentation/section_configuration_deployment#server_hosting
"""