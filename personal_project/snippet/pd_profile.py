import pandas as pd
import pandas_profiling
# data = pd.read_csv('data\kaggle\spam\spam.csv',encoding='latin1')
data = pd.read_csv('d://private/data\kaggle\spam\spam.csv',encoding='latin1')

data.head(10)

pr=data.profile_report()

pr.to_file('./pr_report.html') 
#주피터 노트북에선 프린트가 되지만, vscode 등에서는 위와 같은 방식으로 html로 저장해서 알 수 있다.