class Graph:
    def __init__(self, dataframe):
        self.df = dataframe

    def display(self):
        raise NotImplementedError("Subclasses must implement this method.")
