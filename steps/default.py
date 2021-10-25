class DefaultStep:
    def __init__(self, page):
        self.page = page

    def auth(self, email, password):
        self.page.open()
        self.page.fill_Email(email)
        self.page.fill_password(password)
        self.page.submit()
        self.page.wait_profile_container()
