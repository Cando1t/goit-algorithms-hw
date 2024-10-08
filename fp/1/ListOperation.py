# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X0sw2GZq00Zeww935UPOfY7Yr5AyLSVd
"""

class Node:
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None

    def insert(self, data):
      newNode = Node(data)
      if(self.head):
        current = self.head
        while(current.next):
          current = current.next
        current.next = newNode
      else:
        self.head = newNode


    def insertAtBeg(self, data):
        newNode = Node(data)
        if self.head == None:
           self.head = newNode
           return
        temp = self.head
        self.head = newNode
        self.head.next = temp

    # Вставити в початок
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Вставити в кінець
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    # UДрукувати
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data,end=" ")
            temp = temp.next

    # реверс
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def sortedMerge(self, a, b):
        result = None

        # Base cases
        if a == None:
            return b
        if b == None:
            return a

        # pick either a or b and recur..
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result

    def mergeSort(self, h):

        # Base case if head is None
        if h == None or h.next == None:
            return h

        # get the middle of the list
        middle = self.getMiddle(h)
        nexttomiddle = middle.next

        # set the next of middle node to None
        middle.next = None

        # Apply mergeSort on left list
        left = self.mergeSort(h)

        # Apply mergeSort on right list
        right = self.mergeSort(nexttomiddle)

        # Merge the left and right lists
        sortedlist = self.sortedMerge(left, right)
        return sortedlist

    def getMiddle(self, head):
        if (head == None):
            return head

        slow = head
        fast = head

        while (fast.next != None and
                fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow

def mergeTwoLinkList(list1: LinkedList, list2: LinkedList):

    mergeList = LinkedList()
    if list1 is None:
        mergeList = list2

    if list2 is None:
        mergeList = list1

    if list1 is not None and list2 is not None:
        list1_current_loc = list1.head
        list2_current_loc = list2.head

        while True:
            if list1_current_loc is None or list2_current_loc is None:
                break
            if list1_current_loc.data <= list2_current_loc.data:
                mergeList.insertAtBeg(list1_current_loc.data)
                list1_current_loc = list1_current_loc.next
            else:
                mergeList.insertAtBeg(list2_current_loc.data)
                list2_current_loc = list2_current_loc.next

    while list1_current_loc is not None:
        mergeList.insertAtBeg(list1_current_loc.data)
        list1_current_loc = list1_current_loc.next

    while list2_current_loc is not None:
        mergeList.insertAtBeg(list2_current_loc.data)
        list2_current_loc = list2_current_loc.next

    mergeList.head = mergeList.mergeSort(mergeList.head)
    return mergeList




llist1 = LinkedList()
llist1.push(20)
llist1.push(4)
llist1.push(15)
llist1.push(85)
llist1.append(52)


llist2 = LinkedList()
llist2.push(16)
llist2.push(47)
llist2.push(5)
llist2.push(8)
llist2.append(58)


print ("Прямий список")
llist1.printList()
llist1.reverse()
print ("\nРеверс списку")
llist1.printList()
llist1.head = llist1.mergeSort(llist1.head)
llist2.head = llist2.mergeSort(llist2.head)
print('\nСортовані списки:')
llist1.printList()
print()
llist2.printList()
merged_list = mergeTwoLinkList(llist1, llist2)
print("\nОбєднаний сортований список:")
merged_list.printList()