# TaskTracker

Sistema de linha de comando para organizar tarefas, feito em Python e empacotado com Docker.

**Autor:** Thiago Assis Lopes
**Curso:** Ciência da Computação

## O que o sistema faz

- Cadastra tarefas (título, descrição, prioridade e data limite)
- Lista as tarefas cadastradas
- Marca tarefas como concluídas

Regras: o título é obrigatório, a prioridade deve ser Alta, Média ou Baixa e toda tarefa nova começa como Pendente.

## Como rodar com Docker

Pré-requisito: ter o Docker instalado.

### 1. Como construir a imagem

```bash
docker build -t tasktracker .
```

### 2. Como rodar o container em modo isolado

```bash
docker run -it --rm tasktracker
```

### 3. Como rodar via orquestração (Recomendado)

```bash
docker compose run --rm tasktracker-app
```

> O `-it` (no `docker run`) e o `stdin_open` + `tty` (no compose) são necessários porque o programa usa `input()` e precisa de um terminal interativo.

## Estrutura do projeto

```
tasktracker-projeto/
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
├── src/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```
