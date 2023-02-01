from tkinter import * # '*'คือทั้งหมด
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title("Calculator")
GUI.geometry('700x600')

bg = PhotoImage(file = 'pngegg.png')

BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text = 'ใส่จำนวนกิโล:',font = (None,20))
L.pack()
M = Label(GUI,text = 'ราคากิโลละ 75 บาท:',font = (None,20))
M.pack()

v_quantity = StringVar() #เป็นตัวแปรที่ใช้กับข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None, 20))
E1.pack() #การแปะเข้าไปใน GUI

def Cal():
    try:
        quan = float(v_quantity.get())
        calc = quan * 75
        messagebox.showinfo('ราคา','ราคาทั้งหมด {}'.format(calc))
        v_quantity.set('')
        E1.focus()
    except:
        messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะเลขเท่านั้น')
        v_quantity.set('')
        E1.focus()

B = ttk.Button(GUI, text = 'คำนวณ', command = Cal)
B.pack(ipadx = 20, ipady = 10)

GUI.mainloop() #เพื่อให้โปรแกรมรันตลอดเวลา