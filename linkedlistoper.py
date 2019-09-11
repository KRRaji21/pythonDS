class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbeg(self,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            newnode=Node(value)
            newnode.next=self.head
            self.head=newnode
    def insertatend(self,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            newnode=Node(value)
            self.tail.next=newnode
            self.tail=newnode
    def insertatpos(self,position,value):
        temp=self.head
        for i in range(1,position-1):
            temp=temp.next
        newnode=Node(value)
        newnode.next=temp.next
        temp.next=newnode
        temp=None
        
    def display(self):
        count=0
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next
            count+=1
        print("The whole list is : ",count)
        
    def deletepos(self,position):
        if(self.head==None):
            print("List is empty")
        else:
            count=0
            temp=self.head
            while(temp.data is not position):
                count=count+1
                if(temp.next is not None):
                    prev = temp
                    temp = prev.next
                else:
                    print("Value is not found in the list")
                    break  
            if(count is not 0):
                prev.next=temp.next
            else:
                print("You are trying to delete the first value in the list")
            
            temp=None
            prev=None
    def deletebeg(self):
        temp = self.head 
        if(temp is not None): 
          #  if (temp.data == key): 
            self.head = temp.next
            temp = None
            return
    def deleteend(self):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while(temp.next is not None):
                prev = temp
                temp = prev.next
            self.tail=prev
            self.tail.next=None

    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next
    def update(self,old,newval):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while(temp.data is not old):
                if(temp.next is not None):
                    temp=temp.next
                else:
                    print("Value is not found in the list")
                    break
            else:
                temp.data=newval
            temp=None
    def search(self,key):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while(temp.data is not key):
                if(temp.next is not None):
                    prev = temp
                    temp = prev.next
                else:
                    print("Value is not found in the list")
                    break
            else:
                print("Value is found")
            temp=None


s=SLL()
while(1):
    print("1.Insert   2.Delete    3.Update     4.Search    5.Display    6.Exit")
    ch=int(input("Enter your choice : "))
    if ch==1:
        print("1.beginning  2.end  3.anyposition")
        choice=int(input("Enter your position choice : "))
        if choice==1:
            print("Enter the data to insert : ")
            data=input()
            s.insertatbeg(data)
        elif choice==2:
            print("Enter the data to insert : ")
            data=input()
            s.insertatend(data)
        else:
            print("Enter the data to insert : ")
            data=input()
            print("Enter the position to insert")
            posi=int(input())
            s.insertatpos(posi,data)
    if ch==5:
        s.display()
    if ch==3:
        print("Enter the data which you want update : ")
        old=input()
        print("Enter the new value")
        newval=input()
        s.update(old,newval)
    if ch==2:
        print("1.beginning  2.end  3.anyposition")
        choice=int(input("Enter your position choice : "))
        if choice==1:
            s.deletebeg()
        elif choice==2:
            s.deleteend()
        else:
            print("Enter the data to delete : ")
            data=input()
            s.deletepos(data)
    if ch==4:
        print("Enter the data which you want search : ")
        seek=input()
        s.search(seek)


    

    



            
