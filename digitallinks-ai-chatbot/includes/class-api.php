<?php

class DL_AI_API {

    public static function init(){

        add_action(
            'rest_api_init',
            function(){

                register_rest_route(
                    'dlai/v1',
                    '/chat',
                    [
                        'methods'=>'POST',
                        'callback'=>[
                            self::class,
                            'chat'
                        ],
                        'permission_callback'=>'__return_true'
                    ]
                );

            }
        );

    }


    public static function chat($request){

        $message = sanitize_text_field(
            $request['message']
        );


        $response = wp_remote_post(
            get_option('dlai_backend_url').'/chat',
            [
                'headers'=>[
                    'Content-Type'=>'application/json'
                ],
                'body'=>json_encode([
                    'message'=>$message
                ])
            ]
        );


        return json_decode(
            wp_remote_retrieve_body($response),
            true
        );

    }

}