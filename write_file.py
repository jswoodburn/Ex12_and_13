text_file = open('pelican.txt', 'a') # can use 'x', 'a' or 'a+' - 'x' will fail if file exists
text_file.write('A wonderful bird is the pelican,\n')
text_file.write('His bill holds more than his belican,\n')

lines = ['He can take in his beak,\n', 'Enough food for a week,\n', 'But I\u0027m damned if I see how the helican.\n']

text_file.writelines(lines)
