import multiprocessing
import os

def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))

# #we do this next part for the script to be runnable.  it is basically saying the name of the file is the entry point to the program
# if __name__ == "__main__":
    whoami("Im the main program")
    for n in range(4):
        p = multiprocessing.Process(target=whoami,
          args=("I'm function %s" % n,))
        p.start()