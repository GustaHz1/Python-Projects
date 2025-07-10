import numpy as np
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
from time import time
from torchvision import datasets, transforms
from torch import nn, optim

# =============================
# 1. Preparação dos Dados (MNIST)
# =============================

# Converte as imagens do dataset para tensores normalizados
transform = transforms.ToTensor()

# Baixa e carrega o dataset de treino
trainset = datasets.MNIST('./MNIST_data/', download=True, train=True, transform=transform) 
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

# Baixa e carrega o dataset de validação
valset = datasets.MNIST('./MNIST_data/', download=True, train=False, transform=transform)
valloader = torch.utils.data.DataLoader(valset, batch_size=64, shuffle=True)

# Mostra uma imagem de exemplo
dataiter = iter(trainloader)
imagens, etiquetas = next(dataiter)
plt.imshow(imagens[0].numpy().squeeze(), cmap='gray_r')
plt.title(f"Etiqueta: {etiquetas[0].item()}")
plt.show()

print("Shape da imagem:", imagens[0].shape)
print("Shape da etiqueta:", etiquetas[0].shape)

# =============================
# 2. Definição do Modelo (Rede Neural)
# =============================

class Modelo(nn.Module):
    def __init__(self):
        super(Modelo, self).__init__()
        # Camada de entrada: 784 (28x28) -> 128 neurônios
        self.linear1 = nn.Linear(28*28, 128)
        # Camada intermediária: 128 -> 64 neurônios
        self.linear2 = nn.Linear(128, 64)
        # Camada de saída: 64 -> 10 (um para cada dígito de 0 a 9)
        self.linear3 = nn.Linear(64, 10)

    def forward(self, x):
        # Ativações ReLU nas camadas ocultas
        x = F.relu(self.linear1(x))
        x = F.relu(self.linear2(x))
        # Última camada sem ativação
        x = self.linear3(x)
        # Aplica log-softmax para facilitar o cálculo da perda (NLLLoss)
        return F.log_softmax(x, dim=1)

# =============================
# 3. Função de Treinamento
# =============================

def treino(modelo, trainloader, device):
    # Otimizador (Stochastic Gradient Descent)
    otimizador = optim.SGD(modelo.parameters(), lr=0.003, momentum=0.5)
    criterio = nn.NLLLoss()
    EPOCHS = 10

    modelo.train()  # Coloca o modelo em modo de treino
    inicio = time()

    for epoch in range(EPOCHS):
        perda_acumulada = 0

        for imagens, etiquetas in trainloader:
            # Achata as imagens de 28x28 para vetor de 784 (1D)
            imagens = imagens.view(imagens.shape[0], -1).to(device)
            etiquetas = etiquetas.to(device)

            otimizador.zero_grad()  # Zera os gradientes

            output = modelo(imagens)  # Faz a previsão
            perda = criterio(output, etiquetas)  # Calcula a perda

            perda.backward()  # Propagação reversa
            otimizador.step()  # Atualiza os pesos

            perda_acumulada += perda.item()

        print(f"Epoch {epoch+1} - Perda média: {perda_acumulada/len(trainloader):.4f}")

    print("\nTempo de treino (em minutos): {:.2f}".format((time() - inicio) / 60))

# =============================
# 4. Função de Validação
# =============================

def validacao(modelo, valloader, device):
    modelo.eval()  # Modo avaliação (desliga dropout, batchnorm, etc.)
    total_corretas = 0
    total_amostras = 0

    with torch.no_grad():  # Desativa o cálculo do gradiente
        for imagens, etiquetas in valloader:
            for i in range(len(etiquetas)):
                img = imagens[i].view(1, 784).to(device)
                etiqueta_real = etiquetas[i].item()

                logps = modelo(img)
                ps = torch.exp(logps)  # Converte de log-probabilidades para probabilidades
                predicao = torch.argmax(ps, dim=1).item()

                if predicao == etiqueta_real:
                    total_corretas += 1
                total_amostras += 1

    print(f"\nTotal de imagens testadas = {total_amostras}")
    print(f"Precisão do modelo = {100 * total_corretas / total_amostras:.2f}%")

# =============================
# 5. Execução
# =============================

# Usa GPU se disponível
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Cria uma instância do modelo
modelo = Modelo().to(device)

# Treina o modelo
treino(modelo, trainloader, device)

# Valida o modelo
validacao(modelo, valloader, device)
