import marimo

__generated_with = "0.17.2"
app = marimo.App()


@app.cell
def _():
    class Table:
        def __init__(self, length, width, material, diameter, cross_section) -> None:
            self.length = length
            self.width = width
            self.material = material
            self.diameter = diameter
            self.cross_section = cross_section
    
        def table_info(self):
            print(f"Table Info:\nLength: {self.length} | Width: {self.width} | Material: {self.material} | Diameter: {self.diameter} | Cross Section: {self.cross_section}")

    table_one = Table(23, 12, 'Wood', 3, 43)
    table_one.table_info()
    return (Table,)


@app.cell
def _(Table):
    class SofaTable(Table):
        def __init__(self, length, width, material, diameter, cross_section, style, glass) -> None:
            super().__init__(length, width, material, diameter, cross_section)
        
            self.style = style
            self.glass = glass

        def table_info(self):
            print(f"Table Info:\nLength: {self.length} | Width: {self.width} | Material: {self.material} | Diameter: {self.diameter} | Cross Section: {self.cross_section} | Style: {self.style} | Glass: {self.glass}")
        
    table_two = SofaTable(23, 12, 'Wood', 3, 43, 'abcd', True)
    table_two.table_info()
    return


if __name__ == "__main__":
    app.run()
