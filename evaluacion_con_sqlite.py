from tkinter import *
from tkinter.messagebox import *
import sqlite3
from tkinter import ttk
import re

def crear_base():
    conn=sqlite3.connect("database15.db")
    return conn
def crear_tabla():
    conn = crear_base()
    c = conn.cursor()
    sql = """CREATE TABLE IF NOT EXISTS Superficie1 (id_vinedo,razon_social text, CUIT INTEGER, color text, variedad text, hectareas real)"""
    c.execute(sql)
    conn.commit()
    
crear_base()
crear_tabla()

#TKINTER
root = Tk()
root.title('Información Superficie Vitivinícola')
root.geometry("1000x500")

#SQULITE3
# Data base con datos viejos
datos_viejos = [
	[1,"La Reina SA", 30711245, "BLANCA", "SAUVIGNON", 23],
 [2,"DON ANTONIO SRL", 30114756, "BLANCA", "SAUVIGNON", 17],
 [3,"Pepe Hongo", 27542125, "BLANCA", "SAUVIGNON", 5],
 [4,"La Reina SA", 30711245, "TINTA", "MALBEC", 84],
 [5,"DON ANTONIO SRL", 30114756, "TINTA", "MALBEC", 56],
 [6,"Pepe Hongo", 27542125, "TINTA", "MALBEC", 21],
 [7,"La Reina SA", 30711245, "ROSADA", "SYRAH", 42],
 [8,"DON ANTONIO SRL", 30114756, "ROSADA", "SYRAH", 38],
 [9,"Pepe Hongo", 27542125, "ROSADA", "SYRAH", 9]
]

# Agregamos estilos
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")
style.map('Treeview',
	background=[('selected', "#347083")])


#TREEVIEW
# Crear marco de Treeview
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# CrearTreeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Crear tabla Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configurar el Scrollbar en la tabla
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("id_vinedo","razon_social", "CUIT", "provincia","color", "variedad", "hectareas")

# Formato de Columnas
my_tree.column("#0", width=0, anchor=W)
my_tree.column("id_vinedo", anchor=W, width=140)
my_tree.column("razon_social", anchor=W, width=140)
my_tree.column("CUIT", anchor=CENTER, width=100)
my_tree.column("color", anchor=CENTER, width=140)
my_tree.column("variedad", anchor=CENTER, width=140)
my_tree.column("hectareas", anchor=CENTER, width=140)

# Colocamos titulos a las columnas de la tabla
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("id_vinedo", text="ID_Viñedo", anchor=W)
my_tree.heading("razon_social", text="Razón Social", anchor=W)
my_tree.heading("CUIT", text="CUIT", anchor=CENTER)
my_tree.heading("color", text="Color", anchor=CENTER)
my_tree.heading("variedad", text="Variedad", anchor=CENTER)
my_tree.heading("hectareas", text="Hectáreas", anchor=CENTER)

# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# Agregar datos viejos
def insertar_datos_viejos():
    global count
    count = 0
    conn=crear_base()
    c=conn.cursor()
    for  record in datos_viejos:
        datosv=(record[0], record[1], record[2], record[3], record[4], record[5])
        sql="INSERT INTO Superficie1(id_vinedo,razon_social,CUIT,color,variedad,hectareas) VALUES(?, ?, ?, ?, ?, ?)"
        c.execute(sql,datosv)
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', text='', values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', text='', values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags=('oddrow',))
        count += 1
    conn.commit()    

#TKINTER
# Defino variables para tomar valores de campos de entrada
id_val,rs_val, cuit_val, color_val, variedad_val, ha_val = IntVar(), StringVar(), IntVar(), StringVar(), StringVar(), DoubleVar()
w_ancho = 20

# Creamos boxes de entra de datos
data_frame = LabelFrame(root, text="Ingreso de datos")
data_frame.pack(fill="x", expand="yes", padx=20)

id_label = Label(data_frame, text="ID Viñedo")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_entry = Entry(data_frame, textvariable = id_val, width = w_ancho) 
id_entry.grid(row=0, column=1, padx=10, pady=10)

rs_label = Label(data_frame, text="Razón Social")
rs_label.grid(row=0, column=2, padx=10, pady=10)
rs_entry = Entry(data_frame, textvariable = rs_val, width = w_ancho) 
rs_entry.grid(row=0, column=3, padx=10, pady=10)

cuit_label = Label(data_frame, text="CUIT")
cuit_label.grid(row=0, column=4, padx=10, pady=10)
cuit_entry = Entry(data_frame, textvariable = cuit_val, width = w_ancho) 
cuit_entry.grid(row=0, column=5, padx=10, pady=10)

color_label = Label(data_frame, text="Color")
color_label.grid(row=1, column=0, padx=10, pady=10)
color_entry = Entry(data_frame, textvariable = color_val, width = w_ancho) 
color_entry.grid(row=1, column=1, padx=10, pady=10)

variedad_label = Label(data_frame, text="Variedad")
variedad_label.grid(row=1, column=2, padx=10, pady=10)
variedad_entry = Entry(data_frame, textvariable = variedad_val, width = w_ancho) 
variedad_entry.grid(row=1, column=3, padx=10, pady=10)

ha_label = Label(data_frame, text="Hectáreas")
ha_label.grid(row=1, column=4, padx=10, pady=10)
ha_entry = Entry(data_frame, textvariable = ha_val, width = w_ancho) 
ha_entry.grid(row=1, column=5, padx=10, pady=10)


# Definir funciones para maniopular la tabla
def actualizar():
    global count
    count=0
    datosh = my_tree.get_children()
    for element in datosh:
        my_tree.delete(element)

    sql = "SELECT * FROM productos ORDER BY id_vinedo ASC"
    conn=crear_base()
    c=conn.cursor()
    datosf=c.execute(sql)

    resultado = datosf.fetchall()
    for record in resultado:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', text='', values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', text='', values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags=('oddrow',))
        count += 1


