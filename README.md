# Modulo_1_projeto_sofIA
# <span style="color:#1E90FF;">**Projeto em Python – Boletim EduSimples**</span>

## <span style="color:#32CD32;">**Módulo 1 – Curso Compet Médio (Extensão em Inteligência Artificial)**</span>

O projeto do **Boletim EduSimples** foi desenvolvido como atividade prática do **Módulo 1** do curso Compet Médio, no curso de extensão em Inteligência Artificial.  
Seu objetivo é proporcionar uma experiência inicial de programação em Python, aplicando conceitos de **lógica de programação, estruturas de dados e funções** em um contexto educacional.  

---

## <span style="color:#FF8C00;">**Objetivo do Projeto**</span>

O sistema tem como finalidade **gerenciar o boletim dos alunos**, permitindo o cadastro, consulta e manipulação de informações essenciais, como matrícula, nome e notas.  
A partir desses dados, o programa calcula automaticamente a **média** do aluno e define sua **situação final**, classificando-o como:  

- ✅ **Aprovado** – média maior ou igual a 7,0  
- ⚠️ **Em recuperação** – média entre 5,0 e 6,9  
- ❌ **Reprovado** – média inferior a 5,0  

---

## <span style="color:#8A2BE2;">**Estrutura e Funcionalidades**</span>

O projeto foi construído com base em **funções** para organizar o código e facilitar a manutenção.  
As principais funções implementadas são:  

- `cadastrar()` – responsável por registrar novos alunos com validação de dados.  
- `alterar()` – permite modificar informações já cadastradas.  
- `excluir()` – remove um aluno da lista.  
- `listar()` – exibe todos os alunos cadastrados com seus respectivos boletins.  

📌 Para representar cada aluno, pode-se utilizar **dicionários** ou uma **classe Aluno**, contendo os atributos:  

- `matricula`  
- `nome`  
- `n1`, `n2`  
- Método `media()`  
- Método `situacao()`  

---

## <span style="color:#DC143C;">**Tratamento de Erros**</span>

O projeto incorpora **estruturas de tratamento de exceções (`try/except`)**, garantindo que entradas inválidas, como notas fora do intervalo ou valores incorretos, sejam devidamente tratadas, evitando falhas no sistema.  

---

## <span style="color:#20B2AA;">**Resultado Esperado**</span>

Ao final da execução, o programa deverá apresentar uma **lista clara e organizada no console**, exibindo:  

- Nome do aluno  
- Matrícula  
- Nota 1 e Nota 2  
- Média  
- Situação  
