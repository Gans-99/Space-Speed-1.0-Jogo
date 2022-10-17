'''

                             TRABALHO INDIVIDUAL 1 DE FUNDAMENTOS DE PROGRAMAÇÃO
                                         CORRIDA COM OBSTÁCULOS
                                  DISCENTE: Mahatma Gandhi Pereira Leite
                                            MATRÍCULA: 542480

'''
# SESSÃO DE IMPORTAÇÕES DE BIBLIOTECAS DO PYTHON:
import turtle, random, math, time     # Importa a biblioteca Turtle, Sorteio e Fórmulas de Matemática

# SESSÃO DE ABERTURA DA JANELA DO TURTLE:
janela = turtle.Screen()                    # Abre a janela
janela.tracer(0)                            # Ativa a animação do jogo
janela.title('SPACE SPEED 1.0')             # Título do jogo
janela.setup(1200, 750)                     # Resolução (tamanho) da janela
janela.bgcolor('black')                     # Cor do plano de fundo

# ADICIONANDO IMAGENS AO CÓDIGO:
janela.addshape('background05_2.gif')       # Plano de fundo
janela.addshape('personagem_red.gif')       # Personagem
janela.addshape('inimigo01_red.gif')        # Inimigo 1
janela.addshape('inimigo02_red.gif')        # Inimigo 2
janela.addshape('inimigo03_red.gif')        # Inimigo 3
janela.addshape('combustivel01_redm.gif')   # Combustível
janela.addshape('explosao01_red1.gif')      # Explosão

# SESSÃO DE VARIÁVEIS DE VELOCIDADE INICIAL:
spaceVeloc = 0
personagemVeloc = 0
inimigoVeloc = 0
combustivelVeloc = 0
FPS = 60                # Variável global do frame por segundo

# DETERMINANDO ARENA, SPACE, PERSONAGEM, INIMIGOS, PONTOS, VELOCIDADE E COMBUSTÍVEL:
arena = turtle.Turtle()     # Cria um turtle da variável
arena.penup()               # Não risca o trajeto
arena.speed(0)              # Velocidade do turtle
arena.color('white')        # Cor do turtle
arena.pensize(width=4)      # Tamanho do turtle
arena.goto(-300, -400)      # O turtle vai para a coordenada determinada
arena.pendown()             # Risca o trajeto
arena.hideturtle()          # Esconde o turtle no final

space = turtle.Turtle()
space.penup()
space.speed(0)
space.shape('background05_2.gif')   # Adiciona a imagem no turtle

space2 = turtle.Turtle()
space2.penup()
space2.speed(0)
space2.shape('background05_2.gif')

personagem = turtle.Turtle()
personagem.penup()
personagem.speed(0)
personagem.shape('personagem_red.gif')
personagem.goto(0, -250)

inimigo1 = turtle.Turtle()
inimigo1.penup()
inimigo1.speed(0)
inimigo1.shape('inimigo01_red.gif')
inimigo1_x = random.randint(-250, 250)      # Variável para sortear uma coordenada X inicial
inimigo1_y = random.randint(760, 860)      # Variável para sortear uma coordenada Y inicial

inimigo2 = turtle.Turtle()
inimigo2.penup()
inimigo2.speed(0)
inimigo2.shape('inimigo02_red.gif')
inimigo2_x = random.randint(-250, 250)
inimigo2_y = random.randint(860, 960)

inimigo3 = turtle.Turtle()
inimigo3.penup()
inimigo3.speed(0)
inimigo3.shape('inimigo03_red.gif')
inimigo3_x = random.randint(-250, 250)
inimigo3_y = random.randint(960, 1060)

combustivel = turtle.Turtle()
combustivel.penup()
combustivel.speed(0)
combustivel.shape('combustivel01_redm.gif')
combustivel_x = random.randint(-250, 250)
combustivel_y = random.randint(800, 1200)

# DETERMINANDO OS NOMES NA JANELA:
nome_corrida = turtle.Turtle()
nome_corrida.penup()
nome_corrida.speed(0)
nome_corrida.color('white')
nome_corrida.goto(-575, -10)
nome_corrida.write('SPACE SPEED \n        1.0', font=('Arial Black', 25, 'bold'))   # Escreve o nome determinado com fonte, tamanho e estilo
nome_corrida.color('white')
nome_corrida.goto(-555, -50)
nome_corrida.write('Ao infinito e além!', font=('Arial Black', 15, 'bold'))
nome_corrida.hideturtle()

