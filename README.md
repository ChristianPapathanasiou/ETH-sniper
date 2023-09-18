# ETH sniper
 
ETH sniper is a tool which generates ETH addresses and corresponding private keys starting from a starting position (index) all the way to an end index eg. create all private keys from 1 to 10,000,000. 

ETH sniper works in conjunction with the Sniper smart contract which concurrently checks  500 addresses supplied by ETH sniper for USDC balances.

Similar tools check each generated wallet sequentially using infura and this is very time consuming and does not scale.

By leveraging the smart contract we are able to very quickly batch check hundreds of addresses at the same time to check if any of them have a positive balance.

If an address is found which has a positive USDC balance, then the deployed ETH sniper contract will emit an event that is observable on the blockchain and can be alerted upon using conventional blockchain event alerting tools.

Update:
In v2, I have now integrated Tenderly simulations to run the contract executions against the tenderly API and to parse the Tenderly API JSON reply to check if any logs were emmited from the contract which would indicate an address was found with a positive balance. By using Tenderly simulations we do not need to execute these transactions on the blockchain adding a) a layer of stealth execution and b) saving on gas costs.

Created as a proof of concept, no liability accepted. This will never work and liklihood of finding any wallet with a positive balance is infinitesimally small. 

- C. Papathanasiou
