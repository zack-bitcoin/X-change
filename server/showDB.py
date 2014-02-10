#!/usr/bin/python
from server import *
import pprint

def users():
    db='users.db'
    out=gdbm.open(db, 'c')
    keys=out.keys()
    for key in keys:
        print('out[{}]=={}'.format(str(key), str(out[key])))

def other():
    dbs=['litecoin_bitcoin_bids.db', 'bitcoin_litecoin_bids.db']
    for db in dbs:
        print('in db: ' +str(db))
        pprint.pprint(fs_load(db))


users()
print('DDDD')
other()
