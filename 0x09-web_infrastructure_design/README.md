# 0x09. Web infrastructure design
__Web infrastructure__ refers to the underlying technology and architecture that supports the function of a website and makes it accessible to users. It is the machinery that powers our online presence.  
The current project involved learning and understanding how the web works, the different infrastructure that makes possibe.  
The second part of the project involved, using the knowledge to design various infrastructures.  
## Project Tasks  
### Task 0: Simple web stack
This task involved whiteboarding and designing a one server web infrastructure that hosts the website that is reachable via www.foobar.com.  
#### **Requirements:**  
	- 1 server  
	- 1 web server(Nginx)  
	- 1 application server  
	- 1 application files (your code base)  
	- 1 database  
	- 1 domain name __foobar.com__ configured with a __www__ record that points to your server IP __8.8.8.8__  
#### **Possible Issues:**  
	- **SPOF:**  
SPOF stands for Single Point Of Failure. This refers to a situation in which a component or process failure can bring down the entire system or significantly disrupt its functionality. It is a weak link in the design.  
In our design above, the single server is a SPOF. If the server crashes, we won't be able to access the website.  
	- **Downtime:**    
When maintenance is needed there must be downtime since we have to restart the server.
	- **Scaling:**   
Our current design cannot scale to handle more than a certain amount of traffic.  
Given that the design has just a single server, if we have traffic beyond the servers capacity, it is not possible to scale up and handle excess traffic.  

### Task 1: Distributed wen infrastructure
Here, we tried to improve on the shortcomings in the Simple web stack design. In this design we are making the infrastructure more robust, by adding more devices.
#### **Requirements:**    
	- 2 servers  
	- 1 web server (Nginx)  
	- 1 application server  
	- 1 load-balancer (HAproxy)  
	- 1 set of application files (code base)  
	- 1 database (MYSQL)  
#### **Issues:**  
	- **SPOF**    
In the current design, the HAproxy load balancer is a SPOF. Since we have just one load balancer, if it breaks down, our system crashes.
	- **No firewall, no HTTPS:**    
The current design does not have firewall, making the design vunerable to attacks. Our current design does not have an SSL certificate meaning the user is accessinig our website over an insecure connection.  
	- **Monitoring:**    
In the current design, our system is not being monitored, meaning we cannot tell if our system is performing well or not. We cannot tell if our system is being attacked. We cannot easily tell which part of our design needs to be improved upon.  

### Task 2: Secured and monitored web infrastructure
In the current task, we made improvementsto the previous design. To add security and monitoring to the design, we added 3 firewalls, 3 monitoring clients and an SSL certificate.  
#### **Requirements:**  
	- 3 firewalls  
	- 1 SSL certificate to server __www.foobar.com__ over HTTPS  
	- 3 monitoring clients  
#### **Issues:**    
	- **Terminating SSL at load balancer:**  
Terminating SSL at load balancer level (SSL offloading) offers some advantages like performance improvement and simplified certificate management but also introduces security and operational concerns.
	- Advantages:  
		- Performance: offloading task to load balancer frees up processing power on webserver, improving website performance.    
		- Certificate management: managing SSL certificate for multiple servers can be cumbersome. Centralizing it on the load balancer simplifies the process.
	- Disadvantages:  
		- Man-in-the-Middle-Attack    
Traffic between the load balancer and webservers is unencrypted, making it vulnerable to eavesdropping.  
		- Lack of visibility    
		- Application compatibility    
Some applications might rely on a server-specific SSL features not available with offloading.  
		- Session stickiness   
	- **Having only one MYSQL server capable of accepting writes**  
		- Single point of failure  
		- Limited scalability  
		- No High Availability  
		- Maintenance challenges  

