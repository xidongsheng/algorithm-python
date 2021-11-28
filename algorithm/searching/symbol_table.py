import abc

class SymbolTable(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def put(self, k, v):
        pass

    @abc.abstractclassmethod
    def get(self, k):
        pass

    @abc.abstractclassmethod
    def keys(self):
        pass


class Node(object):
    def __init__(self, key='', value='', next=None):
        self.key = key
        self.value = value
        self.next = next


class SequentialSearchST(SymbolTable):
    """sequential implement symbol table, unordered linked list"""

    def __init__(self):
        self.first = None

    def put(self, k, v):
        n = self.first
        while n is not None:
            if n.key == k:
                n.value = v
                return
            n = n.next
        
        self.first = Node(k, v, self.first)

    def get(self, k):
        n = self.first
        while n is not None:
            if n.key == k:
                return n.value
            n = n.next

        return None

    def keys(self):
        key_list = []
        n = self.first
        while n is not None:
            key_list.append(n.key)
            n = n.next

        return key_list


# st = SequentialSearchST()
# st.put('aa', 'a')
# st.put('bb', 'b')
# print(st.get('aa'))
# print(st.get('a'))
# print(st.keys())

class BinarySearchST(SymbolTable):
    """in an orderd array, keys and values are sperately in ordered array"""

    def __init__(self):
        pass

    def rank(self, k):
        pass

    def put(self, k, v):
        pass

    def get(self, k):
        pass

    def keys(self):
        pass