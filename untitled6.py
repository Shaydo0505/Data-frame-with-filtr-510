# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C1WdJA9l_qBVDTXxIekEarUlLd8J9-Vu
"""

import pandas as pd
baza={
    "FISh":['Aliyev Vali' ,'Valiyev Ali','Ahrorova Alora','Ibrogemova Malika','Boltoyev Baxtiyor', 'Azizov Abror', 'Rashidov Jasur','Baratov Ahror','Rajabov Zokir','Jurayeva Madina','Akramova Kumush'  ],
    "yoshi":[ '12','13','11','11','10','12','11','10','14','12','11' ],
    "Jinsi": ['ogil bola', 'ogil bola', 'qiz bola','qiz bola','ogil bola','ogil bola','ogil bola','ogil bola','ogil bola','qiz bola','qiz bola' ],
    "Qaysi maktabda":[ '40-maktab','38-maktab', 'Prizendent maktabi','11-maktab ','11-maktab ','161-maktab','1-maktab ','111-maktab ','101-maktab ','15-maktab ','41-maktab '  ]
}
df=pd.DataFrame(baza)
print(df)

filtr=df[(df['Jinsi']=="qiz bola") &(df['yoshi']=='11')]
print(filtr)

filtr=df[(df['Jinsi']=="ogil bola") &(df['yoshi']>'10')]
print(filtr)

filtr=df[(df['Qaysi maktabda']>"40") ]
print(filtr)