import sys
from data import Data
from link import SingleLink, CompleteLink
from agglomerative_clustering import AgglomerativeClustering
from cluster import Cluster

def foo(d, samples, link):
    clusters = [Cluster(sample.s_id, [sample]) for sample in samples]
    a = AgglomerativeClustering(link, clusters)
    a.run(7)
    print(f"{link}:")
    for cluster in a.clusters:
        cluster.print_details()
    print()

def main(argv):
    d = Data(argv[1])

    samples = d.create_samples()

    foo(d, samples, SingleLink())
    foo(d, samples, CompleteLink())

if __name__ == '__main__':
    main(sys.argv)
