Introduction:

A linked list is a data structure that is commonly used in computer programming. It consists of a sequence of nodes, where each node contains a piece of data and a reference (or a “pointer”) to the next node in the sequence.

![Screenshot (935)](https://github.com/Nadia-Mas/LeetCode_Solutions/assets/88572957/227459ca-74d6-48b1-9114-7d52251df9e4)

Linked lists are useful for representing sequences of data where the order of the data is important, but where the actual physical arrangement of the data in memory is not important. This is because linked lists can be easily modified to insert, delete or rearrange elements in constant time, regardless of the size of the list.

The main advantage of linked lists over other data structures, such as arrays, is that they can be used to build more complex data structures. For example, linked lists are used to implement stacks, queues, and hash tables.

Linked lists come in different variations, such as singly linked lists, doubly linked lists, and circular linked lists. In a singly linked list, each node has only one pointer to the next node in the list. In a doubly linked list, each node has two pointers, one to the next node and one to the previous node. In a circular linked list, the last node points back to the first node, forming a loop.

Examples: Here is an example schematic of a singly linked list structure:

| 1 | -> | 2 | -> | 3 | -> | 4 | -> NULL

Each node in the linked list has a value and a next pointer that points to the next node in the list. The last node in the list has a next pointer that points to NULL, indicating the end of the list.

Here is an example schematic of a doubly linked list structure:

NULL <--> | 1 | <--> | 2 | <--> | 3 | <--> | 4 | <--> NULL

Each node in the doubly linked list has a value, a prev pointer that points to the previous node in the list, and a next pointer that points to the next node in the list. The first node in the list has a prev pointer that points to NULL, indicating the beginning of the list, and the last node in the list has a next pointer that points to NULL, indicating the end of the list.

We are going to use these classes to implement a linked list and print_linked_list function to print the linked list.

![Screenshot (937)](https://github.com/Nadia-Mas/LeetCode_Solutions/assets/88572957/68837189-6d5d-4934-b77f-2c6862d69d86)

1. Insert a value in a linked list:
Given a sorted linked list and a value to insert, write a function to insert the value in a sorted way.

You are given a sorted linked list of integers and a single integer value. Write a function to insert the value in a sorted way, such that the resulting linked list is also sorted. The function should return a reference to the head of the modified, linked list.

Example: Input: linked list: 1 -> 2 -> 4, value to insert: 3 Output: 1 -> 2 -> 3 -> 4

![Screenshot (939)](https://github.com/Nadia-Mas/LeetCode_Solutions/assets/88572957/08426e19-74b8-4920-9367-ac93ad62a078)

Explanation:

Check if the linked list is empty. If it is, set the head to the new node.
If the new node should be inserted at the head of the list, set the new node’s next pointer to the head and update the head to point to the new node.
Otherwise, traverse the list starting at the head and find the node whose data value is less than the new node’s data value, but whose next node (if any) has a data value greater than or equal to the new node’s data value.
Insert the new node between the found node and its next node (if any). Once the correct position is found, the code updates the links to insert the new node into the linked list. The new_node.next is set to current.next to maintain the remaining linked list after the insertion. Then, current.next is set to new_node to insert the new node between current and current.next.
Space and time complexity:

The time complexity of the sorted_insert function depends on the position where the new node is to be inserted in the sorted linked list. In the best case, when the new node is to be inserted at the beginning of the list, the time complexity is O(1). In the worst case, when the new node is to be inserted at the end of the list or the list is unsorted, the time complexity is O(n), where n is the number of nodes in the linked list.

The space complexity of the sorted_insert function is O(1), since it uses a constant amount of additional space to store the new node and the current node.

Test:
![Screenshot (942)](https://github.com/Nadia-Mas/LeetCode_Solutions/assets/88572957/ea21828a-2a7c-4529-9877-037b345aa281)
![Screenshot (943)](https://github.com/Nadia-Mas/LeetCode_Solutions/assets/88572957/c5e703ba-6877-46a3-bee8-4a4e2ecb6106)

2. Delete a given node in Linked List under the given constraints:
Given a Singly Linked List, write a function to delete a given node. Your function must follow the following constraints:

It must accept a pointer to the start node as the first parameter and the node to be deleted as the second parameter, i.e., a pointer to the head node is not global.
It should not return a pointer to the head node.
It should not accept pointer to pointer to the head node. You may assume that the Linked List never becomes empty.

![Screenshot (947)](https://github.com/Nadia-Mas/LeetCode_Solutions/assets/88572957/5b353262-0923-49ab-a205-5eb6e8f88f65)

Explanation:

The function first initializes two pointers temp and prev to the head of the linked list. It then checks if the node to be deleted is the head node, and if so, it updates the head to the next node. If the node to be deleted is not the head node, it traverses through the linked list until it finds the node with the given data, updating temp and prev pointers as it goes. Once the node is found, the function updates the prev.next pointer to temp.next, effectively removing the node from the linked list.

Space and time complexity:

The time complexity of this function is O(n) where n is the length of the linked list since we may have to traverse through the entire linked list to find the node to be deleted. The space complexity of this function is O(1) since we are only using a constant amount of extra space, regardless of the size of the linked list.

Test:

![Screenshot (948)](https://github.com/Nadia-Mas/LeetCode_Solutions/assets/88572957/7bed297a-a493-405c-ac95-0903deaf2c77)
![Screenshot (949)](https://github.com/Nadia-Mas/LeetCode_Solutions/assets/88572957/2715d799-7b21-48ae-931a-fecbae704501)


3. Compare two strings represented as linked lists
Given two strings, represented as linked lists (every character is a node in a linked list). Write a function compare() that works similarly to strcmp(), i.e., it returns 0 if both strings are the same, 1 if the first linked list is lexicographically greater, and -1 if the second string is lexicographically greater.

To compare two strings, you need to compare the characters of the strings in order, from left to right. If the characters at the corresponding positions of both strings are the same, you move on to the next pair of characters. If the characters are different, the string with the lexicographically smaller character is considered to be smaller. If one string ends and the other does not, the shorter string is considered to be smaller. If both strings end at the same position and all characters match, then they are equal.

For example, if the first linked list is “abc” and the second linked list is “abd”, the function should return -1 because “abd” is lexicographically greater than “abc”.

![Screenshot (953)](https://github.com/Nadia-Mas/LeetCode_Solutions/assets/88572957/4435f1b9-9238-4af3-8f10-d09b9566fb8d)

Explanation:

The function first initializes two pointers temp and prev to the head of the linked list. It then checks if the node to be deleted is the head node, and if so, it updates the head to the next node. If the node to be deleted is not the head node, it traverses through the linked list until it finds the node with the given data, updating temp and prev pointers as it goes. Once the node is found, the function updates the prev.next pointer to temp.next, effectively removing the node from the linked list.

Space and time complexity:

The time complexity of the code is O(n + m) where n and m are the number of nodes in list1 and list2, respectively. This is because the code traverses both lists once until either the end of a list is reached or the characters don't match.

The space complexity of the code is O(1) since the code only uses a constant amount of memory to store the current nodes being compared.

Test:

![Screenshot (954)](https://github.com/Nadia-Mas/LeetCode_Solutions/assets/88572957/bac2c064-56e4-4f17-807d-3d7706152ed3)
![Screenshot (955)](https://github.com/Nadia-Mas/LeetCode_Solutions/assets/88572957/a9ca28d0-799f-4c42-988d-618a49863139)




