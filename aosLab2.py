# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:07:51 2020

@author: koka5
"""
from pathlib import Path
import numpy as np

class Processor:
    def __init__ (self):
        self.n = 14
        self.first_reg = 1
        self.R1 = '10110110001111'
        self.R2 = '10011001111000'
        self.PS = ''
        self.PC = 0
        self.TC = 0
        self.IR = ''
        self.first_bit = 0
        self.command = ''
        self.opperand = ''
        self.info()
        self.file_name = 'commands.txt'
        print("Press enter")
        with open(Path(self.file_name), encoding = "utf-8", mode = 'r') as file:
            for self.line in file:
                self.line = self.line.split("\n")[0]
                line_ = self.line.split(" ")
                self.command = line_[0]
                self.opperand = line_[1].split(",")
                if self.opperand[0] == 'R1':
                    self.first_reg = 1
                else:
                    self.first_reg = 2
                if self.command == "mov":
                    self.func_mov()
                elif self.command == "bm2":
                    self.func_bitAddMod2()
                elif self.command == "sub":
                    self.func_subtracting()
     
    def info(self):
        print("Лабораторна робота №2")
        print("Киричека Миколи Павловича, К-21")
    
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
            self.R1 = list(np.binary_repr(int(self.opperand[1]), width=self.n))
            self.first_bit = self.R1[0]
        else:
            self.R2 = list(np.binary_repr(int(self.opperand[1]), width=self.n))
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
        for i in range(self.n):
            if self.first_reg == 1:
                if self.R1[i] == '1' and self.R2[i] == '1' or self.R1[i] == '0' and self.R2[i] == '0':
                    self.R1[i] = 0
                else:
                    self.R1[i] = 1
            else:
                if self.R1[i] == '1' and self.R2[i] == '1' or self.R1[i] == '0' and self.R2[i] == '0':
                    self.R2[i] = 0
                else:
                    self.R2[i] = 1
                
        self.first_bit = self.R1[0]
        self.check_par()
        self.print_table()
    
    def func_subtracting(self):
        input()
        self.PC += 1
        self.IR = self.line
        self.check_par()
        self.print_table()
        input()
        for i in range(self.n):
            if self.first_reg == 1:
                if self.R2[i] == '1':
                    self.R2[i] = '0'
                else:
                    self.R2[i] = '1'
            else:
                if self.R1[i] == '1':
                    self.R1[i] = '0'
                else:
                    self.R1[i] = '1'
        
        if self.first_reg == 1:
            if self.R2[self.n - 1] == '0':
                self.R2[self.n - 1] = '1'
            else:
                self.R2[self.n - 1] = '0'
                for j in range(self.n - 1):
                    if self.R2[self.n - 2 - j] == '0':
                        self.R2[self.n - 2 - j] = '1'
                        break
                    else:
                        self.R2[self.n - 2 - j] = '0'
        else:
            if self.R1[self.n - 1] == '0':
                self.R1[self.n - 1] = '1'
            else:
                self.R1[self.n - 1] = '0'
                for j in range(self.n - 1):
                    if self.R1[self.n - 2 - j] == '0':
                        self.R1[self.n - 2 - j] = '1'
                        break
                    else:
                        self.R1[self.n - 2 - j] = '0'       
        i = 0
        while (i < self.n):
            if self.first_reg == 1:
                if self.R1[self.n - i - 1] == '0' and self.R2[self.n - i - 1] == '0':
                    self.R1[self.n - i - 1] = '0'
                elif self.R1[self.n - i - 1] == '0' and self.R2[self.n - i - 1] == '1':
                    self.R1[self.n - i - 1] = '1'  
                elif self.R1[self.n - i - 1] == '1' and self.R2[self.n - i - 1] == '0':
                    self.R1[self.n - i - 1] = '1'
                elif self.R1[self.n - i - 1] == '1' and self.R2[self.n - i - 1] == '1':
                    self.R1[self.n - i - 1] = '0'
                    for n in range(self.n - i - 1):
                        if self.R1[self.n - i - 2 - n] == '1' and self.R2[self.n - i - 2 - n] == '1':
                            self.R1[self.n - i - 2 - n] = '1'
                        elif self.R1[self.n - i - 2 - n] == '1' and self.R2[self.n - i - 2 - n] == '0':
                            self.R1[self.n - i - 2 - n] = '0'
                        elif self.R1[self.n - i - 2 - n] == '0' and self.R2[self.n - i - 2 - n] == '0':
                            self.R1[self.n - i - 2 - n] = '1'
                            break
                        elif self.R1[self.n - i - 2 - n] == '0' and self.R2[self.n - i - 2 - n] == '1':
                            self.R1[self.n - i - 2 - n] = '0'
                    i = i + n + 1
            else:
                if str(self.R1[self.n - i - 1]) == '0' and str(self.R2[self.n - i - 1]) == '0':
                    self.R2[self.n - i - 1] = 0
                elif str(self.R1[self.n - i - 1]) == '0' and str(self.R2[self.n - i - 1]) == '1':
                    self.R2[self.n - i - 1] = 1
                elif str(self.R1[self.n - i - 1]) == '1' and str(self.R2[self.n - i - 1]) == '0':
                    self.R2[self.n - i - 1] = 1  
                elif str(self.R1[self.n - i - 1]) == '1' and str(self.R2[self.n - i - 1]) == '1':
                    self.R2[self.n - i - 1] = '0'
                    for n in range(self.n - i - 1):
                        if self.R1[self.n - i - 2 - n] == '1' and self.R2[self.n - i - 2 - n] == '1':
                            self.R2[self.n - i - 2 - n] = '1'
                        elif self.R1[self.n - i - 2 - n] == '1' and self.R2[self.n - i - 2 - n] == '0':
                            self.R2[self.n - i - 2 - n] = '0'
                        elif self.R1[self.n - i - 2 - n] == '0' and self.R2[self.n - i - 2 - n] == '0':
                            self.R2[self.n - i - 2 - n] = '1'
                            break
                        elif self.R1[self.n - i - 2 - n] == '0' and self.R2[self.n - i - 2 - n] == '1':
                            self.R2[self.n - i - 2 - n] = '0'
                    i = i + n + 1 
            i += 1
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
print()
input("Press enter to exit")
