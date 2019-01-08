nums = set(range(2, 20))
comps = {j for i in nums for j in range(i * i, 20, i)}
primes = nums - comps
print(primes)
