from urllib import request
from aiogram.dispatcher.filters.state import State, StatesGroup

class Link(StatesGroup):
    text = State()
    link = State()

    @staticmethod
    def getTagLink(text: str, link: str):
        return f'<a href="{link}">{text}</a>'

    @staticmethod
    def is_valid(url):
        try:
            request.urlopen(url)
            return True
        except Exception:
            return False

    @staticmethod
    def getLink(text: str):
        b = text.split(" ")[0]
        if "http://" in b or "https://" in b:
            if Link.is_valid(b):
                return b
            else:
                return None
        else:
            return None

