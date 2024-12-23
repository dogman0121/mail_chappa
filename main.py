import json

from inbox import Inbox
from requests import post
from dotenv import load_dotenv

import os


load_dotenv()

inbox = Inbox()


def parse_http_response(response: bytes):
    if b"\r\n\r\n" in response:
        headers, body = response.split(b"\r\n\r\n")
    elif b"\n\n" in response:
        headers, body = response.split(b"\n\n")
    else:
        raise ValueError("Unknown separator")

    return headers, body


@inbox.collate
def handle(to, sender, subject, body):
    html = parse_http_response(body)[1]
    if os.environ.get("REDIRECT_URL"):
        post(
            "REDIRECT_URL",
            data=json.dumps({
                "to": to,
                "sender": sender,
                "text": subject,
                "html": html
            }))


if __name__ == "__main__":
    inbox.serve(os.environ.get("PORT"), os.environ.get("ADDRESS"))
    inbox.dispatch()
