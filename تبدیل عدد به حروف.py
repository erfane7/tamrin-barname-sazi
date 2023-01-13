#tabdil adad be horoof
#erfan eslami kahriz
#kelas sunday 7:45

import sys

digit_text = {
	'00': 'Zero',
	'01': 'One',
	'02': 'Two',
	'03': 'Three',
	'04': 'Four',
	'05': 'Five',
	'06': 'Six',
	'07': 'Seven',
	'08': 'Eight',
	'09': 'Nine',
	'10': 'Ten',
	'11': 'Eleven',
	'12': 'Twelve',
	'13': 'Thirteen',
	'14': 'Fourteen',
	'15': 'Fifteen',
	'16': 'Sixteen',
	'17': 'Seventeen',
	'18': 'Eighteen',
	'19': 'Nineteen',
	'20': 'Twenty',
	'30': 'Thirty',
	'40': 'Forty',
	'50': 'Fifty',
	'60': 'Sixty',
	'70': 'Seventy',
	'80': 'Eighty',
	'90': 'Ninety',
}

cats = ['Billion', 'Million', 'Thousand']


def convert_hundred(a):
	a = str(a)
	if len(a) < 2:
		a = '0' + a
	if a[0] == '1' or a[1] == '0':
		return digit_text[a]
	else:
		if int(a) < 10:
			return digit_text['0' + a[1]]
		else:
			return digit_text[a[0] + '0'] + ' ' + digit_text['0' + a[1]]


def convert_thousand(a):
	assert a < 1000
	if a < 10:
		return digit_text['0' + str(a)]
	if a < 100:
		return convert_hundred(a)
	a = str(a)
	if a[1:] == '00':
		return f"{digit_text['0'+a[0]]} Hundred"
	return f"{digit_text['0'+a[0]]} Hundred {convert_hundred(int(a[1:]))}"


def convert(a):
	a = str(a)
	a = a.zfill(12)
	s = []
	for (i, cat) in enumerate(cats):
		start, end = i * 3, (i + 1) * 3
		if int(a[start:end]) > 0:
			s.append(convert_thousand(int(a[start:end])) + ' ' + cat)
	if int(a[-3:]) > 0:
		s.append(convert_thousand(int(a[-3:])))
	if s:
		return ', '.join(s)


def testRandom():
	import random
	k = random.randrange(999999999999)
	print(k)
	print(convert(k))


if __name__ == '__main__':
	for arg in sys.argv[1:]:
		try:
			k = int(arg)
		except ValueError:
			print(f'{arg}: non-numeric argument')
		else:
			if k > 999999999999:
				print(f'{k}: number must be less than 999,999,999,999')
			else:
				print(f'{k}\t{convert(k)}')
erfan=int(input("enter number : "))
print(convert(erfan))
