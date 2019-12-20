import os
import sys
def  ReplaceFileWithExtension(path,extension,newExtension):
    flag=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path);
        

    exists=os.path.isdir(path)

    if exists:
        for Folder,Subfolder,Files in os.walk(path):
            for filename in Files:
               if filename.endswith(extension):
                  print("old fiename:",filename,end=" ") 
                  newFile=os.path.splitext(filename)[0]+newExtension;
                  print("new Fiename:",newFile)


    else:
        print("Invalid Path")



def main():
    if((len(sys.argv)<2)):
        print("Error Invalid number of argument");
        print("You can use -h =For help -u=knowing usage")
        exit();
    if (sys.argv[1]=="-h") or (sys.argv[1]=="-H"):
        print("This script is designed for file duplication");
        exit();
    if (sys.argv[1]=="-u") or (sys.argv[1]=="-U") :
        print("usage:Application_name absolutePath_of_directory file_extension_to_search file_extension_to_replace");
        exit();
    try:
        ReplaceFileWithExtension(sys.argv[1],sys.argv[2],sys.argv[3]);
    except ValueError:
        print("Error:Invalid datatype of input")
    except Exception:
        print("Error:Invalid Input")    


if __name__=="__main__":
    main()        
