from os import getenv,environ
from dotenv import dotenv_values

assert(open('.env'))
config = dotenv_values('.env')

def main():
    print('the env:', getenv('MY_ENV'))
    print('from dotenv:', config['MY_EXISTENCE'])

if __name__ == "__main__":
    main()
