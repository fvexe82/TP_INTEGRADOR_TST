from tkinter import *
from tkinter import ttk
class Ventana(Frame):
    def __init__(self,master=None):
        super().__init__(master,width=1200, height=600)
        self.master=master
        self.pack()
        self.create_widgets()

    def fNuevo(self):
        pass
    
    def fModificar(self):
        pass
    
    def fEliminar (self):
        pass

    def fGuardar (self):
        pass
    
    def fCancelar (self):
        pass

    def fPropiedades_Totales (self):
        pass

    def fDisponibles_Venta (self):
        pass

    def fDisponibles_Alquiler (self):
        pass
    def fVendidas (self):
        pass

    def fAlquiladas(self):
        pass
    
    def create_widgets(self):
        frame1=Frame(self,bg="#bfdaff")
        frame1.place(x=0,y=0,width=160,height=600)
        self.btnNuevo=Button(frame1,text="Ingresar Propiedad",command=self.fNuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5,y=50,width=150, height=30)
    
        self.btnNuevo=Button(frame1,text="Modificar Propiedad",command=self.fModificar, bg="blue", fg="white")
        self.btnNuevo.place(x=5,y=90,width=150, height=30)

        self.btnNuevo=Button(frame1,text="Eliminar Propiedad",command=self.fEliminar, bg="blue", fg="white")
        self.btnNuevo.place(x=5,y=130,width=150, height=30)

        self.btnNuevo=Button(frame1,text="Propiedades Totales",command=self.fPropiedades_Totales, bg="orange", fg="black")
        self.btnNuevo.place(x=5,y=170,width=150, height=30)

        self.btnNuevo=Button(frame1,text="Disponibles para Venta",command=self.fDisponibles_Venta, bg="orange", fg="black")
        self.btnNuevo.place(x=5,y=210,width=150, height=30)

        self.btnNuevo=Button(frame1,text="Disponibles Alquiler",command=self.fDisponibles_Alquiler, bg="orange", fg="black")
        self.btnNuevo.place(x=5,y=250,width=150, height=30)

        self.btnNuevo=Button(frame1,text="Vendidas",command=self.fVendidas, bg="orange", fg="black")
        self.btnNuevo.place(x=5,y=290,width=150, height=30)

        self.btnNuevo=Button(frame1,text="Alquiladas",command=self.fAlquiladas, bg="orange", fg="black")
        self.btnNuevo.place(x=5,y=330,width=150, height=30)

        frame2= Frame(self, bg="#d3dde3")
        frame2.place (x=160,y=0,width=200,height=600)

        lbl1=Label(frame2, text="Id_Tipo: ")
        lbl1.place(x=3,y=5)
        self.txtId_Tipo=Entry(frame2)
        self.txtId_Tipo.place(x=3,y=25,width=190,height=20)

        lbl2=Label(frame2, text="Id_Estado: ")
        lbl2.place(x=3,y=55)
        self.txtId_Estado=Entry(frame2)
        self.txtId_Estado.place(x=3,y=75,width=190,height=20)

        lbl3=Label(frame2, text="Id_Operacion_Comercial: ")
        lbl3.place(x=3,y=105)
        self.txtId_Operacion_Comercial=Entry(frame2)
        self.txtId_Operacion_Comercial.place(x=3,y=125,width=190,height=20)

        lbl4=Label(frame2, text="Id_Propietario: ")
        lbl4.place(x=3,y=155)
        self.txtId_Propietario=Entry(frame2)
        self.txtId_Propietario.place(x=3,y=175,width=190,height=20)

        lbl5=Label(frame2, text="Nombre: ")
        lbl5.place(x=3,y=205)
        self.txtNombre=Entry(frame2)
        self.txtNombre.place(x=3,y=225,width=190,height=20)

        lbl6=Label(frame2, text="Direccion: ")
        lbl6.place(x=3,y=255)
        self.txtDireccion=Entry(frame2)
        self.txtDireccion.place(x=3,y=275,width=190,height=20)

        lbl7=Label(frame2, text="Contacto: ")
        lbl7.place(x=3,y=305)
        self.txtContacto=Entry(frame2)
        self.txtContacto.place(x=3,y=325,width=190,height=20)

        self.btnGuardar=Button(frame2,text="Guardar",command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=10,y= 350,width=75, height=30)

        self.btnCancelar=Button(frame2,text="Cancelar",command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=90,y= 350,width=75, height=30)

        self.grid=ttk.Treeview(self, columns=("col1","col2","col3","col4","col5","col6","col7"))

        self.grid.column ("#0",width=50)
        self.grid.column ("col1",width=80,anchor=CENTER)
        self.grid.column ("col2",width=80,anchor= CENTER)
        self.grid.column ("col3",width=70, anchor=CENTER)
        self.grid.column ("col4",width=100, anchor=CENTER)
        self.grid.column ("col5",width=100, anchor=CENTER)
        self.grid.column ("col6",width=100, anchor=CENTER)
        self.grid.column ("col7",width=80,anchor=CENTER)

        self.grid.heading("#0", text="Id_Propiedad", anchor=CENTER)
        self.grid.heading("col1", text="Id_Tipo", anchor=CENTER)
        self.grid.heading("col2", text="Id_Estado", anchor=CENTER)
        self.grid.heading("col3", text="Id_Operacion_Comercial", anchor=CENTER)
        self.grid.heading("col4", text="Id_Propietario", anchor=CENTER)
        self.grid.heading("col5", text="Nombre", anchor=CENTER)
        self.grid.heading("col6", text="Direccion", anchor=CENTER)
        self.grid.heading("col7", text="Contacto", anchor=CENTER)

        self.grid.place(x=360,y=0,width=800, height=600)

        self.grid.insert("",END,text="1",values=("aa","bb","cc","dd","ee","ff","gg"))
        
        
      






        
