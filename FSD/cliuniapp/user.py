import re


class User:
    def __init__(self, name: str, email: str, password: str):
        if not all([name, email, password]):
            raise ValueError("All fields are compulsory and cannot be null.")

        email_regex = re.compile(r"[a-zA-Z]+(?:\.[a-zA-Z]+)?@university\.com")
        if not email_regex.match(email):
            raise ValueError("Invalid email format.")

        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long.")

        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {"name": self.name, "email": self.email, "password": self.password}

    @classmethod
    def add_subject(cls, subject: list[str]):
        cls.subject = subject
