from Stack import Stack


def balanced(brackets: str):

    list_brackets: Stack = Stack(list(brackets))
    if list_brackets.size() % 2 != 0:
        return 'Несбалансированно'

    dict_brackets = {
        '(': 0,
        ')': 0,
        '[': 0,
        ']': 0,
        '{': 0,
        '}': 0
    }

    while not list_brackets.is_empty():
        dict_brackets[list_brackets.pop()] += 1

    if dict_brackets['('] == dict_brackets[')'] and dict_brackets['['] == dict_brackets[']'] and dict_brackets['{'] == dict_brackets['}']:
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


brackets_1 = '(((([{}]))))'
brackets_2 = '[([])((([[[]]])))]{()}'
brackets_3 = '{{[()]}}'

brackets_4 = '}{}'
brackets_5 = '{{[(])]}}'
brackets_6 = '[[{())}]'

test_brackets = [brackets_1, brackets_2, brackets_3, brackets_4, brackets_5, brackets_6]

for brackets in test_brackets:
    print(balanced(brackets=brackets))

