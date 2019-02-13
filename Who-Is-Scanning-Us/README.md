# Who is scanning us?

### Difficulty: intermediate 

### Type: network forensic

### Hint: Who is scanning us?

### Flag: Poland 

### Solution:

    ~$ wireshark gud.pcapng

    #filters:
    #to see dest:
    tcp.flags.reset eq 1

    #to see src:
    tcp.nalysis.flags && !tcp.analysis.window_update

    #you can easily see this IP 193.59.101.240 
    
    #then geoiplookup
    #via browser:
    ~$ firefox http://geoiplookup.net/ip/193.59.101.240 

    #bash CLI
    ~$ geoiplookup 193.59.101.240 
