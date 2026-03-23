import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino


class CoffeeMachine:
    def __init__(self):
        self.drinks_served = 0

    class EmptyCup(HotBeverage):
        name = "empty cup"
        price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self, message="This coffee machine has to be repaired."):
            super().__init__(message)

    def repair(self):
        self.drinks_served = 0

    def serve(self, beverage_class: HotBeverage):
        if self.drinks_served >= 10:
            raise CoffeeMachine.BrokenMachineException()

        self.drinks_served += 1

        if random.choice([True, False]):
            return beverage_class()
        else:
            return CoffeeMachine.EmptyCup()


if __name__ == '__main__':
    machine = CoffeeMachine()
    available_beverages = [Coffee, Tea, Chocolate, Cappuccino, HotBeverage]

    for _ in range(2):
        try:
            for i in range(12):
                print(machine.serve(random.choice(available_beverages)))
                print("\n")
        except CoffeeMachine.BrokenMachineException as e:
            print("------")
            print(e)
            print("------\n")
            machine.repair()
