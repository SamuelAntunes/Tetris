import pygame
import random

# Configurações do jogo
LARGURA, ALTURA = 300, 600
TAMANHO_BLOCO = 30
LARGURA_GRADE, ALTURA_GRADE = LARGURA // TAMANHO_BLOCO, ALTURA // TAMANHO_BLOCO
VELOCIDADE_QUEDA = 500  # Tempo de queda em milissegundos

# Cores
CORES = [
    (0, 255, 255), (0, 0, 255), (255, 165, 0),
    (255, 255, 0), (0, 255, 0), (128, 0, 128), (255, 0, 0)
]

# Peças do Tetris
PECAS = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]   # Z
]

pygame.font.init()
FONTE = pygame.font.SysFont("Arial", 24, bold=True)

class Peca:
    def __init__(self):
        self.forma = random.choice(PECAS)
        self.cor = random.choice(CORES)
        self.x = LARGURA_GRADE // 2 - len(self.forma[0]) // 2
        self.y = 0

    def girar(self):
        nova_forma = [list(row) for row in zip(*self.forma[::-1])]
        self.forma = nova_forma

def criar_grade():
    return [[(0, 0, 0) for _ in range(LARGURA_GRADE)] for _ in range(ALTURA_GRADE)]

def desenhar_grade(tela, grade):
    for y, linha in enumerate(grade):
        for x, cor in enumerate(linha):
            pygame.draw.rect(tela, cor, (x * TAMANHO_BLOCO, y * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO))
            pygame.draw.rect(tela, (50, 50, 50), (x * TAMANHO_BLOCO, y * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO), 1)

def validar_movimento(peca, grade, dx=0, dy=0):
    for y, linha in enumerate(peca.forma):
        for x, bloco in enumerate(linha):
            if bloco:
                nx, ny = peca.x + x + dx, peca.y + y + dy
                if nx < 0 or nx >= LARGURA_GRADE or ny >= ALTURA_GRADE or (ny >= 0 and grade[ny][nx] != (0, 0, 0)):
                    return False
    return True

def fixar_peca(peca, grade):
    for y, linha in enumerate(peca.forma):
        for x, bloco in enumerate(linha):
            if bloco:
                grade[peca.y + y][peca.x + x] = peca.cor

def remover_linhas(grade):
    novas_linhas = [linha for linha in grade if (0, 0, 0) in linha]
    linhas_removidas = ALTURA_GRADE - len(novas_linhas)
    return [[(0, 0, 0)] * LARGURA_GRADE] * linhas_removidas + novas_linhas, linhas_removidas

def exibir_texto(tela, texto, cor, y_offset=0):
    render = FONTE.render(texto, True, cor)
    x = (LARGURA - render.get_width()) // 2
    y = (ALTURA - render.get_height()) // 2 + y_offset
    tela.blit(render, (x, y))

def tela_inicial(tela):
    tela.fill((0, 0, 0))
    exibir_texto(tela, "START", (255, 255, 255), 0)
    pygame.display.flip()

def tela_gameover(tela, pontuacao):
    tela.fill((0, 0, 0))
    exibir_texto(tela, "GAME OVER", (255, 0, 0), -60)
    exibir_texto(tela, f"PONTUAÇÃO: {pontuacao}", (255, 255, 255), 0)
    exibir_texto(tela, "Pressione R para reiniciar", (255, 255, 255), 60)
    pygame.display.flip()

def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    clock = pygame.time.Clock()

    tela_inicial(tela)
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return
            elif evento.type == pygame.KEYDOWN:
                esperando = False

    grade = criar_grade()
    peca = Peca()
    pontuacao = 0
    ultima_queda = pygame.time.get_ticks()
    rodando = True

    while rodando:
        tela.fill((0, 0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and validar_movimento(peca, grade, dx=-1):
                    peca.x -= 1
                if evento.key == pygame.K_RIGHT and validar_movimento(peca, grade, dx=1):
                    peca.x += 1
                if evento.key == pygame.K_DOWN and validar_movimento(peca, grade, dy=1):
                    peca.y += 1
                if evento.key == pygame.K_UP:
                    peca.girar()
                    if not validar_movimento(peca, grade):
                        for _ in range(3):
                            peca.girar()

        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - ultima_queda > VELOCIDADE_QUEDA:
            if validar_movimento(peca, grade, dy=1):
                peca.y += 1
            else:
                fixar_peca(peca, grade)
                grade, linhas_removidas = remover_linhas(grade)
                pontuacao += linhas_removidas * 100
                peca = Peca()
                if not validar_movimento(peca, grade):
                    rodando = False
            ultima_queda = tempo_atual

        desenhar_grade(tela, grade)
        
        for y, linha in enumerate(peca.forma):
            for x, bloco in enumerate(linha):
                if bloco:
                    pygame.draw.rect(tela, peca.cor, ((peca.x + x) * TAMANHO_BLOCO, (peca.y + y) * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO))

        pontos_texto = FONTE.render(f"Pontos: {pontuacao}", True, (255, 255, 255))
        tela.blit(pontos_texto, (10, 10))

        pygame.display.flip()

    tela_gameover(tela, pontuacao)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                main()

    pygame.quit()

if __name__ == "__main__":
    main()
