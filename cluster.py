class Cluster:
    def __init__(self, c_id, samples):
        self.c_id = c_id
        self.samples = samples

    def merge(self, other):
        for sample in other.samples:
            self.samples.append(sample)

        self.samples = sorted(self.samples, key=lambda s: s.s_id)
        self.c_id = min(self.c_id, other.c_id)
        del other

    def print_details(self):#, silhouette):
        print(f"Cluster {self.c_id}: {[sample.s_id for sample in self.samples]}")

