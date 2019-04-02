"""
Utility module for stuff
"""
import warnings


def new_msg(name, greeting='Hey,', question='How\'s it going?'):
    """
    print a friendly message
    """
    print(greeting, name)
    print(question)


def msg(name, greeting='Hi,'):
    """
    print a friendly message
    """
    warnings.warn('msg is deprecated, use newmsg instead',
                  DeprecationWarning)
    print(greeting, name)


def main():
    print('Testing, testing...')
    msg('Eric')
    new_msg('Jim', greeting='Afternoon,')
    

if __name__ == '__main__':
    main()

    
    
    
    
    
    
    