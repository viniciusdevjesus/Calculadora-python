import customtkinter

customtkinter.set_appearance_mode("dark-blue")

Window = customtkinter.CTk()
Window.title("Calculadora")
Window.geometry("500x500")

text = customtkinter.CTkLabel(Window, text="Calculadora")
text.pack(padx = 10, pady = 10)


Window.mainloop()