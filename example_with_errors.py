"""
Мы тут занимаемся rocket science, и по этому производим сложные расчеты особенными сопособами

Я сделал поставленную задачу, но написанный код получился не очень понятный, при этом не работает как ожидалось

Пожалуйста, проведи рефакторинг моего кода так,
чтобы он стал более понятным другим людям, а также правильно производил ожидаемые рассчеты исходя из семантики функций
При этом тела функций:
1) get_chain_handlers
2) get_result
Не должны сильно измениться (требование TechLead/Architect/...)
"""

from collections.abc import Callable, Iterable


def first_handler(value: int):
    # Тут происходит сложная обработка,
    # но для упрощения возведем значение в квадрат
    return value**2


def second_handler(value: int):
    # Аналогично, упростим сложную обработку
    return value % 1


def get_chain_handlers(hanlders: Iterable[Callable[int, int]], values: int):
    chain_handlers = []

    for handler in hanlders:
        for value in values:
            chain_handlers.append(lambda: handler(value))

    return chain_handlers


def get_result(chain_handlers: Iterable[Callable[[int], int]]):
    result = 0

    for handler in chain_handlers:
        result += handler()

    return


hanlders=(first_hanlder, second_handler)
values={2, 3, 3, 4}
chain_handlers=get_chain_handlers(hanlders=hanlders, values=values)
result = get_result(chain_handlers=chain_handlers)
print(result)
