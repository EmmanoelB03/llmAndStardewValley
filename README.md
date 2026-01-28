# IA Abigail - Stardew Valley

Integração de IA generativa com Stardew Valley, permitindo que a personagem Abigail responda dinamicamente usando o modelo Gemma-3-27b via Google Generative AI.

## 📋 Descrição

Este projeto monitora os logs do SMAPI (Stardew Valley Mod API) em tempo real e utiliza IA generativa para gerar respostas contextualizadas para a personagem Abigail. As respostas são enviadas diretamente ao jogo através de comandos tmux usando o comando `debug speech`.

## 🔧 Requisitos

* Python 3.8+
* Stardew Valley com SMAPI instalado
* Steam via Flatpak (Ubuntu/Linux)
* Tmux instalado
* Chave de API do Google Generative AI
* Dependências Python:
  + `langchain-google-genai`
  + `python-dotenv`

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

Edite o arquivo `.env` com sua chave de API:

```
GOOGLE_API_KEY=sua-chave-aqui
```

## 🚀 Como Usar

1. Inicie o Stardew Valley com SMAPI em uma sessão tmux chamada `ia_stardew`:

```bash
tmux new-session -s ia_stardew
# Dentro da sessão tmux, inicie o jogo normalmente pelo Steam
```

2. Em outro terminal, inicie o script de monitoramento:

```bash
python main.py
```

3. No jogo, abra o console de chat pressionando a tecla **T** e digite suas mensagens. A IA Abigail responderá automaticamente!

## 📁 Estrutura do Projeto

```
llmAndStardewValley/
├── main.py           # Script principal de monitoramento
├── .example.env      # Exemplo de variáveis de ambiente
├── .env              # Variáveis de ambiente (não versionar)
└── documentos/       # Documentação adicional
```

## 🔑 Configuração do Código

O script utiliza as seguintes configurações (definidas em `main.py`):

| Variável | Valor Padrão | Descrição |
| --- | --- | --- |
| `GOOGLE_API_KEY` | (do .env) | Chave de API do Google Generative AI |
| `MODEL` | `gemma-3-27b-it` | Modelo de IA utilizado |
| `LOG_PATH` | `~/.var/app/com.valvesoftware.Steam/.config/StardewValley/ErrorLogs/SMAPI-latest.txt` | Caminho do log do SMAPI (Steam Flatpak) |
| `TMUX_SESSION` | `ia_stardew` | Nome da sessão tmux |
| `NPC_NAME` | `Abi` | Nome usado no comando debug speech |

**Nota:** O caminho do log é específico para Steam instalado via Flatpak no Linux. Se você usa Steam nativo, o caminho geralmente é `~/.config/StardewValley/ErrorLogs/SMAPI-latest.txt`.

## 🎮 Funcionalidades

* **Monitoramento em Tempo Real**: Acompanha logs do SMAPI continuamente
* **Respostas Contextualizadas**: IA gera respostas baseadas no personagem Abigail e no contexto de Stardew Valley
* **Limpeza de Strings**: Remove caracteres problemáticos (aspas duplas, quebras de linha)
* **Limite de Tamanho**: Mensagens com mais de 400 caracteres são truncadas automaticamente
* **Integração com Tmux**: Envia comandos `debug speech` ao jogo através da sessão tmux

## ⚙️ Como Funciona

1. O script monitora o arquivo de log do SMAPI
2. Quando detecta uma mensagem iniciada com `> chat command:`, extrai o texto
3. Envia a mensagem para o modelo Gemma-3-27b com o prompt contextualizado
4. Recebe a resposta da IA (limitada a 2 frases)
5. Limpa e formata a resposta (remove aspas duplas, quebras de linha, limita a 400 caracteres)
6. Envia o comando `debug speech Abi 0 "mensagem"` via tmux para o jogo

## ⚠️ Observações Importantes

* As respostas da IA são limitadas a **2 frases** para manter imersão e performance
* Mensagens com mais de **400 caracteres** são automaticamente truncadas com "..."
* **Aspas duplas** são convertidas em aspas simples para evitar conflitos de parsing
* **Quebras de linha** são removidas das mensagens
* O script usa `Abi` como nome do NPC no comando debug speech (forma curta de Abigail)
* Requer Steam via Flatpak - o caminho do log é específico para essa instalação

## 🐛 Troubleshooting

**Problema:** `FileNotFoundError` - Log do SMAPI não encontrado

**Solução:** Verifique se o SMAPI está instalado e se você já executou o jogo pelo menos uma vez. Se usa Steam nativo ao invés de Flatpak, altere o `LOG_PATH` no código.

---

**Problema:** Sessão tmux não encontrada

**Solução:** Certifique-se de criar a sessão tmux com o nome exato `ia_stardew` antes de iniciar o script.

---

**Problema:** IA não responde no jogo

**Solução:** Verifique se:
1. A sessão tmux está ativa e rodando o jogo
2. O console de chat do SMAPI está habilitado (geralmente pressionando `~` ou ` `` `)
3. Você está usando o chat do jogo (tecla T) e não o console do SMAPI

## 📝 Exemplo de Uso

```
[No jogo, pressione T e digite:]
> Oi Abigail, como você está?

[A IA responde:]
Abigail: Oi! Estou bem, obrigada por perguntar. Estava pensando em explorar as minas mais tarde.
```

## 📄 Licença

Projeto criado para fins educacionais.

## 🤝 Contribuindo

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias!

## 👨‍💻 Autor

[EmmanoelB03](https://github.com/EmmanoelB03)
