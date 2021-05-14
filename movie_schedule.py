movies_schedule = {
    'Radhe': '11.00am',
    'Ironman 3': '11.00pm',
    'Aquaman 3': '12.00am',
    'Batman 3': '2.00pm',
}

print('We are showing following movies:')

for key in movies_schedule:
    print(key)

movie = input("Which movie do you wanna see ?")

showtime = movies_schedule.get(movie)

if showtime:
    print('Movie timing is :', movies_schedule[movie])
else:
    print('requested movie is not available now')
