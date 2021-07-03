def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Products", bg="darkblue", fg="white", bd=5)
    lblrestaurant.grid(row=0, column=0)
    lblrestaurant = Label(roo, font=('aria', 15,'bold'), text="_____", fg="white", anchor=W)
    lblrestaurant.grid(row=0, column=2)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="PRICE",bg="darkblue", fg="white", anchor=W)
    lblrestaurant.grid(row=0, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Adobong manok", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="50", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Lechon Baboy", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="60", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Sinigang na Hipon", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="250", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="kari-Kari", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="50", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Isdang Paksiw", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="75", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="45", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=3)
 
    roo.mainloop()

#Complete Source Code of Restaurant Management System Project in Python
from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")

Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Restaurant Management System",bg="darkblue",fg="white",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="black",anchor=W)
lblinfo.grid(row=1,column=0)

#---------------Calculator------------------
text_Input=StringVar()
operator =""

txtdisplay = Entry(f2,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="white",justify='right')
txtdisplay.grid(columnspan=4)

def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator=""
    text_Input.set("")

def eqals():
    global operator
    sumup=str(eval(operator))

    text_Input.set(sumup)
    operator = ""

def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    ado.set(randomRef)

    adobo =float(adobongmanok.get())
    adobongbaboy= float(lechonbaboys.get())
    hipon= float(siniganghipon.get())
    karikari= float(paksiws.get())
    paksiw= float(karikaris.get())
    drinkwine= float(mountaindew.get())

    adoboprice = adobo*50
    adobongbaboyprice = adobongbaboy*60
    hiponprice = hipon*250
    karikariprice = karikari*50
    paksiwprice = paksiw*75
    drinksprice = drinkwine*45

    dinnercost = "P",str('%.2f'% (adoboprice +  adobongbaboyprice + hiponprice + karikariprice + paksiwprice + drinksprice))
    PayTax=((adoboprice +  adobongbaboyprice + hiponprice + karikariprice +  paksiwprice + drinksprice)*0.33)
    Totalcost=(adoboprice +  adobongbaboyprice + hiponprice + karikariprice  + paksiwprice + drinksprice)
    Ser_Charge=((adoboprice +  adobongbaboyprice + hiponprice + karikariprice + paksiwprice + drinksprice)/99)
    Service="P",str('%.2f'% Ser_Charge)
    OverAllCost="P",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="P",str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(dinnercost)
    Tax.set(PaidTax)
    Subtotal.set(dinnercost)
    Total.set(OverAllCost)


def qexit():
    root.destroy()

def reset():
    ado.set("")
    adobongmanok.set("")
    lechonbaboys.set("")
    siniganghipon.set("")
    paksiws.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    mountaindew.set("")
    Tax.set("")
    cost.set("")
    karikaris.set("")


btn7=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="7",bg="black", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="8",bg="black", command=lambda: btnclick(8) )
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="9",bg="black", command=lambda: btnclick(9) )
btn9.grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="+",bg="black", command=lambda: btnclick("+") )
Addition.grid(row=2,column=3)
#---------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="4",bg="black", command=lambda: btnclick(4) )
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="5",bg="black", command=lambda: btnclick(5) )
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="6",bg="black", command=lambda: btnclick(6) )
btn6.grid(row=3,column=2)

Substraction=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="-",bg="black", command=lambda: btnclick("-") )
Substraction.grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="1",bg="black", command=lambda: btnclick(1) )
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="2",bg="black", command=lambda: btnclick(2) )
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="3",bg="black", command=lambda: btnclick(3) )
btn3.grid(row=4,column=2)

multiply=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="",bg="black", command=lambda: btnclick("") )
multiply.grid(row=4,column=3)
#------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="0",bg="black", command=lambda: btnclick(0) )
btn0.grid(row=5,column=0)

btnc=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="c",bg="black", command=clrdisplay)
btnc.grid(row=5,column=1)

btnequal=Button(f2,padx=16,pady=16,bd=4,width = 16, fg="red", font=('ariel', 20 ,'bold'),text="=",bg="black",command=eqals)
btnequal.grid(columnspan=4)

