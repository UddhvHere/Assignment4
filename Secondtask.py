try:
    file=open('output.txt', 'w')
    r_file=file.write(input('enter text to write to the file:'))
    file.close()
    print('Data successfully written to output.txt.')
except:
    print('error')
try:
    file=open('output.txt', 'a')
    a_file=file.write("\n"+input('write the text to enter?'))
    file.close()
    print('Data successfully appended.')
except:
    print('error')
file0=open('output.txt','r')
read0=file0.read()
file0.close()
print('Final content of output.txt:',"\n" , read0)


