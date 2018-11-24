#pip3 install beautifulsoup4
#pip3 install google

try:
	from google import search
except ImportError:
	print("no module named 'google' found")

query="Geeksforgeeks"

for j in search(query, tld="co.in", num=10, stop=1, pause=2):
	print(j)

