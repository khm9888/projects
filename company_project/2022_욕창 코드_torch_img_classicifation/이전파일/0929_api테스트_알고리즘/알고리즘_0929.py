infection=None #1-있음/0-없음
sagang=None #1-있음/0-없음
skin_state=None #1- 건강하지 않음/0-건강함
exudate_amount=None #0~4 소량~다량
stage=None #0-미분류, 1~4-1~4등급, 5-심부조직손상

input_dressing_list=[0]
input_dressing_list.extend(list(range(1007,1010)))

cover_dressing_list=list(range(1000,1007))
cover_dressing_list.extend(list(range(1010,1019)))

print(input_dressing_list)
print(cover_dressing_list)

input_dressing=0
# cover_dressing=1000

if infection:
    if sagang:
        if skin_state==0:
            if exudate_amount<=2:
                if stage==3 or stage==4 or stage==0 :
                    input_dressing=1007
                else:
                    cover_dressing=1010
            else:   
                if stage==3 or stage==4 or stage==0 :
                    input_dressing=1007
                    cover_dressing=1002
                else:                 
                    cover_dressing=1010
        else:     
            if exudate_amount<=2:
                if stage==3 or stage==4 or stage==0 :
                    input_dressing=1007
                    cover_dressing=1001
                else:                 
                    cover_dressing=1010   
            else:
                if stage==3 or stage==4 or stage==0 :
                    input_dressing=1007
                    cover_dressing=1003     
                else:                 
                    cover_dressing=1010   
            
    else:
        if skin_state==0:
            if exudate_amount==0:
                if stage==1 :
                    cover_dressing=1006
                elif stage==3 or stage==4 or stage==2 or stage==0:
                    cover_dressing=1004
                else:
                    cover_dressing=1014
            else:   
                if stage==1 :
                    cover_dressing=1010
                else:                 
                    cover_dressing=1004
        else:     
            if exudate_amount==0:
                if stage==1 :
                    cover_dressing=1001
                elif stage==3 or stage==4 or stage==2 or stage==0:
                    cover_dressing=1005
                else:
                    cover_dressing=1015
                    
            else:
                if stage==1 :
                    cover_dressing=1010     
                else:                 
                    cover_dressing=1005
else:
    if sagang:
        if skin_state==0:
            if exudate_amount<=2:
                if stage==3 or stage==4 or stage==0 :
                    input_dressing=1008
                else:
                    cover_dressing=1010
            else:   
                if stage==3 or stage==4 or stage==0 :
                    input_dressing=1009
                    cover_dressing=1002
                else:                 
                    cover_dressing=1010
        else:     
            if exudate_amount<=2:
                if stage==3 or stage==4 or stage==0 :
                    input_dressing=1008
                    cover_dressing=1001
                else:                 
                    cover_dressing=1010   
            else:
                if stage==3 or stage==4 or stage==0 :
                    input_dressing=1009
                    cover_dressing=1003     
                else:                 
                    cover_dressing=1010   
            
    else:
        if skin_state==0:
            if exudate_amount==0:
                if stage==1 or stage==3 or stage==4 or stage==0:
                    cover_dressing=1006
                elif  stage==2:
                    cover_dressing=1011
                else:
                    cover_dressing=1014
            elif exudate_amount==1 or exudate_amount==2:
                if stage==1:
                    cover_dressing=1010
                elif stage==2:
                    cover_dressing=1011
                elif stage==3 or stage==4 or stage==0:
                    cover_dressing=1006
                else:
                    cover_dressing=1016                    
            else:   
                if stage==1:
                    cover_dressing=1010
                elif stage==2:
                    cover_dressing=1013
                elif stage==3 or stage==4 or stage==0:
                    cover_dressing=1002
                else:
                    cover_dressing=1017
        else:     
            if exudate_amount==0:
                if stage==1 or stage==3 or stage==4 or stage==0:
                    cover_dressing=1001
                elif  stage==2:
                    cover_dressing=1012
                else:
                    cover_dressing=1015
            elif exudate_amount==1 or exudate_amount==2:
                if stage==1:
                    cover_dressing=1010
                elif stage==2:
                    cover_dressing=1012
                elif stage==3 or stage==4 or stage==0:
                    cover_dressing=1001
                else:
                    cover_dressing=1015                  
            else:   
                if stage==1:
                    cover_dressing=1010
                elif stage==2:
                    cover_dressing=1012
                elif stage==3 or stage==4 or stage==0:
                    cover_dressing=1003
                else:
                    cover_dressing=1018