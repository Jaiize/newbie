#include <iostream>
#include <cstdlib>

using namespace std;

// Creating a container adaptor

template <class type> // This "type" can be anything you want in character!
struct Node{  
    type data;
    Node<type>* next;
};

template <class type>
class Stack{
    private:
        Node<type>* top;
    public:
        Stack(): top(nullptr){}
        void push(type x){
            Node<type>* newNode = new Node<type>();
            newNode->data = x;
            newNode->next = top;
            top = newNode;
        }
        type pop(){
            if(isEmpty()){
                // return -1; // Won't work for string type elements
            }
            type value = top->data;
            Node<type>* temp = top;
            top = top->next;
            delete temp;
            return value;
        }
        type topper(){
            if(isEmpty()){
                // return -1;
            }
            return top->data;
        }
        bool isEmpty(){
            return top == nullptr;
        }
        
};

int main(){
    Stack<string> stack;
    // Stack<int> stack;
    // stack.push(5); // Push front
    // stack.push(7);
    // stack.push(1);

    stack.push("Hello");
    stack.push("Tosin");
    stack.push("Joseph");


    while(!(stack.isEmpty())){
        cout << stack.topper() << " ";
        stack.pop();
    }

    // cout << "Top element: " << stack.topper() << endl;
    // cout << "Popped element: " << stack.pop() << endl;
    // cout << "Popped element: " << stack.pop() << endl;
    // cout << "Popped element: " << stack.pop() << endl;
    cout << (stack.isEmpty() ? "Yes, it's empty" : "No it's not empty") << endl;

    return 0;
}

