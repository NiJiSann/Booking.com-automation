from dataclasses import dataclass
from faker import Faker


@dataclass
class AccountData:
    empty_email = ''
    incorrect_email = 'abc'
    correct_email = 'sally@gmail.com'
    empty_password = ''
    only_lowercase_password = 'aaaaaaaaaa'
    short_password = 'Aaaaa'
    no_uppercase_password = 'aaaaaaaaa1'
    correct_password = 'RightPassword1'

    @staticmethod
    def random_email() -> str:
        fake = Faker()
        email = fake.name().replace(' ', '') + Faker().email()
        return email

    email_data = [(empty_email, 'Please enter your email address'),
                  (incorrect_email, 'Please check if the email address you\'ve entered is correct.'),
                  (random_email(), 'Success')
                  ]

    password_confirm_data = [(empty_password, empty_password, 'Please enter your new password'),
                             (only_lowercase_password, empty_password,
                              'Your password must include at least one number'),
                             (short_password, empty_password,
                              'Your password must be at least 10 characters'),
                             (no_uppercase_password, empty_password,
                              'Your password must include at least one uppercase letter'),
                             (correct_password, empty_password,
                              'Please confirm your password'),
                             (correct_password, only_lowercase_password,
                              'The passwords you entered did not match, please try again'),
                             (correct_password, correct_password, 'Success')
                             ]

    sign_in_email_data = [(empty_email, 'Please enter your email address'),
                          (incorrect_email, 'Please check if the email address you\'ve entered is correct.'),
                          (correct_email, 'Success')
                          ]

    sign_in_password_data = [(empty_password, 'Please enter your Booking.com password'),
                             (short_password, 'Oops! Your password seems to be incorrect. Please try again or use a '
                                              'verification link'),
                             (correct_password, 'Success')
                             ]
