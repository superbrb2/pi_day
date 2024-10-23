from tqdm import tqdm
'''
CREATED USING THE BAILEY-BORWEIN-PLOUFFE FORMULA

COULD HAVE PROGRAMMED CHUDNOVSKY BUT HARDER TO DO

WILL GENERATE DIGITS OF PI TO ANY LENGTH
'''
import decimal
from decimal import Decimal
from decimal import getcontext
from mpmath import mp

def get_digits_of_pi(precision):
    getcontext().prec=precision
    return str(sum(1/Decimal(16)**k * 
        (Decimal(4)/(8*k+1) - 
         Decimal(2)/(8*k+4) - 
         Decimal(1)/(8*k+5) -
         Decimal(1)/(8*k+6)) for k in tqdm(range(precision),colour='green')))


def BBP_mp(precision):
    mp.dps = precision + 2  # Set precision (extra digits for accuracy)
    
    pi = mp.mpf(0)  # Initialize π as a mpmath floating-point number
    
    for k in tqdm(range(precision),colour='green'):
        term = (1 / mp.power(16, k) * 
                (4 / (8 * k + 1) - 
                 2 / (8 * k + 4) - 
                 1 / (8 * k + 5) - 
                 1 / (8 * k + 6)))
        pi += term  # Accumulate the sum
    
    return str(pi)[:precision + 2]

def chuds(n):
    decimal.getcontext().prec = n + 2
    C = 426880 * decimal.Decimal(10005).sqrt()
    M, L, X, K, S = 1, 13591409, 1, 6, 13591409

    for i in tqdm(range(1, n)):
        M = (K**3 - 16*K) * M // i**3
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
        K += 12

    return str(C / S)[:n + 2]


def chuds_mp(digits):
    # Set the precision
    mp.dps = digits + 2  # Add extra digits for accuracy

    C = mp.mpf(426880) * mp.sqrt(mp.mpf(10005))
    M = mp.mpf(1)
    L = mp.mpf(13591409)
    X = mp.mpf(1)
    K = mp.mpf(6)
    S = L

    for k in tqdm(range(1, digits)):
        M = (K**3 - 16*K) * M / (k**3)
        L += 545140134
        X *= -262537412640768000
        S += M * L / X
        K += 12

    pi = C / S
    return str(pi)[:digits + 2]

if __name__ == '__main__':
    print(get_digits_of_pi(10))