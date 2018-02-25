# Wolfram Automata Rule 30 - Python
Naive python implementation of the Wolfram Automata Rule 30.


It's computed in a finite buffer, so to do that we use "cyclic buffer": the first bit has for left neighbour the latest bit of the line, and the last bit has for right neighbour the first bit of the line.


Just download and run the script you want to.



### Display Triangle

This script will display the rule 30 computed from a single bit.


Choose the number of lines and it will display something like :

                                    █                                
                                   ███                               
                                  ██  █                              
                                 ██ ████                             
                                ██  █   █                            
                               ██ ████ ███                           
                              ██  █    █  █                          
                             ██ ████  ██████                         
                            ██  █   ███     █                        
                           ██ ████ ██  █   ███                       
                          ██  █    █ ████ ██  █                      
                         ██ ████  ██ █    █ ████                     
                        ██  █   ███  ██  ██ █   █                    
                       ██ ████ ██  ███ ███  ██ ███                   
                      ██  █    █ ███   █  ███  █  █                  
                     ██ ████  ██ █  █ █████  ███████                 
                    ██  █   ███  ████ █    ███      █                
                   ██ ████ ██  ███    ██  ██  █    ███               
                  ██  █    █ ███  █  ██ ███ ████  ██  █              
                 ██ ████  ██ █  ██████  █   █   ███ ████             
                ██  █   ███  ████     ████ ███ ██   █   █            
               ██ ████ ██  ███   █   ██    █   █ █ ███ ███           
              ██  █    █ ███  █ ███ ██ █  ███ ██ █ █   █  █          
             ██ ████  ██ █  ███ █   █  ████   █  █ ██ ██████         
            ██  █   ███  ████   ██ █████   █ █████ █  █     █        
           ██ ████ ██  ███   █ ██  █    █ ██ █     █████   ███       
          ██  █    █ ███  █ ██ █ ████  ██ █  ██   ██    █ ██  █      
         ██ ████  ██ █  ███ █  █ █   ███  ████ █ ██ █  ██ █ ████     
        ██  █   ███  ████   ████ ██ ██  ███    █ █  ████  █ █   █    
       ██ ████ ██  ███   █ ██    █  █ ███  █  ██ ████   ███ ██ ███   
      ██  █    █ ███  █ ██ █ █  █████ █  ██████  █   █ ██   █  █  █  
     ██ ████  ██ █  ███ █  █ ████     ████     ████ ██ █ █ █████████ 
    ██  █   ███  ████   ████ █   █   ██   █   ██    █  █ █ █        █



### Generate Image

This script will create a PGM image of the rule 30 computed from a single bit. Choose the number of lines and it will create an image named output.pgm.


You can use ToyViewer (on MAC) or IrfanView (on Windows) to see the computed image (and export it in another format).
![Generated image](art/rule30_triangle_1000.png)

### Binarize text (tool)

    Message a binariser : abcde
    a = 01100001
    b = 01100010
    c = 01100011
    d = 01100100
    e = 01100101
    message with spaces: 01100001 01100010 01100011 01100100 01100101
    message: 0110000101100010011000110110010001100101

