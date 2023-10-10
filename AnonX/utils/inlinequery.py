from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="⏸️ Pause ⏸️",
            description=f"Pause The Current Playing Stream On Video chat.",
            thumb_url="https://te.legra.ph/file/82cb25e411498ed5b990b.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="▶️ Resume ▶️",
            description=f"Resume The Paused Stream On Video chat.",
            thumb_url="https://te.legra.ph/file/82cb25e411498ed5b990b.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="⏭ Skip ⏭",
            description=f"Skip The Current Playing Stream On Video chat & Moves To The Next Stream.",
            thumb_url="https://te.legra.ph/file/82cb25e411498ed5b990b.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="⏹ End ⏹",
            description="End The Current Playing Stream On Video chat.",
            thumb_url="https://te.legra.ph/file/82cb25e411498ed5b990b.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title=" Suffle ",
            description="Shuffle The Quequed Songs In Playlist.",
            thumb_url="https://te.legra.ph/file/82cb25e411498ed5b990b.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title=" Loop ",
            description="Loop The Current Playing Track On Video chat.",
            thumb_url="https://te.legra.ph/file/82cb25e411498ed5b990b.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
