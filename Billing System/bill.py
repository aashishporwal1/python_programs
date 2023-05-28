<<<<<<< HEAD
from tkinter import *
import math,random
import os
from tkinter import messagebox
import mysql.connector

class Bill_App:
    def __init__(self,root):
        self.root=root
        #"0" and "0" specifies the position from x and y-axis respectively
        self.root.geometry("1350x700+0+0")
        # TITLE PART
        self.root.title("Biiling System")
        bg_color="#074463" # Code for Dark Blue color
        title=Label(self.root,text="Billing System",font=("time new roman",30,"bold"),pady=0,bd=12,relief=GROOVE,bg=bg_color,fg="white").pack(fill=X)

        # VARIABLES
        # COSMETICS
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.lotion=IntVar()
        
        # GROCERY
        self.rice=IntVar()
        self.oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()

        # OTHERS
        self.maaza=IntVar()
        self.coke=IntVar()
        self.frooti=IntVar()
        self.nimkos=IntVar()
        self.biscuit=IntVar()
        
        # TOTAL PRODUCTS AND TAX
        self.cosmetics=StringVar()
        self.grocery=StringVar()
        self.others=StringVar()

        self.cosmetics_tax=StringVar()
        self.grocery_tax=StringVar()
        self.others_tax=StringVar()
        
        # CUSTOMER 
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        
        
        # CUSTOMER DETAILS FRAME
        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_label=Label(F1,text="Customer Name",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=20,pady=5)
        cname_text=Entry(F1,textvariable=self.c_name,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_label=Label(F1,text="Phone No.",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=3,padx=20,pady=5)
        cphone_text=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=4,pady=5,padx=10)

        c_bill_label=Label(F1,text="Bill No.",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=5,padx=20,pady=5)
        c_bill_text=Entry(F1,textvariable=self.search_bill,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=6,pady=5,padx=10)

        entry_btn=Button(F1,text="Enter",command=self.find_bill,width=10,bd=7,font="arial 12 bold",bg=bg_color,fg="white").grid(row=0,column=7,padx=40,pady=10)
        
        # COSMETICS FRAME
        F2=LabelFrame(self.root,text="Cosmetics",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=190,width=325,height=340)

        
        soap_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        soap_txt=Entry(F2,textvariable=self.soap,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=30,pady=10)

        f_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        f_cream_txt=Entry(F2,textvariable=self.face_cream,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=30,pady=10)

        f_wash_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        f_wash_txt=Entry(F2,textvariable=self.face_wash,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=30,pady=10)

        spray_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        spray_txt=Entry(F2,textvariable=self.spray,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=30,pady=10)

        lotion_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        lotion_txt=Entry(F2,textvariable=self.lotion,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=30,pady=10)

        # GROCERY FRAME
        F3=LabelFrame(self.root,text="Grocery",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=190,width=325,height=340)

        
        rice_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_txt=Entry(F3,textvariable=self.rice,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=60,pady=10)

        oil_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        oil_txt=Entry(F3,textvariable=self.oil,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=60,pady=10)

        daal_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        daal_txt=Entry(F3,textvariable=self.daal,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=60,pady=10)

        wheat_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        wheat_txt=Entry(F3,textvariable=self.wheat,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=60,pady=10)

        sugar_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        sugar_txt=Entry(F3,textvariable=self.sugar,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=60,pady=10)

        # OTHERS FRAME
        F4=LabelFrame(self.root,text="Others",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=190,width=325,height=340)

        
        maaza_lbl=Label(F4,text="Maaza",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        maaza_txt=Entry(F4,textvariable=self.maaza,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=60,pady=10)

        coke_lbl=Label(F4,text="Coke",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        coke_txt=Entry(F4,textvariable=self.coke,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=60,pady=10)

        frooti_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        frooti_txt=Entry(F4,textvariable=self.frooti,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=60,pady=10)

        nimkos_lbl=Label(F4,text="Nimkos",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        nimkos_txt=Entry(F4,textvariable=self.nimkos,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=60,pady=10)

        biscuits_lbl=Label(F4,text="Biscuits",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        biscuits_txt=Entry(F4,textvariable=self.biscuit,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=60,pady=10)

        # BILL AREA        
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=190,width=340,height=340)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        # SCROLL BAR
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        # self is used coz we want scroll-bar throughout the page
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        
        # TOTAL AREA
        F6=LabelFrame(self.root,text="Bill Menu",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=540,relwidth=1,height=150)
        
        t_cosmetics_lbl=Label(F6,text="Total Cosmetics",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=2,sticky="w")
        t_cosmetics_txt=Entry(F6,textvariable=self.cosmetics,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=2)
        
        t_grocery_lbl=Label(F6,text="Total Grocery",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=2,sticky="w")
        t_grocery_txt=Entry(F6,textvariable=self.grocery,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=2)

        t_others_lbl=Label(F6,text="Others Total",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=2,sticky="w")
        t_others_txt=Entry(F6,textvariable=self.others,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=2)
        
        # TAX AREA
        
        tax_cosmetics_lbl=Label(F6,text="Cosmetics Tax",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=10,pady=2,sticky="w")
        tax_cosmetics_txt=Entry(F6,textvariable=self.cosmetics_tax,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=30,pady=2)
        
        tax_grocery_lbl=Label(F6,text="Grocery Tax",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=1,column=2,padx=10,pady=2,sticky="w")
        tax_grocery_txt=Entry(F6,textvariable=self.grocery_tax,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=30,pady=2)

        tax_others_lbl=Label(F6,text="Others Tax",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=2,column=2,padx=10,pady=2,sticky="w")
        tax_others_txt=Entry(F6,textvariable=self.others_tax,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=30,pady=2)
        
        # BUTTON FRAME
        
        btn_F=Frame(F6,bd=7,relief=GROOVE,bg=bg_color)
        btn_F.place(x=670,width=650,height=110  )

        total_btn=Button(btn_F,command=self.total,text="Total",width=8,bd=7,font="arial 12 bold",bg=bg_color,fg="white").grid(row=1,column=0,padx=20,pady=25)
        gen_bill_btn=Button(btn_F,command=lambda:[self.bill_area(),self.insert_data()],text="Generate Bill",width=15,bd=7,font="arial 12 bold",bg=bg_color,fg="white").grid(row=1,column=1,padx=20,pady=25)
        clear_btn=Button(btn_F,command=self.clear_data,text="Clear",width=8,bd=7,font="arial 12 bold",bg=bg_color,fg="white").grid(row=1,column=2,padx=20,pady=25)
        exit_btn=Button(btn_F,command=self.exit_app,text="Exit",width=8,bd=7,font="arial 12 bold",bg=bg_color,fg="white").grid(row=1,column=3,padx=20,pady=25)
        self.bill()
     
    def total(self):
        
        self.soap_total = self.soap.get()*40
        self.face_cream_total = self.face_cream.get()*100
        self.face_wash_total = self.face_wash.get()*150
        self.spray_total = self.spray.get()*200
        self.lotion_total = self.lotion.get()*150
            
        self.total_cosmetics=float(
                                    self.soap_total+
                                    self.face_cream_total+
                                    self.face_wash_total+
                                    self.spray_total+
                                    self.lotion_total                                            
                            )
        self.cosmetics.set("Rs. "+str(self.total_cosmetics))
        self.c_tax = round((self.total_cosmetics*0.05),2)
        self.cosmetics_tax.set("Rs. "+str(self.c_tax))
        
        
        self.rice_total = self.rice.get()*80
        self.oil_total = self.oil.get()*100
        self.daal_total = self.daal.get()*80
        self.wheat_total = self.wheat.get()*200
        self.sugar_total = self.sugar.get()*45
        
        self.total_grocery=float(
                                    self.rice_total+
                                    self.oil_total+
                                    self.daal_total+
                                    self.wheat_total+
                                    self.sugar_total
                            )
        self.grocery.set("Rs. "+str(self.total_grocery))
        self.g_tax = round((self.total_grocery*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))
        
        self.maaza_total = self.maaza.get()*50
        self.coke_total = self.coke.get()*50
        self.frooti_total = self.frooti.get()*50
        self.nimkos_total = self.nimkos.get()*50
        self.biscuit_total = self.biscuit.get()*30
        self.total_others=float(
                                    self.maaza_total+
                                    self.coke_total+
                                    self.frooti_total+
                                    self.nimkos_total+
                                    self.biscuit_total                  
                            )
        self.others.set("Rs. "+str(self.total_others))
        self.o_tax = round((self.total_others*0.1),2)
        self.others_tax.set("Rs. "+str(self.o_tax))

        self.total_bill = float(
                                    self.total_cosmetics+
                                    self.total_grocery+
                                    self.total_others+
                                    self.c_tax+
                                    self.g_tax+
                                    self.o_tax
        )
        self.final_bill = ""
        self.final_bill = str(self.total_bill)
        
    def bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t Welcome to Aashish's Retail \n")
        self.txtarea.insert(END,f"\n Bill No. : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone No. : {self.c_phone.get()}")
        self.txtarea.insert(END,"\n"+"="*37)
        self.txtarea.insert(END,"\n Products\t\tQty\t     Price")
        self.txtarea.insert(END,"\n"+"="*37)
       
        
    def bill_area(self):
        
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error","Please Enter Customer Details")
        
        elif self.total_cosmetics == 0.0 and self.total_grocery == 0.0 and self.total_others == 0.0 :
            messagebox.showerror("Error","Please select some products")
        
        else:
            
            self.bill() 
            # COSMETICS     
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t      {self.soap_total}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t      {self.face_cream_total}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t      {self.face_wash_total}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t      {self.spray_total}")
            if self.lotion.get()!=0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t{self.lotion.get()}\t      {self.lotion_total}")
            
            # GROCERIES
            
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t      {self.rice_total}")
            if self.oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.oil.get()}\t      {self.oil_total}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t      {self.daal_total}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t      {self.wheat_total}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t      {self.sugar_total}")
            
            # OTHERS     

            if self.maaza.get()!=0:
                self.txtarea.insert(END,f"\n Maaza\t\t{self.maaza.get()}\t      {self.maaza_total}")
            if self.coke.get()!=0:
                self.txtarea.insert(END,f"\n Coke\t\t{self.coke.get()}\t      {self.coke_total}")
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t      {self.frooti_total}")
            if self.nimkos.get()!=0:
                self.txtarea.insert(END,f"\n Nimkos\t\t{self.nimkos.get()}\t      {self.nimkos_total}")
            if self.biscuit.get()!=0:
                self.txtarea.insert(END,f"\n Biscuit\t\t{self.biscuit.get()}\t      {self.biscuit_total}")
            
            self.txtarea.insert(END,"\n"+"-"*37)        
            if self.cosmetics_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetics Tax \t\t\t  {self.cosmetics_tax.get()}")
            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END,f"\n Groceries Tax \t\t\t  {self.grocery_tax.get()}")
            if self.others_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END,f"\n Others Tax \t\t\t  {self.others_tax.get()}")
            self.txtarea.insert(END,"\n"+"-"*37)
            self.txtarea.insert(END,f"\n Total Bill \t\t\t  Rs. {self.total_bill}")
            self.txtarea.insert(END,"\n"+"-"*37)
            self.save_bill()
    
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op != 0:
            
            self.bill_data=self.txtarea.get("1.0",END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Your Bill no. : {self.bill_no.get()} Saved Successfully")
        else :
            return
   
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for j in f1:
                    self.txtarea.insert(END,j)
                f1.close()
                present="yes"
        if present=="no" :
            messagebox.showerror("Error","Invalid Bill No.")
   
    def clear_data(self):
         # COSMETICS
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.spray.set(0)
        self.lotion.set(0)
        self.rice.set(0)
        self.oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.maaza.set(0)
        self.coke.set(0)
        self.frooti.set(0)
        self.nimkos.set(0)
        self.biscuit.set(0)
        self.cosmetics.set("")
        self.grocery.set("")
        self.others.set("")
        self.cosmetics_tax.set("")
        self.grocery_tax.set("")
        self.others_tax.set("")
        
        # CUSTOMER 
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.bill()
        
    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to Exit")
        if op != 0:
            self.root.destroy()   
            
    def create_conn(self):
            return mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="billing_system",
            port="3307"
        )
    def insert_data(self):
        if self.c_name.get()=="" or self.c_phone.get()=="" :
            messagebox.showinfo("Insert Status","All Fields are Mandatory")
        else:
            conn=self.create_conn()
            cursor=conn.cursor()
            query="insert into bills(cname,phone,bill_no,total_bill) values(%s,%s,%s,%s)"
            args=(self.c_name.get(),self.c_phone.get(),self.bill_no.get(),self.final_bill)
            cursor.execute(query,args)
            conn.commit()
            conn.close()
            messagebox.showinfo("Insert Status","Data Inserted Successfully")

            #e_fname.delete(0,'end')
            #e_lname.delete(0,'end')
            #e_email.delete(0,'end')
            #e_mobile.delete(0,'end')           

            
               
