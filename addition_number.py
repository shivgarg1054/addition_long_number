str1 = "12345"
str2 = "34989"
t = ""


# make sure length of str2 is larger.
if (len(str1) > len(str2)):
    t = str1
    str1 = str2
    str2 = t

# Take an empty string for
# storing result
str = ""

# Calculate length of both string
n1 = len(str1)
n2 = len(str2)

# Reverse both of strings
str1 = str1[::-1]
str2 = str2[::-1]

carry = 0
for i in range(n1):
    # compute sum of current digits and carry
    sum = ((ord(str1[i]) - 48) +
           ((ord(str2[i]) - 48) + carry))
    str += chr(sum % 10 + 48)

    # Calculate carry for next step
    carry = int(sum / 10)

# Add remaining digits of larger number
for i in range(n1, n2):
    sum = ((ord(str2[i]) - 48) + carry)
    str += chr(sum % 10 + 48)
    carry = (int)(sum / 10)

# Add remaining carry
if (carry):
    str += chr(carry + 48)

# reverse resultant string
str = str[::-1]

print(str)