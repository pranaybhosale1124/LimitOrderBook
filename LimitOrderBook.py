"""
Limit Order: Stand in a queue
Market Order: Buy shares at any Price

In Below Program Provide methods in OrderBook are:
      PlaceOrder(TypeOfOrder, Price, Size ) ->is for placing Limit Order
      MarketOrder(TypeofOrder, Size) -> is for placing Market order
      ** deleteOrder(TypeOfOrder, Price, Size ) ->   is for Deleting Limit Order only
                                                                                    and not for Market Order
      show() -> to print Top 5 entries in OrderBook
      checkBid() -> is to check possible sharing of Securities
                                    this function is called every time a new entry is inserted
entries are sorted according to 1. the Bid Price(Highest first/descending) and Sell Price(Lowest First/ Ascending)
                                                          2. time of arrival (First In First Served)
                                    
5 sample entries are inserted already , user can use simple GUI Provided to add/ remove entries
      
Kindly inform any changes/requirements/additions/mistakes on pranaybhosale1124@gmail.com

"""

from tkinter import *
import tkinter as tk
"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""   
class SellNode:
      def __init__(self,data,Size):#data=Price
            self.data=data
            self.Size=Size
            self.Next=None
class BuyNode:
      def __init__(self,data,Size):#data=Price
            self.data=data
            self.Size=Size
            self.Next=None
            
