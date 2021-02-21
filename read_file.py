text_file = open('pelican.txt', 'r')
read_text = text_file.read()

# print(type(read_text))
# print(read_text)

pelican_list = read_text.splitlines() # splitlines method creates a list

# print(type(pelican_list))
# print(pelican_list)

for line in open('pelican.txt', 'r') :
        print(line, end="")
        # print(line) # this prints new line because of '\n', end removes this
