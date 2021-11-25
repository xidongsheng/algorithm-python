import sys
import resource

def using(point=""):
    usage = resource.getrusage(resource.RUSAGE_SELF)

    return f'{point}: mem= {usage[2]/(1024*1024)} MB'



class FrequencyCounter(object):
    def __init__(self, filename, min_length) -> None:
        self.filename = filename
        self.min_length = min_length
        self.word_dict = {}
        process_mem = using(point="process_init")
        print(f'{ process_mem }')
        with open(filename, 'r') as f:
            for l in f.readlines():
                words = l.split(' ')
                for word in words:
                    if len(word) < min_length:
                        continue
                    else:
                        if word in self.word_dict.keys():
                            self.word_dict[word] = self.word_dict[word] + 1
                        else:
                            self.word_dict[word] = 1
        print(f'the dict keys is {len(self.word_dict.keys())}')
        print(f'the dict size is {sys.getsizeof(self.word_dict)/(1024*1024)} MB')
        process_mem = using(point="dict_initiled")
        print(f'{ process_mem }')

    def highest(self):
        max_count = 1
        word = ''
        for k in self.word_dict.keys():
            if self.word_dict[k] > max_count:
                max_count = self.word_dict[k]
                word = k
        
        print(f'{word} counts {max_count}')

if __name__ == "__main__":
    fc = FrequencyCounter('algs4-data/leipzig1M.txt', 10)
    fc.highest()
