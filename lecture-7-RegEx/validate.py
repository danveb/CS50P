# clean up user input's whitespace
# email = input("What's your email address? ").strip()
# check: if @ in email address
# if "@" in email:
#     print("Valid")
# else:
#     print("Invalid")

# Example 2
# better check: if @ and . in email address
# email = input("What's your email? ").strip()
# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

# Example 3
# email = input("What's your email? ").strip()
# # split email on "@"
# username, domain = email.split("@")
# # check: if username is present, and "." present in domain
# if username and "." in domain:
#     print("Valid")
# else:
#     print("Invalid")

# Example 4
# email = input("What's your email? ").strip()
# username, domain = email.split("@")
# # check: if username is present AND domain contains ".edu"
# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

# Example 5 -> use "re" library
# import re
# email = input("What's your email? ").strip()
# # check: if "@" in email using "search" function
# if re.search("@", email):
#     print("Valid")
# else:
#     print("Invalid")

# Example 6 -> "re" library with validation
# import re
# email = input("What's your email? ").strip()
# if re.search(".+@.+\.edu", email):
#     print("Valid")
# else:
#     print("Invalid")

# Example 7 -> pass a "raw" string always for regex
# import re
# email = input("What's your email? ").strip()
# # if re.search(r".+@.+\.edu", email):
# # if re.search(r"^.+@.+\.edu$", email):
# if re.search(r"^[^@]+@[^@]+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")

# Example 8 -> better regex
# import re
# email = input("What's your email? ").strip()
# # validate characters between a-z, A-z, 0-9 and "_"
# # if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_].+\.edu$", email):
# # OR
# # \w is same as [a-zA-z0-9_]
# # if re.search(r"^\w+@\w.+\.edu$", email):
# # use "OR" keyword |
# if re.search(r"^\w+@\w.+\.(com|edu|gov|net|org)$", email):
#     print("Valid")
# else:
#     print("Invalid")

# Example 9
# import re
# email = input("What's your email? ").strip()
# if re.search(r"^\w+@\w.+\.edu$", email, re.IGNORECASE):
#     print("Valid")
# else:
#     print("Invalid") # DAN@GMAIL.COM

# Example 10
import re
email = input("What's your email? ").strip()
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid") # 
else:
    print("Invalid") # DAN@GMAIL.COM