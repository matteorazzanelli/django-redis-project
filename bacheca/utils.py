from web3 import Web3

def sendTransaction(message):
  w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/7340ba294b4f4b1da1ffdd1d23ef3022'))
  address = '0x670578CF1d98719c14955941Bd0aac190142EaF0'
  privateKey = '0xbf2267b994b76e43ebad88e5bbcec5455aec86dab7328d555de2069145c342fa'
  nonce = w3.eth.getTransactionCount(address)
  gasPrice = w3.eth.gasPrice
  value = w3.toWei('0', 'ether')
  gas = 100000
  print(f'Totale transaction fee : {gas} * {gasPrice} + {value}')
  new_balance =  w3.eth.getBalance(address) - (gas * gasPrice + value)
  print(f'New balance : {new_balance}')
  signedTx = w3.eth.account.signTransaction(dict(
    nonce = nonce,
    gasPrice = gasPrice,
    gas = gas,
    to = '0x0000000000000000000000000000000000000000',
    value = value,
    data = message.encode('utf-8')
  ), privateKey)
  
  tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
  txId = w3.toHex(tx)
  return txId