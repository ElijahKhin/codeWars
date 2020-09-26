# Author: Elijah Khin
# Email:  workbiscap@gmail.com

# Description:
# Complete the method/function so that it converts dash/underscore
# delimited words into camel casing. The first word within the output should be capitalized only
# if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).


def to_camel_case(s):

    if s == '':
        return ""

    right_s = s.replace("-", " ")  # Change wrong signs
    right_s = right_s.replace("_", " ")  # Change wrong signs
    right_s = right_s.split()  # Make list to split first word and others
    cap = ' '.join(right_s[1:])  # Make strings again
    not_cap = ''.join(right_s[0])
    right_s = not_cap + cap.title()
    return right_s.replace(' ', '')  # I get a concatenation to achieve my goal


print(to_camel_case("the_stealth_warrior"))
