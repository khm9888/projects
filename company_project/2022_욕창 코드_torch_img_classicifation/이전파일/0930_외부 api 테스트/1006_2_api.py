import time

from flask import Flask, jsonify, request

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--host', default='0.0.0.0')
parser.add_argument('--port', default=9001)

opt, remain = parser.parse_known_args()


app = Flask(__name__)

code_list = list(range(1001,1011))


@app.route('/dressing', methods=['POST'])
def predict():
    print("----flask print start----")
    st = time.time()
    if request.method == 'POST':
        datas = request.form
        print("datas")
        print(datas)
        
        # infection=None #1-있음/0-없음
        # sagang=None #1-있음/0-없음
        # skin_state=None #1- 건강하지 않음/0-건강함
        # exudate_amount=None #0~4 소량~다량
        # stage=None #0-미분류, 1~4-1~4등급, 5-심부조직손상
    
        infection=int(datas["infection"]) #1-있음/0-없음
        sagang=int(datas["sagang"]) #1-있음/0-없음
        skin_state=int(datas["skin_state"]) #1- 건강하지 않음/0-건강함
        exudate_amount=int(datas["exudate_amount"]) #0~4 소량~다량
        stage=int(datas["stage"]) #0-미분류, 1~4-1~4등급, 5-심부조직손상
  
        input_dressing=0

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
                      
                      
        print('cover_dressing :', cover_dressing)  
        print('input_dressing :', input_dressing)  
        result = {'cover_dressing': cover_dressing, "input_dressing":input_dressing,
                'elapsed_time' : time.time() - st  
                    }
        print(result)
        # for v in result.values():
        #     print(v,type(v))
        return jsonify(result)


if __name__ == '__main__':
    app.run(host=opt.host, port=opt.port, debug=False)