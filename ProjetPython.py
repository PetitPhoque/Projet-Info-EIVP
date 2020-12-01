# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 09:33:45 2020

@author: Albane Héliès
"""

import csv 

f = open('Capt1.csv')
g = open('Capt2.csv')
h = open('Capt3.csv')
i = open('Capt4.csv')
j = open('Capt5.csv')
k = open('Capt6.csv')

fichierCSV1 = csv.reader(f)
fichierCSV2 = csv.reader(g)
fichierCSV3 = csv.reader(h)
fichierCSV4 = csv.reader(i)
fichierCSV5 = csv.reader(j)
fichierCSV6 = csv.reader(k)



#toutes les valeurs de noise dans une liste, idem pour temp, hum, lum et CO2 en float

"""Capteur 1"""

noise_c1=[]
temp_c1=[]
hum_c1=[]
lum_c1=[]
carb_c1=[]
date_c1=[]
        
for ligne in fichierCSV1: 
        n=float(ligne[1])
        noise_c1.append(n) #contient toutes les valeurs noise captées par le capteur 1
        t=float(ligne[2])
        temp_c1.append(t) #temperature
        h=float(ligne[3])
        hum_c1.append(h) #humidity
        l=float(ligne[4])
        lum_c1.append(l) #luminosity
        c=float(ligne[5])
        carb_c1.append(c) #CO2
        d=str(ligne[6])
        date_c1.append(d) #date 
    
    
"""Capteur 2""" 

noise_c2=[]
temp_c2=[]
hum_c2=[]
lum_c2=[]
carb_c2=[]
date_c2=[]     
        

for ligne in fichierCSV2:
        n=float(ligne[1])
        noise_c2.append(n) #contient toutes les valeurs noise captées par le capteur 1
        t=float(ligne[2])
        temp_c2.append(t) #temperature
        h=float(ligne[3])
        hum_c2.append(h) #humidity
        l=float(ligne[4])
        lum_c2.append(l) #luminosity
        c=float(ligne[5])
        carb_c2.append(c) #CO2
        d=str(ligne[6])
        date_c2.append(d) #date 
        

"""Capteur 3"""

noise_c3=[]
temp_c3=[]
hum_c3=[]
lum_c3=[]
carb_c3=[]
date_c3=[]      

for ligne in fichierCSV3: 
        n=float(ligne[1])
        noise_c3.append(n) #contient toutes les valeurs noise captées par le capteur 1
        t=float(ligne[2])
        temp_c3.append(t) #temperature
        h=float(ligne[3])
        hum_c3.append(h) #humidity
        l=float(ligne[4])
        lum_c3.append(l) #luminosity
        c=float(ligne[5])
        carb_c3.append(c) #CO2
        d=str(ligne[6])
        date_c3.append(d) #date 
        
        
"""Capteur 4"""

noise_c4=[]
temp_c4=[]
hum_c4=[]
lum_c4=[]
carb_c4=[]
date_c4=[]      
        
for ligne in fichierCSV4: 
        n=float(ligne[1])
        noise_c4.append(n) #contient toutes les valeurs noise captées par le capteur 1
        t=float(ligne[2])
        temp_c4.append(t) #temperature
        h=float(ligne[3])
        hum_c4.append(h) #humidity
        l=float(ligne[4])
        lum_c4.append(l) #luminosity
        c=float(ligne[5])
        carb_c4.append(c) #CO2
        d=str(ligne[6])
        date_c4.append(d) #date 
        
        
"""Capteur 5"""

noise_c5=[]
temp_c5=[]
hum_c5=[]
lum_c5=[]
carb_c5=[]
date_c5=[]
        
        
for ligne in fichierCSV5: 
        n=float(ligne[1])
        noise_c5.append(n) #contient toutes les valeurs noise captées par le capteur 1
        t=float(ligne[2])
        temp_c5.append(t) #temperature
        h=float(ligne[3])
        hum_c5.append(h) #humidity
        l=float(ligne[4])
        lum_c5.append(l) #luminosity
        c=float(ligne[5])
        carb_c5.append(c) #CO2
        d=str(ligne[6])
        date_c5.append(d) #date 
        
        
"""Capteur 6"""

noise_c6=[]
temp_c6=[]
hum_c6=[]
lum_c6=[]
carb_c6=[]
date_c6=[]
        
        
for ligne in fichierCSV6: 
        n=float(ligne[1])
        noise_c6.append(n) #contient toutes les valeurs noise captées par le capteur 1
        t=float(ligne[2])
        temp_c6.append(t) #temperature
        h=float(ligne[3])
        hum_c6.append(h) #humidity
        l=float(ligne[4])
        lum_c6.append(l) #luminosity
        c=float(ligne[5])
        carb_c6.append(c) #CO2
        d=str(ligne[6])
        date_c6 .append(d) #date 
        
        
        
        
#calcul des min, max, écart-type, moyenne, variance, médiane
    
def minimum(liste):
    min=liste[0]
    for i in liste:
        if i<min:
            min=i
    return min 

def maximum(liste):
    max=liste[0]
    for i in liste:
        if i>max:
            max=i
    return max

def moyenne(liste):
    a=len(liste)
    assert a!=0
    s=0
    for i in range(a):
        s+=liste[i]
    return s/a

from math import sqrt,floor 

def ecarttype(liste):
    a=len(liste)
    m=moyenne(liste)
    v=0
    for i in range(a):
        v+=(liste[i]-m)**2
    return sqrt(v/a) #calcul de la variance et de l'écart-type en appliquant la racine carrée

def mediane(liste):
    a=len(liste)
    liste=liste.sort()
    if a%2==1:
        med=liste[floor(a/2)+1]
    if a%2==0:
        med=((liste[a/2]+liste[a/2+1]))/2
    return med 


#on convertit les dates en fixant la première date comme origine des temps (en secondes)
 

def dateconv(L):
    n=len(L) 
    listeDC=[]
    for i in range(n): 
        j=int(L[i][8:10])-11 #on récupère le jour et on soustrait le n° du 1er jour pour partir de j0
        h=int(L[i][11:13]) #heure
        m=int(L[i][14:16]) #minutes
        s= int(L[i][17:19]) #secondes
        datec= j*24*60*60+h*60*60+m*60+s #on convertit la date en secondes en partant de la 1ère date comme origine des temps
        listeDC.append(datec) #on crée la liste rassemblant toutes les dates
    return listeDC
        

temps_c1= dateconv(date_c1)
temps_c2= dateconv(date_c2)
temps_c3= dateconv(date_c3)
temps_c4= dateconv(date_c4)
temps_c5= dateconv(date_c5)
temps_c6= dateconv(date_c6)


    
    
#on forme une liste regroupant la différence entre les valeurs d'un capteur et d'un autre par rapport à une même variable 


def difference(L1,L2):
    diff=[]
    if len(L1)>=len(L2):
        for i in range(len(L2)):
            diff.append(abs(L2[i]-L1[i]))
    else:
        for i in range(len(L1)):
            diff.append(abs(L2[i]-L1[i]))
    return diff


#Pour les bruits 
    

noise_c1c2=difference(noise_c1,noise_c2)
noise_c1c3=difference(noise_c1,noise_c3)
noise_c1c4=difference(noise_c1,noise_c4)
noise_c1c5=difference(noise_c1,noise_c5)
noise_c1c6=difference(noise_c1,noise_c6)
noise_c2c3=difference(noise_c2,noise_c3)
noise_c2c4=difference(noise_c2,noise_c4)
noise_c2c5=difference(noise_c2,noise_c5)
noise_c2c6=difference(noise_c2,noise_c6)
noise_c3c4=difference(noise_c3,noise_c4)
noise_c3c5=difference(noise_c3,noise_c5)
noise_c3c6=difference(noise_c3,noise_c6)
noise_c4c5=difference(noise_c4,noise_c5)
noise_c4c6=difference(noise_c4,noise_c6)
noise_c5c6=difference(noise_c5,noise_c6)



#Pour la température 


temp_c1c2=difference(temp_c1,temp_c2)
temp_c1c3=difference(temp_c1,temp_c3)
temp_c1c4=difference(temp_c1,temp_c4)
temp_c1c5=difference(temp_c1,temp_c5)
temp_c1c6=difference(temp_c1,temp_c6)
temp_c2c3=difference(temp_c2,temp_c3)
temp_c2c4=difference(temp_c2,temp_c4)
temp_c2c5=difference(temp_c2,temp_c5)
temp_c2c6=difference(temp_c2,temp_c6)
temp_c3c4=difference(temp_c3,temp_c4)
temp_c3c5=difference(temp_c3,temp_c5)
temp_c3c6=difference(temp_c3,temp_c6)
temp_c4c5=difference(temp_c4,temp_c5)
temp_c4c6=difference(temp_c4,temp_c6)
temp_c5c6=difference(temp_c5,temp_c6)



#Pour l'humidité 


hum_c1c2=difference(hum_c1,hum_c2)
hum_c1c3=difference(hum_c1,hum_c3)
hum_c1c4=difference(hum_c1,hum_c4)
hum_c1c5=difference(hum_c1,hum_c5)
hum_c1c6=difference(hum_c1,hum_c6)
hum_c2c3=difference(hum_c2,hum_c3)
hum_c2c4=difference(hum_c2,hum_c4)
hum_c2c5=difference(hum_c2,hum_c5)
hum_c2c6=difference(hum_c2,hum_c6)
hum_c3c4=difference(hum_c3,hum_c4)
hum_c3c5=difference(hum_c3,hum_c5)
hum_c3c6=difference(hum_c3,hum_c6)
hum_c4c5=difference(hum_c4,hum_c5)
hum_c4c6=difference(hum_c4,hum_c6)
hum_c5c6=difference(hum_c5,hum_c6)




#Pour la lumière 


lum_c1c2=difference(lum_c1,lum_c2)
lum_c1c3=difference(lum_c1,lum_c3)
lum_c1c4=difference(lum_c1,lum_c4)
lum_c1c5=difference(lum_c1,lum_c5)
lum_c1c6=difference(lum_c1,lum_c6)
lum_c2c3=difference(lum_c2,lum_c3)
lum_c2c4=difference(lum_c2,lum_c4)
lum_c2c5=difference(lum_c2,lum_c5)
lum_c2c6=difference(lum_c2,lum_c6)
lum_c3c4=difference(lum_c3,lum_c4)
lum_c3c5=difference(lum_c3,lum_c5)
lum_c3c6=difference(lum_c3,lum_c6)
lum_c4c5=difference(lum_c4,lum_c5)
lum_c4c6=difference(lum_c4,lum_c6)
lum_c5c6=difference(lum_c5,lum_c6)




#Pour le CO2


carb_c1c2=difference(carb_c1,carb_c2)
carb_c1c3=difference(carb_c1,carb_c3)
carb_c1c4=difference(carb_c1,carb_c4)
carb_c1c5=difference(carb_c1,carb_c5)
carb_c1c6=difference(carb_c1,carb_c6)
carb_c2c3=difference(carb_c2,carb_c3)
carb_c2c4=difference(carb_c2,carb_c4)
carb_c2c5=difference(carb_c2,carb_c5)
carb_c2c6=difference(carb_c2,carb_c6)
carb_c3c4=difference(carb_c3,carb_c4)
carb_c3c5=difference(carb_c3,carb_c5)
carb_c3c6=difference(carb_c3,carb_c6)
carb_c4c5=difference(carb_c4,carb_c5)
carb_c4c6=difference(carb_c4,carb_c6)
carb_c5c6=difference(carb_c5,carb_c6)


#On calcule le maximum et le minimum de chaque variable et on normalise les listes 


def normalise2(L): #L est la liste dont les sous-listes sont toutes les distances entre les différents capteurs issues du programme difference
    n=min(len(L[i]) for i in range(len(L)))#on prend la plus petite longueur de sous-listes 
    for k in range(len(L)):
        del L[k][n:len(L[k])]
    sousliste=[] 
    for j in range(n) : 
        for k in range(len(L)):
            sousliste.append(L[k][j]) #on regroupe tous les 1ers puis 2ème puis 3ème jusqu'au n-ième (etc) éléments dans n listes 
        maxi=maximum(sousliste)
        mini=minimum(sousliste)
        for k in range(len(L)):
            L[k][j]=(L[k][j]-mini)/(maxi-mini)#on normalise les valeurs
    return L


#Pour le bruit - listes normalisées 
    
n_liste=[noise_c1c2,noise_c1c3,noise_c1c4,noise_c1c5,noise_c1c6,noise_c2c3,noise_c2c4,noise_c2c5,noise_c2c6,noise_c3c4,noise_c3c5,noise_c3c6,noise_c4c5,noise_c4c6,noise_c5c6]

noise_norm=normalise2(n_liste)


#Pour la température - listes normalisées 

t_liste=[temp_c1c2,temp_c1c3,temp_c1c4,temp_c1c5,temp_c1c6,temp_c2c3,temp_c2c4,temp_c2c5,temp_c2c6,temp_c3c4,temp_c3c5,temp_c3c6,temp_c4c5,temp_c4c6,temp_c5c6]

temp_norm=normalise2(t_liste)


#Pour l'humidité - listes normalisées 

h_liste=[hum_c1c2,hum_c1c3,hum_c1c4,hum_c1c5,hum_c1c6,hum_c2c3,hum_c2c4,hum_c2c5,hum_c2c6,hum_c3c4,hum_c3c5,hum_c3c6,hum_c4c5,hum_c4c6,hum_c5c6]

hum_norm=normalise2(h_liste)

#Pour la lumière - listes normalisées 

l_liste=[lum_c1c2,lum_c1c3,lum_c1c4,lum_c1c5,lum_c1c6,lum_c2c3,lum_c2c4,lum_c2c5,lum_c2c6,lum_c3c4,lum_c3c5,lum_c3c6,lum_c4c5,lum_c4c6,lum_c5c6]

lum_norm=normalise2(l_liste)

#Pour le CO2 - listes normalisées 

c_liste=[carb_c1c2,carb_c1c3,carb_c1c4,carb_c1c5,carb_c1c6,carb_c2c3,carb_c2c4,carb_c2c5,carb_c2c6,carb_c3c4,carb_c3c5,carb_c3c6,carb_c4c5,carb_c4c6,carb_c5c6]

carb_norm=normalise2(c_liste)


#on calcule la moyenne de la différence normalisées entre les capteurs pour chaque variable
#on fait un tableau recensant toutes les moyennes des différences normalisées entre les capteurs par rapport aux différents variables



#bruit 
 
n12_moy=moyenne(noise_norm[0]) 
n13_moy=moyenne(noise_norm[1])
n14_moy=moyenne(noise_norm[2])
n15_moy=moyenne(noise_norm[3])
n16_moy=moyenne(noise_norm[4])
n23_moy=moyenne(noise_norm[5])
n24_moy=moyenne(noise_norm[6])
n25_moy=moyenne(noise_norm[7])
n26_moy=moyenne(noise_norm[8])
n34_moy=moyenne(noise_norm[9])
n35_moy=moyenne(noise_norm[10])
n36_moy=moyenne(noise_norm[11])
n45_moy=moyenne(noise_norm[12])
n46_moy=moyenne(noise_norm[13])
n56_moy=moyenne(noise_norm[14])

import numpy as np 

n_tab=np.array([n12_moy,n13_moy,n14_moy,n15_moy,n16_moy,n23_moy,n24_moy,n25_moy,n26_moy,n34_moy,n35_moy,n36_moy,n45_moy,n46_moy,n56_moy])


#température

t12_moy=moyenne(temp_norm[0])
t13_moy=moyenne(temp_norm[1])
t14_moy=moyenne(temp_norm[2])
t15_moy=moyenne(temp_norm[3])
t16_moy=moyenne(temp_norm[4])
t23_moy=moyenne(temp_norm[5])
t24_moy=moyenne(temp_norm[6])
t25_moy=moyenne(temp_norm[7])
t26_moy=moyenne(temp_norm[8])
t34_moy=moyenne(temp_norm[9])
t35_moy=moyenne(temp_norm[10])
t36_moy=moyenne(temp_norm[11])
t45_moy=moyenne(temp_norm[12])
t46_moy=moyenne(temp_norm[13])
t56_moy=moyenne(temp_norm[14])

t_tab=np.array([t12_moy,t13_moy,t14_moy,t15_moy,t16_moy,t23_moy,t24_moy,t25_moy,t26_moy,t34_moy,t35_moy,t36_moy,t45_moy,t46_moy,t56_moy])


#humidité

h12_moy=moyenne(hum_norm[0])
h13_moy=moyenne(hum_norm[1])
h14_moy=moyenne(hum_norm[2])
h15_moy=moyenne(hum_norm[3])
h16_moy=moyenne(hum_norm[4])
h23_moy=moyenne(hum_norm[5])
h24_moy=moyenne(hum_norm[6])
h25_moy=moyenne(hum_norm[7])
h26_moy=moyenne(hum_norm[8])
h34_moy=moyenne(hum_norm[9])
h35_moy=moyenne(hum_norm[10])
h36_moy=moyenne(hum_norm[11])
h45_moy=moyenne(hum_norm[12])
h46_moy=moyenne(hum_norm[13])
h56_moy=moyenne(hum_norm[14])

h_tab=np.array([h12_moy,h13_moy,h14_moy,h15_moy,h16_moy,h23_moy,h24_moy,h25_moy,h26_moy,h34_moy,h35_moy,h36_moy,h45_moy,h46_moy,h56_moy])


#lumière

l12_moy=moyenne(lum_norm[0])
l13_moy=moyenne(lum_norm[1])
l14_moy=moyenne(lum_norm[2])
l15_moy=moyenne(lum_norm[3])
l16_moy=moyenne(lum_norm[4])
l23_moy=moyenne(lum_norm[5])
l24_moy=moyenne(lum_norm[6])
l25_moy=moyenne(lum_norm[7])
l26_moy=moyenne(lum_norm[8])
l34_moy=moyenne(lum_norm[9])
l35_moy=moyenne(lum_norm[10])
l36_moy=moyenne(lum_norm[11])
l45_moy=moyenne(lum_norm[12])
l46_moy=moyenne(lum_norm[13])
l56_moy=moyenne(lum_norm[14])


l_tab=np.array([l12_moy,l13_moy,l14_moy,l15_moy,l16_moy,l23_moy,l24_moy,l25_moy,l26_moy,l34_moy,l35_moy,l36_moy,l45_moy,l46_moy,l56_moy])

#taux de CO2

c12_moy=moyenne(carb_norm[0]) 
c13_moy=moyenne(carb_norm[1])
c14_moy=moyenne(carb_norm[2])
c15_moy=moyenne(carb_norm[3])
c16_moy=moyenne(carb_norm[4])
c23_moy=moyenne(carb_norm[5])
c24_moy=moyenne(carb_norm[6])
c25_moy=moyenne(carb_norm[7])
c26_moy=moyenne(carb_norm[8])
c34_moy=moyenne(carb_norm[9])
c35_moy=moyenne(carb_norm[10])
c36_moy=moyenne(carb_norm[11])
c45_moy=moyenne(carb_norm[12])
c46_moy=moyenne(carb_norm[13])
c56_moy=moyenne(carb_norm[14])


c_tab=np.array([c12_moy,c13_moy,c14_moy,c15_moy,c16_moy,c23_moy,c24_moy,c25_moy,c26_moy,c34_moy,c35_moy,c36_moy,c45_moy,c46_moy,c56_moy])


#on fixe un seuil s=0,20. Si la moyenne est supérieure à ce seuil, on considère que les capteurs ne sont pas considérés comme étant similaires par rapport à cette variable

def verdict(m): #ce programme prend en argument la moyenne des distances normées entre deux capteurs pour une donnée précise 
    s=float(0.20) #on définit un seuil 
    if m>s:
        print('Les deux capteurs ne sont pas similaires par rapport à cette donnée') #dans le cas où la moyenne est supérieure au seuil fixé
    else : 
        print('Les capteurs sont similaires par rapport à cette donnée') #dans le cas où la moyenne est inférieure ou égale au seuil fixé
        
        

#affichage des courbes représentatives des variables de tous les capteurs

import matplotlib.pyplot as plt 

#abscisses - temps 

x1= temps_c1
x2= temps_c2
x3= temps_c3
x4= temps_c4
x5= temps_c5
x6= temps_c6

#ordonnée - noise 

y1= noise_c1
y2= noise_c2
y3= noise_c3
y4= noise_c4
y5= noise_c5
y6= noise_c6

#ordonnée - température 

z1= temp_c1
z2= temp_c2
z3= temp_c3
z4= temp_c4
z5= temp_c5
z6= temp_c6

#ordonnée - humidité 

w1= hum_c1
w2= hum_c2
w3= hum_c3
w4= hum_c4
w5= hum_c5
w6= hum_c6

#ordonnée - luminosité

v1= lum_c1
v2= lum_c2
v3= lum_c3
v4= lum_c4
v5= lum_c5
v6= lum_c6


#ordonnée - taux de CO2

u1= carb_c1
u2= carb_c2
u3= carb_c3
u4= carb_c4
u5= carb_c5
u6= carb_c6

#tracé des courbes 

#bruit

plt.subplot(321)
plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)

#température

plt.subplot(322)
plt.plot(x1,z1,x3,z3,x4,z4,x5,z5,x6,z6)

#humidité

plt.subplot(323)
plt.plot(x1,w1,x2,w2,x3,w3,x4,w4,x5,w5,x6,w6)

#lumière

plt.subplot(324)
plt.plot(x1,v1,x2,v2,x3,v3,x4,v4,x5,v5,x6,v6)

#taux de CO2

plt.subplot(325)
plt.plot(x1,u1,x2,u2,x3,u3,x4,u4,x5,u5,x6,u6)


"""
#autre manière de présenter les courbes : exemple pour le bruit 

