from pathlib import Path

path=Path('D:\github_repository\My_studyproject\python\Python编程从入门到实践\chapt10_file\guest.txt')

while True:
    contents=input("Enter your name(enter 'q' to quit): ")
    if contents=='q':
        break
    contents+='\n'
    path.write_text(contents)   #写入文件

