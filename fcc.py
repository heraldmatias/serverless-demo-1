def make_adder(n):
    def add(x):
        return x + n
    return add



def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)



class Adder:
    def __init__(self, n):
         self.n = n
    def __call__(self, x):
        return self.n + x

    def plus(self, x):
        return self.n + x