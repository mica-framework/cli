
import sys
import os
import re

print("Search current modules..")
module_list = os.listdir("./modules")
module_list = [re.sub('\.py$', '', module) for module in module_list if not str(module).startswith('__') and str(module).endswith('.py')]
print('Found {} modules'.format(len(module_list)))

print('Start loading all modules')
for module in module_list:
    __import__("modules." + module)
    del(module)
print('Finished module load!')

# cleanup the initialization
del(module_list)
del(sys)
del(os)
del(re)