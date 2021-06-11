class Cluster:
    def __init__(self, c_id, samples):
        self.c_id = c_id
        self.samples = samples

    def merge(self, other):
        for sample in other.samples:
            self.samples.append(sample)
        del other

    def print_details(self):#, silhouette):
        print(f"Cluster {self.c_id}: {[sample.s_id for sample in sorted(self.samples, key=lambda sample: sample.s_id)]}")

