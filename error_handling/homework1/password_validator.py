class PasswordTooShortError(Exception):
    pass


class PasswordTooCommonError(Exception):
    pass


class PasswordNoSpecialCharactersError(Exception):
    pass


class PasswordContainsSpacesError(Exception):
    pass


def password_too_common(password_, special_characters):
    only_digit = password_.isdigit()
    only_letters = password_.isalpha()
    only_specials = all(char in special_characters for char in password_)
    return only_digit or only_specials or only_letters


SPECIAL_CHARACTERS = {"@", "*", "&", "%"}


while True:
    password = input()
    if password == "Done":
        break

    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password_too_common(password, SPECIAL_CHARACTERS):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(char in SPECIAL_CHARACTERS for char in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")
