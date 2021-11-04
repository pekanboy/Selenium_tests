from tests.default import DefaultTest
from steps.ClientRegStep import ClientRegStep


class ClientRegTest(DefaultTest):
    def test_login(self):
        step = ClientRegStep(self.driver)
        step.check_err_login()

    def test_name(self):
        step = ClientRegStep(self.driver)
        step.check_err_name()

    def test_email(self):
        step = ClientRegStep(self.driver)
        step.check_err_email()

    def test_password(self):
        step = ClientRegStep(self.driver)
        step.check_err_password()

    def test_good_registration(self):
        step = ClientRegStep(self.driver)
        isOk = step.good_register(self.REG_DATA)
        self.assertEqual(
            isOk,
            True,
            'Не удалось зарегестрироваться'
        )

