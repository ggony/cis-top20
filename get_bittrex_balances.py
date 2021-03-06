from cis import BittrexPortfolio

portfolio = BittrexPortfolio()
balance_df = portfolio.get_balances()

print('GETTING PORTFOLIO...')
print(balance_df.sort_values(by='BTC_value', ascending=False))
print()
print('TOTAL PORTFOLIO')
print('BTC:', portfolio.get_btc_value())
print('USD:', portfolio.get_usd_value())
print()
print('CHECKING REBALANCING...')
print(portfolio.check_rebalancing())
