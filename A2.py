import random
import pandas as pd
with open('Cubit-Form-F.txt', 'r') as f:
    F = [line.strip() for line in f]
with open('Cubit-Ingredient-I.txt', 'r') as f:
    I = [line.strip() for line in f]
with open('Cubit-Process-P.txt', 'r') as f:
    P = [line.strip() for line in f]
with open('Cubit-Quantity-and-Unit-Q.txt', 'r') as f:
    Q = [line.strip() for line in f]
with open('Cubit-Utensil-U.txt', 'r') as f:
    U = [line.strip() for line in f]

l = []
for i in range(0, 50):
    abc = random.choice(Q) + " " + random.choice(I) + " " + random.choice(F)
    l.append(abc)

df = pd.DataFrame(l, columns=['IP'])
df.to_excel('Cubit-IP.xlsx', index=False)