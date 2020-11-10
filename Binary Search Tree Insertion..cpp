/*
Node is defined as 

class Node {
    public:
        int data;
        Node *left;
        Node *right;
        Node(int d) {
            data = d;
            left = NULL;
            right = NULL;
        }
};

*/

Node *insert(Node *root, int value) {
  Node *new_node = new Node(value);
  new_node->data = value;
  new_node->left = NULL;
  new_node->right = NULL;

  if (!root) { // Case 1
    root = new_node;
    return root;
  }
  Node *current_root = root;
  while (1) {
    if (current_root->data > value) {
      if (current_root->left) // case 2
        current_root = current_root->left;
      else { // case 3
        current_root->left = new_node;
        break;
      }
    } else {
      if (current_root->right) // case 4
        current_root = current_root->right;
      else { // case 5
        current_root->right = new_node;
        break;
      }
    }
  }
  return root;
}
