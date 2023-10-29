class TestDataGenerator:
    @staticmethod
    def testdata_for_password_helpers_check():
        test_data = [{"password": "Pass", "helpers_successful": [1], "helpers_failed": [0, 2, 3]},
                     {"password": "password", "helpers_successful": [0], "helpers_failed": [1, 2, 3]},
                     {"password": "12345", "helpers_successful": [2], "helpers_failed": [0, 1, 3]},
                     {"password": "!@#$%", "helpers_successful": [3], "helpers_failed": [0, 1, 2]}
                     ]

        for params in test_data:
            yield params
