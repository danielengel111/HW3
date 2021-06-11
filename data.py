import pandas
from sample import Sample


class Data:
    def __init__(self, path):
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient='list')
        print(len(self.data))
        print(len(self.data['samples']))

    def create_samples(self):
        sample_set = []
        for i in range(0, len(self.data['samples'])):
            for key in self.data:
                gene_list = []
                if key == 'samples':
                    sample_id = self.data[key][i]
                elif key == 'type':
                    sample_type = self.data[key][i]
                else:
                    gene_list.append(self.data[key][i])
            sample_set.append(Sample(sample_id, gene_list, sample_type))

        return sample_set
