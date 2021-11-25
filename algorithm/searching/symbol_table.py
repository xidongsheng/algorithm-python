import abc

class SymbolTable(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def put(self, k, v):
        pass

    @abc.abstractclassmethod
    def get(self, k):
        pass


class SequentialSearchST(SymbolTable):

    def put(self, k, v):
        print(f'put {k} as {v}')

    def get(self, k):
        print(f'get {k}')


st = SequentialSearchST()
st.put('aa', 'b')
st.get('a')
