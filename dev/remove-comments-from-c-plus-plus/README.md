# Remove comments from C++ codebase

Given a string which represents C++ source code, return string without any code comments.

**Exmaple 1**
    
    Input:
    void main()
    {
        char "/* this string shouldn't be removed */" //and this - shoould
        return 3/5  // so what?
    }
    
    Output:
    void main()
    {
        char "/* this string shouldn't be removed */"
        return 3/5  
    }
    
**Exmaple 2**

    Input:
    #include <iostream>
    
    char* mychar()
    {
        char* ch = new char;
        ch = "http://github.com";
        return ch;
    }

    Output:
    #include <iostream>
    
    char* mychar()
    {
        char* ch = new char;
        ch = "http://github.com";
        return ch;
    }
