def vowelReturn(str):
    ans = ''
    for e in str:
        if(e in ['a','e','i','o','u','A','O','E', 'I','U']):
            continue
        else:
            ans+=e
            
    return ans

str1 = 'Rudra'
print(vowelReturn(str1))