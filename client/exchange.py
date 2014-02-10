from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import string,cgi,time, json, random, copy, cPickle, image64, os, gdbm, pprint
import pybitcointools as pt
import urllib
PORT=8090

privkey=pt.sha256("Brain Wallet3 ")
privkey2=pt.sha256("Brain Walle")

user=pt.privtopub(privkey)#your pubkey is your identity
user2=pt.privtopub(privkey2)#your pubkey is your identity

#url='http://6wsygte7i4ly7htk.tor2web.org/checkSig?command={}&signature={}'
#url='http://localhost:8091/checkSig?command={}&signature={}'
url='http://3uc1id.no-ip.biz/checkSig?command={}&signature={}'
database='cmd_num.db'
def package(dic):
    return json.dumps(dic).encode('hex')
def unpackage(dic):
    return json.loads(dic.decode('hex'))
def fs_load():
    try:
        out=cPickle.load(open(database, 'rb'))
        return out
    except:
        fs_save(0)
        return cPickle.load(open(database, 'rb'))      

def fs_save(dic):
    cPickle.dump(dic, open(database, 'wb'))

def increment_cmd_num(num=1):
    a=fs_load()
    a=a+num
    fs_save(a)
def command(command, privkey):
    command['cmd_num']=fs_load()
    increment_cmd_num()
    cmd=package(command)
    sig=package(pt.ecdsa_sign(cmd, privkey))
    URL=urllib.urlopen(url.format(cmd, sig))
    URL=URL.read()
    print('url: ' +str(URL))
    try:
        out=unpackage(URL)
    except:
        print(URL)
        print('out: ' +str())
        return ''
    if 'type' in out and out['type']=='cmd_num_error':
        print('out: ' +str(out))
        increment_cmd_num(1+out['cmd_num'])
        return command(command, privkey)
    return out


def deposit_address(user, privkey, coin):
    return command({'command':'deposit_address', 'user':user, 'currency':coin}, privkey)
def user_data(user, privkey):
    return command({'command':'user_data', 'user':user}, privkey)
def withdraw(user, privkey, amount, to_address, currency):
    dic={'command':'withdraw', 'user':user, 'amount':amount, 'to_address':to_address, 'currency':currency}
    return command(dic, privkey)
def buy_bid(user, privkey, buy_currency, buy_amount, sell_currency, sell_amount):
    dic={'user':user, 'command':'buy_bid', 'buy_amount':buy_amount, 'buy_currency':buy_currency, 'sell_currency':sell_currency, 'sell_amount':sell_amount}
    return command(dic, privkey)
def sell_bid(user, privkey, bid_id):
    dic={'command':'sell_bid', 'user':user, 'bid_id':bid_id}
    return command(dic, privkey)

def test():
    print('deposit: ' +str(deposit_address(user, privkey)))
    pprint.pprint(user_data(user, privkey)['bitcoin'])
    pprint.pprint(user_data(user, privkey)['litecoin'])
    print('deposit: ' +str(deposit_address(user2, privkey2)))
    pprint.pprint(user_data(user2, privkey2)['bitcoin'])
    pprint.pprint(user_data(user2, privkey2)['litecoin'])

    #print('buy_bid: ' +str(buy_bid(user, privkey, 'bitcoin', 0.00002, 'litecoin', 0.000009)))
    print('buy_bid: ' +str(buy_bid(user2, privkey2, 'litecoin', 0.000009, 'bitcoin', 0.00002)))
    #print('sell_bid: ' +str(sell_bid(user2, privkey2, 'fd5b73d52e3c5e008b0c51e6320cd5c66b309da0962963db964d76966d0509c9')))

    print('deposit: ' +str(deposit_address(user, privkey)))
    pprint.pprint(user_data(user, privkey)['bitcoin'])
    pprint.pprint(user_data(user, privkey)['litecoin'])
    print('deposit: ' +str(deposit_address(user2, privkey2)))
    pprint.pprint(user_data(user2, privkey2)['bitcoin'])
    pprint.pprint(user_data(user2, privkey2)['litecoin'])


    #print('withdraw: ' +str(withdraw(user, privkey, 0.0001, '18yRXfk8dXD1YkJ9yZTz48X4oAywGJ1PB', 'bitcoin')))
    #print('buy_bid: ' +str(buy_bid(user, privkey, 'litecoin', 0.00001, 'bitcoin', 0.00002)))
    #print('sell_bid: ' +str(sell_bid(user, privkey, '90b8251186d0960a0cbee9de0d3736f50db6a7f318729d2a988affad1c34f690')))
