class User(Exception):
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def change_password(self):
        return

    def add_voice_samples(self):
        return

    def update_username(self):
        return


if __name__ == "__main__":
    l = User('Zanetta Tyler', 'zrtyler', '0000')
    print(l)
