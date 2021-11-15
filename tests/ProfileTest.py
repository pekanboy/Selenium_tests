from tests.default import DefaultTest
from pages.ProfilePage import ProfilePage as Page


class ProfileTest(DefaultTest):
    def test_about_text(self):
        self.initPage(Page(self.driver))
        self.auth_executor()

        about = self.page.get_about_text()

        self.assertEqual(about != "", True, "Описание пользователся не отображается")

    def test_delete_add_spec(self):
        self.initPage(Page(self.driver))
        self.auth_executor()

        self.page.add_spec()
        self.page.select_spec()

        before = len(self.page.get_specs())
        self.page.delete_spec()
        after = len(self.page.get_specs())

        self.assertNotEqual(before, after, "Не удалось удалить специализацию")

    def test_exit(self):
        self.initPage(Page(self.driver))
        self.auth_executor()

        self.page.click_on_exit()
        cookies = self.page.get_cookies()

        self.assertEqual(cookies[0].get("sessionID"), None)
