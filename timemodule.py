import time

initial1=time.time()
k=0
while(k<45):
    print("Hello World")
    time.sleep(1) # stops the time for 1 second
    k+=1
print(f"While loop took {time.time()-initial1} seconds to run")

initial2=time.time()
for i in range(45):
    print("Hello World")
print(f"For loop took {time.time()-initial2} seconds to run")

localtime=time.asctime(time.localtime(time.time()))
print(localtime)
