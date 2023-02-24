""" linked_list.py

Student: Victor Wong
Mail: victor.wong.8183@student.uu.se
Reviewed by: Maximilian Meyer-Mölleringhof
Date reviewed: 19 September 2022
"""


class LinkedList(object):
    class Node(object):
        def __init__(self, data=None, next=None) -> None:
            self.data = data
            self.next = next

        def __str__(self) -> str:
            return f"Data: {self.data}\nNext:{self.next}"

    def __init__(self):
        self.first = None

    def __iter__(self):  # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.next

    def __in__(self, x):  # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x: int):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.next and x > f.next.data:
                f = f.next
            f.next = self.Node(x, f.next)

    def print(self):
        print("(", end="")
        f = self.first
        while f:
            print(f.data, end="")
            f = f.next
            if f:
                print(", ", end="")
        print(")")

    # To be implemented

    def length(self) -> int:  # Optional
        if self.first is None:
            return 0
        counter = 1
        cur_node = self.first
        while cur_node.next:
            cur_node = cur_node.next
            counter += 1
        return counter

    def mean(self) -> float:  # Optional
        if self.first is None:
            return 0
        sum = self.first.data
        cur_node = self.first
        while cur_node.next:
            cur_node = cur_node.next
            sum += cur_node.data
        return sum / self.length()

    def remove_last(self) -> int:  # Optional
        if self.first is None:
            return None

        if self.first.next is None:
            res = self.first.data
            self.first = None
            return res

        cur_node = self.first

        while cur_node.next.next:
            cur_node = cur_node.next
        res = cur_node.next.data
        cur_node.next = None
        return res

    def remove(self, x: int) -> bool:
        cur_node = self.first
        if cur_node is None:  # Empty list
            return False
        if cur_node.data == x:  # Found x, first node data is x
            self.first = cur_node.next
            return True
        # Iterate through the list whilst there is a next node
        while cur_node.next is not None:
            prev_node = cur_node  # Use a pointer to point at the previous node
            cur_node = cur_node.next  # Update current node to next node
            if cur_node.data == x:  # Found x
                # Updates the previous nodes pointer to the node after the current node
                prev_node.next = cur_node.next
                del cur_node  # Delete current node
                # cur_node = None
                return True
        return False

    def count(self, x: int) -> int:  # Optional
        return self._count(x, self.first)

    def _count(self, x: int, f: Node) -> int:
        if f is None:
            return 0
        if f.data == x:
            return 1 + self._count(x, f.next)
        return self._count(x, f.next)

    def to_list(self) -> list:  # Compulsory
        return self._to_list(self.first)

    def _to_list(self, f: Node) -> list:
        if f is None:
            return []
        return [f.data] + self._to_list(f.next)

    def remove_all(self, x: int):
        if self.first is None:
            return None

        # Handles case where the first element should be removed
        if self.first.data == x:
            self.first = self.first.next
            return self.remove_all(x)

        return self._remove_all(x, self.first)

    def _remove_all(self, x, f):
        if f is None:
            return None

        current_node = f
        prev_node = current_node
        # print(prev_node.data, "PREV")
        if current_node.next:
            # If there is a next node, iterate the current node pointer
            current_node = current_node.next

            if current_node.data == x:
                # set the previous node's pointer to the one after the current node
                prev_node.next = current_node.next
                del current_node

                # Call the function again for the previous node which will check the "new" (updated) current node
                return self._remove_all(x, prev_node)

        # If the current node does not contain the data we are trying to remove, call the function for the current node
        # print(prev_node.next.data, "NEXT")
        return self._remove_all(x, prev_node.next)

    def __str__(self) -> str:  # Compulsary
        if self is None:
            return None
        res = "("
        for d in self:
            res += f"{str(d)}, "
        if len(res) > 2:
            res = res[:-2]
        return res + ")"

    def copy(self):  # Compulsary
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result

    """ Complexity for this implementation: 
    O(n^2). Man går igenom hela listan som man ska kopiera och går igenom hela listan som den ska
    kopieras till för varje element. There is no need to go through the new list for comparisons since we 
    know that the list we are copying is ordered. We just add the next node to the back of the new list. 

    """

    def copy(self):  # Compulsary
        # Creates the LinkedList that will be returned and the first node
        copy_list = LinkedList()
        if self.first is None:
            return copy_list
        copy_list.first = LinkedList.Node(self.first.data, None)

        # Uses recursive help function to copy the subsequent nodes
        copy_list.first.next = self._copy(self.first.next)
        return copy_list

    def _copy(self, node: Node):
        if node is None:
            return None
        # Copies the next nodes
        return LinkedList.Node(node.data, self._copy(node.next))

    """ Complexity for this implementation:
    O(n). We assume that the list is already sorted so the operation does not need to check
    where the node should be inserted. We already know that it should go in the back.
    """

    def __getitem__(self, index):  # Compulsory
        i = 0
        for node in self:
            if i == index:
                return node
            i += 1
        raise IndexError(f"LinkedList index {index} out of range")


class Person:  # Compulsory to complete
    def __init__(self, name: str, pnr: str) -> None:
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"

    def __lt__(self, p):
        return self.name < p.name

    def __le__(self, p):
        return self.name <= p.name

    def __eq__(self, p):
        return self.name == p.name

    def __gt__(self, p):
        return self.name > p.name

    def __ge__(self, p):
        return self.name >= p.name


def main():
    # Test code:
    lst = LinkedList()
    for x in [3, 1, 2, 3, 4, 3, 4, 7, 3]:
        lst.insert(x)
    lst.print()
    # lst_copy = lst.copy()
    # lst_copy.print()
    lst.remove_all(3)
    lst.print()


if __name__ == "__main__":
    main()


"""     def remove_all(self, x):  # Compulsory
        return self._remove_all(x, self.first)

    # Not a very efficient solution, sleek though
    def _remove_all(self, x, f):
        if f is None:
            return None
        self.remove(x)  # Removes x from list
        self._remove_all(x, f.next)  # Does it for each node """


"""     def copy(self):
        copy_list = LinkedList()
        if self.first is None:
            return copy_list

        copy_list.first = LinkedList.Node(self.first.data, None)
        cur_node = copy_list.first
        
        for n in self:
            cur_node.next = LinkedList.Node(n, None)
            cur_node = cur_node.next

        return copy_list """
