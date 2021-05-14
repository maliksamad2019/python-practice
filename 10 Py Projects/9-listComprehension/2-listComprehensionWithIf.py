temps = [221, 234,340,-9999,230]

newtemps = [temp/10 for temp in temps if temp != -9999]
print(newtemps,"\ntemps: ", temps)


# 5-List Comprehension with if-else 
# moves conditions befor loop
newtemps = [temp/10 if temp != -9999 else 0 for temp in temps]
print(newtemps,"\ntemps: ", temps)