Decimal=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text=".",bg="black", command=lambda: btnclick(".") )
Decimal.grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="/",bg="black", command=lambda: btnclick("/") )
Division.grid(row=5,column=3)
status = Label(f2,font=('aria', 15, 'bold'),width = 20, text="By Madhumita & Deepti",bd=5,relief=SUNKEN)
status.grid(row=7,columnspan=3)

#---------------------------------------------------------------------------------------
ado = StringVar()
adobongmanok = StringVar()
lechonbaboys = StringVar()
siniganghipon = StringVar()
paksiws = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
mountaindew = StringVar()
Tax = StringVar()
cost = StringVar()
karikaris = StringVar()


lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="red",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1, font=('ariel' ,16,'bold'), textvariable=ado, bd=6, insertwidth=4, bg="white", justify='right')
txtreference.grid(row=0,column=1)

lblmanok = Label(f1, font=('aria' , 16, 'bold'), text="Adobong Manok", fg="green", bd=10, anchor='w')
lblmanok.grid(row=1, column=0)
txtmanok = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=adobongmanok, bd=6, insertwidth=4, bg="white", justify='right')
txtmanok.grid(row=1, column=1)

lblbaboy = Label(f1, font=('aria' , 16, 'bold'), text="Letchon Baboy", fg="green", bd=10, anchor='w')
lblbaboy.grid(row=2, column=0)
txtbaboy = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=lechonbaboys, bd=6, insertwidth=4, bg="white", justify='right')
txtbaboy.grid(row=2, column=1)


lblhipon = Label(f1, font=('aria' , 16, 'bold'), text="Sinigang na Hipon", fg="green", bd=10, anchor='w')
lblhipon.grid(row=3, column=0)
txthipon = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=siniganghipon, bd=6, insertwidth=4, bg="white", justify='right')
txthipon.grid(row=3, column=1)

lblkarikari = Label(f1, font=('aria' , 16, 'bold'), text="Kari-Kari", fg="green", bd=10, anchor='w')
lblkarikari.grid(row=4, column=0)
txtkarikari = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=paksiws, bd=6, insertwidth=4, bg="white", justify='right')
txtkarikari.grid(row=4, column=1)

lblpaksiw = Label(f1, font=('aria' , 16, 'bold'), text="Isdang Paksiw", fg="green", bd=10, anchor='w')
lblpaksiw.grid(row=5, column=0)
txtpaksiw = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=karikaris, bd=6, insertwidth=4, bg="white", justify='right')
txtpaksiw.grid(row=5, column=1)

#--------------------------------------------------------------------------------------
lblmountaindew = Label(f1, font=('aria' , 16, 'bold'), text="Drinks", fg="green", bd=10, anchor='w')
lblmountaindew.grid(row=0, column=2)
txtmountaindew = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=mountaindew, bd=6, insertwidth=4, bg="white", justify='right')
txtmountaindew.grid(row=0, column=3)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="cost",fg="red",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="white" ,justify='right')
txtcost.grid(row=1,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="red",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="white" ,justify='right')
txtService_Charge.grid(row=2,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="red",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="white" ,justify='right')
txtTax.grid(row=3,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="red",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="white" ,justify='right')
txtSubtotal.grid(row=4,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="red",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="white" ,justify='right')
txtTotal.grid(row=5,column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="blue",command=Ref)
btnTotal.grid(row=7, column=1)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="green",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="red",command=qexit)
btnexit.grid(row=7, column=3)

def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Products", bg="darkblue", fg="white", bd=5)
    lblrestaurant.grid(row=0, column=0)
    lblrestaurant = Label(roo, font=('aria', 15,'bold'), text="_____", fg="white", anchor=W)
    lblrestaurant.grid(row=0, column=2)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="PRICE",bg="darkblue", fg="white", anchor=W)
    lblrestaurant.grid(row=0, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Adobong manok", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="50", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Lechon Baboy", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="60", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Sinigang na Hipon", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="250", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="kari-Kari", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="50", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Isdang Paksiw", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="75", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="45", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=3)

    roo.mainloop()

btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="green",command=price)
btnprice.grid(row=7, column=0)

root.mainloop()
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
from tkinter import*
import random
import time
 
root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")
 
Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)
 
f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
 
f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Restaurant Management System",bg="darkblue",fg="white",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="black",anchor=W)
lblinfo.grid(row=1,column=0)
 
