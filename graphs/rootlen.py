class Solver:
    depth = []
    max_depth = 0
    graph = []
    def __init__(self, fin, fout) -> None:
        self.fout = fout
        with open(fin) as f:
            n = int(f.readline())