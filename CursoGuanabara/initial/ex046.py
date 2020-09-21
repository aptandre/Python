import emoji
import time
for x in range(10, 0, -1):
    print(x)
    time.sleep(1)
print('Happy new year!', (emoji.emojize(':sparkles:', use_aliases= True) * 10))