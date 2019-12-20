import psutil
def ProcessMonitor():
  
    listprocess=[]
    fobj=open("Process.log",'w')
    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            fobj.write(str(pinfo)+'\n')      
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass   
     
def main():
      print("Process Monitoring Script")
      ProcessMonitor()
     
if __name__=="__main__":
    main()
