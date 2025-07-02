class Tarefa:
    def __init__(self, titulo, status="pendente"):
        self.titulo = titulo
        self.status = status

    def concluir(self):
        self.status = "concluída"

class ListaTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)

    def listar(self):
        for t in self.tarefas:
            print(f"{t.titulo} - {t.status}")
