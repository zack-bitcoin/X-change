new_user: address signature
  add to datastructure users
  generate address for depositing to
withdraw: currency amount address_to_send_to address_for_identification signature
  if they have that much +12 block confirmationtime:
      remove amount from currency for username
      send amount of currency to address
  else:
      error_page
trade: currency1 amount1 currency2 amount2 address signature
  decrease currency2 by amount2
  while I can buy more for better than this price:
    buy more at better price
      remove/adjust entry from BTC/LTC_bids
      add entry to trades
      increase money in 2 places.
  if I still want to buy more:
    submit bid at price
      add entry to BTC/LTC_bids
undo_trade: trade_id address signature
  remove entry from BTC/LTC_bids
  increase money in 1 place.
mainpage:
  graphs
  download links 
userdata: address password
  amount of each cryptocurrency on hold.
  amount of each cryptocurrency
  bids

datastructures...
  users
    main address or NamecoinID <--sorted by this
    amount of each cryptocurrency with nlocktimes
    amount of each cryptocurrency ready to spend
    bids
  BTC/LTC_bids
    an ordered list of the same bids as in the users database.
  BTC/LTC_graph
    new one made frequently. generated from BTC/LTC_bids.
  BTC/LTC_trades
    list of trades made in the last N blocks. who, what, how much.

cron every block
  generate new graph
