'''
import paramiko

#pip install paramiko

ip="192.168.0.192"
password="winteck@2025"
port=22
username="root"



def exec_cmd() :                         #keep this entire code in one resusable function
ssh = paramiko.SSHClient()  #ssh object  #sshclient is a module  inside paramiko class #This line is used in Python to create an SSH connection to a remote Linux system using the paramiko library.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #whenever we do shh it will ask password,to ignore the password we need to add the some host keys to ssh  
ssf.connect(ip,port=port,username='UserName',password='Password',timeout=3)#when we are working with remote we use ip ,password,port number,post name(username)

#after connectiong we execute the command we have method called ssh.excute

  #once we send command we get three response from target,that response we need to capture 
stdin,stdout,stderr=ssh.exec_command(cmd)

stderr(standard error) ---> command execute succesfully ,but not a valid command
rm -rf file1.py if file not their (not such file or directory not their)

1.when ever there is a error in your command  output that error capture in "standard error"(stderr)

2.command execute succesfully output store in "standard output "(stdout)

3.when you are trying to remove file , but you don't have permission to remove(permission denied)that output stored in "standard input",command execute succesfully but permission denied
'''


import paramiko

ip="192.168.0.192"
password="winteck@2025"
port=22
username="root"

def exec_cmd():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port=port,username='UserName',password='Password',timeout=3)
    
    stdin,stdout,stderr=ssh.exec_command("lsblk")
    if stderr:
        raise Exception("Command executio  got failed",stderr.read())
    else:
        return stdout.read()
