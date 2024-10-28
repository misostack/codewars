class InvalidCase(Exception):
    pass

def assert_equals(value, expected_value, tc = ""):
    print(f"{tc}: {value == expected_value}!")