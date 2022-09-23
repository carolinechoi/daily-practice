def playlist(songs):
    # Write your code here
    counter = 0
    for j in range(len(songs)):
        for i in range(j+1, len(songs)):
            song_length = songs[j] + songs[i]
            if song_length % 60 == 0:
                counter += 1    
    print(counter)
    return counter

playlist([])