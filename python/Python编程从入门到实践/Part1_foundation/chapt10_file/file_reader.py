from pathlib import Path

path=Path("D:\github_repository\My_studyproject\python\Python编程从入门到实践\chapt10_file\pi_million_digits.txt")
contents = path.read_text().rstrip()    #链式调用

#lines=contents.splitlines()

pi_string=''
for line in contents.splitlines():
    pi_string+=line.lstrip()

birthday=input("Enter your birthday , in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appears in the first million digits of pi.")