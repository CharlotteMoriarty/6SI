def tribonacci(signature, n):
    #your code here
    tribonacci = []
    #n = int(input("How many numbers you want to have in sequence")) w testach input nie przechodzi
    for i in range(n):
        new_element = signature[-1] + signature[-2] + signature[-3]
        signature.append(new_element)
        element = signature.pop(0)
        tribonacci.append(element)
    return tribonacci