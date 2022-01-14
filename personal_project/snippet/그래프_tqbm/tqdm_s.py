# taqaddum 
# https://github.com/tqdm/tqdm

from tqdm import tqdm
def calc_tqdm(value=int(9e6)):
    
    for i in tqdm(range(value)):
        pass
    
calc_tqdm()