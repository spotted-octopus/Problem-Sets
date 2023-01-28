import numpy as np

user_input_01 = int(input("Enter number x:"))
user_input_02 = int(input("Enter number y:"))

output_1 = user_input_01**user_input_02
output_2 = np.log2(user_input_01)

print("X**y = ", str(output_1))
print("log(x) = " + str(int(output_2)))
