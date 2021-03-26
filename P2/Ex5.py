from Client0 import Client
from pathlib import Path

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


IP = "127.0.0.1"
PORT = 5000
c = Client(IP, PORT)
c.debug_talk("Sending the U5 Gene to the server...")
c.debug_talk(Path("U5.txt").read_text())
