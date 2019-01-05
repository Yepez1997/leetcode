/*
 * Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 * An input string is valid if:
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 * Note that an empty string is also considered valid. 
 */

class ValidParen {
  public:
    bool isValid(string s) {
    stack<char> stack;

    if(s.length() == 0){
        return true;
    }
    if(s.length() == 1){
        return false;
    }
    
    for(int i =0 ; i < s.length(); i++){
        char c = s[i];
        if(c == '}'|| c == ')' || c == ']'){
            if(stack.size() == 0 ) return false;
            if(c == '}' && stack.top() != '{') return false;
            if(c == ')' && stack.top() != '(') return false;
            if(c == ']' && stack.top() != '[') return false;
            stack.pop();
            
         } else {
            stack.push(c);
        }
    }
    if(stack.size() == 0) return true;
    return false;
    }
};





