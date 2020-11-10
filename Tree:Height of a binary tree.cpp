/*The tree node has data, left child and right child 
class Node {
    int data;
    Node* left;
    Node* right;
};

*/
// fill up the following code in the given section 

    int height(Node* root)
{
    int x = -1, y = -1 ;
    if(root != NULL)
    {
        x = 1 + height(root->left) ;
        y = 1 + height(root->right) ;
    }
    return x > y ? x : y ;
}
