

def make_album(album_name,singer_name,number=None):
    album={'album_name':album_name,'singer_name':singer_name}
    if number:
        album['number']=number
    return album


while True:
    print("Enter 'q' at any time to quit.")
    album_name=input("The album_name: ")
    if album_name=='q':
        break

    singer_name=input("The singer_name: ")
    if singer_name=='q':
        break

    number=input("songs_number: ")
    if number=='q':
        break
    
    if number=='None':
        music=make_album(album_name,singer_name)
    else:
        music=make_album(album_name,singer_name,number)
    
    print(music)

