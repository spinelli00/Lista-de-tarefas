lista_tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa que deseja adicionar : ")
    lista_tarefas.append(tarefa)
    if tarefa in lista_tarefas :
        print("Tarefa adicionada com sucesso")
    else :
        print("A tarefa não foi adicionada, tente novamente")

def remover_tarefa():
    remover = input("Digite a tarefa que deseja remover : ")
    if remover in lista_tarefas :
        lista_tarefas.remove(remover)
        print("Tarefa removida com sucesso")
    else : 
        print("A tarefa não foi encontrada, tente buscar novamente")

def listar_tarefas():
    if lista_tarefas:
        for indice, tarefa in enumerate(lista_tarefas, start=1):
            print(f"Tarefa {indice}: {tarefa}")
    else:
        print("Nenhuma tarefa foi registrada ainda!")

while True :
    opcao = int(input("Digite uma opcao : \n1.Adicionar tarefa\n2.Remover tarefa\n3.Listar tarefas\n4. Sair"))
    if opcao > 0 & opcao < 4 :
        if opcao == 1 :
            adicionar_tarefa()
        elif opcao == 2 :
            remover_tarefa()
        elif opcao == 3 :
            listar_tarefas()
        elif opcao == 4 :
            print("Programa sendo encerrado ...")
            break
    else :
        print("Opção invalida !")


    