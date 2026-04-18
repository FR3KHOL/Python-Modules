from ex0.factories import CreatureFactory, FlameFactory, AquaFactory
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategies import BattleStrategy, NormalStrategy
from ex2.strategies import AggressiveStrategy, DefensiveStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("\n* Battle *")
            f1, s1 = opponents[i]
            f2, s2 = opponents[j]

            c1 = f1.create_base()
            c2 = f2.create_base()

            print(c1.describe())
            print(" vs.")
            print(c2.describe())
            print(" now fight!")

            try:
                s1.act(c1)
                s2.act(c2)
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    f_flame = FlameFactory()
    f_aqua = AquaFactory()
    f_heal = HealingCreatureFactory()
    f_trans = TransformCreatureFactory()

    s_norm = NormalStrategy()
    s_aggro = AggressiveStrategy()
    s_def = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[(Flameling+Normal), (Healing+Defensive)]")
    battle([(f_flame, s_norm), (f_heal, s_def)])
    print()

    print("Tournament 1 (error)")
    print("[(Flameling+Aggressive), (Healing+Defensive)]")
    battle([(f_flame, s_aggro), (f_heal, s_def)])
    print()

    print("Tournament 2 (multiple)")
    t2_str = "[(Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]"
    print(t2_str)
    battle([(f_aqua, s_norm), (f_heal, s_def), (f_trans, s_aggro)])


if __name__ == "__main__":
    main()
