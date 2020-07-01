## Sparse Table

Sparse table concept is used for fast queries on a set of static data (elements do not change). It does preprocessing so that the queries can be answered efficiently.
Example:

Input:  arr[]   = {7, 2, 3, 0, 5, 10, 3, 12, 18};
        query[] = [0, 4], [4, 7], [7, 8]

Output: Minimum of [0, 4] is 0
        Minimum of [4, 7] is 3
        Minimum of [7, 8] is 12
        
  
  
  
  
        
        
        
The idea is to precompute minimum of all subarrays of size 2j where j varies from 0 to Log n. We make a table lookup[i][j] such that lookup[i][j] contains minimum of range starting from i and of size 2j. For example lookup[0][3] contains minimum of range [0, 7] (starting with 0 and of size 23)