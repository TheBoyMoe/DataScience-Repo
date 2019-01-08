nums = range(1, 21)
trips = [(a, b, c) for a in nums for b in nums for
    c in nums if a*a + b*b == c*c]
print(trips)



    

    
    


