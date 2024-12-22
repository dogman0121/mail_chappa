import json

from inbox import Inbox
from requests import post

import os


inbox = Inbox()

inbox.serve(os.environ.get("PORT"), os.environ.get("ADDRESS"))


@inbox.collate
def handle(to, sender, body):
    if os.environ.get("REDIRECT_URL"):
        post(
            "REDIRECT_URL",
            data=json.dumps({
                "to": to,
                "sender": sender,
                "body": body
            }))
        print(to, sender, body)


if __name__ == "__main__":
    inbox.dispatch()
