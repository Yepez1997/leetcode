class PalindromeNumber {
public:
    bool isPalindrome(int x) {
        
        std::stack<char> results_reversed; 
        std::string x_reversed("");
        // convert int to string 
        // reverse process is stoi ie string to in
        std::string x_str = to_string(x); 
        
        // push char to stack 
        for (char x : x_str) {
            results_reversed.push(x);
        }
        
        // pop from stack, note this will be in reversed 
        while (!results_reversed.empty()) {
            x_reversed += results_reversed.top(); 
            results_reversed.pop(); 
        }
        
        // if reversed is equal to original -> true 
        if (x_reversed == x_str) {
            return true; 
        }
        return false; 
             
    }
};
