from Client0 import Client


PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
msg = input("Testing ")
c.debug_talk(msg)
