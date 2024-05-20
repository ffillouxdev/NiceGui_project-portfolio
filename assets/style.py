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
                background: url('static/parallax/montainsss.jpg') no-repeat center center fixed;
                background-size: cover;
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
            
            
            section{
                position: relative;
                height: 100vh;
                width: 100%;
                overflow: hidden;
                padding: 5vw;
            }
            

            section img{
                position: absolute;
                top 0;
                left: 0;
                display: block;
                object-fit: cover;
            }
            
            .parallax_group{
            }
            
            .parallax_group:after{
                content: "";
                height: 30vh;
                postion: absolute;
                bottom: 0;
                left: 0;
                width: 100%;
                background: linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.5) 100%);
            }
            
            .shadow_transi{
                postion: absolute;
                bottom: 100%;
                height: 300px;
                width: 100%;
                left: 0;
                z-index: 50;
                background: linear-gradient(to top, #151515, transparent);
            }
            
            .first.section {
            }
            
            .second.section {
                background: rgb(37, 27, 24);
                background: linear-gradient(180deg, rgba(37, 27, 24, 1) 10%, rgba(0, 0, 0, 1) 90%, #031D38);
            }
            
            .third.section {
                background: linear-gradient(180deg, #031D38, 85%, #2560A6);
            }
            
            .fourth.section {
                background: linear-gradient(180deg, #2560A6, 90%, #0C4C8C);
            }
            
            .fifth.section {
                background: linear-gradient(180deg, #0C4C8C, 90%, #FFF);
            }
            
            .container{
                max-height: 100vh;
                scroll-snap-type: y mandatory;
            }
            """
    )


# https://cdna.artstation.com/p/assets/images/images/031/726/410/original/adele-meunier-finaltitregifloop.gif?1604422953
