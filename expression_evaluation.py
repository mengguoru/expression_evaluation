import re

class Expression:
    def split(self,expr):
        '''split numbers and operators into a array,return the array (without whiteSpace)'''
        temp = re.split(r"(\+|\-|\*|\/|\(|\))",re.sub(r"\s+",'',expr))
        temp2 = []
        for i in range(len(temp)):
            if temp[i] != '':
                temp2.append(temp[i])
        return temp2
    def infix_to_suffix(self,expr):
        '''Shutting Yard Algorithm'''
        stack_out = []
        stack_operator = []
        for i in range(len(expr)):
            if str(expr[i]) >= '0' and str(expr[i]) <= '9':
                stack_out.append(expr[i])
            else:
                if(len(stack_operator) == 0):
                    stack_operator.append(expr[i])
                else:
                    if str(expr[i]) == ')':
                        temp = stack_operator.pop()
                        while temp != '(':
                            stack_out.append(temp)
                    else:
                        temp = stack_operator.pop()
                        while self.cmp_Precedence(expr[i],temp) == False:
                            stack_out.append(temp)
                            if len(stack_operator) > 0:
                                temp = stack_operator.pop()
                            else:
                                break
                        # if expr[i] precedence >= temp,temp should push back
                        stack_operator.append(temp)
                        stack_operator.append(expr[i])
        while len(stack_operator) > 0:
            stack_out.append(stack_operator.pop())
        return stack_out
    def cmp_Precedence(self,op1,op2):
        if(op1 == '*'or op1 == '/') and (op2 == '+'or op2 == '-'):
            return True
        elif(op1 == '*'or op1 == '/') and (op2 == '*'or op2=='/'):
            return True
        elif(op1=='+'or op1=='-')and(op2=='+'or op2=='-'):
            return True
        else:
            return False
    def evaluate_suffix(self,expr):
        '''Reverse Polish Notation'''
        stack = []
        for i in range(len(expr)):
            if str(expr[i]) >= '0' and str(expr[i]) <='9':
                stack.append(int(expr[i]))
            else:
                stack.append(self.calculate_2_param(expr[i],stack.pop(),stack.pop()))
        return stack.pop()
    def calculate_2_param(self,oper,num1,num2):
        return {'+':num1+num2,'-':num2-num1,'*':num1*num2,'/':num1/num2}[oper]
    def evaluate(self):
        pass
if __name__ == '__main__':
    '''
    5 + ((1 + 2) * 4) − 3转成 [5,1,2,'+',4,'*','+',3,'-']
    '''
    a = Expression()
    b = a.split("5 + ((1 + 2) * 4)−3")
    print(b)
    # print(Expression.split.__doc_    print(b)_)
    # 5 1 2 + 4 * + 3 − 对应后缀    后缀求值应该为14
    c = a.infix_to_suffix(b)
    print(c)