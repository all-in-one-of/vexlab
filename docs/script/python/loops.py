
#############
# Loops
#############


# Simple for loop that prints each individual character/letter in the given string
word = '東京市大学院'
for letter in word:
    print(letter)

# For each item in the list, that item gets printed out
songs = ['ミラージュ', '劣等上等', 'サイサキ']
for music in songs:
    print(music)

# Prints each single numbered value up to a specific value index
for index in range(10):
    print(index)

# Prints each single numbered value based on a given range
for i in range(3, 15):
    print('The value for i is ' + str(i))

# Prints out all of the elements in that list based on its index value
songs = ['ミラージュ', '劣等上等', 'サイサキ']
for index in range(len(songs)):
    print(songs[index])

# Prints out the index value of each item in the list
songs = ['ミラージュ', '劣等上等', 'サイサキ']
for index in range(len(songs)):
    print(index)

# Prints out the index value of each item in the list
songs = ['ミラージュ', '劣等上等', 'サイサキ']
for index in range(len(songs)):
    if index == 0:
        print('First Track = ' + str(songs[index]))
    elif index == 1:
        print('Second Track = ' + str(songs[index]))
    else:
        print('Unknown Track = ' + str(songs[index]))
