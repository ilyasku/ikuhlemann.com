from typing import List
import os


class Page:

    def __init__(self, title: str, url: str, **render_kwargs):
        self.title = title
        self.url = url
        self.render_kwargs = render_kwargs
        

class Message:

    def __init__(self, text: str, blacklist: List[str]=[]):
        self.text = text
        self.blacklist = blacklist

class Contact:

    def __init__(self, room: str, mail: str, phone: str):
        self.room  = room
        self.mail  = mail
        self.phone = phone
        
class Member:
    
    def __init__(self, name: str, contact: Contact, picture: str, topics: List[str],
                 position: str=""):
        self.name = name
        self.contact = contact
        self.picture = os.path.join('static', 'pictures', picture)
        self.topics = topics
        self.position = position
