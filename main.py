import os
import time
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# 2. Busca a variável (usando o nome exato que está no .env)
api_key = os.getenv("GOOGLE_API_KEY")

# Use a sua chave aqui (Recomendo colocar em variável de ambiente no .bashrc depois)
MODEL = ChatGoogleGenerativeAI(model="gemma-3-27b-it", api_key=api_key)

LOG_PATH = os.path.expanduser("~/.var/app/com.valvesoftware.Steam/.config/StardewValley/ErrorLogs/SMAPI-latest.txt")
TMUX_SESSION = "ia_stardew"

def enviar_fala(npc, msg):
    """Trata a string para evitar quebras no parser do jogo e do shell."""
    # 1. Remove aspas duplas para não conflitar com o comando tmux/debug
    msg_limpa = msg.replace('"', "'").replace("\n", " ")
    
    # 2. Limita o tamanho (o motor do jogo tem limites de buffer para o console)
    if len(msg_limpa) > 400:
        msg_limpa = msg_limpa[:397] + "..."

    comando = f"tmux send-keys -t {TMUX_SESSION} 'debug speech {npc} 0 \"{msg_limpa}\" $h' ENTER"
    os.system(comando)

def monitorar():
    print(f"🚀 [SISTEMA ONLINE] IA Abigail pronta no Ubuntu.")
    
    with open(LOG_PATH, "r", errors="ignore") as f:
        f.seek(0, os.SEEK_END)
        while True:
            linha = f.readline()
            if not linha:
                time.sleep(0.1)
                continue
            
            if "> chat command:" in linha:
                try:
                    pergunta = linha.split("chat command:")[1].strip()
                    print(f"📩 Processando: {pergunta}")
                    
                    # RIGOR: Acessamos apenas o .content da resposta
                    resposta_ai = MODEL.invoke(
                        f"Você é a Abigail do jogo Stardew Valley. "
                        f"Responda de forma curta (máximo 2 frases) à mensagem: {pergunta}"
                        f"RESPONDA COM BASE NO JOGO STARDEW VALLEY, APENAS."
                    )
                    
                    enviar_fala("Abi", resposta_ai.content)
                    
                except Exception as e:
                    print(f"⚠️ Erro: {e}")

if __name__ == "__main__":
    monitorar()