nome_iniciar = turtle.Turtle()
nome_iniciar.penup()
nome_iniciar.speed(0)
nome_iniciar.color('red')
nome_iniciar.goto(-190, 0)
nome_iniciar.write('Aperte a tecla ESPAÇO para Iniciar!', font=('Arial Black', 15, 'bold'))
nome_iniciar.hideturtle()

nome_fim = turtle.Turtle()
nome_fim.penup()
nome_fim.speed(0)
nome_fim.color('red')
nome_fim.goto(-130, 0)
nome_fim.hideturtle()

nome_pontos = turtle.Turtle()
nome_pontos.penup()
nome_pontos.speed(0)
nome_pontos.color('white')
nome_pontos.goto(340, 300)
nome_pontos.write('PONTUAÇÃO', font=('Arial Black', 15, 'bold'))
nome_pontos.hideturtle()

nome_velocidade = turtle.Turtle()
nome_velocidade.penup()
nome_velocidade.speed(0)
nome_velocidade.color('white')
nome_velocidade.goto(340, 130)
nome_velocidade.write('VELOCIDADE', font=('Arial Black', 15, 'bold'))
nome_velocidade.hideturtle()

nome_combustivel = turtle.Turtle()
nome_combustivel.penup()
nome_combustivel.speed(0)
nome_combustivel.color('red')
nome_combustivel.goto(340, -50)
nome_combustivel.write('COMBUSTÍVEL', font=('Arial Black', 15, 'bold'))
nome_combustivel.hideturtle()

# DETERMINANDO OS VALORES DE PONTOS, VELOCIDADE E COMBUSTÍVEL NA JANELA:
pontos = turtle.Turtle()
pontos_valor = 0
pontos.penup()
pontos.hideturtle()
pontos.speed(0)
pontos.color('white')
pontos.goto(340, 260)
pontos.write(f'{pontos_valor}', font=('Arial Black', 15, 'bold'))

velocidade = turtle.Turtle()
velocidade.penup()
velocidade.hideturtle()
velocidade.speed(0)
velocidade.color('white')
velocidade.goto(340, 90)
velocidade.write('1000 Km/h', font=('Arial Black', 15, 'bold'))

combustivel_valor = turtle.Turtle()
combustivel_valorInicio = 1000
combustivel_valor.penup()
combustivel_valor.hideturtle()
combustivel_valor.speed(0)
combustivel_valor.color('red')
combustivel_valor.goto(340, -90)
combustivel_valor.write(f'{combustivel_valorInicio} litros', font=('Arial Black', 15, 'bold'))

# FUNÇÕES EM GERAL:
def distancia(x1, x2, y1, y2):                      # Função geral para cálculo da distância
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # Fórmula da distância
    return d                                        # Devolve o resultado do cálculo
def colisao():
    # FUNÇÃO GLOBAL QUE PEGA VARIÁVEIS QUE ATENDEM O CÓDIGO INTEIRO:
    global inimigo1_x, inimigo1_y, inimigo2_x, inimigo2_y, inimigo3_x, inimigo3_y
    global spaceVeloc, personagemVeloc, inimigoVeloc, combustivelVeloc, combustivel_valorInicio
    # VARIÁVEIS DE VELODIDADE SÃO ZERADAS AO COLIDIR:
    janela.tracer(1)
    personagem.shape('explosao01_red1.gif')
    spaceVeloc = 0
    personagemVeloc = 0
    inimigoVeloc = 0
    combustivelVeloc = 0
    # VARIÁVEIS DAS COORDENADAS SÃO SORTEADAS NOVAMENTE AO COLIDIR:
    inimigo1_x = random.randint(-250, 250)
    inimigo1_y = random.randint(760, 860)
    inimigo2_x = random.randint(-250, 250)
    inimigo2_y = random.randint(860, 960)
    inimigo3_x = random.randint(-250, 250)
    inimigo3_y = random.randint(960, 1060)
    combustivel_x = random.randint(-250, 250)
    combustivel_y = random.randint(800, 1200)
    time.sleep(1)
    personagem.shape('personagem_red.gif')
    janela.tracer(0)
    # COMANDOS PARA REDIRECIONAR AS COORDENADAS INICIAIS DOS TURTLES AO COLIDIR:
    personagem.setx(0)                        # Personagem volta à coordenada X inicial
    space.goto(0, 0)                          # Plano de fundo volta para a coordenada inicial
    space2.goto(0, 830)                       # Plano de fundo 2 volta para a coordenada inicial
    inimigo1.goto(inimigo1_x, inimigo1_y)     # Sorteia novas coordenadas aleatórias
    inimigo2.goto(inimigo2_x, inimigo2_y)
    inimigo3.goto(inimigo3_x, inimigo3_y)
    combustivel.goto(combustivel_x, combustivel_y)
    # COMANDOS PARA ADICIONAR INFORMAÇÕES NOVAS AO JOGO QUANDO COLIDIR:
    combustivel_valorInicio -= 50       # Diminui o valor do combustível ao colidir
    combustivel_valor.clear()           # Limpa o valor anterior do combustível
    combustivel_valor.write(f'{combustivel_valorInicio} litros', font=('Arial Black', 15, 'bold'))    # Escreve o novo valor do combustível
    nome_iniciar.goto(-210, 0)          # Redireciona o turtle referido
    nome_iniciar.write('Aperte a tecla ESPAÇO para Continuar!', font=('Arial Black', 15, 'bold'))     # Escreve um novo nome para o turtle
