import BBP


with open('BBP.txt','w') as f:
    f.write(BBP.get_digits_of_pi(10000))
    
with open('BBP_mp.txt','w') as f:
    f.write(BBP.BBP_mp(10000))    

with open('chuds_mp.txt','w') as f:
    f.write(BBP.chuds_mp(10000))

with open('chuds.txt','w') as f:
    f.write(BBP.chuds(10000))


    