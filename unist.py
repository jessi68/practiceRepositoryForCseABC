#uni-uni!

class student :
    def __init__(self, name, id) :
        self.name = name
        self.id = id
    def introduce(self):
        print("Hello! I'm {} {}! Nice to meet you!".format(self.id, self.name))

if __name__ == "__main__":
    a = student("방재현", 20221193)
    a.introduce()
