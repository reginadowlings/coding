def has_invalid_characters(string):
    valid = "abcdefghijklmnopqrstuvwxyz0123456789."
    
    # your code here
    for character in string:
        if character not in valid:
            return True
    return False 
            

def is_valid(email):
   
    if email.count('@') != 1:
        return False
    prefix,domain = email.split('@')
    if len(prefix) < 1:
            return False 
    if email.count('.') != 1:
        return False
    if has_invalid_characters(prefix) or has_invalid_characters(domain):
        return False
        
    domain_parts = domain.split('.')
    if len(domain_parts) != 2 or '' in domain_parts:
        return False
        
    domain_name,extension = domain.split('.')
    if len(domain_name) == 0 or len(extension) == 0:
        return False
    return True 

emails = [
    "test@example.com",
    "valid@gmail.com",
    "invalid@gmail",
    "invalid",
    "not an email",
    "invalid@email",
    "!@/",
    "test@@example.com",
    "test@.com",
    "test@site.",
    "@example.com",
    "an.example@test",
    "te#st@example.com",
    "test@exam!ple.com"
]
for mail in emails:
    if is_valid(mail):
        print(mail + ' is valid')
    else:
        print(mail + ' is invalid')










        