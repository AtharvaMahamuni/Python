# 19. Create random vector of size 10 and replace the maximum value by 0.

import numpy as np

vector = np.random.random(10)
vector[vector.argmax()] = 0

print(vector)


'''
[0.51491781 0.         0.38390968 0.28275036 0.44043039 0.35042389
 0.16387027 0.42792548 0.29104465 0.36103436]
'''
