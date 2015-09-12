## encoding:utf-8--
## author :happybeetle
import numpy as np
myfavorites={}
myfavorites['gikoneko']=[
u'''
 ∧ ∧
(´ー`)%s
 U  U
''',
u'''
      ∧ ∧
 〜′‾‾(´ー`)%s
 UU‾‾ U  U
''',
u'''

　　＿
  〜′＿＼＿
　　U＼＿ ＼∧ ∧
　　　U  ＼(´ー`)%s
　           U  U
''',
u'''
    ∧ ∧
 〜′ (´ー`)%s
  UU U  U
''',
u'''
  ∧∧
~(´ｰ`)%s
  UUUU
''',
u'''
         ∧ ∧　 
   〜′‾‾( ﾟДﾟ)%s
     UU‾‾U U　
''' 
]
np.save('myfavorites.npy', myfavorites)



