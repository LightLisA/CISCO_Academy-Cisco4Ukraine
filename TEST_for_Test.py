class Stack:
    def __init__(self):
        self.__stk = []
        # print("Stack  __init__ = ", self.__stk)

    def push(self, val):
        # print("Stack  push = ", val)
        self.__stk.append(val)
        # print("Stack  push       = ", self.__stk)

    def pop(self):
        val = self.__stk[-1]
        # print("Stack  POP = ", val)
        del self.__stk[-1]
        # print("Stack  DEL     = ", self.__stk)
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    # Fill the constructor with appropriate actions.

    def get_counter(self):
        return self.__sum

    # Present the counter's current value to the world.

    def pop(self):
        # print("Stack.pop(self) = = = = = >>>>")
        val = Stack.pop(self)
        # print("CountingStack  POP = ", val)
        self.__sum += 1
        # print("CountingStack  SUM      = ", self.__sum)
        return val
    # Do pop and update the counter.


stk = CountingStack()
for i in range(100):
    stk.push(i)
    # print("push ====================================================== ")
    stk.pop()
    # print("pop ++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(stk.get_counter())
