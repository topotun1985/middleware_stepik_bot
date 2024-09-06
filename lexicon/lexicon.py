LEXICON_RU: dict[str, str] = {
    '/start': '✅ <b>Привет!\n\n⭐ Я эхо-бот для демонстрации работы миддлварей!</b>\n\n'
              '⏰ <u>Если хотите - можете мне что-нибудь прислать</u>\n\n'
              '❌ <code>Это моноширинный текст</code>\n\n'
              '⚪🟡🔵 <a href="tg://user?id=855277058">Ссылка на мою телегу</a>',
    'no_echo': 'Данный тип апдейтов не поддерживается '
               'методом send_copy',
    'button': 'Кнопка',
    'button_pressed': 'Вы нажали кнопку!'
}


LEXICON_EN: dict[str, str] = {
    '/start': "Hello!\n\nI'm an echo bot to demonstrate how middleware works!\n\n"
              "If you want, you can send me something",
    'no_echo': 'This type of update is not supported by the send_copy method',
    'button': 'Button',
    'button_pressed': "You've pressed the button!"
}
