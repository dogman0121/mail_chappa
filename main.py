import json

from inbox import Inbox
from requests import post
from dotenv import load_dotenv
import logging

import os

logging.basicConfig(filename='mail.log', level=logging.INFO)

load_dotenv()

inbox = Inbox()


@inbox.collate
def handle(to, sender, subject, body, media):
    if os.environ.get("REDIRECT_URL"):
        logging.info("Отправляю запрос на " + os.environ.get("REDIRECT_URL"))
        try:
            response = post(
                os.environ.get("REDIRECT_URL"),
                data=json.dumps({
                    "to": to,
                    "sender": sender,
                    "text": subject,
                    "html": body
                }),
                files=media
            )
            logging.info("Запрос отправлен. Код ответа: " + str(response.status))
        except:
            logging.error("Ошибка подключения к серверу.")


if __name__ == "__main__":
    inbox.serve(port=int(os.environ.get("PORT")), address=os.environ.get("ADDRESS"))
    logging.info(f"Создан сервер по адресу {os.environ.get('ADDRESS')} с портом {os.environ.get('PORT')}")
    inbox.dispatch()
