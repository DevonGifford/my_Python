import requests 
import hashlib
import sys



def request_api_data(querey_char):
    '''Function to check if we can, and if we can = connect and request data from API'''
    url = 'https://api.pwnedpasswords.com/range/' + querey_char
    res = requests.get(url)
    if res.status_code != 200:                                                         
        raise RuntimeError (f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leak_count(hashes, my_short_hash):
    '''Function to get all the hash keys that have leaked '''
    hashes = (line.split(':') for line in hashes.text.splitlines())                      
    # print ("Calculating ... ")
    for hashes_hacked, no_times_hacked in hashes:                                         
        if hashes_hacked == my_short_hash:
            return no_times_hacked
    return 0


def pwned_api_check(password):
    '''Turning our password into a hash & preparing to send to the API'''
    sha1password = (hashlib.sha1(password.encode('utf-8')).hexdigest().upper())         
    first5, tail = sha1password[:5], sha1password[5:]                                    
    response = request_api_data(first5)                                                                                                                     
    return get_password_leak_count(response, tail)
   

def main(args):
    '''Main function that will accept our passwords as an argument in the terminal and then depending on breaches will respond accordingly'''
    print ("\nWelcome to the password checker.  Let's check if your passwords are secure...\n")
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'For the password:  "{password}"\nThis password has been found {count} times - you should consider changing your password ASAP!\n')
        else:
            print(f'For the password:  "{password}"\nThis password has been found {count} times - the password is safe!\n')
    return 'Your request is complete'

def usage():
    print("""Please use the utility as follows:
>>> python file_name.py Insert_Password_Here
Note:  you can insert multiple passwords, just seperate them with a space\n""")
    exit()
 
 
if len(sys.argv) < 2:
    print("\nOh no - there has been an error:  Incorrect number of arguments.\n")
    usage()

if __name__ == '__main__':
    main(sys.argv[1:])

