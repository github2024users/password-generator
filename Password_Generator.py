import random

import array

# maximum length of password needed

# this can be changed to suit your password length

max_len = 12

# declare arrays of the character that we need in out password

# Represented as chars to enable easy string concatenation

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'T', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'T', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '1', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

symbols = ['@', '#', '$', '%', '', '', '?']

#combines all the character arrays above to form one array

combined_list= digits+upper_case+lower_case+symbols

# randomly select at least one character from each character set above

random_digits = random.choice(digits)

random_upper = random.choice(upper_case)

random_lower = random.choice(lower_case)

random_symbols = random.choice(symbols)

# combine the character randomly selected above

# at this stage, the password contains only 4 characters but

#we want a 12-character password

temporary_password = random_digits + random_upper + random_lower +random_symbols
#now that we are sure we have at least one character from each

# set of characters, we fill the rest of

# the password length by selecting randomly from the combined

#list of character above.

for x in range(max_len-4):
    temporary_password = temporary_password +random.choice(combined_list)

# convert temporary password into array and shuffle to

# prevent it from having a consistent pattern

#where the beginning of the password is predictable

temp_pass_list = array.array('u', temporary_password)

random.shuffle(temp_pass_list)

# traverse the temporary password array and append the chars

# to form the password

password = ""

for x in temp_pass_list:
    password = password + x

# print out password

print("here is your password:-", password)