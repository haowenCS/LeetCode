# class Foo:
#     def __init__(self):
#         self.first_done = False
#         self.second_done = False


#     def first(self, printFirst: 'Callable[[], None]') -> None:

#         # printFirst() outputs "first". Do not change or remove this line.
#         printFirst()
#         self.first_done = True


#     def second(self, printSecond: 'Callable[[], None]') -> None:
#         while not self.first_done:
#             continue
#         # self.first_done = False

#         # printSecond() outputs "second". Do not change or remove this line.
#         printSecond()
#         self.second_done = True


#     def third(self, printThird: 'Callable[[], None]') -> None:
#         while not self.second_done:
#             continue
#         # self.second_done = False

#         # printThird() outputs "third". Do not change or remove this line.
#         printThird()


import threading


class Foo:
    def __init__(self):
        self.event1 = threading.Event()
        self.event2 = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.event1.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.event1.wait()
        printSecond()
        self.event2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.event2.wait()
        printThird()