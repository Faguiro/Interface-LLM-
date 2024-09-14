# LLM Interface 🤖

Este repositório contém uma aplicação de interface gráfica construída com **Tkinter** que permite a interação com um modelo de linguagem (LLM). O usuário pode inserir um texto e receber uma resposta processada pelo modelo, com funcionalidades adicionais como a visualização de uma animação enquanto a solicitação é processada e a possibilidade de salvar a resposta em um arquivo de texto.

## Funcionalidades

- **Entrada de Texto:** Insira um texto para ser processado pelo modelo LLM.
- **GIF Animado:** Uma animação é exibida enquanto o modelo processa a resposta.
- **Resposta e Tempo de Execução:** O resultado do modelo é exibido junto com o tempo total de processamento.
- **Salvar Resposta:** O usuário pode salvar a resposta gerada em um arquivo `.txt`.

## Requisitos

- Python 3.x
- Tkinter (instalado por padrão com Python)
- Biblioteca externa para o modelo LLM (`llm`)
- Biblioteca para controle do GIF (`GIFPlayer`)

### Instalação

1. Clone o repositório:

   ```git clone https://github.com/Faguiro/ollama_tkinter.git```
   
   ```cd ollama_tkinter```

2. Instale as dependências do projeto:

```pip install llm```


3. Execute a aplicação:

```python main.py```

## Estrutura do Projeto

├── main.py                # Código principal da aplicação
├── gif_player.py          # Gerenciador de GIF animado
├── robot.gif              # Arquivo GIF utilizado na interface
└── README.md              # Documentação do projeto


## Uso
Abra a interface e insira o texto no campo de entrada.
Clique no botão Enviar 🚀 para iniciar o processamento.
A resposta será exibida na área de texto após o processamento.
Para salvar a resposta, clique no botão Salvar Resposta 💾.
Exemplo
Após inserir o texto, a interface irá exibir uma resposta do modelo LLM em português brasileiro e mostrará o tempo de execução.


## Melhorias Futuras
- Melhorar o suporte a múltiplos modelos de linguagem.
- Adicionar suporte para diferentes idiomas na resposta do LLM.
- Implementar suporte a mais formatos de exportação (JSON, CSV).