#---------------Calculator------------------
text_Input=StringVar()
operator =""
 
txtdisplay = Entry(f2,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="white",justify='right')
txtdisplay.grid(columnspan=4)
 
def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)
 
def clrdisplay():
    global operator
    operator=""
    text_Input.set("")
 
def eqals():
    global operator
    sumup=str(eval(operator))
 
    text_Input.set(sumup)
    operator = ""
 
def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    ado.set(randomRef)
 
    adobo =float(adobongmanok.get())
    adobongbaboy= float(lechonbaboys.get())
    hipon= float(siniganghipon.get())
    karikari= float(paksiws.get())
    paksiw= float(karikaris.get())
    drinkwine= float(mountaindew.get())
 
    adoboprice = adobo*50
    adobongbaboyprice = adobongbaboy*60
    hiponprice = hipon*250
    karikariprice = karikari*50
    paksiwprice = paksiw*75
    drinksprice = drinkwine*45
 
    dinnercost = "P",str('%.2f'% (adoboprice +  adobongbaboyprice + hiponprice + karikariprice + paksiwprice + drinksprice))
    PayTax=((adoboprice +  adobongbaboyprice + hiponprice + karikariprice +  paksiwprice + drinksprice)*0.33)
    Totalcost=(adoboprice +  adobongbaboyprice + hiponprice + karikariprice  + paksiwprice + drinksprice)
    Ser_Charge=((adoboprice +  adobongbaboyprice + hiponprice + karikariprice + paksiwprice + drinksprice)/99)
    Service="P",str('%.2f'% Ser_Charge)
    OverAllCost="P",str( PayTax + Totalcost + Ser_Charge)
    PaidTax="P",str('%.2f'% PayTax)
 
    Service_Charge.set(Service)
    cost.set(dinnercost)
    Tax.set(PaidTax)
    Subtotal.set(dinnercost)
    Total.set(OverAllCost)
 
 
def qexit():
    root.destroy()
 
def reset():
    ado.set("")
    adobongmanok.set("")
    lechonbaboys.set("")
    siniganghipon.set("")
    paksiws.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    mountaindew.set("")
    Tax.set("")
    cost.set("")
    karikaris.set("")
 
 
btn7=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="7",bg="black", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0)
 
btn8=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="8",bg="black", command=lambda: btnclick(8) )
btn8.grid(row=2,column=1)
 
btn9=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="9",bg="black", command=lambda: btnclick(9) )
btn9.grid(row=2,column=2)
 
Addition=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="+",bg="black", command=lambda: btnclick("+") )
Addition.grid(row=2,column=3)
#---------------------------------------------------------------------------------------------
btn4=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="4",bg="black", command=lambda: btnclick(4) )
btn4.grid(row=3,column=0)
 
btn5=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="5",bg="black", command=lambda: btnclick(5) )
btn5.grid(row=3,column=1)
 
btn6=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="6",bg="black", command=lambda: btnclick(6) )
btn6.grid(row=3,column=2)
 
Substraction=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="-",bg="black", command=lambda: btnclick("-") )
Substraction.grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------
btn1=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="1",bg="black", command=lambda: btnclick(1) )
btn1.grid(row=4,column=0)
 
btn2=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="2",bg="black", command=lambda: btnclick(2) )
btn2.grid(row=4,column=1)
 
btn3=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="3",bg="black", command=lambda: btnclick(3) )
btn3.grid(row=4,column=2)
 
multiply=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="",bg="black", command=lambda: btnclick("") )
multiply.grid(row=4,column=3)
#------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="0",bg="black", command=lambda: btnclick(0) )
btn0.grid(row=5,column=0)
 
btnc=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="c",bg="black", command=clrdisplay)
btnc.grid(row=5,column=1)
 
btnequal=Button(f2,padx=16,pady=16,bd=4,width = 16, fg="red", font=('ariel', 20 ,'bold'),text="=",bg="black",command=eqals)
btnequal.grid(columnspan=4)
 
Decimal=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text=".",bg="black", command=lambda: btnclick(".") )
Decimal.grid(row=5,column=2)
 
