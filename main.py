import sys
from data import Data
from link import SingleLink, CompleteLink
from agglomerative_clustering import AgglomerativeClustering


def foo(d, samples, link):
    a = AgglomerativeClustering(link, samples)
    a.run(7)
    print(f"{link}:")
    for cluster in a.clusters:
        cluster.print_details(a.compute_summery_silhoeutte()[cluster.c_id])
    print()


def main(argv):
    d = Data(argv[1])
    samples = d.create_samples()
    foo(d, samples, SingleLink())
    foo(d, samples, CompleteLink())


if __name__ == '__main__':
    main(sys.argv)
