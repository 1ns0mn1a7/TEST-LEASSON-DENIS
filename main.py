def is_very_long(password):
    return len(password) >= 12


def has_digit(password):
    return any(symbol.isdigit() for symbol in password)


def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)


def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)


def has_symbols(password):
    return any(not (symbol.isdigit() or symbol.isalpha()) for symbol in password)


def password_score(password):
    score = 0

    password_check = [
        (has_digit, 2),
        (is_very_long, 2),
        (has_lower_letters, 2),
        (has_upper_letters, 2),
        (has_symbols, 2)
    ]

    for check, points in password_check:
        if check(password):
            score += points

    return score


def main():
    password = input("Введите пароль: ")
    score = password_score(password)
    print(f"Рейтинг пароля: {score}")


if __name__ == '__main__':
    main()
