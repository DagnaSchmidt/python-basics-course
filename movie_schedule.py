current_movies = {
    'Wonka': '19:00pm',
    'Blue Beetle': '11:00am',
    'The Retirement Plan': '21:00pm'
}

print('We are currently showing:')
for key in current_movies:
    print(key)

movie = input('What movie would you like a showtime for?\n')

showtime = current_movies.get(movie)

if showtime == None:
    print('Requested movie is not playing')
else:
    print(showtime)