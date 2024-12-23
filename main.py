import json

from inbox import Inbox
from requests import post

import os


inbox = Inbox()


@inbox.collate
def handle(to, sender, subject, body):
    print(to)
    print("--------")
    print(sender)
    print("--------")
    print(subject)
    print("--------")
    print(body)
    if os.environ.get("REDIRECT_URL"):
        post(
            "REDIRECT_URL",
            data=json.dumps({
                "to": to,
                "sender": sender,
                "body": body
            }))


if __name__ == "__main__":
    inbox.serve(25,"217.144.189.150")
    inbox.dispatch()
