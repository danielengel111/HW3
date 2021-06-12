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

    def print_details(self, silhouette):
        max=0
        for first_sample in self.samples:
            current=0
            for second_sample in self.samples:
                if first_sample.label==second_sample.label:
                    current+=1
            if current>max:
                dominanet_label=first_sample.label
                max=current
        print(f"Cluster {self.c_id}: {[sample.s_id for sample in sorted(self.samples, key=lambda sample: sample.s_id)]},")
        print(f"dominant label = {dominanet_label}, silhouette = {silhouette}")

