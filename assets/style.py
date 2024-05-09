from nicegui import ui


def setupStyle():
    ui.add_css(
        """
            .cardLang{
                background-color: #fff;  
                border: #000 2px solid;
                margin: 1rem;
                padding: 3rem;
                border-radius: 10px;
            }
            
            .cardlang img{
                width: 100px;
                padding: 1rem;
            }
            
            .card-plus {
                width: 150px;
                height: 250px;
            }
            
            body {
                margin: 0;
                padding: 0;
                width: 100%;
            }

            textarea{
                resize: none;

            }

            .card-plus {
                max-width: 200px;
                max-height: 300px;
            }

            .card-plus img {
                width: 100%;
                height: auto;
                
            }

            .usul {
                margin-left: -14px;
            }

            #c31 {
                margin-left: -16px;
            }

            .col1_sec{
                margin-left: 10%;
                margin-top: 3%;
            }

            .col2_sec{
                margin-top: 3%;
            }


            .img1 {
                width: 500px;
                height: 500px;
            }

            .first_section{
                margin-left: 7%;
                margin-top: 6%;
                height: 80vh;
            }

            .card-plus1 {
                background-color: white;
            }

            .set_navbar_el_black{
                color: #000;
            }

            .set_navbar_hr_black{
                border-top: 1px solid #000;
            }

            .text-white1{
                color: #fff;
            }

            .screen-section{
                padding-left: 80%;
            }
            
            .img-spe{
                width: 300px;
                height: 350px;
            }
            
            /*.maxSize{
                max-width: 200px;
            }*/
            """
    )
