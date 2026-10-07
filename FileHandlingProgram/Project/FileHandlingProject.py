from pathlib import Path
import os
def createFile():
                 try :
                       name=input('plz tell your file name..:- ')
                       path=Path(name)
                       if not path.exists():
                                       with open(name,'w') as f :
                                               data =input('file is not exist ,creating new file ,what is you want write something..  :- ')
                                               f.write(data)
                                               print('succesfully create file')
                       else :
                        print('error file is already present...')                               
                 except Exception as err :
                                          print(f'this is exception {err}')

def readFile():
               try:
                name =input('Enter the file name:')
                path=Path(name)
                if path.exists():
                                        with open(path,'r') as fr:
                                                content=fr.read()
                                                print(f'your file content is: \n{content}')
               except Exception as err:
                                print(f'error is {err}')                                             
                                                  
def updateFile(): 
                try:
                        print('options...')
                        print('choose 1 for update for file name')
                        print('choose 2 for update the content')
                        print('choose 3 for overwrite the content')
                        choice=int(input('Enter the options..:- '))
                        if choice == 1 :
                                        old_file=input('Enter the file Name which you want change the name:')
                                        old_name=Path(old_file)
                                        if old_name.exists() :
                                                        new_file=input('Enter the new name:')
                                                        new_name=Path(new_file)
                                                        old_name.rename(new_name)
                                                        print("File renamed successfully")
                                                        prev=input('if want previous menu...say Y/y or N/n:- ')
                                                        if prev == 'y' or prev =='Y' :
                                                                                      updateFile()
                                                        else :
                                                             return                                
                                                        
                                        else :
                                                print('File not present..')
                        elif choice ==2 :
                                        old_file=input('Enter the file Name which you want change the content:')
                                        old_name=Path(old_file)
                                        if old_name.exists() :
                                                        newData=input('Enter the new add content:')
                                                        with open(old_name,'a') as f :
                                                                                        f.write(' '+newData)
                                                                                        print("File is updated content  successfully")
                                                                                        prev=input('if want previous menu...say Y/y or N/n')
                                                                                        if prev == 'y' or prev =='Y' :
                                                                                          updateFile()
                                                                                        else :
                                                                                             return   
                                        else :
                                          print('File not present..')      
                        elif choice ==3 :
                                        old_file=input('Enter the file Name which you want to overwrite:')
                                        old_name=Path(old_file)
                                        if old_name.exists() :
                                                        newData=input('Enter the new content:')
                                                        with open(old_name,'w') as f :
                                                                                        f.write(newData)
                                                                                        print("File is overwritten successfully")
                                                                                        prev=input('if want previous menu...say Y/y or N/n:- ')
                                                                                        if prev == 'y' or prev =='Y' :
                                                                                         updateFile()
                                                                                        else :
                                                                                             return                                    
                                        else :
                                          print('File not present..')


                        else :
                               print('Worng Option ! please select the right options..')                   
                except Exception as err:
                                                print(f'error is {err}')                                                        
def delFile():
              try :
                   fileName=input('Enter the file name which you want to delete:- ')        
                   delFileName =  Path(fileName)
                   if delFileName.exists():
                                           os.remove(delFileName)
                                           print("File deleted successfully")
                   else :
                         print('File not present..')
              except Exception as err :
                                        print(f'error is {err}')          

print('Press 1 for create file ....')
print('Press 2 for read file ....')
print('Press 3 for update file ....')
print('Press 4 for delete file ....')

a=int(input('tell your response..:= '))

if a==1 :
         createFile()
elif a==2 :
         readFile()
elif a==3 :
         updateFile()
elif a==4 :
         delFile()  
else :
       print('Wrong options! plz select right options')                          