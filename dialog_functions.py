


def age_check(text: str) -> str:
    print('we are into age function')
    if all(ch.isdigit() for ch in text) and 13 <= int(text) <= 60:
        print(f'in external func  {text}')
        return text
    raise ValueError

def name_check(text: str) -> str:
    return text