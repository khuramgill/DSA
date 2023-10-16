#include <iostream>
using namespace std;

// creating a linked list;
class Node {
public:
	int value;
	Node* link;

	// Constructor
	Node(int value)
	{
		this->value = value;
		this->link = NULL;
	}
};

class Stack {
	Node* head;

public:
	//Default Constructor
	Stack()
	{
		head = NULL;
	}

	void push(int data)
	{

		// Create new node temp and allocate memory in heap
		Node* temp = new Node(data);

		// Check if stack (heap) is full.
		// Then inserting an element would
		// lead to stack overflow
		if (!temp) {
			cout << "\nStack Overflow";
			exit(1);
		} 

		// Initialize data into temp data field
		temp->value = data;

		// Put top pointer reference into temp link
		temp->link = head;

		// Make temp as top of Stack
		head = temp;
	}

	// Utility function to check if
	// the stack is empty or not
	bool isEmpty()
	{
		// If top is NULL it means that
		// there are no elements are in stack
		return head == NULL;
	}

	// Utility function to return top element in a stack
	int peek()
	{
		// If stack is not empty , return the top element
		if (!isEmpty())
			return head->value;
		else
			exit(1);
	}

	// Function to remove
	// a key from given queue q
	void pop()
	{
		Node* temp;

		// Check for stack underflow
		if (head == NULL) {
			cout << "\nStack Underflow" << endl;
			exit(1);
		}
		else {

			// Assign top to temp
			temp = head;

			// Assign second node to top
			head = head->link;

			// This will automatically destroy
			// the link between first node and second node

			// Release memory of top node
			// i.e delete the node
			free(temp);
		}
	}

	// Function to print all the
	// elements of the stack
	void display()
	{
		Node* temp;

		// Check for stack underflow
		if (head == NULL) {
			cout << "\nStack Underflow";
			exit(1);
		}
		else {
			temp = head;
			while (temp != NULL) {

				// Print node data
				cout << temp->value;

				// Assign temp link to temp
				temp = temp->link;
				if (temp != NULL)
					cout << " -> ";
			}
		}
	}
};

// Driven Program
int main()
{
	// Creating a stack Object
	Stack s;

	// Push the elements of stack
	s.push(11);
	s.push(22);
	s.push(33);
	s.push(44);
	s.display();

	// Print top element of stack
	cout << "\nTop element is " << s.peek() << endl;

	// Delete top elements of stack
	s.pop();
	s.pop();
	s.display();

	// Print top element of stack
	cout << "\nTop element is " << s.peek() << endl;

	return 0;
}
