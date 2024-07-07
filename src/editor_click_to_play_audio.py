import os
import aqt
from aqt.editor import Editor
import aqt.sound


MSG_PREFIX = "click-to-play-audio:play:"

py_file_path = os.path.abspath(__file__)
js_file_path = py_file_path[:-2] + "js"

with open(js_file_path, encoding="utf-8") as f:
    js_data = f.read()


def on_webview_will_set_content(web_content, context):
    if type(context) != aqt.editor.Editor:
        return

    web_content.head += f"<script>{js_data}</script>"


def on_webview_did_receive_js_message(handled, message, context):
    if type(context) != aqt.editor.Editor:
        return handled

    if message.startswith(MSG_PREFIX):
        sound_file = message[len(MSG_PREFIX) :]
        aqt.sound.av_player.play_file(sound_file)
        return (True, None)

    return handled


aqt.gui_hooks.webview_will_set_content.append(on_webview_will_set_content)
aqt.gui_hooks.webview_did_receive_js_message.append(
    on_webview_did_receive_js_message
)
