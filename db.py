# Simulando banco de dados com dicionários
cursos = {
    1: {'nome': 'Engenharia de Software'},
    2: {'nome': 'Ciência da Computação'}
}

pessoas = {
    1: {'nome': 'Ana Silva'},
    2: {'nome': 'Bruno Costa'},
    3: {'nome': 'Carlos Pereira'},
    4: {'nome': 'Daniela Souza'},
    5: {'nome': 'Eduardo Lima'},
    6: {'nome': 'Fernanda Rocha'},
    7: {'nome': 'Gustavo Almeida'},
    8: {'nome': 'Helena Martins'},
    9: {'nome': 'Igor Ribeiro'},
    10: {'nome': 'Juliana Alves'}
}

alunos = {
    1: {'pessoa_id': 1, 'curso_id': 1, 'tipo': 'aluno'},
    2: {'pessoa_id': 2, 'curso_id': 1, 'tipo': 'aluno'},
    3: {'pessoa_id': 3, 'curso_id': 2, 'tipo': 'aluno'},
    4: {'pessoa_id': 4, 'curso_id': 2, 'tipo': 'aluno'},
    5: {'pessoa_id': 5, 'curso_id': 1, 'tipo': 'aluno'}
}

professores = {
    1: {'pessoa_id': 6, 'curso_id': 1, 'tipo': 'professor'},
    2: {'pessoa_id': 7, 'curso_id': 2, 'tipo': 'professor'},
    3: {'pessoa_id': 8, 'curso_id': 3, 'tipo': 'professor'},
    4: {'pessoa_id': 9, 'curso_id': 4, 'tipo': 'professor'},
    5: {'pessoa_id': 10, 'curso_id': 5, 'tipo': 'professor'}
}