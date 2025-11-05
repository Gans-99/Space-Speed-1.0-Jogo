# 🚀 SPACE SPEED 1.0 — Corrida com Obstáculos

Trabalho individual desenvolvido para a disciplina **Fundamentos de Programação**, com o objetivo de implementar um jogo interativo utilizando funções, eventos de teclado e manipulação gráfica com a biblioteca Turtle. O sistema simula uma corrida espacial com obstáculos, na qual o jogador controla uma nave que deve desviar de inimigos, coletar combustível e acumular pontos até o término do jogo.

---

## 🎮 Sobre o Jogo

**SPACE SPEED 1.0** é um jogo de **corrida espacial com obstáculos**, desenvolvido em **Python** utilizando a biblioteca **Turtle Graphics**.
O objetivo é controlar uma nave que deve **desviar de inimigos**, **coletar combustível** e **acumular pontos**, mantendo o máximo de combustível possível até o final. Cada colisão reduz o combustível; quando ele acaba, o jogo termina com **GAME OVER**.

---

## 🧩 Objetivo Acadêmico

Este trabalho foi desenvolvido para consolidar conceitos fundamentais de programação, como:

* Estruturas de repetição e decisão
* Criação e uso de **funções**
* Utilização de **variáveis globais e locais**
* Aplicação de **módulos externos** (`turtle`, `random`, `math`, `time`)
* Manipulação de **gráficos 2D com Turtle**
* Implementação de **eventos de teclado**

---

## 🧠 Conceitos Envolvidos

| Conceito               | Aplicação no Projeto                                                     |
| ---------------------- | ------------------------------------------------------------------------ |
| **Funções**            | Controle de colisões, movimentos e reinício do jogo                      |
| **Condicionais**       | Limite de tela, detecção de colisões, fim de jogo                        |
| **Laços de repetição** | Atualização contínua da tela (loop principal)                            |
| **Bibliotecas**        | Turtle (gráficos), Random (coordenadas), Math (distância), Time (pausas) |
| **Eventos**            | Controle via teclado (setas e espaço)                                    |

---

## ⚙️ Tecnologias e Bibliotecas

* **Python 3.x**
* **Turtle Graphics**
* **Random**
* **Math**
* **Time**

---

## 🧮 Mecânica do Jogo

### 🎯 Objetivo:

* Evite colisões com inimigos.
* Colete combustível para não ficar sem energia.
* Ganhe pontos conforme o plano de fundo se move.

### 💥 Colisões:

* Colidir com inimigos diminui o combustível.
* Colidir com combustível aumenta a quantidade.
* Se o combustível chegar a **0 litros**, o jogo termina com **GAME OVER**.

---

## 🕹️ Controles

| Tecla         | Função                            |
| ------------- | --------------------------------- |
| **← (Left)**  | Move o personagem para a esquerda |
| **→ (Right)** | Move o personagem para a direita  |
| **Espaço**    | Inicia ou reinicia o jogo         |

---

## 💡 Variáveis Principais

| Variável                  | Função                          |
| ------------------------- | ------------------------------- |
| `spaceVeloc`              | Velocidade do plano de fundo    |
| `personagemVeloc`         | Velocidade do personagem        |
| `inimigoVeloc`            | Velocidade dos inimigos         |
| `combustivelVeloc`        | Velocidade do item combustível  |
| `pontos_valor`            | Armazena a pontuação            |
| `combustivel_valorInicio` | Quantidade atual de combustível |

---

## 🧠 Funções Importantes

| Função                      | Descrição                                        |
| --------------------------- | ------------------------------------------------ |
| `Principal()`               | Loop principal do jogo (movimento e colisões)    |
| `colisao()`                 | Reseta posições e reduz combustível após colisão |
| `iniciarJogo()`             | Inicializa ou reinicia o jogo                    |
| `distancia(x1, x2, y1, y2)` | Calcula a distância entre dois objetos           |
| `personagem_p_direita()`    | Move o personagem para a direita                 |
| `personagem_p_esquerda()`   | Move o personagem para a esquerda                |

---

## 🧩 Estrutura Geral

```
.
├── Jogo_No_Turtle.py        # Código principal
├── background05_2.gif       # Plano de fundo
├── personagem_red.gif       # Imagem do personagem
├── inimigo01_red.gif        # Inimigo 1
├── inimigo02_red.gif        # Inimigo 2
├── inimigo03_red.gif        # Inimigo 3
├── combustivel01_redm.gif   # Item combustível
└── explosao01_red1.gif      # Imagem de explosão
```

---

## 🔢 Pontuação e Combustível

* A cada **movimento completo do cenário**, o jogador ganha **+175 pontos**.
* A cada colisão com inimigo: **–100 litros de combustível**.
* A cada coleta de combustível: **+50 litros de combustível**.
* Ao colidir com obstáculos ou sair da pista: **–50 litros de combustível**.

---

## 💻 Como Executar o Jogo

### 1️⃣ Instale o Python

Baixe e instale a versão mais recente em:
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 2️⃣ Coloque todas as imagens e o arquivo `.py` na mesma pasta.

### 3️⃣ Execute o jogo:

Abra o terminal ou prompt de comando na pasta do jogo e digite:

```bash
python Jogo_No_Turtle.py
```

---

## 🎨 Dicas Visuais

* O fundo se move continuamente para dar a sensação de corrida.
* Os inimigos e combustíveis aparecem aleatoriamente na pista.
* A explosão indica colisão — após isso, o jogo pausa por 1 segundo.

---

## 🏁 Condição de Fim

* O jogo encerra automaticamente quando **o combustível chega a 0 litros**.
* A mensagem **“GAME OVER”** aparece, e o jogador pode reiniciar pressionando **ESPAÇO**.

---

## 📈 Possíveis Melhorias Futuras

* Adicionar sons e efeitos (colisão, combustível, motor)
* Criar diferentes níveis de dificuldade
* Implementar tela inicial e menu de pausa
* Incluir ranking com pontuação máxima

---

## 📜 Créditos

| Informações                                          |
|------------------------------------------------------|
| **Autor:** Mahatma Gandhi Pereira Leite              |
| **Disciplina:** Fundamentos de Programação           |
| **Instituição:** Universidade Federal do Ceará (UFC) |
| **Professor:** Prof. Dr. Rafael Ivo Fernandes        |
| **Versão:** 1.0 — SPACE SPEED                        |
| **Ano:** 2022                                        |

---

🛰️ *“Ao infinito e além!”*
