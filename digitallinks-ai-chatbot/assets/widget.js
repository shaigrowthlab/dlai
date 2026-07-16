(function () {

    'use strict';


    document.addEventListener(
        'DOMContentLoaded',
        function () {


            const root =
                document.getElementById(
                    'dl-ai-chatbot-root'
                );


            if (!root) {
                return;
            }



            root.innerHTML = `

                <button 
                    id="dl-chatbot-open"
                    class="dl-chatbot-button">
                    💬
                </button>


                <div 
                    id="dl-chatbot-window"
                    class="dl-chatbot-window">


                    <div class="dl-chatbot-header">

                        <span>
                            DigitalLinks AI Assistant
                        </span>


                        <span 
                            id="dl-chatbot-close"
                            class="dl-chatbot-close">
                            ×
                        </span>

                    </div>



                    <div 
                        id="dl-chatbot-messages"
                        class="dl-chatbot-messages">

                        <div class="dl-message dl-ai-message">

                            Hi 👋  
                            How can I help you today?

                        </div>

                    </div>



                    <div class="dl-chatbot-input">


                        <input 
                            id="dl-chatbot-input"
                            type="text"
                            placeholder="Ask me anything..."
                        />


                        <button 
                            id="dl-chatbot-send">
                            Send
                        </button>


                    </div>


                </div>

            `;



            const openBtn =
                document.getElementById(
                    'dl-chatbot-open'
                );


            const closeBtn =
                document.getElementById(
                    'dl-chatbot-close'
                );


            const windowBox =
                document.getElementById(
                    'dl-chatbot-window'
                );


            const sendBtn =
                document.getElementById(
                    'dl-chatbot-send'
                );


            const input =
                document.getElementById(
                    'dl-chatbot-input'
                );


            const messages =
                document.getElementById(
                    'dl-chatbot-messages'
                );



            openBtn.onclick = function () {

                windowBox.style.display =
                    'flex';

            };



            closeBtn.onclick = function () {

                windowBox.style.display =
                    'none';

            };



            sendBtn.onclick =
                sendMessage;



            input.addEventListener(
                'keypress',
                function(e){

                    if(e.key === 'Enter'){

                        sendMessage();

                    }

                }
            );



            function addMessage(
                text,
                type
            ){


                const div =
                    document.createElement(
                        'div'
                    );


                div.className =
                    'dl-message ' +
                    (
                        type === 'user'
                        ?
                        'dl-user-message'
                        :
                        'dl-ai-message'
                    );


                div.innerText =
                    text;


                messages.appendChild(
                    div
                );


                messages.scrollTop =
                    messages.scrollHeight;


            }





            function sendMessage(){


                const message =
                    input.value.trim();



                if(!message){

                    return;

                }



                addMessage(
                    message,
                    'user'
                );


                input.value = '';



                addMessage(
                    'Thinking...',
                    'ai'
                );



                const thinking =
                    messages.lastChild;



                const formData =
                    new FormData();



                formData.append(
                    'action',
                    'dl_ai_chat'
                );


                formData.append(
                    'nonce',
                    DL_AI_CONFIG.nonce
                );


                formData.append(
                    'message',
                    message
                );



                fetch(
                    DL_AI_CONFIG.ajax_url,
                    {

                        method:'POST',

                        body:formData

                    }

                )


                .then(
                    response =>
                    response.json()
                )


                .then(
                    data => {


                        thinking.remove();



                        if(
                            data.success
                        ){


                            const reply =
                                data.data.reply ||
                                data.data.response ||
                                JSON.stringify(
                                    data.data
                                );


                            addMessage(
                                reply,
                                'ai'
                            );


                        }

                        else {


                            addMessage(
                                'Sorry, something went wrong.',
                                'ai'
                            );


                        }


                    }

                )


                .catch(
                    error => {


                        thinking.remove();


                        addMessage(
                            error.message,
                            'ai'
                        );


                    }
                );


            }


        }

    );


})();