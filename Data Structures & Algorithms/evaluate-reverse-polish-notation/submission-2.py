class Solution:
    def operation(self, num1: str, num2: str, operand: str) -> int:
        numOne = int(num1)
        numTwo = int(num2)
        if ord(operand) == 42:
            return numOne * numTwo
        elif ord(operand) == 43:
            return numOne + numTwo
        elif ord(operand) == 45:
            return numOne - numTwo
        elif ord(operand) == 47:
            return int(numOne / numTwo)
        else:
            return "error"
        
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"+", "-", "*", "/"}
        token = tokens
        stack = []
        for t in token:
            if t in operands:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.operation(num1,num2, t))
            else:
                stack.append(int(t))
        return stack[0]

        