import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page



#st.write('Please provide information regarding soil type of the project area')
soil=['Filling material (no contamination)','Sand','Gravel','Rock','Silt','Clay','Peat','Filling material (contaminated)']
factor=['0.02','0.03','0.05','0.075','0.1','0.15','0.2','0.5']
number_fruits=[]
top=[]
max_value=None

col=st.columns(len(soil[:3]),gap='small')
col2=st.columns(len(soil[3:]),gap='small')
for index,types in enumerate(soil):
	if index<3:
		number=col[index].number_input(f'{types} %',max_value=max_value)
	else:
		number=col2[index-3].
	top.append(number*float(factor[index]))
	number_fruits.append(number)

	if sum(number_fruits)==100:
		break
soil_sum=sum(top)/100
try:
	print(soil_sum)
except:
	pass
#df=pd.read_csv('new.csv')
#df['soil_col']=soil_sum*df['base']
#
#df.to_csv('new.csv',index=False)
#if st.button('NEXT :arrow_forward:'):
#	switch_page('landuse')
