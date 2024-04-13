from random import choice,randint

def get_response(userinput:str):
    lowered=userinput.lower()

    if lowered == '':
        return 'dokpo tsik tongpa resha'
    elif 'ls' in lowered:
        return "Command created till date (use ? at starting to send it in private):\n1. hello\n2. whoru\n3. createdat\n4. creator\n5. tibetan?\n6. give a random num"
    elif 'hello' in lowered:
        return 'Tashi Delek bhu'
    elif 'whoru' in lowered:
        return 'A Tibetan Bot'
    elif 'createdat' in lowered:
        return '13-4-2024 11.25 pm IST'
    elif 'creator' in lowered:
        return 'Master Delek haha'
    elif 'tibetan?' in lowered:
        return '100% bodpa'
    elif 'give a random num' in lowered:
        return f'you got: {randint(1,10)}'
    else:
        return choice(['bhu, chik norsha','joke manag nordu layi','oh bahi nordu layi'])