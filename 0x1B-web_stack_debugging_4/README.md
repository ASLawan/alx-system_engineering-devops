# 0x1B Web stack debugging #4
Continuation of debugging projects.
In today's project we are expecting to figure out why our nginx server  
is unable to handle beyond a certain number requests at a time  

This was handled by writing a puppet manifest that increases the ulimit  
of the server to an even higher value  

The second part of the debugging project involved setting up file limits   
for user holberton.  
This was done to ensure the said user can login and open files without any error meessages.
