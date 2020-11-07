#!/usr/bin/python3

from colorama import Fore, Back, Style 
 
import sys, getopt,os

print( Fore.GREEN+"..................................................................................................................")
print( "..................................................................................................................")
print( "......................iiii..........tttt...............tttt.......................................................")
print( ".....................i::::i......ttt:::t............ttt:::t.......................................................")
print( "......................iiii.......t:::::t............t:::::t.......................................................")
print( ".................................t:::::t............t:::::t.......................................................")
print( "...ggggggggg...gggggiiiiiiittttttt:::::tttttttttttttt:::::ttttttt........eeeeeeeeeeee....rrrrr...rrrrrrrrr........")
print( "..g:::::::::ggg::::gi:::::it:::::::::::::::::tt:::::::::::::::::t......ee::::::::::::ee..r::::rrr:::::::::r.......")
print( ".g:::::::::::::::::g.i::::it:::::::::::::::::tt:::::::::::::::::t.....e::::::eeeee:::::eer:::::::::::::::::r......")
print( "g::::::ggggg::::::gg.i::::itttttt:::::::tttttttttttt:::::::tttttt....e::::::e.....e:::::err::::::rrrrr::::::r.....")
print( "g:::::g.....g:::::g..i::::i......t:::::t............t:::::t..........e:::::::eeeee::::::e.r:::::r.....r:::::r.....")
print( "g:::::g.....g:::::g..i::::i......t:::::t............t:::::t..........e:::::::::::::::::e..r:::::r.....rrrrrrr.....")
print( "g:::::g.....g:::::g..i::::i......t:::::t............t:::::t..........e::::::eeeeeeeeeee...r:::::r.................")
print( "g::::::g....g:::::g..i::::i......t:::::t....tttttt..t:::::t....tttttte:::::::e............r:::::r.................")
print( "g:::::::ggggg:::::g.i::::::i.....t::::::tttt:::::t..t::::::tttt:::::te::::::::e...........r:::::r.................")
print( ".g::::::::::::::::g.i::::::i.....tt::::::::::::::t..tt::::::::::::::t.e::::::::eeeeeeee...r:::::r.................")
print( "..gg::::::::::::::g.i::::::i.......tt:::::::::::tt....tt:::::::::::tt..ee:::::::::::::e...r:::::r.................")
print( "....gggggggg::::::g.iiiiiiii.........ttttttttttt........ttttttttttt......eeeeeeeeeeeeee...rrrrrrr.................")
print( "............g:::::g...............................................................................................")
print( "gggggg......g:::::g...............................................................................................")
print( "g:::::gg...gg:::::g...............................................................................................")
print( ".g::::::ggg:::::::g...............................................................................................")
print( "..gg:::::::::::::g................................................................................................")
print( "....ggg::::::ggg..................................................................................................")
print( ".......gggggg.....................................................................................................\n")



def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hs:i:",["search=","install="])
   except getopt.GetoptError:
      print ('USAGE : gitter -s  --search toolname , -i --install toolname')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('USAGE : gitter -s  --search toolname')
      
         sys.exit()
      elif opt in ("-s", "--search"):
         inputfile = arg
         searching(inputfile)
      elif opt in ("-i", "--install"):
         outputfile = arg
 
def searching(wee):
    import os   
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
   
  
# to search 
    import os
    query = "github/"+wee
    x=list()
    outFileName="/tmp/search.txt"
    outFile=open(outFileName, "w")
    
  
    for j in search(query, tld="com", num=10, stop=10, pause=2): 
        outFile.write(j+"\n")
        x.append(j)
    outFile.close() 
    os.system(' cat /tmp/search.txt | grep https://github.com | cut -d / -f 1,2,3,4,5 > /tmp/search2.txt')
    cmd="cat /tmp/search2.txt | awk -F / '{print $4'}"
    my=os.popen(cmd).read()
    print(Fore.RED+'The following authors tools are found:')
    print(Fore.BLUE+"[+]note:All the tools listed here are according to their rating\n")
    
    a=my.split()
    a = list(dict.fromkeys(a))
    x=1;
    if "topics" in a:
           a.remove("topics")
    
    for i in a:
    	print(Fore.YELLOW+str(x)+ "."+i)
    	x+=1 
    i=input(Fore.CYAN+"enter your choice:")
    f=open("/tmp/search2.txt","r")
    list_of_lists = []
    for line in f:
      
      list_of_lists.append(line)
      				    
    link=list_of_lists[int(i)-1]
    dependecy=["apt install","apt-get install","pip install","pip3 install","gem install","cargo install","npm install","snap install"]


    s= input("Enter the location:")
    st="pip"
    os.system("cd "+s+"&& sudo git clone "+link.rstrip()+" "+wee)
    for i in dependecy:
           c=" cd "+s+"/"+wee+" && cat *[rR][eE][aA][dD]* | grep '"+ i+"'"
           m=os.popen(c).read()
           #print(m)
           sad=m.split("\n")

           for j in sad:
                  j=j.strip()
                  if j[0:1] == '$':
                         j=j[1:]
                  if st in m:
                         os.system("cd "+s+"/"+wee+" && pip install -r requirements.txt")
                         os.system("cd "+s+"/"+wee+" && pip3 install -r requirements.txt")
                         os.system("cd "+s+"/"+wee+" && sudo python3 setup.py install")
                         os.system("cd "+s+"/"+wee+" && sudo python2 setup.py install")
                         os.system("sudo pip3 install "+wee)
                         os.system("sudo pip install "+wee) 
                  elif(len(j)!=0): 
                          os.system("sudo "+j)
                
                 
if __name__ == "__main__":
   main(sys.argv[1:])

   
