def help_ali():
    vowels = ["A","E","I","O","U","Y"]
    string = input()
    passcheck = 0
    
    for v in range(len(vowels)):
        if string[2] == vowels[v]:
            return "invalid"    
    passcheck+=1
    if (int(string[0]) + int(string[1]))%2 ==0:
        passcheck += 1      
    if (int(string[3]) + int(string[4]))%2 ==0:
        passcheck += 1
    if (int(string[4]) + int(string[5]))%2 ==0:
        passcheck += 1      
    if (int(string[7]) + int(string[8]))%2 ==0:
        passcheck += 1           
    if passcheck == 5:
        return 'valid' 
    else:
        return 'invalid'   
    #DDXDDD-DD
    #012345678
    #we should check those pairs(0,1)(1,3)(4,5)(7,8) and if the 2 is a vowel
print(help_ali())
