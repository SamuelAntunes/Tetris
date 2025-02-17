# Tetris Clone - Pygame

Este é um clone do jogo Tetris implementado em Python utilizando a biblioteca Pygame. O jogo apresenta uma interface simples e a mecânica clássica do Tetris: peças que caem, podem ser movidas e giradas, e linhas completas são removidas para aumentar a pontuação.

---

## Funcionalidades

- **Mecânica Clássica do Tetris:**  
  Peças caem automaticamente e podem ser movidas lateralmente e giradas.

- **Detecção de Colisão:**  
  Validação dos movimentos para evitar que as peças ultrapassem os limites da área de jogo ou se sobreponham.

- **Remoção de Linhas:**  
  Linhas completas são eliminadas, e a pontuação é atualizada de acordo com as linhas removidas.

- **Reinício do Jogo:**  
  Após o fim do jogo, pressione `R` para reiniciar.

- **Interface Simples:**  
  Visualização gráfica gerenciada pelo Pygame, com uma grade que representa o campo de jogo.

---

## Requisitos

- **Python 3.x**
- **Pygame**

Para instalar o Pygame, utilize o comando:

```bash
pip install pygame
```

---

## Como Executar o Projeto

1. **Verifique a Instalação do Python:**
   - Certifique-se de que o Python 3 está instalado no seu sistema. Para verificar, execute no terminal:
     ```bash
     python --version
     ```
     ou
     ```bash
     python3 --version
     ```

2. **Configure um Ambiente Virtual (Opcional):**
   - Crie um ambiente virtual para isolar as dependências do projeto:
     ```bash
     python -m venv venv
     ```
   - Ative o ambiente virtual:
     - No Windows:
       ```bash
       venv\Scripts\activate
       ```
     - No macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

3. **Instale as Dependências:**
   - Instale o Pygame usando o `pip`:
     ```bash
     pip install pygame
     ```

4. **Baixe o Projeto:**
   - Se você ainda não clonou o repositório, faça-o usando:
     ```bash
     git clone https://github.com/seu-usuario/tetris-clone.git
     ```
   - Caso o projeto já esteja em seu computador, navegue até a pasta do projeto:
     ```bash
     cd tetris-clone
     ```

5. **Execute o Jogo:**
   - Inicie o jogo executando o script principal:
     ```bash
     python nome_do_arquivo.py
     ```
     *Substitua `nome_do_arquivo.py` pelo nome real do arquivo que contém o código do jogo.*

6. **Controles do Jogo:**
   - **Seta para a Esquerda:** Move a peça para a esquerda.
   - **Seta para a Direita:** Move a peça para a direita.
   - **Seta para Baixo:** Acelera a queda da peça.
   - **Seta para Cima:** Gira a peça.
   - **R:** Reinicia o jogo após o game over.

7. **Observações:**
   - Certifique-se de que sua janela do terminal ou IDE está configurada para permitir a execução de janelas gráficas, pois o Pygame abre uma nova janela para o jogo.
   - Se estiver usando um ambiente virtual, lembre-se de ativá-lo sempre que for executar o jogo.

---

## Estrutura do Código

- **Configurações do Jogo:**  
  Define dimensões da tela, tamanho dos blocos, velocidade de queda, cores e peças do Tetris.

- **Classe `Peca`:**  
  Responsável pela criação, posicionamento e rotação das peças.

- **Funções de Suporte:**
  - `criar_grade`: Cria e inicializa a grade do jogo.
  - `desenhar_grade`: Renderiza a grade e os blocos na tela.
  - `validar_movimento`: Verifica se o movimento da peça é válido.
  - `fixar_peca`: Insere a peça fixa na grade após seu posicionamento.
  - `remover_linhas`: Elimina as linhas completas e atualiza a pontuação.
  - `exibir_texto`: Exibe mensagens na tela (como "START" ou "GAME OVER").
  - `tela_inicial` e `tela_gameover`: Gerenciam as telas de início e fim de jogo.

- **Função `main`:**  
  Contém o loop principal do jogo, gerenciando eventos, atualizações e renderizações.

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Divirta-se jogando e sinta-se livre para modificar e melhorar o jogo conforme suas preferências!
