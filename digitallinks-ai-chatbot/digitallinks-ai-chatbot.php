<?php
/**
 * Plugin Name: DigitalLinks AI Chatbot
 * Plugin URI: https://digitallinks.net
 * Description: AI Sales Assistant chatbot powered by DigitalLinks AI backend and FastAPI.
 * Version: 0.1.0
 * Requires at least: 6.0
 * Requires PHP: 7.4
 * Author: DigitalLinks
 * Author URI: https://digitallinks.net
 * License: GPL v2 or later
 * Text Domain: digitallinks-ai-chatbot
 */

if (!defined('ABSPATH')) {
    exit;
}


/**
 * Plugin Constants
 */
define(
    'DLAI_VERSION',
    '0.1.0'
);

define(
    'DLAI_PLUGIN_FILE',
    __FILE__
);

define(
    'DLAI_PLUGIN_DIR',
    plugin_dir_path(__FILE__)
);

define(
    'DLAI_PLUGIN_URL',
    plugin_dir_url(__FILE__)
);


/**
 * Load API Class
 */
require_once DLAI_PLUGIN_DIR . 'includes/class-api.php';


/**
 * Initialize REST API
 */
DL_AI_API::init();


/**
 * Main Plugin Class
 */
final class DigitalLinks_AI_Chatbot {


    public static function init() {

        add_action(
            'admin_menu',
            [
                self::class,
                'register_settings_page'
            ]
        );


        add_action(
            'admin_init',
            [
                self::class,
                'register_settings'
            ]
        );


        add_action(
            'wp_enqueue_scripts',
            [
                self::class,
                'enqueue_assets'
            ]
        );


        add_action(
            'wp_footer',
            [
                self::class,
                'render_chat_mount'
            ]
        );

    }



    /**
     * Register Settings Page
     */
    public static function register_settings_page() {


        add_options_page(
            'DigitalLinks AI Chatbot',
            'DigitalLinks AI Chatbot',
            'manage_options',
            'digitallinks-ai-chatbot',
            [
                self::class,
                'settings_page'
            ]
        );

    }



    /**
     * Register Settings
     */
    public static function register_settings() {


        register_setting(
            'dlai_settings_group',
            'dlai_backend_url',
            [
                'sanitize_callback'=>'esc_url_raw'
            ]
        );


    }



    /**
     * Load Frontend Assets
     */
    public static function enqueue_assets() {


        wp_enqueue_style(
            'dlai-chatbot-style',
            DLAI_PLUGIN_URL . 'assets/site-context-chat.css',
            [],
            DLAI_VERSION
        );


        wp_enqueue_script(
            'dlai-chatbot-widget',
            DLAI_PLUGIN_URL . 'assets/widget.js',
            [],
            DLAI_VERSION,
            true
        );


        wp_localize_script(
            'dlai-chatbot-widget',
            'dlaiConfig',
            [
                'apiUrl'=>rest_url('dlai/v1/chat')
            ]
        );


    }



    /**
     * Chat Widget Mount
     */
    public static function render_chat_mount() {

        echo '<div id="dlai-chat-root"></div>';

    }




    /**
     * Settings Page
     */
    public static function settings_page() {


        if(!current_user_can('manage_options')){
            return;
        }


        $backend_url = get_option(
            'dlai_backend_url',
            ''
        );

        ?>

        <div class="wrap">

            <h1>
                DigitalLinks AI Chatbot
            </h1>


            <form method="post" action="options.php">

                <?php

                settings_fields(
                    'dlai_settings_group'
                );

                ?>


                <table class="form-table">

                    <tr>

                        <th>
                            <label>
                                FastAPI Backend URL
                            </label>
                        </th>


                        <td>

                            <input
                                type="url"
                                class="regular-text"
                                name="dlai_backend_url"
                                value="<?php echo esc_attr($backend_url); ?>"
                                placeholder="https://api.digitallinks.net"
                            />

                            <p class="description">
                                Your DigitalLinks AI FastAPI backend endpoint.
                            </p>

                        </td>

                    </tr>


                </table>


                <?php

                submit_button();

                ?>


            </form>


        </div>


        <?php

    }

}


/**
 * Start Plugin
 */
DigitalLinks_AI_Chatbot::init();