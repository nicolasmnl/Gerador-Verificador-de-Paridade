from random import randint

#Giving some style : )
RED   = "\033[1;31m"  
RESET = "\033[0;0m" #default value


def parity_even(data):
    mensagem = data
    bit_paridade = int(mensagem[0])
    for i in range(1, len(mensagem)):
        bit_paridade = bit_paridade ^ int(mensagem[i])

    return mensagem + str(bit_paridade)
        
def parity_odd(data):
    mensagem = data
    bit_paridade = int(mensagem[0])
    for i in range(1, len(mensagem)):
        bit_paridade = bit_paridade ^ int(mensagem[i])

    if (bit_paridade == 0):
        bit_paridade = 1
    else:
        bit_paridade = 0

    return mensagem + (bit_paridade)

'''
Função que vai detectar se houve o erro na mensagem transmitida
Lembrando que o detector de paridade só detecta erro em um único bit
'''
def verificador_de_paridade(gerador_de_paridade,dado_enviado, dado_recebido):
    gerador = gerador_de_paridade
    dado_enviado_com_paridade = gerador(dado_enviado)

    dado_recebido_com_paridade = gerador(dado_recebido)

    print(f"Dado enviado com paridade: {dado_enviado_com_paridade[:len(dado_enviado_com_paridade) - 1] + RED + dado_enviado_com_paridade[len(dado_enviado_com_paridade) - 1] + RESET}")
    print(f"Dado recebido com paridade: {dado_recebido_com_paridade[:len(dado_recebido_com_paridade) - 1] + RED + dado_recebido_com_paridade[len(dado_enviado_com_paridade) - 1] + RESET}")
    flag = True
    if(dado_enviado_com_paridade != dado_recebido_com_paridade):
        flag = False
    
    return flag

#Função responsável por corromper um bit da mensagem a ser enviada. Esse bit é gerado aleatoriamente
def altera_mensagem(dado_enviado):
    bit_que_vai_mudar = randint(0, len(dado_enviado) - 1)

    dado_recebido = dado_enviado[:]
    dado_alterado = ""
    count = 0
    for c in dado_recebido:
        if count == bit_que_vai_mudar:
            if dado_recebido[bit_que_vai_mudar] == '0':
                dado_alterado += '1'
            else:
                dado_alterado += '0'
        else:
            dado_alterado += c
        count += 1
    return dado_alterado

func = parity_even

paridade = input("Digite a paridade do seu sistema(pp - paridade par/ pi - paridade impar): ")


if(paridade.lower() == "pp"):
    print("\n" + "A paridade do seu sistema é: Paridade Par")
    func = parity_even
else:
    print("\n" + "A paridade do seu sistema é: Paridade Ímpar")
    func = parity_odd

dado = input("Digite a mensagem a ser transmitida: ")

res = input("Você quer que a mensagem seja corrompida durante a transmissão (s/n)? ")
if(res.lower() == "s"):
    dado_recebido = altera_mensagem(dado)
else:
    dado_recebido = dado[:]

print()
print(f"Mensagem a ser enviada: {dado}")

if(res.lower() == "s"):
    #Dado recebido com erro
    print(f"Mensagem a ser recebida(com erro): {dado_recebido}")
else:
    #Dado recebido sem erro
    print(f"Mensagem a ser recebida(sem erro): {dado_recebido}")
print()


if(verificador_de_paridade(func, dado, dado_recebido) == True):
    print ("Não foram detectados erros na sua mensagem")
else:
    print("Sua mensagem está corrompida")

