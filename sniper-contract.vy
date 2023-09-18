

# Import the USDC interface
from vyper.interfaces import ERC20

# USDC Token Contract Address (replace with the actual USDC token contract address)
usdc_address: constant(address) = 0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174 

# Event to log USDC balances
event USDBalances:
    _address: address
    _balance: uint256


@external
def getUSDCBalances(addresses: address[500]) -> uint256:

    
    # Loop through the addresses and get their USDC balances
    for addr in addresses:
        usdc_balance: uint256 = ERC20(usdc_address).balanceOf(addr)
        if (usdc_balance > 0):
            log USDBalances(addr,usdc_balance)
    
    return 0
