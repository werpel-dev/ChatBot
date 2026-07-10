import tkinter as tk
import random
from datetime import datetime

MATERIAS=[
    "Fundamentos de Redes de Computadores",
    "Segurança da Informação",
    "Computação em Nuvem",
    "Programação",
    "Matemática e Lógica"
]
HORARIO_ESTUDO="20:00"

def sugestao_materia():
    return random.choice(MATERIAS)

def responder(msg):
    msg=msg.lower()
    if "oi" in msg:
        return "Olá! Tudo certo por aí? Vamos estudar?"
    elif "estudar" in msg:
        return f"Vamos lá! Hoje recomendo estudar:\n{sugestao_materia()}"
    elif "qual materia" in msg or "qual matéria" in msg:
        return f"Minha sugestão é:\n{sugestao_materia()}"
    elif "hora" in msg:
        return "Agora são "+datetime.now().strftime("%H:%M")
    elif "tchau" in msg:
        return "Até mais! Bons estudos!"
    elif "tudo bem?" in msg or "tudo bem" in msg or "como vai" in msg or "como você está" in msg:
        return "Tudo otimo! E voce? Bora estudar?"
    return "Não entendi. Posso ajudar nos seus estudos."

def adicionar_msg(remetente,texto):
    hora=datetime.now().strftime("%H:%M")
    cor="#C725D3" if remetente=="Você" else "#46ACE7"
    anchor="e" if remetente=="Você" else "w"
    pad=(80,10) if remetente=="Você" else (10,80)

    frame=tk.Frame(chat_area,bg="#121212")
    frame.pack(fill="x",padx=pad,pady=5)

    tk.Label(frame,text=texto,bg=cor,fg="white",wraplength=280,
             justify="left",padx=12,pady=8,font=("Arial",11)).pack(anchor=anchor)

    tk.Label(frame,text=hora,bg="#121212",fg="#AAAAAA",
             font=("Arial",8)).pack(anchor=anchor)

    canvas.update_idletasks()
    canvas.yview_moveto(1.0)

def enviar():
    m=entrada.get().strip()
    if not m: return
    entrada.delete(0,tk.END)
    adicionar_msg("Você",m)
    adicionar_msg("Bot",responder(m))

def checar_horario():
    if datetime.now().strftime("%H:%M")==HORARIO_ESTUDO:
        adicionar_msg("Bot",f"⏰ Hora de estudar!\nHoje: {sugestao_materia()}")
    janela.after(60000,checar_horario)

janela=tk.Tk()
janela.title("Chat Estudo")
janela.geometry("450x550")
janela.configure(bg="#0B0B0B")

container=tk.Frame(janela,bg="#0C0C0C")
container.pack(fill="both",expand=True,padx=10,pady=10)

canvas=tk.Canvas(container,bg="#121212",highlightthickness=0)
scroll=tk.Scrollbar(container,command=canvas.yview)
chat_area=tk.Frame(canvas,bg="#121212")
chat_area.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0,0),window=chat_area,anchor="nw")
canvas.configure(yscrollcommand=scroll.set)
canvas.pack(side="left",fill="both",expand=True)
scroll.pack(side="right",fill="y")

entrada=tk.Entry(janela,font=("Arial",11))
entrada.pack(fill="x",padx=10,pady=(0,5))
entrada.bind("<Return>",lambda e: enviar())

tk.Button(janela,text="Enviar",command=enviar).pack(pady=(0,10))

adicionar_msg("Bot","Olá! Posso ajudar nos seus estudos.")
checar_horario()
janela.mainloop()
