import pandas as pd

purchase_1 = pd.Series({'Name': 'Rushil',
                       'Item Purchased': 'Watch',
                       'Cost': 50})

purchase_2 = pd.Series({'Name': 'Sunita',
                       'Item Purchased': 'Purse',
                       'Cost': 75})


purchase_3 = pd.Series({'Name': 'Mukesh',
                       'Item Purchased': 'Jivan Charitra',
                       'Cost': 25,
                       'Gamer': 58})

purchase_4 = pd.Series({'Name': 'Joe',
                       'Item Purchased': 'Can',
                       'State': 'New York',
                       'Cost': 78})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3, purchase_4], index = ['Store 1', 'Store 1', 'Store 3', 'Store 5'])

df.head()
