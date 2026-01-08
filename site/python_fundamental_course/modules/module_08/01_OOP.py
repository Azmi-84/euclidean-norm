import marimo

__generated_with = "0.17.2"
app = marimo.App()


@app.cell
def _():
    # Creating a class
    class Phone:
        category = "Electronics"
    
        def __init__(self, model, battery, camera, battery_percentage=100):
            self.model = model
            self.battery = battery
            self.camera = camera
            self.battery_percentage = battery_percentage
    
    apple = Phone("iPhone 15", "3000mAh", "40MPx")
    motorola = Phone("MT-15", "5000mAh", "80MPx", 40)

    motorola.category = "Super Electronics"

    print(f"{type(apple)} | {apple.category} | {apple.model} | {apple.camera} | {apple.battery} | {apple.battery_percentage}")
    print(f"{type(motorola)} | {motorola.category} | {motorola.model} | {motorola.camera} | {motorola.battery} | {motorola.battery_percentage}")
    return


@app.cell
def _():
    # Creating methods
    class Book:
        def __init__(self, book_name, page, publication, author) -> None:
            self.book_name = book_name
            self.page = page
            self.publication = publication
            self.author = author
    
        def book_information(self): # this is called method
            print(f"Book name: {self.book_name} | Page: {self.page} | Publication: {self.publication} | Author: {self.author}")

    book_one = Book("abcd", 450, 'abcd', 'abcd')
    book_one.book_information()
    return


if __name__ == "__main__":
    app.run()
