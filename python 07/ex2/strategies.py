import abc
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            m = f"Invalid Creature '{creature.name}' for normal strategy"
            raise Exception(m)
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            m = (f"Invalid Creature '{creature.name}' "
                 "for this aggressive strategy")
            raise Exception(m)
        assert isinstance(creature, TransformCapability)
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            m = (f"Invalid Creature '{creature.name}' "
                 "for this defensive strategy")
            raise Exception(m)
        assert isinstance(creature, HealCapability)
        print(creature.attack())
        print(creature.heal())
