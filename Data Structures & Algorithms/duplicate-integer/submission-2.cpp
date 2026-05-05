#include <vector>
#include <set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // so firstly, i see that our recommended time and space are O(n)
        // so when I firstly look at this, what comes to mind is 
        // to loop through nums, then create a new container, adding all unique nums
        // to new container. if its not unique, return true, else return false.
        set<int> container;

        for(auto i : nums) 
        {
            if (container.count(i) < 1) {
                container.insert(i);
            } else {
                return true;
            }
        }
        return false;
    }
};