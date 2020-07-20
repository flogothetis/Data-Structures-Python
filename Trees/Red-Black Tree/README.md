## Red Black Trees
- Every node is red or black.
- Root is always black.
- New insertions are always red.
- Every path from root->leaf has the some number of black nodes.
- No path have two consecutive red nodes.
- Nulls are black.

What happens if the tree violates that rules ?
Answer: We have to fix that tree

Fix:
1. Rebalance 
- Black Aunt Rotate
- Red Aunt color Flip

After Rotation :

        BLACK     
        /   \
       RED  RED 

After  color flip:   
       
          RED
        /    \
     BLACK   BLACK
     

        
            