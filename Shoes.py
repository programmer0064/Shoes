class Shoes:

    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def budget_check(self, budget):
        if isinstance(budget, (int, float)):
            print('Invalid input. Please give a number!')
            exit()

    def change(self, budget):
        return(budget-self.price)

    def buy(self, change):
        self.budget_check(budget)

        if budget >= self.price:
            print(f'You can have some {self.name}')

            if budget == self.price:
                print(f'You get no change because it is{change}')
            else:
                print(f"You get some change, which is {change}")
            exit()
              
    

    

    

