

class Stack:
    """
    Stack implementation using Python list.
    """
    def __init__(self):
        self.stack = []

    def __repr__(self):
        """
        Override __repr__ value to show values inside the stack.
        :return: str. Values of the tokens in the stack.
        """
        desc = ""

        # List comprehension, fyi.
        return desc.join(str(elem.get_value()) for elem in self.stack)

    def is_empty(self) -> bool:
        """
        Shows if the stack is empty or not.
        :return: bool. True if empty, false if not empty.
        """
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, value: any) -> None:
        """
        Pushs an element to the stack.
        :param value: any value.
        """
        self.stack.append(value)

    def top(self) -> any:
        """
        Shows top element of the stack.
        :return: Top element of the stack.
        """
        return self.stack[-1]

    def pop(self) -> any:
        """
        Shows top element of the stack and removes it from
        the stack.
        :return: Top element of the stack.
        """
        return self.stack.pop()

