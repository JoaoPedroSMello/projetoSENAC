import classeDisciplina
import classeSala

lst_sala = []


def cadastrar_sala():
    sala = input("Qual o número da sala deseja cadastrar? ")
    capacidade = input("Qual a capacidade da sala? ")
    objeto_sala = classeSala.Sala(sala)
    if sala[0] == '0':
        print("A sala não pode pode começar com 0")
        return cadastrar_sala()
    if capacidade.isnumeric() and sala.isnumeric() and '0' < capacidade < '42':
        lst_sala.append(objeto_sala)
        objeto_sala.set_capacidade(capacidade)
    else:
        print("A capacidade deve estar entra 0 e 41")
        print("Somente números! ")
        return cadastrar_sala()


def relatorio_salas():
    if not lst_sala:
        input("Não temos nenhum dado ainda [Enter] para continuar")
    else:
        for ind, v in enumerate(lst_sala):
            print(ind, v)


lst_disciplina = []


def relatorio_por_semestre():
    semestre = input("Digite o semestre que você deseja saber os cursos cadastrados: ")
    if semestre.isnumeric():
        for disc in lst_disciplina:
            if disc.get_semestre() == semestre:
                print(disc.get_nome())
    else:
        print("Somente numeros! ")
        return relatorio_por_semestre()


def cadastrar_disciplina():
    disciplina = input("Qual disciplina gostaria de cadastrar? ")
    semestre = input("Qual semestre? ")
    if '0' > semestre > '11':
        print("O semestre deve ser maior que 0 e menor que 11! ")
        return cadastrar_disciplina()
    else:
        lst_disciplina.append(classeDisciplina.Disciplina(disciplina.upper(), semestre))


def imprime_disciplina():
    if not lst_disciplina:
        input("Não temos nenhum dado ainda [Enter] para continuar")
    for ind, v in enumerate(lst_disciplina):
        print(ind, v)


def relacionar_salas():
    imprime_disciplina()
    escolha_disciplina = int(input("Qual a disciplina gostaria de vincular a sala? [Escolha pelo índice] "))
    relatorio_salas()
    escolha_sala = int(input("A qual Sala? [Escolha pelo índice] "))
    disciplina = lst_disciplina[escolha_disciplina]
    sala = lst_sala[escolha_sala]
    disciplina.set_sala_disciplina(sala)


while True:
    escolha = input( """
     MENU

     1- Cadastrar Sala

     2- Relatório de Salas

     3- Cadastrar Disciplina 

     4- Relatório de Disciplinas

     5- Relatório de disciplinas por semestre

     6- Relacionar Salas as disciplinas
     
     7- Sair do programa

     Escolha: """)
    if escolha == '1':
        cadastrar_sala()

    if escolha == '2':
        relatorio_salas()

    if escolha == '3':
        cadastrar_disciplina()

    if escolha == '4':
        imprime_disciplina()

    if escolha == '5':
        relatorio_por_semestre()

    if escolha == '6':
        relacionar_salas()

    if escolha == '7':
        break


