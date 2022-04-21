import re


class Uteis:

    @staticmethod
    def is_not_blank(s):
        return bool(s and not s.isspace())

    @staticmethod
    def check(email):
        email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        if re.search(email_regex, email):
            return True
        return False