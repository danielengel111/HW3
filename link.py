class Link:
    def __init__(self):
        self.distance_dict = {}

    def compute(self, cluster, other):
        pass

    def compute_distance_dict(self, samples):
        for i in range(0, len(samples)):
            for j in range(i + 1, len(samples)):
                self.distance_dict[(samples[i].s_id, samples[j].s_id)] = samples[i].compute_euclidean_distance(samples[j])

    def create_distance_arr(self, cluster, other):
        distance_arr = []
        for x in cluster.samples:
            for y in other.samples:
                if x.s_id > y.s_id:
                    distance_arr.append(self.distance_dict[(y.s_id, x.s_id)])
                else:
                    distance_arr.append(self.distance_dict[(x.s_id, y.s_id)])

        return distance_arr


class SingleLink(Link):
    def compute(self, cluster, other):
        distance_arr = self.create_distance_arr(cluster, other)
        return min(distance_arr)

    def __str__(self):
        return "single link"


class CompleteLink(Link):
    def compute(self, cluster, other):
        distance_arr = self.create_distance_arr(cluster, other)
        return max(distance_arr)

    def __str__(self):
        return "complete link"

