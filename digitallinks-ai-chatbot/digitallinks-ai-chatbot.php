<?php
/**
 * Plugin Name: DigitalLinks AI Chatbot
 * Plugin URI: https://digitallinks.net
 * Description: AI Sales Assistant chatbot powered by DigitalLinks AI backend.
 * Version: 1.0.0
 * Author: DigitalLinks
 * Author URI: https://digitallinks.net
 * License: GPL v2 or later
 * Text Domain: digitallinks-ai-chatbot
 */

if (!defined('ABSPATH')) {
    exit;
}


/*
|--------------------------------------------------------------------------
| Plugin Constants
|--------------------------------------------------------------------------
*/

define(
    'DL_AI_CHATBOT_VERSION',
    '1.0.0'
);

define(
    'DL_AI_CHATBOT_PATH',
    plugin_dir_path(__FILE__)
);

define(
    'DL_AI_CHATBOT_URL',
    plugin_dir_url(__FILE__)
);



/*
|--------------------------------------------------------------------------
| Load API Class
|--------------------------------------------------------------------------
*/

require_once DL_AI_CHATBOT_PATH . 'includes/class-api.php';



/*
|--------------------------------------------------------------------------
| Initialize Plugin
|--------------------------------------------------------------------------
*/

function dl_ai_chatbot_init() {

    DL_AI_API::init();

}

add_action(
    'plugins_loaded',
    'dl_ai_chatbot_init'
);



/*
|--------------------------------------------------------------------------
| Load Frontend Assets
|--------------------------------------------------------------------------
*/

function dl_ai_chatbot_enqueue_assets() {


    wp_enqueue_style(
        'dl-ai-chatbot-style',
        DL_AI_CHATBOT_URL . 'assets/digitallinks-chat.css',
        array(),
        DL_AI_CHATBOT_VERSION
    );


    wp_enqueue_script(
        'dl-ai-chatbot-widget',
        DL_AI_CHATBOT_URL . 'assets/widget.js',
        array(),
        DL_AI_CHATBOT_VERSION,
        true
    );


    wp_localize_script(
    'dl-ai-chatbot-widget',
    'DL_AI_CONFIG',
    array(

        'api_url' => DL_AI_API::get_api_url(),

        'ajax_url' => admin_url(
            'admin-ajax.php'
        ),

        'nonce' => wp_create_nonce(
            'dl_ai_chatbot_nonce'
        )

        )
    );

}

add_action(
    'wp_enqueue_scripts',
    'dl_ai_chatbot_enqueue_assets'
);



/*
|--------------------------------------------------------------------------
| Chatbot Container
|--------------------------------------------------------------------------
*/

function dl_ai_chatbot_render_widget() {

    echo '<div id="dl-ai-chatbot-root"></div>';

}

add_action(
    'wp_footer',
    'dl_ai_chatbot_render_widget'
);