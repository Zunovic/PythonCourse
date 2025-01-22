# def add(*args):
#     calc = 0
#     for n in args:
#         calc += n
#     print(calc)
# # Das *args nimmt beliebig viele inputs
# add(1,2,3,4,5,6,7,8,9)
#
#
# # Das **kwargs nimmt beliebig viele Key:Word inputs und speichert diese in einem Dictionary
# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
# # In diesem Fall wird ein Input (n) mit der Value aus dem Dictionary addiert und dann multipliziert
# calculate(2, add=3, multiply=5,)

# # Am Beispiel einer Klasse können wir optionale Key-Word Paare als input nehmen
# class Car:
#     def __init__(self, **kw):
#         # Die get Methode wartet beim init auf den Input mit dem Namen "make". Wenn dieser nicht kommt,
#         # wird der Datatype auf "None" gesetzt damit es bei einem eventuellen Zugriff auf diese zu keinem Absturz kommt.
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.colour = kw.get("color")
#         self.seats = kw.get("seats")