from mlxtend.preprocessing import TransactionEncoder
import pandas as pd



def calculate_support(x,df):
	support=[]
	supp=0.0
	for i in range(len(x)):
		supp=float(x[i])/float(len(df.index))
		support.append(supp)
		
	return(support)	
	


def freq_initial(df,colums,support_thresh):
	

	initial_freq=[]
	for i in range(len(colums)):
		initial_freq.append(df[df.columns[i]].sum())


	support_=calculate_support(initial_freq,df)
	freq_table=pd.DataFrame(support_)
	freq_table.insert(1, "freq", initial_freq)
	print('data frme with support and frequency of all the items ')
	print(freq_table)
 
	df_with_initial_threshold=freq_table[(freq_table[freq_table.columns[0]]>=support_thresh)]
	return(df_with_initial_threshold)



def item_pair(x):
	
	item_column_index=x.index
	#print(item_column_index)
	
	list1=[]
	list2=[]
	list3=[]
	#print(item_column_index[1])
	

	for i in range(len(item_column_index)):
		for j in range(i+1,len(item_column_index)):
			#print(i,j)
			list1.append(item_column_index[i])
			list2.append(item_column_index[j])
			
		
	#print(list1)
	#print(list2)
	for i in range(len(list1)):
		list3.append([list1[i],list2[i]])
	#out=list3.append(list1

	#print(list3)
	
	return(list3)







dataset = [['Apple', 'Beer', 'Rice', 'Chicken'],
           ['Apple', 'Beer', 'Rice'],
           ['Apple', 'Beer'],
           ['Apple', 'Bananas'],
           ['Milk', 'Beer', 'Rice', 'Chicken'],
           ['Milk', 'Beer', 'Rice'],
           ['Milk', 'Beer'],
           ['Apple', 'Bananas']]
           
           
te = TransactionEncoder()

te_ary = te.fit(dataset).transform(dataset)
data=te_ary.astype("int")
colums=te.columns_
df=pd.DataFrame(data, columns=te.columns_)
print('initial datafram ')
print(df)


support_thresh=0.5

df_with_initial_threshold=freq_initial(df,colums,support_thresh)
#print(ll)

'''
initial_freq=[]
for i in range(len(colums)):
	initial_freq.append(df[df.columns[i]].sum())


support_=calculate_support(initial_freq,df)
freq_table=pd.DataFrame(support_)
freq_table.insert(1, "freq", initial_freq)
print('data frme with support and frequency of all the items ')
print(freq_table)
 
df_with_initial_threshold=freq_table[(freq_table[freq_table.columns[0]]>=support_thresh)]

'''

print('Threshold filterd dataframe')

print(df_with_initial_threshold)

pairs=item_pair(df_with_initial_threshold)

print(pairs)


frq_pairs=[]
for i in range(len(pairs)):
	item_set=pairs[i]
	#print(item_set)
	#for j in range(len(item_set)):
	#a=df[[,df.columns[int(item_set[1])]]]
	a=df[ (df[df.columns[int(item_set[0])]] == 1) &(df[df.columns[int(item_set[1])]]==1) ].sum()

	#print(a[int(item_set[0])])
	
	frq_pairs.append(a[int(item_set[0])])
print(frq_pairs)	
		





























'''
support__ = pd.Series(support_)

print(support__)

support_column_position=len(df.columns)
print(support_column_position)

df.insert(support_column_position, "support", support__) 


print(df)


'''






