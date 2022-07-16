# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 01:34:39 2019

@author: Asım
"""

matris1 = [[0,0,0],[0,0,0],[0,0,0]]
matris2 = [[0,0,0],[0,0,0],[0,0,0]]
matris3 = [[0,0,0],[0,0,0],[0,0,0]]

def matris(q,w,e,r,t,y,u,i,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m,ak,ay):
    print("""
{}  {}  {}     {}  {}  {}     {}  {}  {}
{}  {}  {}  +  {}  {}  {}  =  {}  {}  {}
{}  {}  {}     {}  {}  {}     {}  {}  {}

""".format(q,w,e,r,t,y,u,i,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m,ak,ay))
    

matris101 = int(input("Matris1-1 : "))
matris102 = int(input("Matris1-2 : "))
matris103 = int(input("Matris1-3 : "))
matris111 = int(input("Matris1-4 : "))
matris112 = int(input("Matris1-5 : "))
matris113 = int(input("Matris1-6 : "))
matris121 = int(input("Matris1-7 : "))
matris122 = int(input("Matris1-8 : "))
matris123 = int(input("Matris1-9 : "))
matris1[0][0] = matris101
matris1[0][1] = matris102
matris1[0][2] = matris103
matris1[1][0] = matris111
matris1[1][1] = matris112
matris1[1][2] = matris113
matris1[2][0] = matris121
matris1[2][1] = matris122
matris1[2][2] = matris123
matris201 = int(input("Matris2-1 : "))
matris202 = int(input("Matris2-2 : "))
matris203 = int(input("Matris2-3 : "))
matris211 = int(input("Matris2-4 : "))
matris212 = int(input("Matris2-5 : "))
matris213 = int(input("Matris2-6 : "))
matris221 = int(input("Matris2-7 : "))
matris222 = int(input("Matris2-8 : "))
matris223 = int(input("Matris2-9 : "))
matris2[0][0] = matris201
matris2[0][1] = matris202
matris2[0][2] = matris203
matris2[1][0] = matris211
matris2[1][1] = matris212
matris2[1][2] = matris213
matris2[2][0] = matris221
matris2[2][1] = matris222
matris2[2][2] = matris223
matris301 = matris101 + matris201
matris302 = matris102 + matris202
matris303 = matris103 + matris203
matris311 = matris111 + matris211
matris312 = matris112 + matris212
matris313 = matris113 + matris213
matris321 = matris121 + matris221
matris322 = matris122 + matris222
matris323 = matris123 + matris223
matris3[0][0] = matris301
matris3[0][1] = matris302
matris3[0][2] = matris303
matris3[1][0] = matris311
matris3[1][1] = matris312
matris3[1][2] = matris313
matris3[2][0] = matris321
matris3[2][1] = matris322
matris3[2][2] = matris323
matris(matris1[0][0],matris1[0][1],matris1[0][2],matris2[0][0],matris2[0][1],matris2[0][2],matris3[0][0],matris3[0][1],matris3[0][2],matris1[1][0],matris1[1][1],matris1[1][2],matris2[1][0],matris2[1][1],matris2[1][2],matris3[1][0],matris3[1][1],matris3[1][2],matris1[2][0],matris1[2][1],matris1[2][2],matris2[2][0],matris2[2][1],matris2[2][2],matris3[2][0],matris3[2][1],matris3[2][2])    
