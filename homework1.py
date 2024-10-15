from queue import Queue
import random

q = Queue()

class Request():
    def __init__(self, number: int):
        self.__number = number

    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, number):
        self.__number = number

    def __str__(self):
        return f'Request number is {self.number}'
    
    def __repr__(self):
        return f'Request [number = {self.number}]'

def generate_request():
    request = Request(random.randint(1, 100))
    q.put(request)
    print(q.queue)


def process_request():
    if not q.empty():
        request = q.get()
        print(f"Handle request with number {request.number} ") 
    else:
        print("Queue is empty")


while True:
    generate_request()
    process_request()
    user_input = input("Бажаєте продовжити? (так/ні): ")
    if user_input.lower() == "ні":
        break
