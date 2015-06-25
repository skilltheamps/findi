# findi
tool to easily discover unindexed but interesting deep web content

// DISCLAIMER This is a proof of concept and nowhere near a production tool //

findi_scan.py is basically a simple port scanner that searches only for port 80. When it finds one that is open it pulls the data, searches it for keywords and puts it in a simple database. 

findi_list.py is super simple and just dumps the database on the screen. It shows title of the page, size and a few hints like whether it's a router or a printer etc. (more hints can be added in findi_scan.py based on keywords).
You can then look for interesting things and (at least in Gnome's terminal) open the links with ctrl+click

How to use:
 - in findi_scan.py see lines 173-175 to set the range it should scan. It's ipv4 only xxx.xxx.i.j with i and j being for-loops. You want to scan around private people's ips since they're the ones having lots of funny stuff mindlessly online. To decide for a range you can just visit a site like https://www.whatismyip.com/ and then go from a few hundred devices below your ip to a few hundred above
 - in findi_scan.py you find "while(runningCtr >= 30):". This limits the number of maximum connections. You can set this higher if you have a good internet connection. Don't set it too high though since you're basically running DDOS against yourself and answers might not get back to your computer
 - run "python3 ./findy_scan"
 - run "python3 ./findy_list"
 - ctrl+click on interesting links to open them
 - you can rename the "data" folder to backup your database so that you can run a new scan on another range and not have the lists of results mixed with links you already visited
