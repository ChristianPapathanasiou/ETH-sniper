from eth_keys import keys
from eth_utils import encode_hex, decode_hex
from web3 import Web3
import json
import requests
from decimal import Decimal
w3 = Web3(Web3.HTTPProvider("")) #infura

abi = json.loads('[{"name":"USDBalances","inputs":[{"name":"_address","type":"address","indexed":false},{"name":"_balance","type":"uint256","indexed":false}],"anonymous":false,"type":"event"},{"stateMutability":"nonpayable","type":"function","name":"getUSDCBalances","inputs":[{"name":"addresses","type":"address[500]"}],"outputs":[{"name":"","type":"uint256"}],"gas":4820524}]')

private = "" #Private key
acct = w3.eth.account.from_key(private)

w3.eth.defaultAccount = acct.address

contract_address_polygon = "" 
contract_address = ""
contract = w3.eth.contract(address=w3.to_checksum_address(contract_address), abi=abi)
tenderly_user = ""
tenderly_project = ""
tenderly_access_code = ""


# Define the start and end indices
start_index = 1
end_index = 1000000 

# Create a list to store the generated Ethereum addresses
generated_addresses = []

batch_size = 500  # Set the batch size to 500 addresses

for i in range(start_index, end_index + 1):
    # Generate a private key from the index (You should use a more secure method for generating private keys)
    private_key_bytes = decode_hex(f'0x{i:064x}')
    private_key = keys.PrivateKey(private_key_bytes)
    
    # Get the corresponding Ethereum address
    ethereum_address = private_key.public_key.to_checksum_address()
    
    # Add the formatted Ethereum address to the list
    generated_addresses.append(f'"{ethereum_address}"')

    # Check if the batch size is reached
    if i % batch_size == 0:
        # Format the list of addresses as a string with square brackets
        formatted_addresses = '[' + ', '.join(generated_addresses) + ']'

        # Print the formatted addresses for the current batch

        # Clear the list for the next batch
        generated_addresses = []

        # Pause every 1000 addresses (wait for user input to continue)
        if i < end_index:
            try:
                nonce = w3.eth.get_transaction_count(acct.address)
                transaction = contract.functions.getUSDCBalances(eval(formatted_addresses)).build_transaction({
                    'chainId': 1,  # Mainnet
                    'gas': 2500000,  # Adjust the gas limit as needed
                    'gasPrice': 238000000000,  # Adjust the gas price as needed
                    'nonce': nonce
                })

                #signed = acct.sign_transaction(transaction)
                #tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
                #tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
             


                data = {"network_id":"1","from":"0x0000000000000000000000000000000000000000","input":transaction["data"],"to":contract_address,"gas":8000000,"gas_price":"0","value":"0"}

                headers = { 
                "content-type": "application/json",
                "X-Access-Key": tenderly_access_code
                }

                response=requests.post("https://api.tenderly.co/api/v1/account/" + tenderly_user + "/project/" + tenderly_project + "/simulate",data=json.dumps(data),headers=headers)

                x = json.loads(response.text)
                logs = x["transaction"]["transaction_info"]["logs"]
                if logs is None:
                    print("nothing found")
                else:
                    
                    print("******************************")
                    print(formatted_addresses)
                    print("0x" + logs[0]["raw"]["data"][26:66])
                    _hex = Decimal(int(logs[0]["raw"]["data"][-7:],base=16))
                    print(_hex / 10**6)
                    print("******************************")


                #print(tx_receipt)
            except Exception as e:
                print("Exception!!: %s" % e)

