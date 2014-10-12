ENTRIES_PER_ROW = 8
LONELIES_PER_ROW = 16
INPUT_FILENAME = 'hsk3.txt'
CAPTION = 'HSK3 Words indexed by characters'

f = open(INPUT_FILENAME, 'r')

words = []
chars = {}
lonely_words = []

for line in f:
	words.append(line.rstrip().decode('utf-8'))

def stringify_with_commas(s):
	n = len(s)
	text = ''
	for word in s:
		text = text + word
		n = n - 1
		if n > 0:
			text = text + ', '
	return text


for word in words:
	for char in set(word):
		if ord(char) != 65279:
			if char not in chars:
				chars[char] = []
			chars[char].append(word);

print "<html><head><meta charset=\"UTF-8\"><title>Chinese word list</title></head><body>"
print "<center><table style =\"width:80%\"><tr><td>"
print "<table style=\"width:100%\">"

print "<center><h1>" + CAPTION + "</h1></center>"

c = 0

wid = 100.0 / ENTRIES_PER_ROW

for char in chars:
	n = len(chars[char])
	if n > 1:
		if c == 0:
			print "<tr>"

		print "<td style=\"vertical-align:text-top; width:{:.2f}%\">".format(wid)
		print "<center>"
		print "<h1>" + char.encode('utf-8') + "</h1>"

		for char in sorted(chars[char], key = lambda a: len(a)):
			print char.encode('utf-8')
			print "<br>"

		print "</center>"

		c = c + 1
		if c >= ENTRIES_PER_ROW:
			c = 0
	else:
		lonely_word = chars[char][0]
		any_higher = False
		for char in lonely_word:
			any_higher = any_higher or (len(chars[char]) > 1)
		if not any_higher:
			lonely_words.append(lonely_word)

print "</table>"
print "<center><h2>Words with unique characters</h2></center>"

wid2 = 100.0 / LONELIES_PER_ROW

c = 0

print "<table style=\"width:100%\">"

for word in sorted(set(lonely_words), key = lambda a: len(a)):
	if c == 0:
		print "<tr>"
	print "<td style=\"vertical-align:text-top; width:{:.2f}%\">".format(wid2)
	print "<center><h2>" + word.encode('utf-8') + "</h2></center>"
	c = c + 1
	if c >= LONELIES_PER_ROW:
		c = 0

print "</table>"
print "</table></center>"
print "</body></html>"

