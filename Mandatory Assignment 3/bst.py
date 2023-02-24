""" bst.py

Student: Victor Wong
Mail: victor.wong.8183@student.uu.se
Reviewed by: Maximilian Meyer-Mölleringhof
Date reviewed:19 September 2022
"""


from linked_list import LinkedList
from math import log2, log10
import random
import matplotlib.pyplot as plt


class BST:
    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):  # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):  # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=" ")
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

    #
    #   Methods to be completed
    #

    def height(self):  # Compulsory
        return self._height(self.root)

    def _height(self, r):
        if r is None:
            return 0
        return 1 + max(self._height(r.left), self._height(r.right))

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):  # Compulsory
        if r is None:
            return None
        elif k < r.key:
            # r.left = left subtree with k removed
            r.left = self._remove(r.left, k)

        elif k > r.key:
            # r.right =  right subtree with k removed
            r.right = self._remove(r.right, k)

        else:  # This is the key to be removed
            if r.left is None:  # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                cur_node = r.right  # Keeps track of current node
                prev_node = cur_node  # Keeps track of previous node
                if cur_node.left:
                    cur_node = cur_node.left
                # If there is a node to the left update current node
                while cur_node.left:
                    prev_node = cur_node
                    cur_node = cur_node.left
                r.key = cur_node.key
                prev_node.left = None

                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above

    def __str__(self):  # Compulsory
        res = "<"
        for d in self:
            res += f"{str(d)}, "
        if len(res) > 2:
            res = res[:-2]
        return res + ">"

    def to_list(self):  # Compulsory
        return self._to_list(self.root)

    def _to_list(self, r):
        if r is None:
            return []
        return self._to_list(r.left) + [r.key] + self._to_list(r.right)

    def to_LinkedList(self):  # Compulsory
        res = LinkedList()
        for node in self:
            res.insert(node)
        return res

    def ipl(self):  # Compulsory
        return self._ipl(self.root)

    def _ipl(self, r, lvl=1):
        if r is None:
            return 0
        return lvl + self._ipl(r.left, lvl + 1) + self._ipl(r.right, lvl + 1)

    def iter_insert(self, key):
        # Handles the first node
        if self.root is None:
            self.root = self.Node(key)
            return self.root

        r = self.root
        while r is not None:
            if key < r.key:
                # Add new node to the left if None to left
                if r.left is None:
                    r.left = self.Node(key)
                    return r
                else:
                    # Traverse left
                    r = r.left
            if key > r.key:
                # Add new node to the right if None to right
                if r.right is None:
                    r.right = self.Node(key)
                    return r
                else:
                    # Traverse right
                    r = r.right


def random_tree(n):  # Useful
    r_tree = BST()
    for _ in range(n):
        r_tree.insert(random.random())
    return r_tree


def main():
    t = BST()
    print(t)
    for x in [7, 4, 2, 6, 9, 5]:
        t.iter_insert(x)
    print(t.to_list())

    # print("size  : ", t.size())
    # for k in [0, 1, 2, 5, 9]:
    #   print(f"contains({k}): {t.contains(k)}")

    # print(diff)
    sizes = [10, 100, 1000, 10000, 100000]
    height, average_node_height, diff = [], [], []
    for i, e in enumerate(sizes):
        r = random_tree(e)
        height.append(r.height())
        average_node_height.append(r.ipl() / r.size())
        diff.append(average_node_height[i] - 1.39 * log2(e))

    """
    diff = [-1.1174800518934331, -1.914960103786866, -1.9654401556802998, -1.5611202075737332, -1.424060259467165]
    The difference between the theoretical and experimental value does not grow with n. It stays more or less constant
    (n grows by 10-fold each step).
    """

    plt.figure()
    plt.subplot(211)
    plt.xlabel("log10 Size")
    plt.ylabel("Height")
    plt.xticks(list(map(log10, sizes)))
    plt.grid()
    plt.plot(list(map(log10, sizes)), height)

    plt.subplot(212)
    plt.xlabel("log10 Size")
    plt.ylabel("Average Node Height")
    plt.xticks(list(map(log10, sizes)))

    plt.grid()
    plt.plot(list(map(log10, sizes)), average_node_height)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size?
Yes!
2. computing height?
No
3. contains?
Works, but not as good as recursion
4. insert?
No, does not "see" the structure 
5. remove?
No, does not "see" the structure




Results for ipl of random trees
===============================





"""
