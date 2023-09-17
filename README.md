# ETH sniper
 
ETH sniper is a tool which generates ETH addresses and corresponding private keys starting from a starting position (index) all the way to an end index eg. create all private keys from 1 to 10,000,000. 

ETH sniper works in conjunction with the Sniper smart contract which concurrently checks  100 addresses supplied by ETH sniper for USDC balances.

Similar tools check each generated wallet sequentially using infura and this is very time consuming and does not scale.

By leveraging the smart contract we are able to very quickly batch check hundreds of addresses at the same time to check if any of them have a positive balance.

If an address is found which has a positive USDC balance, then the deployed ETH sniper contract will emit an event that is observable on the blockchain and can be alerted upon using conventional blockchain event alerting tools.

Created as a proof of concept, no liability accepted. This will never work and liklihood of finding any wallet with a positive balance is infinitesimally small. Running this will likely result in spending all your funds in your wallet in gas fees.

- C. Papathanasiou