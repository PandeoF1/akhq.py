class akhq:
    def __init__(self, url, username = None, password = None):
        self.url = url
        self.username = username
        self.password = password
        if username and password:
            self.auth = (username, password)
        else:
            self.auth = None
        