def desenhoDaArena():
    for i in range(2):          # Laço 'for' para fechar o desenho da Arena
        arena.forward(600)      # Anda para frente 600px
        arena.left(90)          # Gira para a 90º para a esquerda
        arena.forward(810)      # Anda para frente 810px
        arena.left(90)          # Gira para a 90º para a esquerda
desenhoDaArena()                # Ativa a função no código
def personagem_p_direita():
    if personagem.xcor() < 220:                 # Condição para limitar as laterais da pista à direita
        personagem.forward(personagemVeloc)     # Personagem mantém a velocidade
    else:                                       # Condição para o personagem voltar à posição inicial
        colisao()                               # Retorna à coordenada x inicial
def personagem_p_esquerda():
    if personagem.xcor() > -220:                # Condição para limitar as laterais da pista à esquerda
        personagem.backward(personagemVeloc)    # Personagem mantém a velocidade
    else:                                       # Condição para o personagem voltar à posição inicial
        colisao()                               # Retorna à coordenada x inicia
def iniciarJogo():          # Função para início ou reinício do jogo
    global spaceVeloc, personagemVeloc, inimigoVeloc, combustivelVeloc
    global nome_iniciar, nome_fim, combustivel_valorInicio, pontos_valor
    # FUNÇÕES QUE LIMPAM SEUS DETERMINADOS TURTLES AO APERTAR 'ESPAÇO':
    nome_fim.clear()        # O nome GAME OVER é apagado ao reiniciar o jogo
    nome_iniciar.clear()    # A frase no início do jogo é apagada ao reiniciar o jogo
    # VARIÁVEIS DE VELODIDADE INICIAL AO APERTAR 'ESPAÇO':
    spaceVeloc = 50
    personagemVeloc = 50
    inimigoVeloc = 15
    combustivelVeloc = 8
    # VARIÁVEIS DAS COORDENADAS SÃO SORTEADAS NOVAMENTE AO APERTAR 'ESPAÇO':
    inimigo1_x = random.randint(-250, 250)
    inimigo1_y = random.randint(760, 860)
    inimigo2_x = random.randint(-250, 250)
    inimigo2_y = random.randint(860, 960)
    inimigo3_x = random.randint(-250, 250)
    inimigo3_y = random.randint(960, 1060)
    combustivel_x = random.randint(-250, 250)
    combustivel_y = random.randint(800, 1200)
    # COMANDOS PARA REDIRECIONAR ÀS COORDENADAS INICIAIS DOS TURTLES AO APERTAR 'ESPAÇO':
    space.goto(0, 0)
    space2.goto(0, 830)
    inimigo1.goto(inimigo1_x, inimigo1_y)
    inimigo2.goto(inimigo2_x, inimigo2_y)
    inimigo3.goto(inimigo3_x, inimigo3_y)
    combustivel.goto(combustivel_x, combustivel_y)
    # CONDIÇÃO PARA QUE, QUANDO O COMBUSTÍVEL ACABAR, O JOGO ZERE E REINICIE DO ZERO:
    if combustivel_valorInicio <= 0:
        combustivel_valorInicio = 1000    # O valor do Combustível volta ao valor inicial
        pontos_valor = 0                  # A pontuação volta a zerar

