from .password_entry import PasswordEntry

class PasswordStore:
    def __init__(self):
        self.entries = []

    def add_entry(self, service, username, password):
        entry = PasswordEntry(service, username, password)
        self.entries.append(entry)

    def list_entries(self):
        return [e.info() for e in self.entries]

    def delete_entry(self, service):
        self.entries = [e for e in self.entries if e.service != service]
