class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
    def insert(self,value):
        if(self.top==None):
            self.top=self.tail=Node(value)
        else:
            newnode=Node(value)
            newnode.next=self.top
            self.top=newnode

    def delete(self):
        if(self.top==None):
            print("List is empty")
        else:
            temp=self.top
            self.top=temp.next
            temp=None

    def end(self):
        if(self.top==None):
            print("List is empty")
        else:
            temp=self.top
            print("Top pointer points to the value:")
            print(temp.data)

    def display(self):
        temp=self.top
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next

s=Stack()
while(True):
    
    print("1. Push  2. Pop  3. Peek  4. Display  5. Exit")
    ch=int(input("Enter your Choice : "))
    if ch==1:
        print("Enter value to be pushed : ")
        val=input()
        s.insert(val)
    elif ch==2:
        s.delete()
    elif ch==3:
        s.end()
    elif ch==4:
        s.display()
    elif ch==5:
        exit()
    else:
        print("Invalid input")
