class SingleLinkedListNode(object):
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr(nval)}]"

class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """append to end of list"""

    def pop(self):
        """removes last item and returns it"""

    def shif(self, obj):
        """ another name for push """
    def unshift(self):
        """removes first item and returns it"""

    def remove(self, obj):
        """ finds a matching item and gets it off the list"""

    def first(self):
        """ returns a ref to the first item """

    def last(self):
        """ returns a ref to the last item"""
    def count(self):
        """counts number of elements"""

    def get(self, index):
        """ get value of index"""

    def dump(self, mark):
        """ debuggin function that dumps contents of the list """

    
