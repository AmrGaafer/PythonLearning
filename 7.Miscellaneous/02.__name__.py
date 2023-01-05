# --------------------------------------------------------------------------------------------------
# __name__ and __main__:
#   __name__ is a built-in variable
#   __main__ is value of __name__ if the file is executed directly
#   'file/module_name' is value of __name__ if the file is executed indirectly
#   Execution Methods:
#       1. Direct Execution: the file is executed directly from command line
#       2. Indirect Execution: the file is imported and called from another file
#   - in some cases, it is important to know if the code is running directly or through import
# --------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command
import MyModule2

print('\n# ********************************************* #')
print('__name__:')
print(__name__) #__main__

MyModule2.Hello()
