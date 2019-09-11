class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    def enque(self,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            newnode=Node(value)
            newnode.next=self.head
            self.head=newnode

    def deque(self):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while(temp.next is not None):
                prev = temp
                temp = prev.next
            self.tail=prev
            self.tail.next=None

    def search(self,key):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while(temp.data is not key):
                if(temp.next is not None):
                    temp=temp.next
                else:
                    print("Value is not found in the list")
                    break
            else:
                print("Value is found")
            temp=None

    def update(self,newv):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while(temp.next is not None):
                temp=temp.next
            temp.data=newv

    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next

s=Queue()
while(True):
    
    print("1. Enque   2. Deque    3. Search   4. Update   5. Display  6. Exit")
    ch=int(input("Enter your choice : "))
    if ch==1:
        print("Enter value to be enqued")
        val=input()
        s.enque(val)
    elif ch==2:
        s.deque()
    elif ch==3:
        print("Enter value to be searched")
        val=input()
        s.search(val)
    elif ch==4:
        print("Enter the new value")
        val1=input()
        s.update(val1)
    elif ch==5:
        s.display()
    elif ch==6:
        exit()
    else:
        print("Invalid input")
