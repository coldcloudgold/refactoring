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
from functools import partial


# > Хинтинг возвращаемого значения
def first_handler(value: int) -> int:
    # Тут происходит сложная обработка,
    # но для упрощения возведем значение в квадрат
    return value**2


# > Хинтинг возвращаемого значения
# > Логически можно понять, что остаток деления любого целого числа на 1 всегда будет равен 0 (не обязательно, но хорошо если было подмечено)
def second_handler(value: int) -> int:
    # Аналогично, упростим сложную обработку
    return value % 1


# > Хинтинг параметров:
# 1) hanlders: в Callable для входных параметор используется список, внутри которого перечисляются типы параметров, иначе не взлетит
# 2) values: по множественному числу и итерации внутри функции - можно понять, что это последовательность целых чисел
# > Замена lambda на partial, чтобы код начал действительно работать как задумывалось (производить нужные рассчеты)
# Без этого - фактически список будет заполнен только последней функцией из параметра hanlders (second_handler), при этом аргумент у функции вообще везде будет последним значением из values (4)
# > Хинтинг возвращаемого значения
def get_chain_handlers(hanlders: Iterable[Callable[[int], int]], values: Iterable[int]) -> list[Callable[[], int]]:
    chain_handlers = []

    for handler in hanlders:
        for value in values:
            chain_handlers.append(partial(handler, value))

    return chain_handlers


# > Хинтинг параметров:
# 1) chain_handlers: здесь первым параметров в Callable должен быть пустой список,
# так как 'обработичики' уже получили параметры в get_chain_handlers
# > Добавление возврата результата
# > Хинтинг возвращаемого значения
def get_result(chain_handlers: Iterable[Callable[[], int]]) -> int:
    result = 0

    for handler in chain_handlers:
        result += handler()

    return result


# > Исправление названия функции first_handler, иначе не взлетит (не обязательно, но хорошо если было подмечено)
# > Удалена лишняя 3 в values (не обязательно, но хорошо если было подмечено)
hanlders=(first_handler, second_handler)
values={2, 3, 4}
chain_handlers=get_chain_handlers(hanlders=hanlders, values=values)
result = get_result(chain_handlers=chain_handlers)
print(result)
