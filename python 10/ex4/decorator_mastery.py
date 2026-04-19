import functools
import time
import inspect
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()

            if 'power' in bound.arguments:
                power_val = bound.arguments['power']
            else:
                power_val = args[0] if args else 0

            if isinstance(power_val, int) and power_val >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    msg = "Spell failed, retrying... "
                    msg += f"(attempt {attempt}/{max_attempts})"
                    print(msg)

            try:
                return func(*args, **kwargs)
            except Exception:
                return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return name.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def waaaaagh_fail() -> str:
    raise Exception("Always fails")


def main() -> None:
    print("Testing spell timer...")
    res1 = fireball()
    print(f"Result: {res1}")

    print("\nTesting retrying spell")
    res2 = waaaaagh_fail()
    print(res2)
    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Merlin"))
    print(guild.validate_mage_name("X"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
