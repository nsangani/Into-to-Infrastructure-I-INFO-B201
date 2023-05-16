# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:07:33 2019

@author: Sangani
"""
'''
A - U
T - A
G - C
C - G
'''

DNA = input("Input a DNA transcript(in A,T,G,C form): ") 
Ew_DNA = DNA.replace("G","B").replace("C", "D")  #giving G and C random variable (intermediates) so it can be changed for Rna trancript
RNA1 = Ew_DNA.replace("B","C").replace("D","G").replace("A","U").replace("T","A") #DNA is transcripted into RNA by replacing A, T and intermediates to U,A,G,C 
New_RNA = RNA1.strip() #this removes the space from the starting or end of the sequencing 
Final_RNA = "The RNA transcript is: \n" + New_RNA 

RNA_length = str(len(New_RNA)) #turns RNA into string and ask to show the length of the RNA
print(Final_RNA) 
print ("Total length: " + RNA_length) #length of RNA
As = str(Final_RNA.count("A")) #turning RNA into string and asking to count the number of base 'A' in the RNA 
Us = str(Final_RNA.count("U"))#same counting protocol for U base 
Cs = str(Final_RNA.count("C"))# Here fro base C
Gs = str(Final_RNA.count("G"))# For base G

print ("As: " + As) # Here we ask to commute the As,Us,Gs, and Cs variable to give the count of each bases. 
print ("Us: " + Us)
print ("Cs: " + Cs)
print ("Gs: " + Gs)



