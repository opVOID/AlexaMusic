# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pause",
            description="Pause the current playing stream on video chat.",
            thumb_url="https://media.discordapp.net/attachments/1006056892616949801/1226317652255965314/OIG1_1.jpeg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Resume",
            description="Resume the paused stream on video chat.",
            thumb_url="https://media.discordapp.net/attachments/1006056892616949801/1226317652255965314/OIG1_1.jpeg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Skip",
            description="Skip the current playing stream on video chat and moves to the next stream.",
            thumb_url="https://media.discordapp.net/attachments/1006056892616949801/1226317652255965314/OIG1_1.jpeg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="End",
            description="End the current playing stream on video chat.",
            thumb_url="https://media.discordapp.net/attachments/1006056892616949801/1226317652255965314/OIG1_1.jpeg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="Shuffle",
            description="Shuffle the queued songs in playlist.",
            thumb_url="https://media.discordapp.net/attachments/1006056892616949801/1226317652255965314/OIG1_1.jpeg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Loop",
            description="Loop the current playing track on video chat.",
            thumb_url="https://media.discordapp.net/attachments/1006056892616949801/1226317652255965314/OIG1_1.jpeg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
