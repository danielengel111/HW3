import sys
from data import Data
from link import SingleLink, CompleteLink
from agglomerative_clustering import AgglomerativeClustering


def foo(d, samples, link):
    a = AgglomerativeClustering(link, samples)
    a.run(7)
    summery_silhoeutte = a.compute_summery_silhoeutte()
    print(f"{link}:")
    for cluster in a.clusters:
        cluster.print_details(summery_silhoeutte[cluster.c_id])
    print(f"whole data: silhouette = {round(summery_silhoeutte[0], 3)}, RI = {round(a.compute_rand_index(), 3)}")


def main(argv):
    d = Data(argv[1])
    samples = d.create_samples()
    foo(d, samples, SingleLink())
    print()
    foo(d, samples, CompleteLink())


if __name__ == '__main__':
    main(sys.argv)
