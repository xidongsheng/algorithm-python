
class QuickFind():

    def __init__(self, n):
        self.ids = []
        self.count = n
        for i in range(n):
            self.ids.append(i)

    def find(self, i):
        return self.ids[i]
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)

        if pId == qId:
            return
        
        for j in range(len(self.ids)):
            if self.ids[j] == pId:
                self.ids[j] = qId

        self.count -= 1

def main():
    with open('algs4-data/mediumUF.txt', 'r') as f:
        data = f.readlines()
    
    qf = QuickFind(int(data[0]))
    print(f'the init QuickFind, components count is {qf.count}')

    for line in data[1:]:
        line = line.strip()
        nums = line.split(' ')
        qf.union(int(nums[0]), int(nums[1]))

    print(f'after connecting, components count is {qf.count}')


if __name__ == "__main__":
    main()