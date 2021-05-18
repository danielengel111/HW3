class Link:
    def compute(self, cluster, other):
        pass


class SingleLink(Link):
    def compute(self, cluster, other):
        x0 = cluster.samples[0]
        y0 = other.samples[0]
        minimal_distance = x0.compute_euclidean_distance(y0)
        for x in cluster.samples:
            for y in other:
                d = x.compute_euclidean_distance(y)
                if d < minimal_distance:
                    minimal_distance = d

        return minimal_distance


class CompleteLink(Link):
    def compute(self, cluster, other):
        x0 = cluster.samples[0]
        y0 = other.samples[0]
        maximal_distance = x0.compute_euclidean_distance(y0)
        for x in cluster.samples:
            for y in other:
                d = x.compute_euclidean_distance(y)
                if d > maximal_distance:
                    maximal_distance = d

        return maximal_distance
