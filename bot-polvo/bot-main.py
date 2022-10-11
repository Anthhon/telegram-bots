'''
Done! Congratulations on your new bot. You will find it at t.me/o_polvo_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
5635652503:AAFG501wIrPhQo-fs_2EDra5__ItIvvlATY
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api
'''

import telebot
from random import choice


# Integração do BOT
CHAVE_API = "5635652503:AAFG501wIrPhQo-fs_2EDra5__ItIvvlATY"
bot = telebot.TeleBot(CHAVE_API)



# Mensagem inicial

def verify(message):
    ms = message.text
    if ms.startswith("Oh polvo,") or ms.startswith("oh polvo,"):
        return True
    else:
        return False

# Define quando a função abaixo vai ser executada
@bot.message_handler(func=verify)
def answer(message):
    
    ms = message.text
    
    if ms.endswith('?'):
        cString = ms[10:-1]
    else:
        cString = ms[10:]


    cList = cString.split(' ou ', 2)
    answer = choice(cList)
    yORn = [
        "Sim",
        "Não"
    ]


    if ' ou ' in ms:
        bot.send_message(message.chat.id, f"Creio que {answer}!")
    else:
        bot.send_message(message.chat.id, choice(yORn))

    # Cita a mensagem e responde com a frase parametrada
    # bot.send_message(message.chat.id, f"Qual a sua dúvida, {message.from_user.first_name}?")


# Faz com que o bot leia as mensagens infinitamente
bot.polling()


'''
SAMPLE MESSAGE DATA

{'content_type': 'text', 'id': 9, 'message_id': 9,
'from_user': {'id': 5151052864, 'is_bot': False, 'first_name': 'Anthony', 'username': 'AlanCcE', 'last_name': 'Silva', 'language_code': 'en', 'can_join_groups': None, 'can_read_all_group_messages': None, 'supports_inline_queries': None, 'is_premium': None, 'added_to_attachment_menu': None}, 'date': 1665505947,
'chat': {'id': 5151052864, 'type': 'private', 'title': None, 'username': 'AlanCcE', 'first_name': 'Anthony', 'last_name': 'Silva', 'photo': None, 'bio': None, 'join_to_send_messages': None, 'join_by_request': None, 'has_private_forwards': None, 'has_restricted_voice_and_video_messages': None, 'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None, 'slow_mode_delay': None, 'message_auto_delete_time': None, 'has_protected_content': None, 'sticker_set_name': None, 'can_set_sticker_set': None, 'linked_chat_id': None, 'location': None},
'sender_chat': None, 'forward_from': None, 'forward_from_chat': None, 'forward_from_message_id': None, 'forward_signature': None, 'forward_sender_name': None, 'forward_date': None, 'is_automatic_forward': None, 'reply_to_message': None, 'via_bot': None, 'edit_date': None, 'has_protected_content': None, 'media_group_id': None, 'author_signature': None, 'text': 'clear', 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'reply_markup': None,
'json': {'message_id': 9, 'from': {'id': 5151052864, 'is_bot': False, 'first_name': 'Anthony', 'last_name': 'Silva', 'username': 'AlanCcE', 'language_code': 'en'}, 'chat': {'id': 5151052864, 'first_name': 'Anthony', 'last_name': 'Silva', 'username': 'AlanCcE', 'type': 'private'}, 'date': 1665505947, 'text': 'clear'}}
'''
