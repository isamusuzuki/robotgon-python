import unittest

from apps.renrakumo.twilio_handler import TwilioHandler

from dotenv import load_dotenv


class Test(unittest.TestCase):
    def setUp(self):
        self.handler = TwilioHandler()

    def test_calc_price(self):
        self.assertEqual(self.handler.calc_price(60), 9)
        self.assertEqual(self.handler.calc_price(80), 18)
        self.assertEqual(self.handler.calc_price(100), 18)
        self.assertEqual(self.handler.calc_price(200), 27)

    def test_format_e164(self):
        self.assertEqual(
            self.handler.format_e164('080-3759-8996'),
            '+818037598996'
        )
        self.assertEqual(
            self.handler.format_e164('070-8469-6246'),
            '+817084696246'
        )


if __name__ == '__main__':
    load_dotenv()
    unittest.main()
