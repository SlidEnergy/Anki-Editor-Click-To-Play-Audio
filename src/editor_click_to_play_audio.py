import os
import aqt
from aqt import mw
from aqt.editor import Editor
import aqt.sound

MSG_PREFIX = "click-to-play-audio:play:"

def on_webview_will_set_content(web_content, context):
    addon_package = mw.addonManager.addonFromModule(__name__)

    if isinstance(context, aqt.editor.Editor):
        print("Injecting JS file into editor")
        web_content.js.append(f"/_addons/{addon_package}/web/editor_click_to_play_audio.js")


def on_webview_did_receive_js_message(handled, message, context):
    print("on_webview_did_receive_js_message called")
    
    if type(context) != aqt.editor.Editor:
        print(f"Ignored: context is not Editor, but {type(context)}")
        return handled

    print(f"Message received: {message}")

    if message.startswith(MSG_PREFIX):
        sound_file = message[len(MSG_PREFIX):]
        print(f"Playing sound file: {sound_file}")
        try:
            aqt.sound.av_player.play_file(sound_file)
            print("Sound playback triggered successfully")
        except Exception as e:
            print(f"Error playing sound: {e}")
        return (True, None)

    print("Message did not match prefix, passing on")
    return handled

mw.addonManager.setWebExports(__name__, r"web/.*\.(js|css)")

aqt.gui_hooks.webview_will_set_content.append(on_webview_will_set_content)
aqt.gui_hooks.webview_did_receive_js_message.append(
    on_webview_did_receive_js_message
)
