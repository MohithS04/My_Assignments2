txt = "hello,and welcome to my world."   #capitalize
x = txt.capitalize()
print(x)

txt = "Hello, And Welcome To My World!"   #casefold
x = txt.casefold()
print(x)

txt = "banana"                            #center
x = txt.center(20)
print(x)
              
txt = "Hello, And Welcome To My World!"     #count
x = txt.count("world")
print(x)

txt = "My name is Mohith"                  #encode
x = txt.encode()
print(x)

txt = "Hello, And Welcome To My World!"      #endswith
x = txt.endswith(".")
print(x)

txt = "H\te\tl\tl\to"                        #expandtabs
x = txt.expandtabs(2)
print(x)

txt = "Hello, welcome to my world."           #find
x = txt.find("welcome")
print(x)

txt = "For only {cost:.3f} dollars!"          #format
print(txt.format(cost = 90))

txt = "hello,and welcome to my world."         #index
x = txt.index("world")
print(x)

txt = "project24"                             #inalnum
x = txt.isalnum()
print(x)

txt = "projectZ"                              #isalpha()
x = txt.isalpha()
print(x)
