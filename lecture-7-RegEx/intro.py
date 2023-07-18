# Regular Expressions

# REGEX
# - enables us to examine "patterns" in our code
# - mainly for validation/formatting purpose
# - we eliminate the need to write lots of conditional statements to check case one by one

# re
# - "re" library allows us to validate user inputs against patterns
# - one of the most versatile functions is "search"
re.search(pattern, string, flags=0)

# Validation -> patterns
# - in regex there are certain symbols that allow us to identify patterns
.   any character except a new line
*   0 or more repetitions
+   1 or more repetitions
?   0 or 1 repetition
{m} m repetitions
{m,n} m-n repetitions

# Match start/end of a regex pattern
^   matches the start of the string
$   matches the end of the string or just before the newline at the end of the string

# Sets of characters to allow on regex pattern
[]  set of characters
[^] complementing the set


\d  decimal digit
\D  not a decimal digit
\s  whitespace characters
\S  not a whitespace character
\w  word character, as well as numbers and the underscore
\W  not a word character

A|B     either A or B
(...)   a group
(?:...) non-capturing version

# Case Sensitivity
# - built-in flag variables
re.IGNORECASE
re.MULTILINE
re.DOTALL