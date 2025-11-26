# Conteúdo Unificado das Aulas de Python

## Aula 1 – Introdução ao Print e Variáveis

```python
print("I Competição de Programação da Start")
ano = "II"
print(ano, "Competição de Programação da Start")
print(f"{ano} Competição de Programação da Start")
```

---

## Aula 2 – Pontuação da Campanha de Leitura

### Contexto

Uma escola está promovendo uma campanha de incentivo à leitura. Cada categoria de livro vale uma quantidade de pontos:

* Ficção: 10 pontos
* Não-ficção: 8 pontos
* Infantil: 6 pontos

Rodrigo leu um livro de cada categoria. Queremos calcular seus pontos.

### Código

```python
livro_ficcao = 10
livro_nficcao = 8
livro_infantil = 6

pontos_rodrigo = livro_ficcao + livro_nficcao + livro_infantil
print(f"Os pontos totais do Rodrigo são: {pontos_rodrigo}")
```

### Desafio

## Ana leu 2 livros de ficção e 5 infantis. Como calcular seus pontos e o total geral?

## Aula 3 – Divisão das Figurinhas

### Contexto

João quer dividir figurinhas de forma justa:

* Todos os amigos recebem a mesma quantidade.
* João recebe o dobro de cada amigo.

### Código

```python
total_figurinhas = int(input("Digite o total de figurinhas: "))
numero_amigos = int(input("Digite o número de amigos: "))

figurinhas_amigos = total_figurinhas // (numero_amigos + 2)
figurinhas_joao = 2 * figurinhas_amigos

print(f"João recebeu {figurinhas_joao} figurinhas.")
```

### Desafio

## Considerar figurinhas extras encontradas na mochila e fazer nova divisão mantendo as regras.

## Aula 4 – Bondinho

### Contexto

Um bondinho leva até 50 pessoas por viagem.

### Código

```python
numero_alunos = int(input("Digite a quantidade de alunos: "))
numero_monitores = int(input("Digite a quantidade de monitores: "))

resposta_positiva = "Pode ir"
resposta_negativa = "Não pode ir"

if numero_alunos + numero_monitores <= 50:
    print(resposta_positiva)
else:
    print(resposta_negativa)
```

### Desafio

## Agora o bondinho só leva 30 pessoas e 8 professores também vão. Verificar se todos cabem.

## Aula 5 – Flíper

### Contexto

No flíper, duas portinhas (P e R) definem o caminho da bolinha.
Valores possíveis: 0 (esquerda) ou 1 (direita).

### Objetivo

Definir para onde a bolinha vai (A, B ou C) conforme P e R.

### Código base (a completar)

```python
P = int(input())
R = int(input())

# lógica para decidir se cai em A, B ou C
```

---

Esse é o conteúdo completo das aulas 1 a 5, organizado e unificado em um único documento.
