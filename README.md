# war30-python
Naive python implementation of the Wolfram Automata Rule 30
It's computed in a finite buffer, so to do that we use "cyclic buffer": the first bit has for left neighbour the latest bit of the line, and the last bit has for right neighbour the first bit of the line.

Just download and run the script to get the following output:

                                    #                                
                                   ###                               
                                  ##  #                              
                                 ## ####                             
                                ##  #   #                            
                               ## #### ###                           
                              ##  #    #  #                          
                             ## ####  ######                         
                            ##  #   ###     #                        
                           ## #### ##  #   ###                       
                          ##  #    # #### ##  #                      
                         ## ####  ## #    # ####                     
                        ##  #   ###  ##  ## #   #                    
                       ## #### ##  ### ###  ## ###                   
                      ##  #    # ###   #  ###  #  #                  
                     ## ####  ## #  # #####  #######                 
                    ##  #   ###  #### #    ###      #                
                   ## #### ##  ###    ##  ##  #    ###               
                  ##  #    # ###  #  ## ### ####  ##  #              
                 ## ####  ## #  ######  #   #   ### ####             
                ##  #   ###  ####     #### ### ##   #   #            
               ## #### ##  ###   #   ##    #   # # ### ###           
              ##  #    # ###  # ### ## #  ### ## # #   #  #          
             ## ####  ## #  ### #   #  ####   #  # ## ######         
            ##  #   ###  ####   ## #####   # ##### #  #     #        
           ## #### ##  ###   # ##  #    # ## #     #####   ###       
          ##  #    # ###  # ## # ####  ## #  ##   ##    # ##  #      
         ## ####  ## #  ### #  # #   ###  #### # ## #  ## # ####     
        ##  #   ###  ####   #### ## ##  ###    # #  ####  # #   #    
       ## #### ##  ###   # ##    #  # ###  #  ## ####   ### ## ###   
      ##  #    # ###  # ## # #  ##### #  ######  #   # ##   #  #  #  
     ## ####  ## #  ### #  # ####     ####     #### ## # # ######### 
    ##  #   ###  ####   #### #   #   ##   #   ##    #  # # #        #
      #### ##  ###   # ##    ## ### ## # ### ## #  ##### # ##      ##
    ###    # ###  # ## # #  ##  #   #  # #   #  ####     # # #    ## 
    #  #  ## #  ### #  # #### #### ##### ## #####   #   ## # ##  ##  
    #######  ####   #### #    #    #     #  #    # ### ##  # # ### ##
           ###   # ##    ##  ###  ###   ######  ## #   # ### # #   # 
          ##  # ## # #  ## ###  ###  # ##     ###  ## ## #   # ## ###
    #    ## ### #  # ####  #  ###  ### # #   ##  ###  #  ## ## #  #  
    ##  ##  #   #### #   ######  ###   # ## ## ###  ######  #  ######
      ### #### ##    ## ##     ###  # ## #  #  #  ###     ######     
     ##   #    # #  ##  # #   ##  ### #  ##########  #   ##     #    
    ## # ###  ## #### ### ## ## ###   ####         #### ## #   ###   
    #  # #  ###  #    #   #  #  #  # ##   #       ##    #  ## ##  # #
     ### ####  ####  ### ########### # # ###     ## #  #####  # ### #
     #   #   ###   ###   #           # # #  #   ##  ####    ### #   #
     ## ### ##  # ##  # ###         ## # ##### ## ###   #  ##   ## ##
     #  #   # ### # ### #  #       ##  # #     #  #  # ##### # ##  # 
    ###### ## #   # #   #####     ## ### ##   ######## #     # # ####
           #  ## ## ## ##    #   ##  #   # # ##        ##   ## # #   
          #####  #  #  # #  ### ## #### ## # # #      ## # ##  # ##  
         ##    ######### ####   #  #    #  # # ##    ##  # # ### # # 
        ## #  ##         #   # ######  ##### # # #  ## ### # #   # ##
    #  ##  #### #       ### ## #     ###     # # ####  #   # ## ## # 
    #### ###    ##     ##   #  ##   ##  #   ## # #   #### ## #  #  # 
    #    #  #  ## #   ## # ##### # ## #### ##  # ## ##    #  ####### 
    ##  ########  ## ##  # #     # #  #    # ### #  # #  #####       
    # ###       ###  # ### ##   ## #####  ## #   #### ####    #     #
      #  #     ##  ### #   # # ##  #    ###  ## ##    #   #  ###   ##
    #######   ## ###   ## ## # # ####  ##  ###  # #  ### #####  # ## 
    #      # ##  #  # ##  #  # # #   ### ###  ### ####   #    ### #  
    ##    ## # ###### # ###### # ## ##   #  ###   #   # ###  ##   ###
      #  ##  # #      # #      # #  # # #####  # ### ## #  ### # ##  
     ##### ### ##    ## ##    ## #### # #    ### #   #  ####   # # # 
    ##     #   # #  ##  # #  ##  #    # ##  ##   ## #####   # ## # ##
      #   ### ## #### ### #### ####  ## # ### # ##  #    # ## #  # # 
     ### ##   #  #    #   #    #   ###  # #   # # ####  ## #  #### ##
     #   # # ######  ### ###  ### ##  ### ## ## # #   ###  ####    # 
    ### ## # #     ###   #  ###   # ###   #  #  # ## ##  ###   #  ###
        #  # ##   ##  # #####  # ## #  # ######## #  # ###  # #####  
       ##### # # ## ### #    ### #  #### #        #### #  ### #    # 
      ##     # # #  #   ##  ##   ####    ##      ##    ####   ##  ###
    ### #   ## # ##### ## ### # ##   #  ## #    ## #  ##   # ## ###  
    #   ## ##  # #     #  #   # # # #####  ##  ##  #### # ## #  #  ##
     # ##  # ### ##   ###### ## # # #    ### ### ###    # #  ####### 
    ## # ### #   # # ##      #  # # ##  ##   #   #  #  ## ####      #
       # #   ## ## # # #    ##### # # ### # ### ########  #   #    ##
    # ## ## ##  #  # # ##  ##     # # #   # #   #       #### ###  ## 
    # #  #  # ###### # # ### #   ## # ## ## ## ###     ##    #  ###  
    # ####### #      # # #   ## ##  # #  #  #  #  #   ## #  #####  ##
      #       ##    ## # ## ##  # ### ############## ##  ####    ### 
     ###     ## #  ##  # #  # ### #   #              # ###   #  ##  #
     #  #   ##  #### ### #### #   ## ###            ## #  # ##### ###
     ##### ## ###    #   #    ## ##  #  #          ##  #### #     #  
    ##     #  #  #  ### ###  ##  # #######        ## ###    ##   ### 
    # #   ###########   #  ### ### #      #      ##  #  #  ## # ##   
    # ## ##          # #####   #   ##    ###    ## #########  # # # #
      #  # #        ## #    # ### ## #  ##  #  ##  #        ### # # #
    ###### ##      ##  ##  ## #   #  #### ###### ####      ##   # # #
           # #    ## ### ###  ## #####    #      #   #    ## # ## # #
    #     ## ##  ##  #   #  ###  #    #  ###    ### ###  ##  # #  # #
     #   ##  # ### #### #####  ####  #####  #  ##   #  ### ### #### #
     ## ## ### #   #    #    ###   ###    ###### # #####   #   #    #
     #  #  #   ## ###  ###  ##  # ##  #  ##      # #    # ### ###  ##
     ######## ##  #  ###  ### ### # ###### #    ## ##  ## #   #  ### 
    ##        # ######  ###   #   # #      ##  ##  # ###  ## #####  #
      #      ## #     ###  # ### ## ##    ## ### ### #  ###  #    ###
    ####    ##  ##   ##  ### #   #  # #  ##  #   #   ####  ####  ##  
    #   #  ## ### # ## ###   ## ##### #### #### ### ##   ###   ### ##
     # #####  #   # #  #  # ##  #     #    #    #   # # ##  # ##   # 
    ## #    #### ## ####### # ####   ###  ###  ### ## # # ### # # ###
       ##  ##    #  #       # #   # ##  ###  ###   #  # # #   # # #  
      ## ### #  ######     ## ## ## # ###  ###  # ##### # ## ## # ## 
     ##  #   ####     #   ##  #  #  # #  ###  ### #     # #  #  # # #
     # #### ##   #   ### ## ######### ####  ###   ##   ## ####### # #
     # #    # # ### ##   #  #         #   ###  # ## # ##  #       # #
     # ##  ## # #   # # ######       ### ##  ### #  # # ####     ## #
     # # ###  # ## ## # #     #     ##   # ###   #### # #   #   ##  #
     # # #  ### #  #  # ##   ###   ## # ## #  # ##    # ## ### ## ###
     # # ####   ####### # # ##  # ##  # #  #### # #  ## #  #   #  #  
    ## # #   # ##       # # # ### # ### ####    # ####  ##### ###### 
    #  # ## ## # #     ## # # #   # #   #   #  ## #   ###     #      
    #### #  #  # ##   ##  # # ## ## ## ### #####  ## ##  #   ###    #
         ####### # # ## ### # #  #  #  #   #    ###  # #### ##  #  ##
    #   ##       # # #  #   # ########### ###  ##  ### #    # ###### 
    ## ## #     ## # ##### ## #           #  ### ###   ##  ## #      
    #  #  ##   ##  # #     #  ##         #####   #  # ## ###  ##    #
     ###### # ## ### ##   ##### #       ##    # ##### #  #  ### #  ##
     #      # #  #   # # ##     ##     ## #  ## #     #######   #### 
    ###    ## ##### ## # # #   ## #   ##  ####  ##   ##      # ##   #
       #  ##  #     #  # # ## ##  ## ## ###   ### # ## #    ## # # ##
    # ##### ####   ##### # #  # ###  #  #  # ##   # #  ##  ##  # # # 
    # #     #   # ##     # #### #  ######### # # ## #### ### ### # # 
    # ##   ### ## # #   ## #    ####         # # #  #    #   #   # # 
    # # # ##   #  # ## ##  ##  ##   #       ## # #####  ### ### ## # 
    # # # # # ##### #  # ### ### # ###     ##  # #    ###   #   #  # 
    # # # # # #     #### #   #   # #  #   ## ### ##  ##  # ### ##### 
    # # # # # ##   ##    ## ### ## ##### ##  #   # ### ### #   #     
    # # # # # # # ## #  ##  #   #  #     # #### ## #   #   ## ###   #
      # # # # # # #  #### #### ######   ## #    #  ## ### ##  #  # ##
    ### # # # # # ####    #    #     # ##  ##  #####  #   # ###### # 
    #   # # # # # #   #  ###  ###   ## # ### ###    #### ## #      # 
    ## ## # # # # ## #####  ###  # ##  # #   #  #  ##    #  ##    ## 
    #  #  # # # # #  #    ###  ### # ### ## ######## #  ##### #  ##  
    ####### # # # #####  ##  ###   # #   #  #        ####     #### ##
            # # # #    ### ###  # ## ## ######      ##   #   ##    # 
           ## # # ##  ##   #  ### #  #  #     #    ## # ### ## #  ###
    #     ##  # # # ### # #####   ########   ###  ##  # #   #  ####  
    ##   ## ### # # #   # #    # ##       # ##  ### ### ## #####   ##
      # ##  #   # # ## ## ##  ## # #     ## # ###   #   #  #    # ## 
     ## # #### ## # #  #  # ###  # ##   ##  # #  # ### ######  ## # #
     #  # #    #  # ####### #  ### # # ## ### #### #   #     ###  # #
     #### ##  ##### #       ####   # # #  #   #    ## ###   ##  ### #
     #    # ###     ##     ##   # ## # ##### ###  ##  #  # ## ###   #
     ##  ## #  #   ## #   ## # ## #  # #     #  ### ###### #  #  # ##
     # ###  ##### ##  ## ##  # #  #### ##   #####   #      ####### # 
    ## #  ###     # ###  # ### ####    # # ##    # ###    ##       ##
       ####  #   ## #  ### #   #   #  ## # # #  ## #  #  ## #     ## 
      ##   #### ##  ####   ## ### #####  # # ####  #######  ##   ## #
    ### # ##    # ###   # ##  #   #    ### # #   ###      ### # ##  #
        # # #  ## #  # ## # #### ###  ##   # ## ##  #    ##   # # ###
    #  ## # ####  #### #  # #    #  ### # ## #  # ####  ## # ## # #  
    ####  # #   ###    #### ##  #####   # #  #### #   ###  # #  # ###
        ### ## ##  #  ##    # ###    # ## ####    ## ##  ### #### #  
       ##   #  # ###### #  ## #  #  ## #  #   #  ##  # ###   #    ## 
      ## # ##### #      ####  #######  ##### ##### ### #  # ###  ## #
    ###  # #     ##    ##   ###      ###     #     #   #### #  ###  #
       ### ##   ## #  ## # ##  #    ##  #   ###   ### ##    ####  ###
    # ##   # # ##  ####  # # ####  ## #### ##  # ##   # #  ##   ###  
    # # # ## # # ###   ### # #   ###  #    # ### # # ## #### # ##  ##
      # # #  # # #  # ##   # ## ##  ####  ## #   # # #  #    # # ### 
     ## # #### # #### # # ## #  # ###   ###  ## ## # #####  ## # #  #
     #  # #    # #    # # #  #### #  # ##  ###  #  # #    ###  # ####
     #### ##  ## ##  ## # ####    #### # ###  ###### ##  ##  ### #   
    ##    # ###  # ###  # #   #  ##    # #  ###      # ### ###   ##  
    # #  ## #  ### #  ### ## ##### #  ## ####  #    ## #   #  # ## ##
      ####  ####   ####   #  #     ####  #   ####  ##  ## ##### #  # 
     ##   ###   # ##   # ######   ##   #### ##   ### ###  #     #####
     # # ##  # ## # # ## #     # ## # ##    # # ##   #  ####   ##    
    ## # # ### #  # # #  ##   ## #  # # #  ## # # # #####   # ## #   
    #  # # #   #### # #### # ##  #### # ####  # # # #    # ## #  ## #
     ### # ## ##    # #    # # ###    # #   ### # # ##  ## #  ####  #
     #   # #  # #  ## ##  ## # #  #  ## ## ##   # # # ###  ####   ###
     ## ## #### ####  # ###  # #######  #  # # ## # # #  ###   # ##  
    ##  #  #    #   ### #  ### #      ###### # #  # # ####  # ## # # 
    # #######  ### ##   ####   ##    ##      # #### # #   ### #  # # 
    # #      ###   # # ##   # ## #  ## #    ## #    # ## ##   #### # 
    # ##    ##  # ## # # # ## #  ####  ##  ##  ##  ## #  # # ##    # 
    # # #  ## ### #  # # # #  ####   ### ### ### ###  #### # # #  ## 
    # # ####  #   #### # # ####   # ##   #   #   #  ###    # # ####  
    # # #   #### ##    # # #   # ## # # ### ### #####  #  ## # #   ##
      # ## ##    # #  ## # ## ## #  # # #   #   #    ######  # ## ## 
     ## #  # #  ## ####  # #  #  #### # ## ### ###  ##     ### #  # #
     #  #### ####  #   ### #######    # #  #   #  ### #   ##   #### #
     ####    #   #### ##   #      #  ## ##### #####   ## ## # ##    #
     #   #  ### ##    # # ###    #####  #     #    # ##  #  # # #  ##
     ## #####   # #  ## # #  #  ##    ####   ###  ## # ###### # #### 
    ##  #    # ## ####  # ####### #  ##   # ##  ###  # #      # #   #
      ####  ## #  #   ### #       #### # ## # ###  ### ##    ## ## ##
    ###   ###  ##### ##   ##     ##    # #  # #  ###   # #  ##  #  # 
    #  # ##  ###     # # ## #   ## #  ## #### ####  # ## #### ###### 
    #### # ###  #   ## # #  ## ##  ####  #    #   ### #  #    #      
    #    # #  #### ##  # ####  # ###   ####  ### ##   #####  ###    #
     #  ## ####    # ### #   ### #  # ##   ###   # # ##    ###  #  ##
     ####  #   #  ## #   ## ##   #### # # ##  # ## # # #  ##  ###### 
    ##   #### #####  ## ##  # # ##    # # # ### #  # # #### ###     #
      # ##    #    ###  # ### # # #  ## # # #   #### # #    #  #   ##
    ### # #  ###  ##  ### #   # # ####  # # ## ##    # ##  ###### ## 
    #   # ####  ### ###   ## ## # #   ### # #  # #  ## # ###      #  
    ## ## #   ###   #  # ##  #  # ## ##   # #### ####  # #  #    ####
       #  ## ##  # ##### # ###### #  # # ## #    #   ### #####  ##   
      #####  # ### #     # #      #### # #  ##  ### ##   #    ### #  
     ##    ### #   ##   ## ##    ##    # #### ###   # # ###  ##   ## 
    ## #  ##   ## ## # ##  # #  ## #  ## #    #  # ## # #  ### # ## #
       #### # ##  #  # # ### ####  ####  ##  ##### #  # ####   # #  #
    # ##    # # ###### # #   #   ###   ### ###     #### #   # ## ####
      # #  ## # #      # ## ### ##  # ##   #  #   ##    ## ## #  #   
     ## ####  # ##    ## #  #   # ### # # ###### ## #  ##  #  #####  
    ##  #   ### # #  ##  ##### ## #   # # #      #  #### ######    # 
    # #### ##   # #### ###     #  ## ## # ##    #####    #     #  ## 
    # #    # # ## #    #  #   #####  #  # # #  ##    #  ###   #####  
    # ##  ## # #  ##  ###### ##    ###### # #### #  #####  # ##    ##
      # ###  # #### ###      # #  ##      # #    ####    ### # #  ## 
     ## #  ### #    #  #    ## #### #    ## ##  ##   #  ##   # #### #
     #  ####   ##  ######  ##  #    ##  ##  # ### # ##### # ## #    #
     ####   # ## ###     ### ####  ## ### ### #   # #     # #  ##  ##
     #   # ## #  #  #   ##   #   ###  #   #   ## ## ##   ## #### ### 
    ### ## #  ######## ## # ### ##  #### ### ##  #  # # ##  #    #  #
        #  ####        #  # #   # ###    #   # ###### # # ####  #####
    #  #####   #      ##### ## ## #  #  ### ## #      # # #   ###    
    ####    # ###    ##     #  #  #######   #  ##    ## # ## ##  #  #
        #  ## #  #  ## #   ########      # ##### #  ##  # #  # ######
    #  #####  #######  ## ##       #    ## #     #### ### #### #     
    ####    ###      ###  # #     ###  ##  ##   ##    #   #    ##   #
        #  ##  #    ##  ### ##   ##  ### ### # ## #  ### ###  ## # ##
    #  ##### ####  ## ###   # # ## ###   #   # #  ####   #  ###  # # 
    ####     #   ###  #  # ## # #  #  # ### ## ####   # #####  ### # 
    #   #   ### ##  ###### #  # ####### #   #  #   # ## #    ###   # 
    ## ### ##   # ###      #### #       ## ###### ## #  ##  ##  # ## 
    #  #   # # ## #  #    ##    ##     ##  #      #  #### ### ### #  
    ##### ## # #  #####  ## #  ## #   ## ####    #####    #   #   ###
          #  # ####    ###  ####  ## ##  #   #  ##    #  ### ### ##  
         ##### #   #  ##  ###   ###  # #### ##### #  #####   #   # # 
        ##     ## ##### ###  # ##  ### #    #     ####    # ### ## ##
    #  ## #   ##  #     #  ### # ###   ##  ###   ##   #  ## #   #  # 
    ####  ## ## ####   #####   # #  # ## ###  # ## # #####  ## ##### 
    #   ###  #  #   # ##    # ## #### #  #  ### #  # #    ###  #     
    ## ##  ####### ## # #  ## #  #    #######   #### ##  ##  ####   #
       # ###       #  # ####  #####  ##      # ##    # ### ###   # ##
    # ## #  #     ##### #   ###    ### #    ## # #  ## #   #  # ## # 
    # #  #####   ##     ## ##  #  ##   ##  ##  # ####  ## ##### #  # 
    # ####    # ## #   ##  # ###### # ## ### ### #   ###  #     #### 
    # #   #  ## #  ## ## ### #      # #  #   #   ## ##  ####   ##    
    # ## #####  ####  #  #   ##    ## ##### ### ##  # ###   # ## #  #
      #  #    ###   ####### ## #  ##  #     #   # ### #  # ## #  ####
    #######  ##  # ##       #  #### ####   ### ## #   #### #  ####   
    #      ### ### # #     #####    #   # ##   #  ## ##    ####   # #
     #    ##   #   # ##   ##    #  ### ## # # #####  # #  ##   # ## #
     ##  ## # ### ## # # ## #  #####   #  # # #    ### #### # ## #  #
     # ###  # #   #  # # #  ####    # ##### # ##  ##   #    # #  ####
     # #  ### ## ##### # ####   #  ## #     # # ### # ###  ## ####   
    ## ####   #  #     # #   # #####  ##   ## # #   # #  ###  #   #  
    #  #   # ######   ## ## ## #    ### # ##  # ## ## ####  #### ####
     #### ## #     # ##  #  #  ##  ##   # # ### #  #  #   ###    #   
    ##    #  ##   ## # ######### ### # ## # #   ######## ##  #  ###  
    # #  ##### # ##  # #         #   # #  # ## ##        # ######  ##
      ####     # # ### ##       ### ## #### #  # #      ## #     ### 
     ##   #   ## # #   # #     ##   #  #    #### ##    ##  ##   ##  #
     # # ### ##  # ## ## ##   ## # ######  ##    # #  ## ### # ## ###
     # # #   # ### #  #  # # ##  # #     ### #  ## ####  #   # #  #  
    ## # ## ## #   ####### # # ### ##   ##   ####  #   #### ## ##### 
    #  # #  #  ## ##       # # #   # # ## # ##   #### ##    #  #     
    #### #######  # #     ## # ## ## # #  # # # ##    # #  ######   #
         #      ### ##   ##  # #  #  # #### # # # #  ## ####     # ##
    #   ###    ##   # # ## ### ####### #    # # # ####  #   #   ## # 
    ## ##  #  ## # ## # #  #   #       ##  ## # # #   #### ### ##  # 
    #  # ######  # #  # ##### ###     ## ###  # # ## ##    #   # ### 
    #### #     ### #### #     #  #   ##  #  ### # #  # #  ### ## #   
    #    ##   ##   #    ##   ###### ## ######   # #### ####   #  ## #
     #  ## # ## # ###  ## # ##      #  #     # ## #    #   # #####  #
     ####  # #  # #  ###  # # #    ######   ## #  ##  ### ## #    ###
     #   ### #### ####  ### # ##  ##     # ##  #### ###   #  ##  ##  
    ### ##   #    #   ###   # # ### #   ## # ###    #  # ##### ### # 
    #   # # ###  ### ##  # ## # #   ## ##  # #  #  ##### #     #   # 
    ## ## # #  ###   # ### #  # ## ##  # ### #######     ##   ### ## 
    #  #  # ####  # ## #   #### #  # ### #   #      #   ## # ##   #  
    ####### #   ### #  ## ##    #### #   ## ###    ### ##  # # # ####
            ## ##   ####  # #  ##    ## ##  #  #  ##   # ### # # #   
           ##  # # ##   ### #### #  ##  # ######### # ## #   # # ##  
          ## ### # # # ##   #    #### ### #         # #  ## ## # # # 
         ##  #   # # # # # ###  ##    #   ##       ## ####  #  # # ##
    #   ## #### ## # # # # #  ### #  ### ## #     ##  #   ###### # # 
    ## ##  #    #  # # # # ####   ####   #  ##   ## #### ##      # # 
    #  # ####  ##### # # # #   # ##   # ##### # ##  #    # #    ## # 
    #### #   ###     # # # ## ## # # ## #     # # ####  ## ##  ##  # 
    #    ## ##  #   ## # # #  #  # # #  ##   ## # #   ###  # ### ### 
    ##  ##  # #### ##  # # ####### # #### # ##  # ## ##  ### #   #   
    # ### ### #    # ### # #       # #    # # ### #  # ###   ## ### #
      #   #   ##  ## #   # ##     ## ##  ## # #   #### #  # ##  #   #
    #### ### ## ###  ## ## # #   ##  # ###  # ## ##    #### # #### ##
         #   #  #  ###  #  # ## ## ### #  ### #  # #  ##    # #    # 
        ### ########  ###### #  #  #   ####   #### #### #  ## ##  ###
    #  ##   #       ###      ######## ##   # ##    #    ####  # ###  
    #### # ###     ##  #    ##        # # ## # #  ###  ##   ### #  ##
         # #  #   ## ####  ## #      ## # #  # ####  ### # ##   #### 
        ## ##### ##  #   ###  ##    ##  # #### #   ###   # # # ##   #
    #  ##  #     # #### ##  ### #  ## ### #    ## ##  # ## # # # # ##
     ### ####   ## #    # ###   ####  #   ##  ##  # ### #  # # # # # 
    ##   #   # ##  ##  ## #  # ##   #### ## ### ### #   #### # # # ##
      # ### ## # ### ###  #### # # ##    #  #   #   ## ##    # # # # 
     ## #   #  # #   #  ###    # # # #  ###### ### ##  # #  ## # # ##
     #  ## ##### ## #####  #  ## # # ####      #   # ### ####  # # # 
    #####  #     #  #    ######  # # #   #    ### ## #   #   ### # ##
         ####   ######  ##     ### # ## ###  ##   #  ## ### ##   # # 
        ##   # ##     ### #   ##   # #  #  ### # #####  #   # # ## ##
    #  ## # ## # #   ##   ## ## # ## #######   # #    #### ## # #  # 
    ####  # #  # ## ## # ##  #  # #  #      # ## ##  ##    #  # #### 
    #   ### #### #  #  # # ###### #####    ## #  # ### #  ##### #    
    ## ##   #    ####### # #      #    #  ##  #### #   ####     ##  #
       # # ###  ##       # ##    ###  ##### ###    ## ##   #   ## ###
    # ## # #  ### #     ## # #  ##  ###     #  #  ##  # # ### ##  #  
    # #  # ####   ##   ##  # #### ###  #   ######## ### # #   # #####
      #### #   # ## # ## ### #    #  #### ##        #   # ## ## #    
     ##    ## ## #  # #  #   ##  #####    # #      ### ## #  #  ##   
    ## #  ##  #  #### ##### ## ###    #  ## ##    ##   #  ####### #  
    #  #### ######    #     #  #  #  #####  # #  ## # #####       ###
     ###    #     #  ###   ###########    ### ####  # #    #     ##  
    ##  #  ###   #####  # ##          #  ##   #   ### ##  ###   ## # 
    # ######  # ##    ### # #        ##### # ### ##   # ###  # ##  # 
    # #     ### # #  ##   # ##      ##     # #   # # ## #  ### # ### 
    # ##   ##   # #### # ## # #    ## #   ## ## ## # #  ####   # #   
    # # # ## # ## #    # #  # ##  ##  ## ##  #  #  # ####   # ## ## #
      # # #  # #  ##  ## #### # ### ###  # ######### #   # ## #  #  #
    ### # #### #### ###  #    # #   #  ### #         ## ## #  #######
        # #    #    #  ####  ## ## #####   ##       ##  #  ####      
       ## ##  ###  #####   ###  #  #    # ## #     ## ######   #     
      ##  # ###  ###    # ##  #######  ## #  ##   ##  #     # ###    
     ## ### #  ###  #  ## # ###      ###  #### # ## ####   ## #  #   
    ##  #   ####  ######  # #  #    ##  ###    # #  #   # ##  #####  
    # #### ##   ###     ### #####  ## ###  #  ## ##### ## # ###    ##
      #    # # ##  #   ##   #    ###  #  ######  #     #  # #  #  ## 
     ###  ## # # #### ## # ###  ##  ######     ####   ##### ####### #
     #  ###  # # #    #  # #  ### ###     #   ##   # ##     #       #
     ####  ### # ##  ##### ####   #  #   ### ## # ## # #   ###     ##
     #   ###   # # ###     #   # ###### ##   #  # #  # ## ##  #   ## 
    ### ##  # ## # #  #   ### ## #      # # ##### #### #  # #### ## #
        # ### #  # ##### ##   #  ##    ## # #     #    #### #    #  #
    #  ## #   #### #     # # ##### #  ##  # ##   ###  ##    ##  #####
     ###  ## ##    ##   ## # #     #### ### # # ##  ### #  ## ###    
    ##  ###  # #  ## # ##  # ##   ##    #   # # # ###   ####  #  #   
    # ###  ### ####  # # ### # # ## #  ### ## # # #  # ##   ####### #
      #  ###   #   ### # #   # # #  ####   #  # # #### # # ##       #
    ######  # ### ##   # ## ## # ####   # ##### # #    # # # #     ##
          ### #   # # ## #  #  # #   # ## #     # ##  ## # # ##   ## 
         ##   ## ## # #  ####### ## ## #  ##   ## # ###  # # # # ## #
    #   ## # ##  #  # ####       #  #  #### # ##  # #  ### # # # #  #
     # ##  # # ###### #   #     ########    # # ### ####   # # # ####
     # # ### # #      ## ###   ##       #  ## # #   #   # ## # # #   
    ## # #   # ##    ##  #  # ## #     #####  # ## ### ## #  # # ##  
    #  # ## ## # #  ## ###### #  ##   ##    ### #  #   #  #### # # ##
     ### #  #  # ####  #      #### # ## #  ##   ##### #####    # # # 
    ##   ####### #   ####    ##    # #  #### # ##     #    #  ## # ##
      # ##       ## ##   #  ## #  ## ####    # # #   ###  #####  # # 
     ## # #     ##  # # #####  ####  #   #  ## # ## ##  ###    ### ##
     #  # ##   ## ### # #    ###   #### #####  # #  # ###  #  ##   # 
    ##### # # ##  #   # ##  ##  # ##    #    ### #### #  ###### # ###
          # # # #### ## # ### ### # #  ###  ##   #    ####      # #  
         ## # # #    #  # #   #   # ####  ### # ###  ##   #    ## ## 
        ##  # # ##  ##### ## ### ## #   ###   # #  ### # ###  ##  # #
    #  ## ### # # ###     #  #   #  ## ##  # ## ####   # #  ### ### #
     ###  #   # # #  #   ###### #####  # ### #  #   # ## ####   #   #
     #  #### ## # ##### ##      #    ### #   ##### ## #  #   # ### ##
     ####    #  # #     # #    ###  ##   ## ##     #  ##### ## #   # 
    ##   #  ##### ##   ## ##  ##  ### # ##  # #   #####     #  ## ###
      # #####     # # ##  # ### ###   # # ### ## ##    #   #####  #  
     ## #    #   ## # # ### #   #  # ## # #   #  # #  ### ##    #### 
    ##  ##  ### ##  # # #   ## ##### #  # ## ##### ####   # #  ##   #
      ### ###   # ### # ## ##  #     #### #  #     #   # ## #### # ##
    ###   #  # ## #   # #  # ####   ##    #####   ### ## #  #    # # 
    #  # ##### #  ## ## #### #   # ## #  ##    # ##   #  #####  ## # 
    #### #     ####  #  #    ## ## #  #### #  ## # # #####    ###  # 
    #    ##   ##   #######  ##  #  ####    ####  # # #    #  ##  ### 
    ##  ## # ## # ##      ### ######   #  ##   ### # ##  ##### ###   
    # ###  # #  # # #    ##   #     # ##### # ##   # # ###     #  # #
      #  ### #### # ##  ## # ###   ## #     # # # ## # #  #   ##### #
    ######   #    # # ###  # #  # ##  ##   ## # # #  # ##### ##     #
          # ###  ## # #  ### #### # ### # ##  # # #### #     # #   ##
    #    ## #  ###  # ####   #    # #   # # ### # #    ##   ## ## ## 
    ##  ##  ####  ### #   # ###  ## ## ## # #   # ##  ## # ##  #  #  
    # ### ###   ###   ## ## #  ###  #  #  # ## ## # ###  # # ########
      #   #  # ##  # ##  #  ####  ######### #  #  # #  ### # #       
     ### ##### # ### # ######   ###         ####### ####   # ##      
    ##   #     # #   # #     # ##  #       ##       #   # ## # #     
    # # ###   ## ## ## ##   ## # ####     ## #     ### ## #  # ##   #
      # #  # ##  #  #  # # ##  # #   #   ##  ##   ##   #  #### # # ##
    ### #### # ######### # # ### ## ### ## ### # ## # #####    # # # 
    #   #    # #         # # #   #  #   #  #   # #  # #    #  ## # # 
    ## ###  ## ##       ## # ## ###### ###### ## #### ##  #####  # # 
    #  #  ###  # #     ##  # #  #      #      #  #    # ###    ### # 
    #######  ### ##   ## ### #####    ###    ######  ## #  #  ##   # 
    #      ###   # # ##  #   #    #  ##  #  ##     ###  ####### # ## 
    ##    ##  # ## # # #### ###  ##### ###### #   ##  ###       # #  
    # #  ## ### #  # # #    #  ###     #      ## ## ###  #     ## ###
      ####  #   #### # ##  #####  #   ###    ##  #  #  ####   ##  #  
     ##   #### ##    # # ###    #### ##  #  ## #########   # ## #### 
    ## # ##    # #  ## # #  #  ##    # ######  #        # ## #  #   #
       # # #  ## ####  # ####### #  ## #     ####      ## #  ##### ##
    # ## # ####  #   ### #       ####  ##   ##   #    ##  ####     # 
    # #  # #   #### ##   ##     ##   ### # ## # ###  ## ###   #   ## 
    # #### ## ##    # # ## #   ## # ##   # #  # #  ###  #  # ### ##  
    # #    #  # #  ## # #  ## ##  # # # ## #### ####  ###### #   # ##
      ##  ##### ####  # ####  # ### # # #  #    #   ###      ## ## # 
     ## ###     #   ### #   ### #   # # #####  ### ##  #    ##  #  ##
     #  #  #   ### ##   ## ##   ## ## # #    ###   # ####  ## ###### 
    ######### ##   # # ##  # # ##  #  # ##  ##  # ## #   ###  #     #
              # # ## # # ### # # ###### # ### ### #  ## ##  ####   ##
    #        ## # #  # # #   # # #      # #   #   ####  # ###   # ## 
    ##      ##  # #### # ## ## # ##    ## ## ### ##   ### #  # ## #  
    # #    ## ### #    # #  #  # # #  ##  #  #   # # ##   #### #  ###
      ##  ##  #   ##  ## ####### # #### ####### ## # # # ##    ####  
     ## ### #### ## ###  #       # #    #       #  # # # # #  ##   # 
    ##  #   #    #  #  ####     ## ##  ###     ##### # # # #### # ###
      #### ###  ########   #   ##  # ###  #   ##     # # # #    # #  
     ##    #  ###       # ### ## ### #  #### ## #   ## # # ##  ## ## 
    ## #  #####  #     ## #   #  #   ####    #  ## ##  # # # ###  # #
       ####    ####   ##  ## ###### ##   #  #####  # ### # # #  ### #
    # ##   #  ##   # ## ###  #      # # #####    ### #   # # ####   #
      # # ##### # ## #  #  ####    ## # #    #  ##   ## ## # #   # ##
    ### # #     # #  #######   #  ##  # ##  ##### # ##  #  # ## ## # 
    #   # ##   ## ####      # ##### ### # ###     # # ###### #  #  # 
    ## ## # # ##  #   #    ## #     #   # #  #   ## # #      ####### 
    #  #  # # # #### ###  ##  ##   ### ## ##### ##  # ##    ##       
    ####### # # #    #  ### ### # ##   #  #     # ### # #  ## #     #
            # # ##  #####   #   # # # ######   ## #   # ####  ##   ##
    #      ## # # ###    # ### ## # # #     # ##  ## ## #   ### # ## 
    ##    ##  # # #  #  ## #   #  # # ##   ## # ###  #  ## ##   # #  
    # #  ## ### # #######  ## ##### # # # ##  # #  ######  # # ## ###
      ####  #   # #      ###  #     # # # # ### ####     ### # #  #  
     ##   #### ## ##    ##  ####   ## # # # #   #   #   ##   # ##### 
    ## # ##    #  # #  ## ###   # ##  # # # ## ### ### ## # ## #    #
       # # #  ##### ####  #  # ## # ### # # #  #   #   #  # #  ##  ##
    # ## # ####     #   ###### #  # #   # # ##### ### ##### #### ### 
    # #  # #   #   ### ##      #### ## ## # #     #   #     #    #   
    # #### ## ### ##   # #    ##    #  #  # ##   ### ###   ###  ### #
      #    #  #   # # ## ##  ## #  ######## # # ##   #  # ##  ###   #
    ####  ###### ## # #  # ###  ####        # # # # ##### # ###  # ##
        ###      #  # #### #  ###   #      ## # # # #     # #  ### # 
       ##  #    ##### #    ####  # ###    ##  # # # ##   ## ####   ##
    # ## ####  ##     ##  ##   ### #  #  ## ### # # # # ##  #   # ## 
    # #  #   ### #   ## ### # ##   #######  #   # # # # # #### ## #  
    # ##### ##   ## ##  #   # # # ##      #### ## # # # # #    #  ###
      #     # # ##  # #### ## # # # #    ##    #  # # # # ##  #####  
     ###   ## # # ### #    #  # # # ##  ## #  ##### # # # # ###    # 
    ##  # ##  # # #   ##  ##### # # # ###  ####     # # # # #  #  ###
      ### # ### # ## ## ###     # # # #  ###   #   ## # # # #######  
     ##   # #   # #  #  #  #   ## # # ####  # ### ##  # # # #      # 
    ## # ## ## ## ########### ##  # # #   ### #   # ### # # ##    ###
       # #  #  #  #           # ### # ## ##   ## ## #   # # # #  ##  
      ## ###########         ## #   # #  # # ##  #  ## ## # # #### # 
     ##  #          #       ##  ## ## #### # # ######  #  # # #    ##
     # ####        ###     ## ###  #  #    # # #     ###### # ##  ## 
    ## #   #      ##  #   ##  #  #######  ## # ##   ##      # # ### #
       ## ###    ## #### ## ######      ###  # # # ## #    ## # #   #
    # ##  #  #  ##  #    #  #     #    ##  ### # # #  ##  ##  # ## ##
      # ######### ####  ######   ###  ## ###   # # #### ### ### #  # 
     ## #         #   ###     # ##  ###  #  # ## # #    #   #   #####
     #  ##       ### ##  #   ## # ###  ###### #  # ##  ### ### ##    
    ##### #     ##   # #### ##  # #  ###      #### # ###   #   # #   
    #     ##   ## # ## #    # ### ####  #    ##    # #  # ### ## ## #
     #   ## # ##  # #  ##  ## #   #   ####  ## #  ## #### #   #  #  #
     ## ##  # # ### #### ###  ## ### ##   ###  ####  #    ## ########
     #  # ### # #   #    #  ###  #   # # ##  ###   ####  ##  #       
    ##### #   # ## ###  #####  #### ## # # ###  # ##   ### ####      
    #     ## ## #  #  ###    ###    #  # # #  ### # # ##   #   #    #
     #   ##  #  #######  #  ##  #  ##### # ####   # # # # ### ###  ##
     ## ## ######      ###### ######     # #   # ## # # # #   #  ### 
    ##  #  #     #    ##      #     #   ## ## ## #  # # # ## #####  #
      #######   ###  ## #    ###   ### ##  #  #  #### # # #  #    ###
    ###      # ##  ###  ##  ##  # ##   # #########    # # #####  ##  
    #  #    ## # ###  ### ### ### # # ## #        #  ## # #    ### ##
     ####  ##  # #  ###   #   #   # # #  ##      #####  # ##  ##   # 
    ##   ### ### ####  # ### ### ## # #### #    ##    ### # ### # ###
      # ##   #   #   ### #   #   #  # #    ##  ## #  ##   # #   # #  
     ## # # ### ### ##   ## ### ##### ##  ## ###  #### # ## ## ## ## 
    ##  # # #   #   # # ##  #   #     # ###  #  ###    # #  #  #  # #
      ### # ## ### ## # # #### ###   ## #  ######  #  ## ########## #
    ###   # #  #   #  # # #    #  # ##  ####     ######  #          #
       # ## ##### ##### # ##  ##### # ###   #   ##     ####        ##
    # ## #  #     #     # # ###     # #  # ### ## #   ##   #      ## 
    # #  #####   ###   ## # #  #   ## #### #   #  ## ## # ###    ##  
    # ####    # ##  # ##  # ##### ##  #    ## #####  #  # #  #  ## ##
      #   #  ## # ### # ### #     # ####  ##  #    ###### #######  # 
     ### #####  # #   # #   ##   ## #   ### ####  ##      #      ####
     #   #    ### ## ## ## ## # ##  ## ##   #   ### #    ###    ##   
    ### ###  ##   #  #  #  #  # # ###  # # ### ##   ##  ##  #  ## #  
    #   #  ### # ############## # #  ### # #   # # ## ### ######  ###
     # #####   # #              # ####   # ## ## # #  #   #     ###  
    ## #    # ## ##            ## #   # ## #  #  # ##### ###   ##  # 
    #  ##  ## #  # #          ##  ## ## #  ####### #     #  # ## ### 
    #### ###  #### ##        ## ###  #  ####       ##   ##### #  #   
    #    #  ###    # #      ##  #  ######   #     ## # ##     ##### #
     #  #####  #  ## ##    ## ######     # ###   ##  # # #   ##     #
     ####    ######  # #  ##  #     #   ## #  # ## ### # ## ## #   ##
     #   #  ##     ### #### ####   ### ##  #### #  #   # #  #  ## ## 
    ### ##### #   ##   #    #   # ##   # ###    ##### ## #######  # #
        #     ## ## # ###  ### ## # # ## #  #  ##     #  #      ### #
    #  ###   ##  #  # #  ###   #  # # #  ####### #   ######    ##   #
     ###  # ## ###### ####  # ##### # ####       ## ##     #  ## # ##
     #  ### #  #      #   ### #     # #   #     ##  # #   #####  # # 
    #####   #####    ### ##   ##   ## ## ###   ## ### ## ##    ### ##
