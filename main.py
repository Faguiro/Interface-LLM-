import tkinter as tk
from tkinter import scrolledtext
import threading
import time
import llm
from gif_player import GIFPlayer 

class LLMInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Interface LLM 🤖")
        self.master.geometry("540x450")
        self.master.configure(bg="white")

        # Modelo LLM
        self.model = llm.get_model("phi3:mini")

        # Criação dos widgets
        self.create_widgets()

        # Adicionando o GIFPlayer com redimensionamento
        self.gif_player = GIFPlayer(master, 'robot.gif', frame_count=40, width=100, height=100)

    def create_widgets(self):
        # Criação da entrada de dados
        self.entry_label = tk.Label(self.master, bg="white", text="Digite seu texto:")
        self.entry_label.grid(row=0, column=0, padx=10, pady=10)

        self.entry = tk.Entry(self.master, width=50,)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        # Criação do botão de enviar
        self.submit_button = tk.Button(self.master, text="Enviar 🚀", command=self.on_submit,  bg="white", borderwidth=2, relief="groove")
        self.submit_button.grid(row=0, column=2, padx=10, pady=10)

        # Criação da área de texto para mostrar a resposta
        self.text_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=60, height=20)
        

        # Adicionar um botão para salvar a resposta
        self.save_button = tk.Button(self.master, text="Salvar Resposta 💾", command=self.save_response)
        

    def on_submit(self):
        user_input = self.entry.get()
        print(f"User input: {user_input}")
        
        # Desativar a entrada e o botão
        self.entry.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)


        # Desativar o botão 
        self.save_button.grid_forget()

        # Iniciar o GIFPlayer
        self.gif_player.start()

        # Iniciar a thread para processar o prompt
        threading.Thread(target=self.async_prompt, args=(user_input,)).start()

    def async_prompt(self, text):
        init_time = time.time()
        print("Starting async prompt...")
        response = self.prompt(text)
        exec_time = time.time() - init_time 
        print(f"Resposta: {response}, Execution Time: {exec_time}")
        self.update_text_area(response, exec_time)

        # Parar o GIFPlayer e reativar a entrada e o botão
        self.gif_player.stop()
        self.entry.config(state=tk.NORMAL)
        self.submit_button.config(state=tk.NORMAL)

    def prompt(self, text):  
        text_br = f"{text}. Responda em português brasileiro"
        response = self.model.prompt(text_br)
        return response.text()  
     

    def update_text_area(self, response, exec_time):
        self.text_area.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        self.save_button.grid(row=2, column=0, columnspan=3, pady=10)
        self.gif_player.destroy()
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, f"Resposta:\n{response}\n\nTempo de Execução: {exec_time:.2f} segundos")

    def save_response(self):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        if response_text := self.text_area.get("1.0", tk.END).strip():
            with open(f"resposta_{timestamp}.txt", "w", encoding="utf-8") as file:
                file.write(response_text)
            print("Resposta salva em resposta.txt")
            self.save_button.grid_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = LLMInterface(root)
    root.mainloop()