plt.subplot(321)
plt.plot(x1,y1)

plt.subplot(322)
plt.plot(x2,y2,"r")

plt.subplot(323)
plt.plot(x3,y3,"g")

plt.subplot(324)
plt.plot(x4,y4,"black")

plt.subplot(325)
plt.plot(x5,y5,"orange")

plt.subplot(326)
plt.plot(x6,y6,"pink")

"""

#indice de corrélation 

def cov(a,b):
    sum = 0
    n=min(len(a),len(b))
    for i in range(n):
        sum += ((a[i]-moyenne(a))*(b[i]-moyenne(b)))
    return sum/(len(a)-1)
    
import random 

def correlation(c,d,e,f,g):
    L=[c,d,e,f,g]
    a=random.choice(L)
    L.pop()
    b=random.choice(L)
    corr= (cov(a,b))/(ecarttype(a)*ecarttype(b))
    return corr

#exemple :
    
"""1ère execution:
correlation(noise_c1,temp_c1,lum_c1,hum_c1,carb_c1)=-0.06694269118979222

2ème execution:
correlation(noise_c1,temp_c1,lum_c1,hum_c1,carb_c1)=-0.20234330813738377

3ème execution:
correlation(noise_c1,temp_c1,lum_c1,hum_c1,carb_c1)=0.24128837471450856"""

