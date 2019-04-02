#!/usr/local/bin/python

import pickle

people = [
    'Fred', 'George', 'Harry', 'Eustace', 'Algernon', 'Jim'
    ]
    
outp = open('people.p', 'wb')
pickle.dump(people, outp, pickle.HIGHEST_PROTOCOL)
outp.close()