# REDIRECIONA AO INÍCIO DA TELA E GIRA90 GRAUS:
space.goto(0, 0)
space2.goto(0, 830)
inimigo1.goto(inimigo1_x, inimigo1_y)
inimigo2.goto(inimigo2_x, inimigo2_y)
inimigo3.goto(inimigo3_x, inimigo3_y)
combustivel.goto(combustivel_x, combustivel_y)
space.right(90)
space2.right(90)
inimigo1.right(90)
inimigo2.right(90)
inimigo3.right(90)
combustivel.right(90)

# FUNÇÃO PRINCIPAL: Faz o jogo rodar
def Principal():
    global space, space2, inimigo1, inimigo2, combustivel, nome_fim, spaceVeloc, personagemVeloc, inimigoVeloc, combustivelVeloc
    global pontos_valor, combustivel_valor, combustivel_valorInicio
    # TURTLES VÃO DESCER ATÉ DETERMINADO PONTO E VOLTAR AO INÍCIO:
    if space.ycor() > -740:             # Condição para que o plano de fundo desça até determinado ponto
        space.forward(spaceVeloc)       # Mantém a velocidade do turtle até o ponto estipulado
    else:
        space.setx(0)                   # O plano de fundo retorna ao ponto X inicial determinado
        space.sety(740)                 # O plano de fundo retorna ao ponto Y inicial determinado
        pontos_valor += 175             # Os pontos vão aumentando conforme o plano de fundo se repete
        pontos.clear()                  # Os pontos são apagados para ser colocados os novos por cima
        pontos.write(f'{pontos_valor}', font=('Arial Black', 15, 'bold'))   # Imprime a pontuação na janela
    if space2.ycor() > -740:
        space2.forward(spaceVeloc)
    else:
        space2.setx(0)
        space2.sety(750)
        combustivel_valorInicio -= 10
        combustivel_valor.clear()
        combustivel_valor.write(f'{combustivel_valorInicio} litros', font=('Arial Black', 15, 'bold'))
    if inimigo1.ycor() > -450:
        inimigo1.forward(inimigoVeloc)              # Mantém a velocidade até o ponto estipulado
    else:
        inimigo1.setx(random.randint(-250, 250))    # Retorna ao ponto X inicial e aleatório
        inimigo1.sety(760)                          # Retorna ao ponto Y determinado
    if inimigo2.ycor() > -450:
        inimigo2.forward(inimigoVeloc)
    else:
        inimigo2.setx(random.randint(-250, 250))
        inimigo2.sety(860)
    if inimigo3.ycor() > -450:
        inimigo3.forward(inimigoVeloc)
    else:
        inimigo3.setx(random.randint(-250, 250))
        inimigo3.sety(960)
    if combustivel.ycor() > -450:
        combustivel.forward(combustivelVeloc)
    else:
        combustivel.setx(random.randint(-250, 250))
        combustivel.sety(800)
    # SESSÃO PARA CÁLCULO DAS DISTÂNCIAS:
    distPI1 = distancia(personagem.xcor(), inimigo1.xcor(), personagem.ycor(), inimigo1.ycor())         # Personagem x Inimigo 1
    distPI2 = distancia(personagem.xcor(), inimigo2.xcor(), personagem.ycor(), inimigo2.ycor())         # Personagem x Inimigo 2
    distPI3 = distancia(personagem.xcor(), inimigo3.xcor(), personagem.ycor(), inimigo3.ycor())         # Personagem x Inimigo 3
    distPCom = distancia(personagem.xcor(), combustivel.xcor(), personagem.ycor(), combustivel.ycor())  # Personagem x Combutível
    distI1I2 = distancia(inimigo1.xcor(), inimigo2.xcor(), inimigo1.ycor(), inimigo2.ycor())            # Inimigo 1 x Inimigo 2
    distI1I3 = distancia(inimigo1.xcor(), inimigo3.xcor(), inimigo1.ycor(), inimigo3.ycor())            # Inimigo 1 x Inimigo 3
    distI2I3 = distancia(inimigo2.xcor(), inimigo3.xcor(), inimigo2.ycor(), inimigo3.ycor())            # Inimigo 2 x Inimigo 3
    # SESSÃO DE CONDIÇÕES PARA COLISÕES ENTRE PERSONAGEM, INIMIGOS E COMBUSTÍVEL:
    if distI1I2 <= 150:                                 # CONDIÇÃO COLISÃO INIMIGO 1 X INIMIGO 2
        inimigo1.setx(random.randint(-250, 250))        # Imagem do Inimigo sobe e sorteia uma nova coordenada X
        inimigo1.sety(random.randint(760, 860))         # Imagem do Inimigo sobe e sorteia uma nova coordenada Y
    if distI1I3 <= 150:                                 # CONDIÇÃO COLISÃO INIMIGO 1 X INIMIGO 3
        inimigo3.setx(random.randint(-250, 250))
        inimigo3.sety(random.randint(860, 960))
    if distI2I3 <= 150:                                 # CONDIÇÃO COLISÃO INIMIGO 2 X INIMIGO 3
        inimigo2.setx(random.randint(-250, 250))
        inimigo2.sety(random.randint(960, 1060))
    if distPCom <= 70:                                  # CONDIÇÃO COLISÃO PERSONAGEM X COMBUSTÍVEL
        combustivel.clear()                             # Imagem do Combustível desaparece
        combustivel_valor.write(f'{combustivel_valorInicio} litros', font=('Arial Black', 15, 'bold'))    # Valor do Combutível aumenta
        combustivel_valorInicio += 50                   # Quantidade que o combustível aumenta os litros
        combustivel.setx(random.randint(-250, 250))
        combustivel.sety(random.randint(800, 1200))
    if distPI1 <= 80:                                   # CONDIÇÃO COLISÃO PERSONAGEM X INIMIGO 1
        combustivel_valorInicio -= 100                  # Combustível diminui os litros
        combustivel_valor.clear()                       # Valor do combustível apaga
        combustivel_valor.write(f'{combustivel_valorInicio} litros', font=('Arial Black', 15, 'bold'))    # Valor do Combutível diminui
        inimigo1.goto(random.randint(-250, 250), 760)   # Inimigo é sorteado novamente
        colisao()                                       # Função colisão para o jogo parar temporariamente e voltar
    if distPI2 <= 73:                                   # CONDIÇÃO COLISÃO PERSONAGEM X INIMIGO 2
        combustivel_valorInicio -= 100
        combustivel_valor.clear()
        combustivel_valor.write(f'{combustivel_valorInicio} litros', font=('Arial Black', 15, 'bold'))
        inimigo2.goto(random.randint(-250, 250), 860)
        colisao()
    if distPI3 <= 71:                                   # CONDIÇÃO COLISÃO PERSONAGEM X INIMIGO 3
        combustivel_valorInicio -= 100
        combustivel_valor.clear()
        combustivel_valor.write(f'{combustivel_valorInicio} litros', font=('Arial Black', 15, 'bold'))
        inimigo3.goto(random.randint(-250, 250), 960)
        colisao()
    # SESSÃO PARA GAME OVER ATRAVÉS DO COMBUSÍVEL:
    if combustivel_valorInicio <= 0:
        nome_fim.write('GAME OVER', font=('Arial Black', 30, 'bold'))   # GAME OVER aparece na janela
        nome_iniciar.clear()                # A frase inicial não vai aparece no final
        spaceVeloc = 0                      # As velocidades vão zerar
        personagemVeloc = 0
        inimigoVeloc = 0
        combustivelVeloc = 0
    janela.update()                         # Atualiza os dados dos comandos da janela
    janela.ontimer(Principal, 1000//FPS)    # Executa a função determinadas quantidades por segundo
Principal()

# SESSÃO DE COMANDOS DO PERSONAGEM NAS TECLAS:
janela.onkeypress(personagem_p_direita, 'Right')    # Comando para precionar Botão 'Right' e ir para a Direita
janela.onkeypress(personagem_p_esquerda, 'Left')    # Comando para precionar Botão 'Left' e ir para a Esquerda
janela.onkey(iniciarJogo, 'space')                  # Comando para apertar botão 'space' e iniciar o jogo
janela.listen()                                     # Permite que os comandos funcionem

# SESSÃO DE MANUTENÇÃO DA TELA ABERTA:
janela.mainloop()