Division=Button(f2,padx=16,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="/",bg="black", command=lambda: btnclick("/") )
Division.grid(row=5,column=3)
status = Label(f2,font=('aria', 15, 'bold'),width = 16, text="By itsourcecode.com",bd=2,relief=SUNKEN)
status.grid(row=7,columnspan=3)
 
#---------------------------------------------------------------------------------------
ado = StringVar()
adobongmanok = StringVar()
lechonbaboys = StringVar()
siniganghipon = StringVar()
paksiws = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
mountaindew = StringVar()
Tax = StringVar()
cost = StringVar()
karikaris = StringVar()
 
 
lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="red",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1, font=('ariel' ,16,'bold'), textvariable=ado, bd=6, insertwidth=4, bg="white", justify='right')
txtreference.grid(row=0,column=1)
 
lblmanok = Label(f1, font=('aria' , 16, 'bold'), text="Adobong Manok", fg="green", bd=10, anchor='w')
lblmanok.grid(row=1, column=0)
txtmanok = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=adobongmanok, bd=6, insertwidth=4, bg="white", justify='right')
txtmanok.grid(row=1, column=1)
 
lblbaboy = Label(f1, font=('aria' , 16, 'bold'), text="Letchon Baboy", fg="green", bd=10, anchor='w')
lblbaboy.grid(row=2, column=0)
txtbaboy = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=lechonbaboys, bd=6, insertwidth=4, bg="white", justify='right')
txtbaboy.grid(row=2, column=1)
 
 
lblhipon = Label(f1, font=('aria' , 16, 'bold'), text="Sinigang na Hipon", fg="green", bd=10, anchor='w')
lblhipon.grid(row=3, column=0)
txthipon = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=siniganghipon, bd=6, insertwidth=4, bg="white", justify='right')
txthipon.grid(row=3, column=1)
 
lblkarikari = Label(f1, font=('aria' , 16, 'bold'), text="Kari-Kari", fg="green", bd=10, anchor='w')
lblkarikari.grid(row=4, column=0)
txtkarikari = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=paksiws, bd=6, insertwidth=4, bg="white", justify='right')
txtkarikari.grid(row=4, column=1)
 
lblpaksiw = Label(f1, font=('aria' , 16, 'bold'), text="Isdang Paksiw", fg="green", bd=10, anchor='w')
lblpaksiw.grid(row=5, column=0)
txtpaksiw = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=karikaris, bd=6, insertwidth=4, bg="white", justify='right')
txtpaksiw.grid(row=5, column=1)
 
#--------------------------------------------------------------------------------------
lblmountaindew = Label(f1, font=('aria' , 16, 'bold'), text="Drinks", fg="green", bd=10, anchor='w')
lblmountaindew.grid(row=0, column=2)
txtmountaindew = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=mountaindew, bd=6, insertwidth=4, bg="white", justify='right')
txtmountaindew.grid(row=0, column=3)
 
lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="cost",fg="red",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="white" ,justify='right')
txtcost.grid(row=1,column=3)
 
lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="red",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="white" ,justify='right')
txtService_Charge.grid(row=2,column=3)
 
lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="red",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="white" ,justify='right')
txtTax.grid(row=3,column=3)
 
lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="red",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="white" ,justify='right')
txtSubtotal.grid(row=4,column=3)
 
lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="red",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="white" ,justify='right')
txtTotal.grid(row=5,column=3)
 
#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)
 
btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="blue",command=Ref)
btnTotal.grid(row=7, column=1)
 
btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="green",command=reset)
btnreset.grid(row=7, column=2)
 
btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="red",command=qexit)
btnexit.grid(row=7, column=3)
 
def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Products", bg="darkblue", fg="white", bd=5)
    lblrestaurant.grid(row=0, column=0)
    lblrestaurant = Label(roo, font=('aria', 15,'bold'), text="_____", fg="white", anchor=W)
    lblrestaurant.grid(row=0, column=2)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="PRICE",bg="darkblue", fg="white", anchor=W)
    lblrestaurant.grid(row=0, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Adobong manok", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="50", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Lechon Baboy", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="60", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Sinigang na Hipon", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="250", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="kari-Kari", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="50", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Isdang Paksiw", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="75", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="45", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=3)
 
    roo.mainloop()
 
btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="green",command=price)
btnprice.grid(row=7, column=0)
 
root.mainloop()

