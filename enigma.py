#Enigma Machine Simulation
#Myles Scholz

import random
import pickle as p
import re

class enigma():
    def __init__(self, num, preset):
        li = []
        for a in range(26): li.append(a)
        self.rotors = []
        for a in range(num): self.rotors.append(random.sample(li,26))
        self.inc_count = []
        for a in self.rotors: self.inc_count.append(0)
        self.preset = preset
        self.set_rotors(preset)
    
    def feed_through(self, i, n):
        if n == 0:
            return self.rotors[n][i]
        else:
            return self.rotors[n][self.feed_through(i,n-1)]
    
    def feed_back(self, i, n):
        if n == 0:
            return self.rotors[n].index(i)
        else:
            return self.feed_back(self.rotors[n].index(i), n-1)
    
    def inc_rotors(self, n):
        end = self.rotors[n][25]
        del self.rotors[n][25]
        self.rotors[n] = [end] + self.rotors[n]
        
        self.inc_count[n] += 1
        if self.inc_count[n] % 26 == 0:
            if n != len(self.rotors)-1:
                self.inc_rotors(n+1)
    
    def set_rotors(self, s):
        for i in range(len(self.rotors)):
            while self.rotors[i][0] != s[i]:
                end = self.rotors[i][25]
                del self.rotors[i][25]
                self.rotors[i] = [end] + self.rotors[i]
    
    def encode(self, message_in):
        message_out = []
        for letter in message_in:
            message_out.append(self.feed_through(letter, len(self.rotors)-1))
            self.inc_rotors(0)
        
        return message_out
    
    def decode(self, message_in):
        self.set_rotors(self.preset)
        message_out = []
        for letter in message_in:
            message_out.append(self.feed_back(letter, len(self.rotors)-1))
            self.inc_rotors(0)
        
        return message_out
    
    def store_rotors(self, file_path):
        self.set_rotors(self.preset)
        f = open(file_path, "wb")
        p.dump(self.rotors, f)
        f.close()
    
    def load_rotors(self, file_path):
        f = open(file_path, "rb")
        self.rotors = p.load(f)
        f.close()
    
    def parse_string(self, string):
        abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        string = string.lower()
        string = re.sub("[^a-z]+","",string)
        char_list = list(string)
        list_out = []
        for char in char_list:
            list_out.append(abc.index(char))
        
        return list_out

    def parse_list(self, list_in):
        abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        string_out = ""
        for num in list_in:
            string_out = string_out + abc[num]
        
        return string_out