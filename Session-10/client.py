import Client0

c = Client0.Client("127.0.0.1", 8080)
for i in range(0, 5):
    c.debug_talk("Message " + str(i))



#import termcolor
#import colorama

#colorama.init(strip="False")
#print("To server:", end="")
#print(termcolor.colored("Message", "yellow"))
