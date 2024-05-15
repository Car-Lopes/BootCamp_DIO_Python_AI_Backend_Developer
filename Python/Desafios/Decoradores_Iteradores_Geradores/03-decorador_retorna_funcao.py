def calculadora(operacao):
    def soma(a, b):
        #print("Somei")
        return a + b
         
    
    def subtratacao(a, b):
        return a - b
    
    def multiplicacao(a, b):
        return a * b
    
    def divisao(a, b):
        return a / b
    
    match operacao:
        case "+":
            return soma
        case "-":
            return subtratacao
        case "*":
            return multiplicacao
        case "/":
            return divisao
        

print(calculadora("+")(2, 2))

op = calculadora("*")
print(op(2,2))

op = calculadora("-")
print(op(2,3))

op = calculadora("/")
print(op(4,2))