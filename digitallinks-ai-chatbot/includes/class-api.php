<?php

if (!defined('ABSPATH')) {
    exit;
}


class DL_AI_API {


    private static $api_url = 'http://localhost:8000';


    public static function init() {

        add_action(
            'wp_ajax_dl_ai_chat',
            array(__CLASS__, 'chat')
        );


        add_action(
            'wp_ajax_nopriv_dl_ai_chat',
            array(__CLASS__, 'chat')
        );

    }



    public static function get_api_url() {

        return self::$api_url;

    }



    public static function chat() {


        check_ajax_referer(
            'dl_ai_chatbot_nonce',
            'nonce'
        );


        $message = sanitize_text_field(
            $_POST['message'] ?? ''
        );


        if (empty($message)) {

            wp_send_json_error(
                array(
                    'message'=>'Message required'
                )
            );

        }



        $response = wp_remote_post(

            self::$api_url . '/chat',

            array(

                'headers'=>array(
                    'Content-Type'=>'application/json'
                ),


                'body'=>json_encode(

                    array(

                        'message'=>$message,

                        'session_id'=>'wordpress-user'

                    )

                ),


                'timeout'=>60

            )

        );



        if(
            is_wp_error($response)
        ){

            wp_send_json_error(

                array(
                    'message'=>$response->get_error_message()
                )

            );

        }



        $body = wp_remote_retrieve_body(
            $response
        );


        wp_send_json_success(

            json_decode(
                $body,
                true
            )

        );


    }

}