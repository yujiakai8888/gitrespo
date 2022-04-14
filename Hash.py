class Hash(object):
    """
         @description:
           create a new Hashmap
         @args:
           size: int
         @return:
           None
         """

    def __init__(self, size=5):
        self.__curr__ = 0
        self.len = size
        self.data = []
        self.keynumber = 0
        for i in range(size):
            self.data.append([])

    """
           @description:
             get the size of HashMap
           @args:
             None
           @return:
             type: int
           """

    def size(self):
        return self.len

    """
        @description:
          get the number of key of HashMap
        @args:
          None
        @return:
          type: int
    """

    def key_number(self):
        return self.keynumber

    """
           @description:
             Check whether the hash table contains the key
           @args:
             int
           @return:
             type: bool
    """

    def is_member(self, key):
        for layer1 in self.data:
            for layer2 in layer1:
                if key == layer2:
                    return True
        return False

    """
    @description:
      add new value to HashMap, and handle collision
    @args:
      value: int
    @return:
      bool
    """

    def put(self, key):
        if not type(key) == int:
            return False
        if self.is_member(key):
            return True
        index = key % self.len
        self.data[index].append(key)
        self.keynumber += 1
        return True

    """
     @description:
       remove existing value from HashMap
     @args:
       value: int
     @return:
       True: if value exits in HashMap
       False: if value does not exit in HashMap
     """

    def remove(self, key):
        if not self.is_member(key):
            return False
        index = key % self.len
        self.keynumber -= 1
        for value in self.data[index]:
            if value == key:
                self.data[index].remove(value)
        return True

    """
     @description:
       form a HashMap from a list
     @args:
       list
     @return:
       None
     """

    def from_list(self, list_A):
        if not type(list_A) == list:
            return False
        for i in list_A:
            self.put(i)

    """
     @description:
       get a list formed by HashMap values
     @args:
       None
     @return:
       type: list
     """

    def to_list(self):
        list_A = []
        for i in range(self.len):
            for v in self.data[i]:
                list_A.append(v)
        return list_A

    """
     @description:
       get a list fromed by values which meet the conditions
     @args:
       func: function
       @description: a function to test if the item in HashMap meet the conditions
       @args: item-one of the item in HashMap
       @return:
         if item meets the condition, return True
         if it does not meet the condition, return False
         type: Boolean
     @return:
       type: list
     """

    def filter(self, func):
        res = []
        for i in range(self.len):
            for v in self.data[i]:
                if func(v):
                    res.append(v)
        return res

    """
     @description:
       get a list formed by items in HashMap which processed by a function
     @args:
       func: function
       @description: a function process each item in HashMap
       @args: item
       @return: Anytype
     @return:
       type: list
     """

    def map(self, func):
        res = []
        for i in range(self.len):
            for v in self.data[i]:
                res.append(func(v))
        return res

    """
     @description:
       process each value in HashMap and return a acculumator
     @args:
       func: function
       initial: AnyType
     @return:
       AnyType
     """

    def hash_reduce(self, func, initial):
        accumulator = initial
        for i in range(self.len):
            for v in self.data[i]:
                accumulator = func(accumulator, v)
        return accumulator

    def monoid_add(self, another_hash):
        if another_hash.keynumber == 0:
            return self
        for i in range(another_hash.len):
            for v in another_hash.data[i]:
                if not self.is_member(i):
                    self.put(i)
        self.keynumber += another_hash.keynumber
        return self

    def __iter__(self):
        return self

    def __next__(self):
        if self.keynumber > 0:
            if self.__curr__ < self.keynumber:
                cur = self.__curr__
                for i in range(self.len):
                    if cur >= len(self.data[i]):
                        cur -= len(self.data[i])
                        continue
                    else:
                        tmp = self.data[i][cur]
                        self.__curr__ += 1
                        return tmp
            else:
                self.__curr__ = 0
                raise StopIteration
        else:
            raise StopIteration
