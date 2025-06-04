lista = []

escolha = 0
cout = 0
while(escolha != 4):    
    print("escolha uma opção:")
    print("digite 1 para adcionar nova tarefa")
    print("digite 2 para listar todas as tarefas")
    print("digite 3 para marcar tarefa como concluida")
    print("digite 4 para sair")
    
    escolha = int(input())
    if(escolha == 1):
        programa = {
            "codigo": " ",
            "tarefa": " ",
            "descrição": " ",
            "status": "pendente"
        }
        cout = cout +1
        print("escreva a descrição da nova tarefa")
        programa["tarefa"] = input()
        programa["codigo"] = cout
        lista.append(programa)
        
    if(escolha == 2):
        print(lista)
        
    if(escolha == 3):
        print("digite o id da tarefa concluida")
        aux = int (input())
        for l in lista:
            if l["codigo"] == aux:
                l["status"] = "concluido" 
                print("status da tarefa alterado para concluido")
        
    