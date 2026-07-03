import tkinter as tk
import random
from datetime import datetime

# ==========================
# CONFIGURAÇÕES
# ==========================

MATERIAS = [
    "Fundamentos de Redes de Computadores",
    "Segurança da Informação",
    "Computação em Nuvem",
    "Programação",
    "Matemática e Lógica"
]

HORARIO_ESTUDO = "20:00"

# ==========================
# FUNÇÕES
# ==========================

def sugestao_materia():
    return random.choice(MATERIAS)


def responder(msg):
    msg = msg.lower()

    if "oi" in msg:
        return "Olá! Pronto para estudar?"

    elif "estudar" in msg:
        return f"Vamos lá! Hoje recomendo estudar:\n{sugestao_materia()}"

    elif "qual matéria" in msg or "qual materia" in msg:
        return f"Minha sugestão é:\n{sugestao_materia()}"

    elif "hora" in msg:
        return "Agora são " + datetime.now().strftime("%H:%M")

    elif "tchau" in msg:
        return "Até mais! Bons estudos!"

    return "Não entendi. Posso ajudar nos seus estudos."


def adicionar_msg(remetente, texto):
    chat.config(state="normal")
    chat.insert(tk.END, f"{remetente}: {texto}\n\n")
    chat.config(state="disabled")
    chat.see(tk.END)


def enviar():
    mensagem = entrada.get().strip()

    if not mensagem:
        return

    entrada.delete(0, tk.END)

    adicionar_msg("Você", mensagem)

    resposta = responder(mensagem)

    adicionar_msg("Bot", resposta)


def checar_horario():
    if datetime.now().strftime("%H:%M") == HORARIO_ESTUDO:
        adicionar_msg(
            "Bot",
            f"⏰ Hora de estudar!\nHoje: {sugestao_materia()}"
        )

    janela.after(60000, checar_horario)


# ==========================
# JANELA
# ==========================

janela = tk.Tk()
janela.title("Chat Estudo")
janela.geometry("450x550")
janela.resizable(False, False)

# Área do chat
chat = tk.Text(
    janela,
    state="disabled",
    wrap="word",
    font=("Arial", 11)
)

chat.pack(fill="both", expand=True, padx=10, pady=10)

# Campo de texto
entrada = tk.Entry(
    janela,
    font=("Arial", 11)
)

entrada.pack(fill="x", padx=10)

# Botão
botao = tk.Button(
    janela,
    text="Enviar",
    command=enviar
)

botao.pack(pady=10)

# Enter envia mensagem
entrada.bind("<Return>", lambda event: enviar())

# Mensagem inicial
adicionar_msg(
    "Bot",
    "Olá! 😊 Posso ajudar nos seus estudos."
)

# Inicia verificação do horário
checar_horario()

# Executa aplicação
janela.mainloop()