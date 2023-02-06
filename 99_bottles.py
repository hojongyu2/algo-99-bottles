
def bottle_song():
	# write your code here!
	numberOfBeer = 100
	while numberOfBeer > 0:
		if numberOfBeer == 1:
			print(f'{numberOfBeer} bottles of beer on the wall, {numberOfBeer} bottles of beer.')
			print('Take one down and pass it around, no more bottles of beer on the wall.')
			print('No more bottles of beer on the wall, no more bottles of beer.')
			print('Go to the store and buy some more, 99 bottles of beer on the wall.')
			break
		print(f'{numberOfBeer} bottles of beer on the wall, {numberOfBeer} bottles of beer.')
		numberOfBeer = numberOfBeer -1
		print(f'Take one down and pass it around, {numberOfBeer} bottles of beer on the wall.')
bottle_song()
# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down and pass it around, 98 bottles of beer on the wall.