from abc import ABCMeta
from abc import abstractmethod

class Set(metaclass=ABCMeta):
    @abstractmethod
    def __contains__(self, element):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Set:
            if any("__contains__" in B.__dict__ for B in C.__mro__) and \
                    any("__iter__" in B.__dict__ for B in C.__mro__) and \
                    any("__len__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

print(issubclass(set, Set))
