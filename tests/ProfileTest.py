from tests.default import DefaultTest
from steps.ProfileStep import ProfileStep


class ProfileTest(DefaultTest):
    def test_about_text(self):
        self.auth_executor()
        step = ProfileStep(self.driver)
        about = step.check_about_text()

        self.assertEqual(
            about != '',
            True,
            'Описание пользователся не отображается'
        )

    def test_delete_add_spec(self):
        self.auth_executor()
        step = ProfileStep(self.driver)
        step.add_spec()
        isOk = step.delete_spec()

        self.assertEqual(
            isOk,
            True,
            'Не удалось удалить специализацию'
        )

    def test_exit(self):
        self.auth_executor()
        step = ProfileStep(self.driver)
        cookies = step.check_exit()

        self.assertEqual(
            cookies[0].get('sessionID'),
            None
        )