############################################################  
class OrderBook:
      def __init__(self):
            self.Sellhead=None
            self.Buyhead=None
      """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""     
      def PlaceOrder(self,Type,Price,Size):
            if Type=="Sell":
                  newnode=SellNode(Price,Size)
                  if self.Sellhead==None:
                        self.Sellhead=newnode
                  else:
                        if Price<self.Sellhead.data:
                              temp=self.Sellhead
                              self.Sellhead=newnode
                              newnode.Next=temp
                        else:
                              current=self.Sellhead
                              prev=None
                              while current.Next!=None:
                                    if Price<current.data:
                                          break
                                    else:
                                          prev=current
                                          current=current.Next
                              #print(prev.data, current.data)
                              if current.Next==None:
                                    current.Next=newnode
                              else:
                                    temp=current
                                    prev.Next=newnode
                                    newnode.Next=temp
            elif Type=="Buy":
                  newnode=BuyNode(Price,Size)
                  if self.Buyhead==None:
                        self.Buyhead=newnode
                  else:
                        if Price>self.Buyhead.data:
                              temp=self.Buyhead
                              self.Buyhead=newnode
                              newnode.Next=temp
                        else:
                              current=self.Buyhead
                              prev=None
                              while current.Next:
                                    if Price>current.data:
                                          break
                                    else:
                                          prev=current
                                          current=current.Next
                              if current.Next==None:
                                    current.Next=newnode
                              else:
                                    temp=current
                                    prev.Next=newnode
                                    newnode.Next=current
            if self.Buyhead and self.Sellhead:
                  self.CheckBid()
      """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" 
      def MarketOrder(self,Type,Size):
            if Type=="Buy":
                  current=self.Sellhead
                  if Size<current.Size:
                        current.Size=current.Size-Size
                  elif Size==current.Size:
                        self.Sellhead=current.Next
                  elif Size>current.Size:
                        Size=Size-current.Size
                        self.Sellhead=current.Next
                        self.MarketOrder("Buy",Size)
            elif Type=="Sell":
                  current=self.Buyhead
                  if Size<current.Size:
                        current.Size=current.Size-Size
                  elif Size==current.Size:
                        self.Buyhead=current.Next
                  elif Size>current.Size:
                        Size=Size-current.Size
                        self.Buyhead=current.Next
                        self.MarketOrder("Sell",Size)
      
      """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""      
      def DeleteOrder(self,Type,Price,Size):
            if Type=="Sell":
                  if self.Sellhead.data==Price and self.Sellhead.Size==Size:
                        self.Sellhead=self.Sellhead.Next
                        return
                  current=self.Sellhead
                  prev=None
                  while current.Next:
                              if current.data==Price and current.Size==Size:
                                    prev.Next=current.Next
                                    return
                              prev =current
                              current=current.Next
                  else:
                        print("Not Found")
            elif Type=="Buy":
                  if self.Buyhead.data==Price and self.Buyhead.Size==Size:
                        self.Buyhead=self.Buyhead.Next
                        return
                  current=self.Buyhead
                  prev=None
                  while current.Next:
                              if current.data==Price and current.Size==Size:
                                    prev.Next=current.Next
                                    return
                              prev =current
                              current=current.Next
                  else:
                        print("Not Found")
                                    
      """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" 
      def show(self):
            if self.Buyhead or self.Sellhead:
                  current1=self.Buyhead
                  current2=self.Sellhead
                  print("          Bid Size","      ","         Bid Price","         ","           Ask Price","      ","        Ask Size")
                  for i in range(0,5):
                              if current1 and current2:
                                    print(("  "*(10-len(str(current1.Size))))+str(current1.Size),"          ",
                                                ("  "*(10-len(str(current1.data))))+str(current1.data),"                    ",
                                                ("  "*(10-len(str(current2.data))))+str(current2.data),"          ",
                                                ("  "*(10-len(str(current2.Size))))+str(current2.Size))
                                    current1=current1.Next
                                    current2=current2.Next
                              elif current1 and current2==None:
                                    print(("  "*(10-len(str(current1.Size))))+str(current1.Size),"          ",
                                                ("   "*(10-len(str(current1.data))))+str(current1.data),"               ",
                                                "---------","          ","---------")
                                    current1=current1.Next
                                    #current2=current2.Next
                              elif current1==None and current2:
                                    print("--------","          ","--------","                   ",
                                          ("  "*(10-len(str(current2.data))))+str(current2.data),"          ",
                                          ("  "*(10-len(str(current2.Size))))+str(current2.Size))
                                    current2=current2.Next
      """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" 
      def CheckBid(self):
            return self.Check(self.Buyhead,self.Sellhead)
      def Check(self,Buyer,Seller):
            if Buyer.data>=Seller.data:
                  #less demand(Size):
                  if Buyer.Size<Seller.Size:
                        Seller.Size=Seller.Size-Buyer.Size
                        self.Buyhead=self.Buyhead.Next
                  #equal demand:(Size)
                  elif Buyer.Size==Seller.Size:
                        self.Sellhead=self.Sellhead.Next
                        self.Buyhead=self.Buyhead.Next     
                  #more demand
                  elif Buyer.Size>Seller.Size:
                        Buyer.Size=Buyer.Size-Seller.Size
                        self.Sellhead=self.Sellhead.Next
                        if Buyer.data>=Seller.data:
                              self.CheckBid()
                  print('Yes')
"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" 
a1=OrderBook()
a1.PlaceOrder("Sell",11.42,900)
a1.PlaceOrder("Sell",11.41,1400)
a1.PlaceOrder("Sell",11.38,400)
a1.PlaceOrder("Sell",11.40,1250)
a1.PlaceOrder("Sell",11.39,1600)

a1.PlaceOrder("Buy", 11.36,2700)
a1.PlaceOrder("Buy", 11.34,1100)
a1.PlaceOrder("Buy", 11.32,700)
a1.PlaceOrder("Buy", 11.35,1100)
a1.PlaceOrder("Buy", 11.33,1600)
#a1.MarketOrder("Sell",2800)
#a1.PlaceOrder("Sell",11.38,300)
a1.show()

"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""  
win=tk.Tk()
win.title('Limit Order Book')     
win.geometry('500x150')
win.resizable(width=False, height=False)

Typeof=tk.StringVar()
Priceof=tk.StringVar()
Sizeof=tk.IntVar()

labelType= tk.Label(win, text="TYPE(Sell/Buy)").grid(row=1, column=1)
labelPrice = tk.Label(win, text="Limit Price").grid(row=1, column=2)
labelSize= tk.Label(win, text="No. of Shares").grid(row=1, column=3)
label1= tk.Label(win, text="Select Buy/ Sell").grid(row=3, column=1)
#label2= tk.Label(win, text="Please Select At least/Only One option:").grid(row=5, column=3)
TypeBuy=Checkbutton(win, text = "Buy", variable = Typeof, onvalue = "Buy",offvalue="Sell").grid(row=4, column=1)
TypeSell=Checkbutton(win, text = "Sell", variable = Typeof, onvalue = "Sell",offvalue="Buy").grid(row=5, column=1)
Type=tk.Entry(win, textvariable=Typeof).grid(row=2, column=1)
Price=tk.Entry(win, textvariable=Priceof).grid(row=2, column=2)
Size=tk.Entry(win, textvariable=Sizeof).grid(row=2, column=3)

def ExecuteLimit():
      if Typeof.get()=="Sell" or Typeof.get()=="Buy":
            if  Sizeof.get()>0 and float(Priceof.get())>1:
                  a1.PlaceOrder(Typeof.get(),float(Priceof.get()),Sizeof.get())
                  a1.show()
                  print()
            else:
                  print("price and Size must be greater than Zero")            
      else:
            print("Please Select Buy or Sell")
def ExecuteMarket():
      if Typeof.get()=="Sell" or Typeof.get()=="Buy":
            if  Sizeof.get()>0 and (Priceof.get()):
                  a1.MarketOrder(Typeof.get(),Sizeof.get())
                  a1.show()
                  print()
            else:
                  print("price and Size must be greater than Zero")
      else:
            print("Please Select Buy or Sell")
def DeleteOrder():
      a1.DeleteOrder(Typeof.get(),int(Priceof.get()),Sizeof.get())
      a1.show()
      print()

Limit_order=Button(win, text = "  Limit Order",command=ExecuteLimit).grid(row=2, column=4)
Market_Order=Button(win, text = "Market Order",command=ExecuteMarket).grid(row=4, column=4)
delete_order=Button(win, text = "Delete Order",command=DeleteOrder).grid(row=6, column=4)
win.mainloop()



                              
