from Funcoes import Click
import customtkinter

customtkinter.set_appearance_mode("dark-blue")

Window = customtkinter.CTk()
Window.title("Calculadora")
Window.geometry("500x500")

#Font
font=customtkinter.CTkFont(family='Arial', size=20)
font=('Arial', 20)

text = customtkinter.CTkLabel(Window, text="Calculadora", font=font)
text.pack(padx = 10, pady = 10)

output = customtkinter.CTkLabel(Window, text="")
output.pack(padx=10, pady= 10)

button = customtkinter.CTkButton(Window, text="clique", function=Click())
button.pack()

#Tela


Window.mainloop()