def insert(id,rs,cuit,color,variedad,ha):
    global count
    validar=color
    patron=re.compile('(?i)blanca|rosada|tinta')
    if re.match(patron,validar):
         record=(id,rs,cuit,color,variedad,ha)
         print(record)
         conn=crear_base()
         c=conn.cursor()
         sql="INSERT INTO Superficie1(id_vinedo,razon_social,CUIT,color,variedad,hectareas) VALUES(?, ?, ?, ?, ?, ?)"
         c.execute(sql, record)
         if count % 2 == 0:
            my_tree.insert(parent='', index='end', text='', values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags=('evenrow',))
         else:
            my_tree.insert(parent='', index='end', text='', values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags=('oddrow',))
         count += 1
    else:
        showerror(message="El color debe ser BLANCA, ROSADA o TINTA", title="Error carga en color")     
    conn.commit       
    
    id_entry.delete(0, END)
    rs_entry.delete(0, END)
    cuit_entry.delete(0, END)
    color_entry.delete(0, END)
    variedad_entry.delete(0, END)
    ha_entry.delete(0, END)
    
    
# Mover fila hacia arriba
def up():
	filas = my_tree.selection()
	for row in filas:
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)  

# Mover fila hacia bajo
def down():
	filas = my_tree.selection()
	for row in reversed(filas):
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

# Eliminar una fila
def remove_one():
    x = my_tree.selection()[0]
    item=my_tree.item(x)
    conn=crear_base()
    c=conn.cursor()
    id_v=item["values"][0]
    data = (id_v,)
    sql = "DELETE FROM Superficie1 WHERE id_vinedo = ?;"
    c.execute(sql, data)
    conn.commit()
    my_tree.delete(x)

# Eliminar varias filas
def remove_many():
    x = my_tree.selection()
    conn=crear_base()
    c=conn.cursor()
    for record in x:
        item=my_tree.item(x)
        id_v=item["values"][0]
        data = (id_v,)
        sql = "DELETE FROM Superficie1 WHERE id_vinedo = ?;"
        c.execute(sql, data)
        conn.commit()
    actualizar()

# Eliminar todas las filas
def remove_all():
    x=my_tree.get_children()
    conn=crear_base()
    c=conn.cursor()
    for record in x:
        item=my_tree.item(x)
        id_v=item["values"][0]
        data = (id_v,)
        sql = "DELETE FROM Superficie1 WHERE id_vinedo = ?;"
        c.execute(sql, data)
        conn.commit()
        my_tree.delete(x)
    actualizar()    

# Seleccionar registros
def select_record():
	# limpiar entrada de boxes
	id_entry.delete(0, END)
	rs_entry.delete(0, END)
	cuit_entry.delete(0, END)
	color_entry.delete(0, END)
	variedad_entry.delete(0, END)
	ha_entry.delete(0, END)

	# tomar datos
	selected = my_tree.focus()
	values = my_tree.item(selected, 'values')


	# registrar de datos en boxes 
	id_entry.insert(0, values[0])
	rs_entry.insert(0, values[1])
	cuit_entry.insert(0, values[2])
	color_entry.insert(0, values[3])
	variedad_entry.insert(0, values[4])
	ha_entry.insert(0, values[5])

# modificar registro
def change_record():
    # captar registros
    showinfo(message="Se modificarán uno o más registros", title="Modificación de un registro")
    selected = my_tree.focus()
    datos=(rs_entry.get(), cuit_entry.get(), color_entry.get(), variedad_entry.get(), ha_entry.get(),id_entry.get(),)
    # Actualizar registro
    conn=crear_base()
    c=conn.cursor()
    sql = "UPDATE Superficie1 SET razon_social=?, CUIT=?, color=?, variedad=?, hectareas=? WHERE id_vinedo=?;"
    c.execute(sql, datos)
    conn.commit()
    my_tree.item(selected, text="", values=(id_entry.get(), rs_entry.get(), cuit_entry.get(), color_entry.get(), variedad_entry.get(), ha_entry.get(),))

    # Clear entry boxes
    id_entry.delete(0, END)
    rs_entry.delete(0, END)
    cuit_entry.delete(0, END)
    color_entry.delete(0, END)
    variedad_entry.delete(0, END)
    ha_entry.delete(0, END)

# Crear boxes de funciones de tabla
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

modificar_button = Button(button_frame, text="Modificar",command=change_record) 
modificar_button.grid(row=0, column=0, padx=10, pady=10)

ingresar_button = Button(button_frame, text="Ingresar",command=lambda:insert(id_val.get(),rs_val.get(), cuit_val.get(), color_val.get(), variedad_val.get(), ha_val.get())) 
ingresar_button.grid(row=0, column=1, padx=10, pady=10)

eliminar_uno_button = Button(button_frame, text="Eliminar uno",command=remove_one)
eliminar_uno_button.grid(row=0, column=3, padx=10, pady=10)


actualizar_button = Button(button_frame, text="Actualizar tabla",command=actualizar) 
actualizar_button.grid(row=0, column=4, padx=10, pady=10)

mover_arriba_button = Button(button_frame, text="Mover arriba",command=up) 
mover_arriba_button.grid(row=0, column=5, padx=10, pady=10)

mover_abajo_button = Button(button_frame, text="Mover abajo",command=down) 
mover_abajo_button.grid(row=0, column=6, padx=10, pady=10)

seleccionar_registro_button = Button(button_frame, text="Seleccionar registro",command=select_record ) 
seleccionar_registro_button.grid(row=0, column=7, padx=10, pady=10)    


insertar_datos_viejos()

root.mainloop()






