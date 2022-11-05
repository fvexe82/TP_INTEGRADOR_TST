#from CONTROLADORES import ListarPropiedades
from tkinter import *
from tkinter import ttk
from tkinter import BOTTOM,RIGHT,X,Y,Scrollbar,VERTICAL,HORIZONTAL,messagebox
from turtle import width
import tkinter as tk
from propiedades import propiedades



class Ventana(Frame):

    propiedades = propiedades()

    def __init__(self,master=None):
        super().__init__(master,width=1200, height=600)
        self.master=master
        self.pack()
        self.create_widgets()
        self.llenadatos()
        self.habilitarcajas("disabled")
        self.habilitarbtnoperaciones("normal")
        self.habilitarbtnguardar("disabled")
        
        self.Id_Propiedad=-1
        #self.listarPropiedades()

    def habilitarcajas(self,estado):
        self.txtIdtipo.configure(state=estado)
        self.txtIdestado.configure(state=estado)
        self.txtIdopcom.configure(state=estado)
        self.txtIdprop.configure(state=estado)
        self.txtnombre.configure(state=estado)
        self.txtdir.configure(state=estado)
        self.txtcontacto.configure(state=estado)

    def habilitarbtnoperaciones(self,estado):
        self.btnNuevo.configure(state=estado)
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)
    def habilitarbtnguardar(self,estado):
        self.btnguardar.configure(state=estado)
        self.btncancelar.configure(state=estado)
      
    def limpiarcajas(self):
        self.txtIdtipo.delete(0,END)
        self.txtIdestado.delete(0,END)
        self.txtIdopcom.delete(0,END)
        self.txtIdprop.delete(0,END)
        self.txtnombre.delete(0,END)
        self.txtdir.delete(0,END)
        self.txtcontacto.delete(0,END)
    
    def limpiargrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
      
    def llenadatos(self):
        datos= self.propiedades.consulta_propiedades()
        for row in datos:
            self.grid.insert("",END,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
    
    def fNuevo (self):
        self.habilitarcajas("normal")
        self.habilitarbtnoperaciones("disabled")
        self.habilitarbtnguardar("normal")
        self.limpiarcajas()
        self.txtIdtipo.focus()
    
    def fGuardar (self):
        if self.Id_Propiedad == -1:
            self.propiedades.inserta_propiedad(self.txtIdtipo.get(),self.txtIdestado.get(),self.txtIdopcom.get()
            , self.txtIdprop.get(), self.txtnombre.get(),self.txtdir.get(),self.txtcontacto.get())
            
        else:
            self.propiedades.modifica_propiedad(self.Id_Propiedad,self.txtIdtipo.get(),self.txtIdestado.get(),
            self.txtIdopcom.get(), self.txtIdprop.get(), self.txtnombre.get(),self.txtdir.get(),self.txtcontacto.get())
            self.Id_Propiedad = -1
        self.limpiargrid()
        self.llenadatos()
        self.limpiarcajas()
        self.habilitarbtnguardar("disabled")
        self.habilitarbtnoperaciones("normal")
        self.habilitarcajas("disabled")
    
    def fModificar (self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')    
        if clave == '':
            messagebox.showwarning("MODIFICAR",'DEBES SELECCIONAR UNA PROPIEDAD A MODIFICAR')
        else:
            self.Id_Propiedad = clave
            self.habilitarcajas("normal")
            valores =self.grid.item(selected,'values')
            self.limpiarcajas()
            self.txtIdtipo.insert(0,valores[0])
            self.txtIdestado.insert(0,valores[1])
            self.txtIdopcom.insert(0,valores[2])
            self.txtIdprop.insert(0,valores[3])
            self.txtnombre.insert(0,valores[4])
            self.txtdir.insert(0,valores[5])
            self.txtcontacto.insert(0,valores[6])
            self.habilitarbtnoperaciones("disabled")
            self.habilitarbtnguardar("normal")
            self.txtIdtipo.focus()

    def fEliminar (self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')    
        if clave == '':
            messagebox.showwarning("ELIMINAR",'DEBES SELECCIONAR UNA PROPIEDAD A ELIMINAR')
        else:
            valores =self.grid.item(selected,'values')
            data = str(clave) #+ "," + valores [6] 
            r = messagebox.askquestion("ELIMINAR", '¿REALMENTE DESEA ELIMINAR LA PROPIEDAD?\n' + data)
            if r == messagebox.YES:
                n = self.propiedades.elimina_propiedad(clave)
                if n == 1 :
                    messagebox.showinfo("ELIMINAR",'PROPIEDAD ELIMINADA CORRECTAMENTE')
                    self.limpiargrid()
                    self.llenadatos()
                else:
                    messagebox.showinfo("ELIMINAR",'NO FUE POSIBLE ELIMINAR LA PROPIEDAD') 
    
    def fCancelar (self):
        self.limpiarcajas()
        self.habilitarbtnguardar("disabled")
        self.habilitarbtnoperaciones("normal")
        self.habilitarcajas("disabled")

    
    def fListatotal (self):
        self.propiedades.listarPropiedades()          

    def fDventa (self):
        self.propiedades.listarPropiedadesventa()
        
    def fDalq (self):
        self.propiedades.listarPropiedadesalquiler()

    def fVen (self):
        self.propiedades.listarPropiedadesvendidas()

    def fAlq (self):
        self.propiedades.listarPropiedadesalquiladas()

    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=0,width=160,height=600)

        self.btnNuevo=Button(frame1,text="INGRESAR PROPIEDAD", command=self.fNuevo, bg="blue",fg="white")
        self.btnNuevo.place(x=5,y=50,width=150,height=30)

        self.btnModificar=Button(frame1,text="MODIFICAR PROPIEDAD", command=self.fModificar, bg="blue",
        fg="white")
        self.btnModificar.place(x=5,y=90,width=150,height=30)

        self.btnEliminar=Button(frame1,text="ELIMINAR PROPIEDAD", command=self.fEliminar, bg="blue",
        fg="white")
        self.btnEliminar.place(x=5,y=130,width=150,height=30)

        self.btnlistatotal=Button(frame1,text="VER TOTAL DE PROP.", command=self.fListatotal, bg="orange",
        fg="black")
        self.btnlistatotal.place(x=5,y=200,width=150,height=30)

        self.btndventa=Button(frame1,text="DISPONIBLES P-VENTA", command=self.fDventa, bg="orange",fg="black")
        self.btndventa.place(x=5,y=240,width=150,height=30)

        self.btndalq=Button(frame1,text="DISP. P-ALQUILER", command=self.fDalq, bg="orange",fg="black")
        self.btndalq.place(x=5,y=280,width=150,height=30)

        self.btnvendidas=Button(frame1,text="PROP. VENDIDAS", command=self.fVen, bg="orange",fg="black")
        self.btnvendidas.place(x=5,y=320,width=150,height=30)

        self.btnalqui=Button(frame1,text="PROP. ALQUILADAS", command=self.fAlq, bg="orange",fg="black")
        self.btnalqui.place(x=5,y=360,width=150,height=30)

        frame2 = Frame(self, bg="#d3dde3")
        frame2.place(x=160,y=0,width=195,height=600)

        lbl1=Label(frame2,text="Id_Tipo")
        lbl1.place(x=3,y=5)
        self.txtIdtipo=Entry(frame2)
        self.txtIdtipo.place(x=3,y=25,width=50,height=20)

        lbl2=Label(frame2,text="Id_Estado")
        lbl2.place(x=3,y=50)
        self.txtIdestado=Entry(frame2)
        self.txtIdestado.place(x=3,y=75,width=50,height=20)

        lbl3=Label(frame2,text="Id_Operacion_Comercial")
        lbl3.place(x=3,y=105)
        self.txtIdopcom=Entry(frame2)
        self.txtIdopcom.place(x=3,y=125,width=50,height=20)

        lbl4=Label(frame2,text="Id_Propietario")
        lbl4.place(x=3,y=155)
        self.txtIdprop=Entry(frame2)
        self.txtIdprop.place(x=3,y=175,width=50,height=20)

        lbl5=Label(frame2,text="Nombre")
        lbl5.place(x=3,y=205)
        self.txtnombre=Entry(frame2)
        self.txtnombre.place(x=3,y=225,width=190,height=20)

        lbl6=Label(frame2,text="Dirección")
        lbl6.place(x=3,y=255)
        self.txtdir=Entry(frame2)
        self.txtdir.place(x=3,y=275,width=190,height=20)

        lbl7=Label(frame2,text="Contacto")
        lbl7.place(x=3,y=305)
        self.txtcontacto=Entry(frame2)
        self.txtcontacto.place(x=3,y=325,width=190,height=20)

        self.btnguardar=Button(frame2,text="GUARDAR", command=self.fGuardar, bg="green",fg="white")
        self.btnguardar.place(x=10,y=350,width=70,height=30)
        self.btncancelar=Button(frame2,text="CANCELAR", command=self.fCancelar, bg="red",fg="white")
        self.btncancelar.place(x=100,y=350,width=70,height=30)

        frame3 = Frame(self, bg="grey")
        frame3.place(x=360,y=0,width= 800, height=600)
        
        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3","col4","col5","col6","col7"))

        self.grid.column("#0",width=80)
        self.grid.column("col1",width=70, anchor=CENTER)
        self.grid.column("col2",width=70, anchor=CENTER)
        self.grid.column("col3",width=100, anchor=CENTER)
        self.grid.column("col4",width=140, anchor=CENTER)
        self.grid.column("col5",width=120, anchor=CENTER)
        self.grid.column("col6",width=120, anchor=CENTER)
        self.grid.column("col7",width=120, anchor=CENTER)

        self.grid.heading("#0", text="Id_Propiedad", anchor=CENTER)
        self.grid.heading("col1", text="Id_Tipo", anchor=CENTER)
        self.grid.heading("col2", text="Id_Estado", anchor=CENTER)
        self.grid.heading("col3", text="Id_Op.Comercial", anchor=CENTER)
        self.grid.heading("col4", text="Id_Propietario", anchor=CENTER)
        self.grid.heading("col5", text="NOMBRE", anchor=CENTER)
        self.grid.heading("col6", text="DIRECCION", anchor=CENTER)
        self.grid.heading("col7", text="CONTACTO", anchor=CENTER)

        
        self.grid.pack(side=LEFT, fill = Y) 
        sb = Scrollbar(frame3,orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.grid.config (yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)

        self.grid[ 'selectmode' ] = 'browse'

        

