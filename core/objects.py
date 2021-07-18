
import uuid
import datetime


class Article:
    def __init__(self, *args):
        self.id = uuid.uuid4().__str__() if args[0] is None else args[0]
        self.title = '' if args[1] is None else args[1]
        self.description = '' if args[2] is None else args[2]
        self.url = '' if args[3] is None else args[3]
        self.timestamp = datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S') if args[4] is None else args[4]

    def __repr__(self):
        return {'id': self.id,
                'title': self.title,
                'description': self.description,
                'url': self.url,
                'timestamp': self.timestamp}

    def __str__(self):
        return self.__repr__().__str__()
