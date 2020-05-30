import classeDisciplina

while True:
    escolha =input( """
     MENU

     1- Cadastrar Sala

     2- Relatório de Salas

     3- Cadastrar Disciplina 

     4- Relatório de Disciplinas

     5- Relatório de disciplinas por semestre

     6- Relacionar Salas as disciplinas

     Escolha: """)
    if escolha == '3':
        classeDisciplina.cadastrar_disciplina()

    if escolha == '4':
        classeDisciplina.imprime_disciplina()



