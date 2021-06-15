from cluster import Cluster


class AgglomerativeClustering:
    def __init__(self, link, samples):
        self.link = link
        self.samples = samples
        self.clusters = [Cluster(sample.s_id, [sample]) for sample in samples]
        self.distance_dict = link.compute_distance_dict(samples)

    def out_s(self, x, x_cluster):
        arr = []
        for cluster in self.clusters:
            if cluster == x_cluster:
                continue
            arr.append(x.distance_of_cluster_from_sample(cluster, len(cluster.samples)))
        return min(arr)

    def compute_silhoeutte(self):
        dict = {}
        for cluster in self.clusters:
            for x in cluster.samples:
                if len(cluster.samples) > 1:
                    in_x = x.distance_of_cluster_from_sample(cluster, len(cluster.samples) - 1)
                    out_x = self.out_s(x, cluster)
                    dict[x.s_id] = (out_x - in_x) / max(out_x, in_x)
                else:
                    dict[x.s_id] = 0
        return dict

    def compute_summery_silhoeutte(self):
        dict = {}
        sample_dict = self.compute_silhoeutte()
        for cluster in self.clusters:
            silhoeutte_sum = 0
            for x in cluster.samples:
                silhoeutte_sum += sample_dict[x.s_id]
            dict[cluster.c_id] = silhoeutte_sum / len(cluster.samples)
        silhoeutte_sum = 0
        for sample in self.samples:
            silhoeutte_sum += sample_dict[sample.s_id]
        dict[0] = silhoeutte_sum / len(self.samples)
        return dict

    def compute_rand_index(self):
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        for cluster in self.clusters:
            for first_sample in cluster.samples:
                for second_sample in cluster.samples:
                    if first_sample != second_sample:
                        if first_sample.label == second_sample.label:
                            tp += 1
                        else:
                            fp += 1
            for second_cluster in self.clusters:
                if cluster != second_cluster:
                    for first_sample in cluster.samples:
                        for second_sample in second_cluster.samples:
                            if first_sample.label != second_sample.label:
                                tn += 1
                            else:
                                fn += 1
        return (tp + tn) / (tp + tn + fp + fn)

    def run(self, max_clusters):
        while len(self.clusters) > max_clusters:
            dict = {}
            index = 1
            temp_dict = {}
            for i in range(len(self.clusters)):
                for j in range(i + 1, len(self.clusters)):
                    temp_dict[index] = [self.clusters[i], self.clusters[j]]
                    dict[index] = self.link.compute(self.clusters[i], self.clusters[j])
                    index += 1

            to_merge_index = [key for key in dict if dict[key] == min(dict.values())][0]
            duo = temp_dict[to_merge_index]
            duo[0].merge(duo[1])
            self.clusters.remove(duo[1])
            del duo[1]

