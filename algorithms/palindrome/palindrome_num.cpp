class PalindromeNumber {
public:
    bool isPalindrome(int x) {
        
        std::stack<char> results_reversed; 
        std::string x_reversed("");
        
        std::string x_str = to_string(x); 
        
        for (char x : x_str) {
            results_reversed.push(x);
        }
        
        while (!results_reversed.empty()) {
            x_reversed += results_reversed.top(); 
            results_reversed.pop(); 
        }
        
        if (x_reversed == x_str) {
            return true; 
        }
        return false; 
             
    }
};
