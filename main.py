import json

from inbox import Inbox
from requests import post
from dotenv import load_dotenv

import os


load_dotenv()

inbox = Inbox()


@inbox.collate
def handle(to, sender, subject, body, media):
    if os.environ.get("REDIRECT_URL"):
        post(
            "REDIRECT_URL",
            data=json.dumps({
                "to": to,
                "sender": sender,
                "text": subject,
                "html": body
            }),
            files=media
        )


if __name__ == "__main__":
    inbox.serve(os.environ.get("PORT"), os.environ.get("ADDRESS"))
    inbox.dispatch()
