class Node:
    def __init__(self, data):
        self.data = data  # stores the data of the node
        self.next = None  # initially, the node does not point to any other node

class LinkedList:
    def __init__(self):
        self.head = None  # initially, the linked list is empty
        self.size=0

    def append(self, data):
        new_node = Node(data)  # create a new node
        if self.head is None:  # if the list is empty
            self.head = new_node  # set head to the new node
            return
        curr = self.head  # start from the head node
        while curr.next is not None:  # traverse to the end of the list
            curr = curr.next
        curr.next = new_node
        self.size += 1

        def length(self):
            return self.size

        def display(self):
            elements = []
            curr = self.head
            while curr is not None:
                elements.append(curr.data)
                curr = curr.next
            return elements

    # Main program
my_list = LinkedList()

while True:
        # Take user input for data to append
        data = input("Enter data for the new node: ")
        my_list.append(data)  # Add new node with the given data

        # Ask the user if they want to add another node
        choice = input("Do you want to add another node? (yes/no): ").strip().lower()
        if choice != 'yes':
            break  # Exit the loop if the user does not want to continue

    # Display the final list and its length
print("Final linked list:", my_list.display())
print("Length of the linked list:", my_list.length())