import time
import webbrowser

total_breaks=3
break_count=0

print("The program start on  "+time.counttime())
while(break_count<total_breaks):
    time.sleep(10)
    webbrowser.open("http://www.youtube.com")
    break_count=break_count+1
