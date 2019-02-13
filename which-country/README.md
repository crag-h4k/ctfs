# Which country is scanning us?

flag: Poland 

    # Solution

        wireshark gud.pcapng

    #filters:

        #to see dest:

            tcp.flags.reset eq 1

        #to see src:

            tcp.nalysis.flags && !tcp.analysis.window_update

        # 193.59.101.240 



    #then geoiplookup

        #browser

            firefox http://geoiplookup.net/ip/193.59.101.240 

        #Bash 

            geoiplookup 193.59.101.240 
