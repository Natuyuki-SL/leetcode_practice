'''
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

 

Example 1:

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
Example 2:

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3
'''

#Using RE but very slow
import re
    
def numUniqueEmails(emails) -> int:
    hashtable = {}
    count = 0
    for n in emails:
        front = re.sub(r'\.', '', n)
        front = re.sub(r'\+\S+@\S+', '', front)
        front = re.sub(r'@\S+', '', front)
        domain = re.sub(r'(\S+)@', '', n)
        mail = front + '@' + domain 
        if mail in hashtable:
            print('duplicate found for:', mail)
        else:
            hashtable[mail] = 1
            count +=1
    return count

print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))

#Without RE
def numUniqueEmails2(self, emails: [str]) -> int:
        hashtable = {}
        count = 0
        for n in emails:
            parts = n.split('@')
            name = parts[0].split('+')
            front = name[0].replace('.', '')
            mail = front + '@' + parts[1]
            if mail not in hashtable:
                hashtable[mail] = 1
                count +=1
        return count