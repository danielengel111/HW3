class Sample:
    def __init__(self, s_id, genes, label):
        self.s_id = s_id
        self.genes = genes
        self.label = label

    def compute_euclidean_distance(self, other):
        sum = 0
        for i in range(0, len(self.genes)):
            sum += (self.genes[i] - other.genes[i]) ** 2
        return sum ** 0.5

    def distance_of_cluster_from_sample(self, cluster, n):
        sum = 0
        for y in cluster.samples:
            sum += self.compute_euclidean_distance(y)
        return sum / n
