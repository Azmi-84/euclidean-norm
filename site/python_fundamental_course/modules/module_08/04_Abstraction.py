import marimo

__generated_with = "0.17.2"
app = marimo.App()


@app.cell
def _():
    from abc import  ABC , abstractmethod

    class Telephone(ABC):

      @abstractmethod
      def make_call(self):
        pass



    class Sphone(Telephone):
      def make_call(self):
        print("Making a call using SPhone")



    class Iphone(Telephone):
      def make_call_one(self):
        print("Making a call using IPhone")
    return (Iphone,)


@app.cell
def _(Iphone):
    ip = Iphone()

    # ip.make_call_one()
    return


if __name__ == "__main__":
    app.run()
