get_ipython().getoutput("pip install pandas")


filename = 'prabowo.csv'
search_keyword = 'prabowo until:2023-12-12 since:2023-07-20'
limit = 50


get_ipython().getoutput("npx --yes tweet-harvest@latest -o filename -s search_keyword -l {limit} --token """)



