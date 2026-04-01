import customtkinter as ctk
import pypower, time
from simpleeval import simple_eval
main = ctk.CTk()
main.geometry('1200x800')
def create_op():
    return ctk.CTkEntry(main, width=1000, font=('arial', 50))
op = create_op()
op.pack(pady=20)
result = create_op()
result.pack(pady=10)
syms = pypower.GUI.CustomTk.console(main, ['-', '+', '÷', '×', '='], 3 , op, return_dic_frame_and_buttons=True, font=('arial', 30))
syms['frame'].pack()
pypower.GUI.CustomTk.console_num(main, entry_to_insert=op, font=('arial', 30)).pack()
def calc():
    try:
        res = simple_eval(pypower.String(op.get()).replace_many(['÷', '×'], ['/', '*']))
        result.delete(0, 'end')
        result.insert(0, res)
    except:
        pypower.GUI.CustomTk.show_hide_message(main, 'Error!')
syms['buttons'][-1].configure(command=calc)
for i in main.winfo_children()[2:]:
    pypower.GUI.CustomTk.move(i)
main.mainloop()
