import configparser

config = configparser.ConfigParser()
config.read("greeting.cfg")
your_name = config.get("NAME","username",fallback = None)

def say_good_luck(greeting_with_you):
    def good_luck(name):
        if name is not None:
            greeting_with_you(name)
            print("Nice to meet you and good luck, " + name.capitalize())
        else:
            print("Oops, it looks like you do not enter your name")
    return good_luck


@say_good_luck
def greeting_with_you(name):
    print("Hello, " + name.capitalize())

greeting_with_you(your_name)
