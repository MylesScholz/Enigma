#Run Script for Enigma
#Myles Scholz

import enigma

def run():
    e = enigma.enigma(3,[0,0,0])
    e.load_rotors("rotors.p")
    print(e.parse_list(e.decode(e.parse_string("hcxx"))))
    e.store_rotors("rotors.p")