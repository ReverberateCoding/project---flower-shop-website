import os

if os.path.exists('basket.txt'):
    os.remove('basket.txt')
with open('basket.txt', 'x') as file:
    pass
