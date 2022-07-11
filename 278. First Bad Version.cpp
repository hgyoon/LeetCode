// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int start = 0;
        int end = n;
        while (start <= end){
            int middle = start + (end-start) / 2;
            bool a = isBadVersion(middle);
            if (a == true){
                end = middle - 1;
            }
            else{
                start = middle + 1;
            }
        }
        cout << "start: " << start << endl;
        cout << "end: " << end << endl;
        return start;
    }
};
