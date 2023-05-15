from tkinter import *
class Bill_App:
    def __init__(self,root):
        self.root=root
        #"0" and "0" specifies the position from x and y-axis respectively
        self.root.geometry("1350x700+0+0")
        # TITLE PART
        self.root.title("Biiling System")
        bg_color="#074463" # Code for Dark Blue color
        title=Label(self.root,text="Billing System",font=("time new roman",30,"bold"),pady=0,bd=12,relief=GROOVE,bg=bg_color,fg="white").pack(fill=X)
        # CUSTOMER DETAILS FRAME
        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_label=Label(F1,text="Customer Name",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=20,pady=5)
        cname_text=Entry(F1,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphone_label=Label(F1,text="Phone No.",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=3,padx=20,pady=5)
        cphone_text=Entry(F1,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=4,pady=5,padx=10)

        c_bill_label=Label(F1,text="Bill No.",font=("times new roman",18,"bold"),bg=bg_color,fg="white").grid(row=0,column=5,padx=20,pady=5)
        c_bill_text=Entry(F1,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=6,pady=5,padx=10)

        entry_btn=Button(F1,text="Enter",width=10,bd=7,font="arial 12 bold",bg=bg_color,fg="white").grid(row=0,column=7,padx=40,pady=10)
        
        # COSMETICS FRAME
        F2=LabelFrame(self.root,text="Cosmetics",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=190,width=325,height=340)

        
        soap_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        soap_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=30,pady=10)

        f_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        f_cream_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=30,pady=10)

        f_wash_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        f_wash_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=30,pady=10)

        spray_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        spray_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=30,pady=10)

        lotion_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        lotion_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=30,pady=10)

        # GROCERY FRAME
        F3=LabelFrame(self.root,text="Grocery",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=190,width=325,height=340)

        
        rice_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=60,pady=10)

        oil_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        oil_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=60,pady=10)

        daal_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        daal_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=60,pady=10)

        wheat_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        wheat_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=60,pady=10)

        sugar_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        sugar_txt=Entry(F3,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=60,pady=10)

        # OTHERS FRAME
        F4=LabelFrame(self.root,text="Others",bd=10,relief=GROOVE,font=("time new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=190,width=325,height=340)

        
        maza_lbl=Label(F4,text="Maaza",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        maza_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=60,pady=10)

        coke_lbl=Label(F4,text="Coke",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        coke_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=60,pady=10)

        frooti_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        frooti_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=60,pady=10)

        nimkos_lbl=Label(F4,text="Nimkos",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        nimkos_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=60,pady=10)

        biscuits_lbl=Label(F4,text="Biscuits",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        biscuits_txt=Entry(F4,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=60,pady=10)

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
        t_cosmetics_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=2)
        
        t_grocery_lbl=Label(F6,text="Total Grocery",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=2,sticky="w")
        t_grocery_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=2)

        t_others_lbl=Label(F6,text="Others Total",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=2,sticky="w")
        t_others_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=2)
        
        # TAX AREA
        
        tax_cosmetics_lbl=Label(F6,text="Cosmetics Tax",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=10,pady=2,sticky="w")
        tax_cosmetics_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=30,pady=2)
        
        tax_grocery_lbl=Label(F6,text="Grocery Tax",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=1,column=2,padx=10,pady=2,sticky="w")
        tax_grocery_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=30,pady=2)

        tax_others_lbl=Label(F6,text="Others Tax",font=("times new roman",15,"bold"),bg=bg_color,fg="white").grid(row=2,column=2,padx=10,pady=2,sticky="w")
        tax_others_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=30,pady=2)
        
        # BUTTON FRAME
        
        btn_F=Frame(F6,bd=7,relief=GROOVE,bg=bg_color)
        btn_F.place(x=670,width=650,height=110  )

        total_btn=Button(btn_F,text="Total",width=8,bd=7,font="arial 12 bold",bg=bg_color,fg="white").grid(row=1,column=0,padx=20,pady=25)
        gen_bill_btn=Button(btn_F,text="Generate Bill",width=15,bd=7,font="arial 12 bold",bg=bg_color,fg="white").grid(row=1,column=1,padx=20,pady=25)
        clear_btn=Button(btn_F,text="Clear",width=8,bd=7,font="arial 12 bold",bg=bg_color,fg="white").grid(row=1,column=2,padx=20,pady=25)
        exit_btn=Button(btn_F,text="Exit",width=8,bd=7,font="arial 12 bold",bg=bg_color,fg="white").grid(row=1,column=3,padx=20,pady=25)
        
root=Tk()
obj= Bill_App(root)
root.mainloop()
