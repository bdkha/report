import random

p = 868189570806118625034727107509  # the prime number

# Step 1: Find a suitable generator g
# You may use the known properties of primitive roots to find a suitable generator g.

# Step 2: Choose a private key x randomly from the range (1, p-1)
x = random.randint(1, p - 1)

# Step 3: Compute the public key y
# Let's assume you have found a suitable generator g
g = 2  # Example value, you need to replace it with an appropriate generator
y = pow(g, x, p)

# Output the private and public keys
print("Private Key (x):", x)
print("Public Key (y):", y)
