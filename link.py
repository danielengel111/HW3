class Link:
    def compute(self, cluster, other):
        pass


class SingleLink(Link):
    def compute(self, cluster, other):
        distance_arr = []
        for x in cluster.samples:
            for y in other.samples:
                distance_arr.append(x.compute_euclidean_distance(y))
        return min(distance_arr)

    def __str__(self):
        return "single link"


class CompleteLink(Link):
    def compute(self, cluster, other):
        distance_arr = []
        for x in cluster.samples:
            for y in other.samples:
                distance_arr.append(x.compute_euclidean_distance(y))
        return max(distance_arr)

    def __str__(self):
        return "complete link"
