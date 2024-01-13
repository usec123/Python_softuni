import re


class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, username):
        if 5 <= len(username) <= 15:
            self.__username = username
        else:
            raise ValueError('The username must be between 5 and 15 characters.')

    @password.setter
    def password(self, password):
        if len(password) >= 8 and len(re.findall(r'[A-Z]', password)) > 0 and \
                len(re.findall(r'\d', password)) > 0:
            self.__password = password
        else:
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*"*len(self.password)}'
