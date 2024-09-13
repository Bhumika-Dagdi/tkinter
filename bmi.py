from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox 

def handle_login():
    try: 
       h=float(height_input.get())
       weight=float(weight_input.get())
       height=h/100
       bmi= float(weight / height**2)
       label_result.config(text=f"BMI {bmi}")
       if bmi>=25.0:
           messagebox.showinfo("BMI","Overweight")
       elif bmi>=18.5 and bmi<=24.9:
          messagebox.showinfo("BMI","You are Healthy.")
       elif bmi<18.5:
          messagebox.showinfo("BMI","Underweight")
       else:
          messagebox.showerror("BMI","Obesity")
    except ValueError:
        messagebox.showerror("Error","Enter valid height or weight.")

root=Tk()

height_label=Label(root,text="height:")
height_label.pack()
height_input=Entry(root)
height_input.pack(pady=10)

weight_label=Label(root,text="weight:")
weight_label.pack()
weight_input=Entry(root)
weight_input.pack(pady=10)


login_botton=Button(root,text="Calculate BMI",fg="black",bg="White",command=handle_login)
login_botton.pack(padx=10,pady=10)

label_result=Button(root,text="Calculate BMI",fg="black",bg="White",command=handle_login)
label_result.pack(padx=10,pady=10)

root.mainloop()