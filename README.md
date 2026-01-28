# IA Abigail - Stardew Valley

Integração de IA generativa com Stardew Valley, permitindo que a personagem Abigail responda dinamicamente usando o modelo Gemma-3-27b via Google Generative AI.

## 📋 Descrição

Este projeto monitora os logs do SMAPI (Stardew Valley Mod API) em tempo real e utiliza IA generativa para gerar respostas contextualizadas para a personagem Abigail. As respostas são enviadas diretamente ao jogo através de comandos tmux.

## 🔧 Requisitos

- Python 3.8+
- Stardew Valley com SMAPI instalado
- Tmux instalado
- Chave de API do Google Generative AI
- Dependências Python:
  - `langchain-google-genai`
  - `python-dotenv`

## ⚙️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/EmmanoelB03/llmAndStardewValley
cd llmAndStardewValley
```

2. Instale as dependências:
```bash
pip install langchain-google-genai python-dotenv
```

3. Configure a variável de ambiente:

Copie o arquivo `.example.env` para `.env`:
```bash
cp .example.env .env
```

Edit o arquivo `.env` com sua chave de API:
```
GOOGLE_API_KEY=sua-chave-aqui
```

## 🚀 Como Usar

1. Abra Stardew Valley com SMAPI em uma sessão tmux chamada `ia_stardew`:
```bash
tmux new-session -d -s ia_stardew
```

2. Inicie o script:
```bash
python main.py
```

3. Digite comandos de chat no jogo usando:
```
Apete a teclar T
```

## 📁 Estrutura do Projeto

```
llmAndStardewValley/
├── main.py           # Script principal
├── .example.env      # Exemplo de variáveis de ambiente
├── .env             # Variáveis de ambiente (não versionar)
└── documentos/      # Documentação adicional
```

## 🔑 Variáveis de Configuração

| Variável | Descrição |
|----------|-----------|
| `GOOGLE_API_KEY` | Chave de API do Google Generative AI |
| `MODEL` | Modelo IA utilizado (padrão: gemma-3-27b-it) |
| `LOG_PATH` | Caminho para o log do SMAPI |
| `TMUX_SESSION` | Nome da sessão tmux (padrão: ia_stardew) |

## 🎮 Funcionalidades

- **Monitoramento em Tempo Real**: Acompanha logs do SMAPI continuamente
- **Respostas Contextualizadas**: IA gera respostas baseadas no personagem Abigail e Stardew Valley
- **Limpeza de Strings**: Remove caracteres problemáticos e limita tamanho das mensagens
- **Integração com Tmux**: Envia comandos automaticamente ao jogo

## ⚠️ Observações

- As respostas são limitadas a 2 frases para manter imersão e performance
- Mensagens com mais de 400 caracteres são truncadas
- Aspas duplas são convertidas em simples para evitar conflitos de parsing
- Quebras de linha são removidas das mensagens

## 📝 Licença

Projeto criado para fins educacionais.
