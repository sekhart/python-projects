# Make an empty list for storing aliens.
aliens = []
i = 0
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': i, 'speed': 'slow'}
    aliens.append(new_alien)
    i = i + 1
# Show the first 5 aliens:
for alien in aliens[0:15]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = i + 1
        alien['speed'] = 'fast'
    print(alien)
print("...")
print(aliens)
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