root=Tk()
obj= Bill_App(root)
root.mainloop()
=======
from tkinter import *
import math,random
import os
from tkinter import messagebox
import mysql.connector

class Bill_App:
    def __init__(self,root):
        self.root=root
        #"0" and "0" specifies the position from x and y-axis respectively
        self.root.geometry("1350x700+0+0")
        # TITLE PART
        self.root.title("Biiling System")
        bg_color="#074463" # Code for Dark Blue color
        title=Label(self.root,text="Billing System",font=("time new roman",30,"bold"),pady=0,bd=12,relief=GROOVE,bg=bg_color,fg="white").pack(fill=X)

        # VARIABLES
        # COSMETICS
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.lotion=IntVar()
        
        # GROCERY
        self.rice=IntVar()
        self.oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()

        # OTHERS
        self.maaza=IntVar()
        self.coke=IntVar()
        self.frooti=IntVar()
        self.nimkos=IntVar()
        self.biscuit=IntVar()
        
        # TOTAL PRODUCTS AND TAX
        self.cosmetics=StringVar()
        self.grocery=StringVar()
        self.others=StringVar()

        self.cosmetics_tax=StringVar()
        self.grocery_tax=StringVar()
        self.others_tax=StringVar()
        
        # CUSTOMER 
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        
        
        # CUSTOMER DETAILS FRAME
        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_label=Label(F1,text="Customer Name",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=20,pady=5)
        cname_text=Entry(F1,textvariable=self.c_name,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_label=Label(F1,text="Phone No.",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=3,padx=20,pady=5)
        cphone_text=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=4,pady=5,padx=10)

        c_bill_label=Label(F1,text="Bill No.",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=5,padx=20,pady=5)
        c_bill_text=Entry(F1,textvariable=self.search_bill,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=6,pady=5,padx=10)

        entry_btn=Button(F1,text="Enter",command=self.find_bill,width=10,bd=7,font="arial 12 bold",bg=bg_color,fg="white").grid(row=0,column=7,padx=40,pady=10)
        
        # COSMETICS FRAME
        F2=LabelFrame(self.root,text="Cosmetics",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=190,width=325,height=340)

        
        soap_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        soap_txt=Entry(F2,textvariable=self.soap,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=30,pady=10)

        f_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        f_cream_txt=Entry(F2,textvariable=self.face_cream,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=30,pady=10)

        f_wash_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        f_wash_txt=Entry(F2,textvariable=self.face_wash,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=30,pady=10)

        spray_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        spray_txt=Entry(F2,textvariable=self.spray,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=30,pady=10)

        lotion_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        lotion_txt=Entry(F2,textvariable=self.lotion,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=30,pady=10)

        # GROCERY FRAME
        F3=LabelFrame(self.root,text="Grocery",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=190,width=325,height=340)

        
        rice_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_txt=Entry(F3,textvariable=self.rice,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=60,pady=10)

        oil_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        oil_txt=Entry(F3,textvariable=self.oil,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=60,pady=10)

        daal_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        daal_txt=Entry(F3,textvariable=self.daal,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=60,pady=10)

        wheat_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        wheat_txt=Entry(F3,textvariable=self.wheat,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=60,pady=10)

        sugar_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        sugar_txt=Entry(F3,textvariable=self.sugar,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=60,pady=10)

        # OTHERS FRAME
        F4=LabelFrame(self.root,text="Others",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=190,width=325,height=340)

        
        maaza_lbl=Label(F4,text="Maaza",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        maaza_txt=Entry(F4,textvariable=self.maaza,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=60,pady=10)

        coke_lbl=Label(F4,text="Coke",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        coke_txt=Entry(F4,textvariable=self.coke,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=60,pady=10)

        frooti_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        frooti_txt=Entry(F4,textvariable=self.frooti,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=60,pady=10)

        nimkos_lbl=Label(F4,text="Nimkos",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        nimkos_txt=Entry(F4,textvariable=self.nimkos,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=60,pady=10)

        biscuits_lbl=Label(F4,text="Biscuits",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        biscuits_txt=Entry(F4,textvariable=self.biscuit,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=60,pady=10)

        # BILL AREA        
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=190,width=340,height=340)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        # SCROLL BAR
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        # self is used coz we want scroll-bar throughout the page
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        
        # TOTAL AREA
        F6=LabelFrame(self.root,text="Bill Menu",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=540,relwidth=1,height=150)
        
        t_cosmetics_lbl=Label(F6,text="Total Cosmetics",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=2,sticky="w")
        t_cosmetics_txt=Entry(F6,textvariable=self.cosmetics,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=2)
        
        t_grocery_lbl=Label(F6,text="Total Grocery",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=2,sticky="w")
        t_grocery_txt=Entry(F6,textvariable=self.grocery,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=2)

        t_others_lbl=Label(F6,text="Others Total",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=2,sticky="w")
        t_others_txt=Entry(F6,textvariable=self.others,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=2)
        
        # TAX AREA
        
        tax_cosmetics_lbl=Label(F6,text="Cosmetics Tax",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=10,pady=2,sticky="w")
        tax_cosmetics_txt=Entry(F6,textvariable=self.cosmetics_tax,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=30,pady=2)
        
        tax_grocery_lbl=Label(F6,text="Grocery Tax",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=1,column=2,padx=10,pady=2,sticky="w")
        tax_grocery_txt=Entry(F6,textvariable=self.grocery_tax,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=30,pady=2)

        tax_others_lbl=Label(F6,text="Others Tax",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=2,column=2,padx=10,pady=2,sticky="w")
        tax_others_txt=Entry(F6,textvariable=self.others_tax,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=30,pady=2)
        
        # BUTTON FRAME
        
        btn_F=Frame(F6,bd=7,relief=GROOVE,bg=bg_color)
        btn_F.place(x=670,width=650,height=110  )

        total_btn=Button(btn_F,command=self.total,text="Total",width=8,bd=7,font="arial 12 bold",bg=bg_color,fg="white").grid(row=1,column=0,padx=20,pady=25)
        gen_bill_btn=Button(btn_F,command=lambda:[self.bill_area(),self.insert_data()],text="Generate Bill",width=15,bd=7,font="arial 12 bold",bg=bg_color,fg="white").grid(row=1,column=1,padx=20,pady=25)
        clear_btn=Button(btn_F,command=self.clear_data,text="Clear",width=8,bd=7,font="arial 12 bold",bg=bg_color,fg="white").grid(row=1,column=2,padx=20,pady=25)
        exit_btn=Button(btn_F,command=self.exit_app,text="Exit",width=8,bd=7,font="arial 12 bold",bg=bg_color,fg="white").grid(row=1,column=3,padx=20,pady=25)
        self.bill()
     
    def total(self):
        
        self.soap_total = self.soap.get()*40
        self.face_cream_total = self.face_cream.get()*100
        self.face_wash_total = self.face_wash.get()*150
        self.spray_total = self.spray.get()*200
        self.lotion_total = self.lotion.get()*150
            
        self.total_cosmetics=float(
                                    self.soap_total+
                                    self.face_cream_total+
                                    self.face_wash_total+
                                    self.spray_total+
                                    self.lotion_total                                            
                            )
        self.cosmetics.set("Rs. "+str(self.total_cosmetics))
        self.c_tax = round((self.total_cosmetics*0.05),2)
        self.cosmetics_tax.set("Rs. "+str(self.c_tax))
        
        
        self.rice_total = self.rice.get()*80
        self.oil_total = self.oil.get()*100
        self.daal_total = self.daal.get()*80
        self.wheat_total = self.wheat.get()*200
        self.sugar_total = self.sugar.get()*45
        
        self.total_grocery=float(
                                    self.rice_total+
                                    self.oil_total+
                                    self.daal_total+
                                    self.wheat_total+
                                    self.sugar_total
                            )
        self.grocery.set("Rs. "+str(self.total_grocery))
        self.g_tax = round((self.total_grocery*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))
        
        self.maaza_total = self.maaza.get()*50
        self.coke_total = self.coke.get()*50
        self.frooti_total = self.frooti.get()*50
        self.nimkos_total = self.nimkos.get()*50
        self.biscuit_total = self.biscuit.get()*30
        self.total_others=float(
                                    self.maaza_total+
                                    self.coke_total+
                                    self.frooti_total+
                                    self.nimkos_total+
                                    self.biscuit_total                  
                            )
        self.others.set("Rs. "+str(self.total_others))
        self.o_tax = round((self.total_others*0.1),2)
        self.others_tax.set("Rs. "+str(self.o_tax))

        self.total_bill = float(
                                    self.total_cosmetics+
                                    self.total_grocery+
                                    self.total_others+
                                    self.c_tax+
                                    self.g_tax+
                                    self.o_tax
        )
        self.final_bill = ""
        self.final_bill = str(self.total_bill)
        
    def bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t Welcome to Aashish's Retail \n")
        self.txtarea.insert(END,f"\n Bill No. : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone No. : {self.c_phone.get()}")
        self.txtarea.insert(END,"\n"+"="*37)
        self.txtarea.insert(END,"\n Products\t\tQty\t     Price")
        self.txtarea.insert(END,"\n"+"="*37)
       
        
    def bill_area(self):
        
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error","Please Enter Customer Details")
        
        elif self.total_cosmetics == 0.0 and self.total_grocery == 0.0 and self.total_others == 0.0 :
            messagebox.showerror("Error","Please select some products")
        
        else:
            
            self.bill() 
            # COSMETICS     
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t      {self.soap_total}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t      {self.face_cream_total}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t      {self.face_wash_total}")
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t      {self.spray_total}")
            if self.lotion.get()!=0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t{self.lotion.get()}\t      {self.lotion_total}")
            
            # GROCERIES
            
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t      {self.rice_total}")
            if self.oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.oil.get()}\t      {self.oil_total}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t      {self.daal_total}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t      {self.wheat_total}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t      {self.sugar_total}")
            
            # OTHERS     

            if self.maaza.get()!=0:
                self.txtarea.insert(END,f"\n Maaza\t\t{self.maaza.get()}\t      {self.maaza_total}")
            if self.coke.get()!=0:
                self.txtarea.insert(END,f"\n Coke\t\t{self.coke.get()}\t      {self.coke_total}")
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t      {self.frooti_total}")
            if self.nimkos.get()!=0:
                self.txtarea.insert(END,f"\n Nimkos\t\t{self.nimkos.get()}\t      {self.nimkos_total}")
            if self.biscuit.get()!=0:
                self.txtarea.insert(END,f"\n Biscuit\t\t{self.biscuit.get()}\t      {self.biscuit_total}")
            
            self.txtarea.insert(END,"\n"+"-"*37)        
            if self.cosmetics_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetics Tax \t\t\t  {self.cosmetics_tax.get()}")
            if self.grocery_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END,f"\n Groceries Tax \t\t\t  {self.grocery_tax.get()}")
            if self.others_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END,f"\n Others Tax \t\t\t  {self.others_tax.get()}")
            self.txtarea.insert(END,"\n"+"-"*37)
            self.txtarea.insert(END,f"\n Total Bill \t\t\t  Rs. {self.total_bill}")
            self.txtarea.insert(END,"\n"+"-"*37)
            self.save_bill()
    
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill?")
        if op != 0:
            
            self.bill_data=self.txtarea.get("1.0",END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Your Bill no. : {self.bill_no.get()} Saved Successfully")
        else :
            return
   
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for j in f1:
                    self.txtarea.insert(END,j)
                f1.close()
                present="yes"
        if present=="no" :
            messagebox.showerror("Error","Invalid Bill No.")
   
    def clear_data(self):
         # COSMETICS
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.spray.set(0)
        self.lotion.set(0)
        self.rice.set(0)
        self.oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.maaza.set(0)
        self.coke.set(0)
        self.frooti.set(0)
        self.nimkos.set(0)
        self.biscuit.set(0)
        self.cosmetics.set("")
        self.grocery.set("")
        self.others.set("")
        self.cosmetics_tax.set("")
        self.grocery_tax.set("")
        self.others_tax.set("")
        
        # CUSTOMER 
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.bill()
        
    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to Exit")
        if op != 0:
            self.root.destroy()   
            
    def create_conn(self):
            return mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="billing_system",
            port="3307"
        )
    def insert_data(self):
        if self.c_name.get()=="" or self.c_phone.get()=="" :
            messagebox.showinfo("Insert Status","All Fields are Mandatory")
        else:
            conn=self.create_conn()
            cursor=conn.cursor()
            query="insert into bills(cname,phone,bill_no,total_bill) values(%s,%s,%s,%s)"
            args=(self.c_name.get(),self.c_phone.get(),self.bill_no.get(),self.final_bill)
            cursor.execute(query,args)
            conn.commit()
            conn.close()
            messagebox.showinfo("Insert Status","Data Inserted Successfully")

            #e_fname.delete(0,'end')
            #e_lname.delete(0,'end')
            #e_email.delete(0,'end')
            #e_mobile.delete(0,'end')           

            
               
root=Tk()
obj= Bill_App(root)
root.mainloop()
>>>>>>> f7b24bcbe34d565b8f5e12538a695113d02f4968
