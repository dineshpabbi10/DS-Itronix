#sudo pip install quandl
import quandl
import matplotlib.pyplot as plt
dataset1=quandl.get("NSE/SBIN", authtoken="x8VdDXzBty3iGsaRLTVs")
print dataset1
for i in range(0,4):
	print dataset1['Open'][i]
my_data=dataset1['Open']
print my_data
plt.plot(my_data)
plt.title('SBI Stock Prices')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.savefig('SBI.pdf')
plt.show()


