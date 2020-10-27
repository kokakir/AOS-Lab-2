# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:07:51 2020

@author: koka5
"""
from pathlib import Path
import numpy as np

class Processor:
    def __init__ (self):
        self.R1 = '1011011000111111111011'
        self.R2 = '1001100111100001111011'
        self.PS = ''
        self.PC = 0
        self.TC = 0
        self.IR = ''
        self.first_bit = 0
        self.command = ''
        self.opperand = ''
        print("Press enter")
        with open(Path('commands.txt'), encoding = "utf-8", mode = 'r') as file:
            for self.line in file:
                self.line = self.line.split("\n")[0]
                line_ = self.line.split(" ")
                self.command = line_[0]
                self.opperand = line_[1].split(",")
                if self.command == "mov":
                    self.func_mov()
                elif self.command == "bm2":
                    self.func_bitAddMod2()
    
    def check_par(self):
        if self.first_bit == '0':
            self.PS = '+'
        else:
            self.PS = '-'
        self.TC += 1
        if self.TC > 2:
            self.TC = 1
    
    def func_mov(self):
        input()
        self.PC += 1
        self.IR = self.line
        if self.opperand[0] == "R1":
            self.first_bit = self.R1[0]
        else:
            self.first_bit = self.R2[0]
        self.check_par()
        self.print_table()
        input()
        if self.opperand[0] == "R1":
            self.R1 = list(np.binary_repr(int(self.opperand[1]), width=22))
            self.first_bit = self.R1[0]
        else:
            self.R2 = list(np.binary_repr(int(self.opperand[1]), width=22))
            self.first_bit = self.R2[0]
        self.check_par()
        self.print_table()
        
    def func_bitAddMod2(self):
        input()
        self.PC += 1
        self.IR = self.line
        self.check_par()
        self.print_table()
        input()
        for i in range(len(self.R1)):
            if self.R1[i] == '1' and self.R2[i] == '1' or self.R1[i] == '0' and self.R2[i] == '0':
                self.R1[i] = 0
            else:
                self.R1[i] = 1
        self.first_bit = self.R1[0]
        self.check_par()
        self.print_table()
    
    def print_table(self):
        print("IR: |  | " + self.IR)
        print("R1: |  | " + ''.join([str(elem) for elem in self.R1]))
        print("R2: |  | " + ''.join([str(elem) for elem in self.R2]))
        print("PS: |  | " + str(self.PS))
        print("PC: |  | " + str(self.PC))
        print("TC: |  | " + str(self.TC), end="")
        
proc = Processor()
input("Press enter to exit")
