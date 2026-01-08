import marimo

__generated_with = "0.17.2"
app = marimo.App()


@app.cell
def _():
    print(len("Hello World"), len((12, 23, 34)), len({'a': 'a', 'b': 'b'}))
    return


@app.cell
def _():
    class Car:
        def __init__(self, brand, model) -> None:
            self.brand = brand
            self.model = model
    
        def info(self):
            return "Brand: {self.brand} and Model: {self.model}"

    class Ship:
        def __init__(self, brand, model) -> None:
            self.brand = brand
            self.model = model
    
        def info(self):
            return "Brand: {self.brand} and Model: {self.model}"

    class Airplane:
        def __init__(self, brand, model) -> None:
            self.brand = brand
            self.model = model
    
        def info(self):
            return "Brand: {self.brand} and Model: {self.model}"

    car_one = Car('abcd', 'efgh')
    ship_one = Ship('ijkl', 'mnop')
    airplane_one = Airplane('qrst', 'uvwx')

    print([item.info() for item in (car_one, ship_one, airplane_one)])
    return


if __name__ == "__main__":
    app.run()
