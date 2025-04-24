
valortotal = float(input('Digite o valor total da compra efetuada: '))
identificacao = input('Digite se você é um cliente comum ("C"), funcionário ("F") ou vip ("V"): ') .lower()

valorfuncionário1 = valortotal * 0.10
valorfuncionário1 = valortotal - valorfuncionário1

valorvip = valortotal * 0.05
valorvip = valortotal -valorvip

match identificacao: 
    case 'c' | 'cliente comum':
        print ('Você é um cliente comum')
        print (f'O valor total da compra foi {valortotal}')

    case 'funcionario' | 'f':
        print ('Você é um funcionário')
        print (f'O valor com desconto é{valorfuncionário1}')

    case 'v' | 'vip':
        print ('Você é um cliente vip')
        print (f'O valor com desconto é {valorvip}')