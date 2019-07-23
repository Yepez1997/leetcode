class AssignBikes:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        def dist(w, b):
          return abs(w[0] - b[0]) + abs(w[1] - b[1])
        pairs = [(dist(posw, posb), idxw, idxb) for idxw, posw in enumerate(
            workers) for idxb, posb in enumerate(bikes)]
        pairs.sort()
        bikesSeen = set()
        res = [None] * len(workers)

        for _, idxw, idxb in pairs:
          if idxb not in bikesSeen and res[idxw] == None:
            res[idxw] = idxb
            bikesSeen.add(idxb)
            if len(bikesSeen) == len(workers):
              break

        return res
