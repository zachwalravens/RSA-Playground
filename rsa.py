

#Key gen

"""
#e = {3, 5, 17, 257, 65537}
e = 17

while !((p % e) = 1)
   p = genprime(k/2)
until (p mod e) ≠ 1
repeat
   q ← genprime(k - k/2)
until (q mod e) ≠ 1
N ← pq
L ← (p-1)(q-1)
d ← modinv(e, L)
return (N, e, d)
"""

p = 104729
q = 104743

phi = (p-1)*(q-1)
