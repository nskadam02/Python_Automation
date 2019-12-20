import os
import sys
import checksum
def  DuplicateFileRemoval(path):
    flag=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path);
        

    exists=os.path.isdir(path)

    if exists:
        fobj=open("log.txt",'w')
        fobj.write("Duplicate Files"+'\n')
        data={}
        for Folder,Subfolder,Files in os.walk(path):
            for filename in Files:
                   src=os.path.join(Folder,filename)
                   check=checksum.CheckSum(src) 

                   if check in data:
                       data[check].append(src)
                    #    fobj.write(os.path.join(Folder,filename)+'\n')
                   else:
                       data[check]=[src]
        newData=[]
        newData=list(filter(lambda x: len(x)>1,data.values()));
        print(newData)
        count=0
        for outer in newData:
            icnt=0
            for inner in outer:
                icnt=icnt+1;
                if icnt>=2:
                    count+=1
                    print("Delete",inner);
                    fobj.write(inner+"\n")
                    os.remove(inner);

    else:
        print("Invalid Path")



def main():
    if(len(sys.argv)<2):
        print("Error Invalid number of argument");
        print("You can use -h =For help -u=knowing usage")
        exit();
    if (sys.argv[1]=="-h") or (sys.argv[1]=="-H"):
        print("This script is designed for file duplication");
        exit();
    if (sys.argv[1]=="-u") or (sys.argv[1]=="-U") :
        print("usage:Application_name absolutePath_of_directory");
        exit();
    try:
       DuplicateFileRemoval(sys.argv[1]);
    except ValueError:
        print("Error:Invalid datatype of input")
    except Exception as e:
        print("Error:Invalid Input",e)    


if __name__=="__main__":
    main()        
