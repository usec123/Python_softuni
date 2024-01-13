import re


class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        search = re.search(r'(.*)@(\w+)\.(\w+)', email)
        return (self.__is_name_valid(search.group(1)) and
                self.__is_mail_valid(search.group(2)) and
                self.__is_domain_valid(search.group(3)))
