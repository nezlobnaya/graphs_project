class Graph:
    def __init__(self):
        self.vertices = {
                            "A": {"B"},
                            "B": {"C", "D"},
                            "C": {"E"},
                            "D": {"F", "G"},
                            "E": {"C"},
                            "F": {"C"},
                            "G": {"A", "F"}
                        }
