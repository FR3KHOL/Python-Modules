import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    # Explicitly type the dictionary so Mypy knows exactly what to expect
    ops: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: max(a, b),
        "min": lambda a, b: min(a, b)
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")

    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": functools.partial(base_enchantment, 50, "fire"),
        "water": functools.partial(base_enchantment, 50, "water"),
        "earth": functools.partial(base_enchantment, 50, "earth")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(arg: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @dispatcher.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @dispatcher.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return dispatcher


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Enchants {target} with {element} (Power: {power})"


def main() -> None:
    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch([1, 2, 3]))
    print(dispatch({"magic": True}))


if __name__ == "__main__":
    main()
