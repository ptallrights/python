#!/usr/bin/env python  
def cpu_stat():  
    cpu = []  
    cpuinfo = {}  
    f = open("/proc/cpuinfo")  
    lines = f.readlines()  
    f.close()  
    for line in lines:  
        if line == '\n':  
            cpu.append(cpuinfo)  
            cpuinfo = {}  
        if len(line) < 2: continue  
        name = line.split(':')[0].rstrip()  
        var = line.split(':')[1].strip() 
        cpuinfo[name] = var
#    print cpuinfo.keys()
#    print cpu
    return cpu

if __name__ == "__main__":
    print cpu_stat()
