# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:18:17 2020

@author: mnafi
"""
class compute:
    def mean(age):
        pembagi = 0
        hasil = 0
        for i in age:
            hasil += i
            pembagi += 1
        hasil1 = round(hasil/pembagi, 2)
        return hasil1
    
    def mode(age):
        nilaiJumlah = {
                "angka" : "jumlah"
                }
        nilaiModus = {
                "angka" : "jumlah"
                }
        for i in range(len(age)):
            bantu=0
            for j in range(len(age)):
                if age[i]==age[i-1]:
                    pass
                elif age[i]==age[j]:
                    bantu+=1
                    nilaiJumlah[age[i]]=bantu
        nt = 0
        for i in range(0,len(age)-1):
            if nilaiJumlah[age[i]]>= nt:
                nt = nilaiJumlah[age[i]]
        for i in range(len(nilaiJumlah)):
            if nilaiJumlah[age[i]]==nt:
                nilaiModus[age[i]]=nt            
        return nilaiModus
    
    def FNS(age):
        tengah = int(round(len(age)/2,0))
        bawah = int(round(len(age)/4,0))
        atas = int(round(len(age)*3/4,0))
        q = []
        q2 = age[tengah-1]
        q1 = age[bawah-1]
        q3 = age[atas-1]
        q.append(min(age))
        q.append(q1)
        q.append(q2)
        q.append(q3)
        q.append(max(age))
        return q
    
    def outlier(age,q):
        iqr = q[3]-q[1]
        ol = 1.5 * iqr
        print(iqr,ol)
        outlier=[]
        for i in age:
            if i > q[3]+ol or i < q[1]-ol:
                outlier.append(i)
        return outlier
                
class tugas:
    def RUN():
        age = [5, 8, 15, 20, 23, 25, 26, 27, 29, 30, 31, 32, 35, 35, 36, 36, 37, 37, 39, 45, 58, 60, 81]
        mean1 = compute.mean(age)
        mode1 = compute.mode(age)
        fns1 = compute.FNS(age)
        outlier = compute.outlier(age,fns1)
        print("Meannya adalah",mean1,"\n")
        print("Modusnya adalah :")
        print(mode1)
        print("\nMin, Q1, Q2, Q3, Max :")
        print(fns1)
        print("\nOutlier: ")
        print(outlier)
    
    if __name__ == "__main__":
        RUN()