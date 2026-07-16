(function () {

    "use strict";


    document.addEventListener("DOMContentLoaded", function () {


        const root = document.getElementById(
            "dl-ai-chatbot-root"
        );


        if (!root) {
            return;
        }



        const config = window.DL_AI_CONFIG || {};



        const chatButton = document.createElement("button");

        chatButton.className = "dl-ai-chat-button";

        chatButton.innerHTML = "💬";



        const chatBox = document.createElement("div");

        chatBox.className = "dl-ai-chat-box";

        chatBox.innerHTML = `

            <div class="dl-ai-header">
                <strong>
                    DigitalLinks AI Assistant
                </strong>

                <button class="dl-ai-close">
                    ×
                </button>
            </div>


            <div class="dl-ai-messages"></div>


            <div class="dl-ai-input-area">

                <input 
                    type="text"
                    class="dl-ai-input"
                    placeholder="Ask me anything..."
                />


                <button class="dl-ai-send">
                    Send
                </button>

            </div>

        `;



        root.appendChild(chatButton);

        root.appendChild(chatBox);



        const closeBtn =
            chatBox.querySelector(".dl-ai-close");


        const sendBtn =
            chatBox.querySelector(".dl-ai-send");


        const input =
            chatBox.querySelector(".dl-ai-input");


        const messages =
            chatBox.querySelector(".dl-ai-messages");




        chatButton.onclick = function () {

            chatBox.classList.toggle(
                "active"
            );

        };



        closeBtn.onclick = function () {

            chatBox.classList.remove(
                "active"
            );

        };




        function addMessage(
            text,
            type
        ) {


            const div =
                document.createElement("div");


            div.className =
                "dl-ai-message " +
                type;


            div.innerText =
                text;


            messages.appendChild(div);


            messages.scrollTop =
                messages.scrollHeight;

        }




        async function sendMessage() {


            const message =
                input.value.trim();



            if (!message) {
                return;
            }



            addMessage(
                message,
                "user"
            );


            input.value = "";



            addMessage(
                "Typing...",
                "bot typing"
            );



            try {


                const response =
                    await fetch(
                        config.api_url,
                        {

                            method: "POST",

                            headers: {

                                "Content-Type":
                                    "application/json"

                            },


                            body:
                                JSON.stringify({

                                    message:
                                        message,

                                    site:
                                        config.site_name

                                })

                        }
                    );



                const data =
                    await response.json();



                messages
                    .querySelector(".typing")
                    ?.remove();



                addMessage(
                    data.reply ||
                    "Sorry, I could not answer.",
                    "bot"
                );



            } catch (error) {


                messages
                    .querySelector(".typing")
                    ?.remove();


                addMessage(
                    "Connection error. Please try again.",
                    "bot"
                );


                console.error(
                    error
                );

            }


        }




        sendBtn.onclick =
            sendMessage;



        input.addEventListener(
            "keypress",
            function(e){

                if(e.key === "Enter"){

                    sendMessage();

                }

            }
        );



    });


})();