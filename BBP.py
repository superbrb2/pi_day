from tqdm import tqdm
'''
CREATED USING THE BAILEY-BORWEIN-PLOUFFE FORMULA

COULD HAVE PROGRAMMED CHUDNOVSKY BUT HARDER TO DO

WILL GENERATE DIGITS OF PI TO ANY LENGTH
'''

from decimal import Decimal
from decimal import getcontext

def get_digits_of_pi(precision):
    getcontext().prec=precision
    return str(sum(1/Decimal(16)**k * 
        (Decimal(4)/(8*k+1) - 
         Decimal(2)/(8*k+4) - 
         Decimal(1)/(8*k+5) -
         Decimal(1)/(8*k+6)) for k in tqdm(range(precision))))
    
    