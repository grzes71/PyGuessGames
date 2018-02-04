class GuessGame:
    "Abstract Game base class."

    def __init__(self, name):
        self.gamename = name
        self.username = self.get_user_name()
        self.hello()

    def hello(self):
        print("Hello {}, time to play {} game!".format(self.username, self.gamename))

    @property
    def username(self):
        return self._username
    
    @property
    def gamename(self):
        return self._gamename 

    @gamename.setter
    def gamename(self, value):
        self._gamename = value.title()

    @username.setter
    def username(self, value):
        self._username = value.capitalize()

    def get_user_name(self):
        username = input("What is your name? ")
        return username
