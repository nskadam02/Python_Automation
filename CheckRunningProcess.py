import psutil
import sys
def ProcessMonitor(name):  
   for pid in psutil.pids():
        try:
            p = psutil.Process(pid)
            if len(p.name())>1:
                if name in p.name():
                    return True
                else:
                    pass
        except:
            return False
def main():
      print("Process Monitoring Script")
      process=ProcessMonitor(sys.argv[1])
      if process==True:
          print("Process is running")
      else:
          print("Process is not running")    
if __name__=="__main__":
    main()
