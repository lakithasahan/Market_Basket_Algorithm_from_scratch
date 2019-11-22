from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import numpy as np
import copy

def calculate_support(frq_of_data,df_):
	support=[]
	supp=0.0
	for i in range(len(frq_of_data)):
		#print(frq_of_data[i],len(df_.index))
		
		supp=float(frq_of_data[i])/float(len(df_.index))
		support.append(supp)
		
	return(support)	
	


def freq_initial(df,support_thresh):
	

	initial_freq=[]
	for i in range(len(df.columns)):
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



def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated 



def element_paring(sets):
	print('kekek')
	print(sets)
	number_set=len(sets)
	elements_in_set=len(sets[0])
	#both = set(list_A).intersection(list_B)
	
	first_elements=[]
	for i in range(number_set):
		first_elements.append(sets[i][0])
		
		
	
	repeat=Repeat(first_elements)
	
	print('ss')
	print(repeat)
	Three_sets=[]
	for j in range(len(repeat)):
		Three_sets.append( [i for i, x in enumerate(first_elements) if x == repeat[j]])
	
	#locations_=first_elements.index(2)
	print(Three_sets)
	
	a=[]
	
	for i in range(len(Three_sets)):
		set_selected=Three_sets[i]
		set_length=len(set_selected)
		print(set_length)
		print('selected sets -'+str(set_selected))
	
		items_pairs=[]
		for j in range(len(set_selected)):
			items_pairs.append(sets[set_selected[j]])
		
		print(items_pairs)
		initial=[]
		for j in range(len(set_selected)):
			initial=sets[set_selected[j]]
			print('initial')
			print(initial)
			#print(ll)
			
			for w in range(j+1,len(set_selected)):
				number_=[sets[set_selected[w]][1]]
				print('instance'+str(w))
				print(number_)
				final=initial
				final.extend(number_)
				print('dfdf')
				print(final)
				a.append(list(final)) 
			
				print(a)
				final.pop()
				
				
				
	
		
		
		
		'''
		for y in range(len(set_selected)):
			for j in range(1,len(set_selected)):
					print(sets[set_selected[y]])
					initial_set=sets[set_selected[y]]
					initial_set.extend(sets[set_selected[j]])
					print(initial_set)
					initial_set.pop(2)
					print(initial_set)
				
			print(ll)
	
		'''	
		
		
	
	return(a)




def calculate_frequency_of_pairs(sets):
	
	frq_pairs=[]
	for i in range(len(sets)):
		item_set=sets[i]
		#print(item_set)
		#for j in range(len(item_set)):
		#a=df[[,df.columns[int(item_set[1])]]]
		a=df[ (df[df.columns[int(item_set[0])]] == 1) &(df[df.columns[int(item_set[1])]]==1) &(df[df.columns[int(item_set[2])]] == 1) ].sum()
		frq_pairs.append(a[int(item_set[0])])
	
	return(frq_pairs)
	
	
	







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


support_thresh=0.2

df_with_initial_threshold=freq_initial(df,support_thresh)
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
	frq_pairs.append(a[int(item_set[0])])
	
	
	
	
print(frq_pairs)	
		
support_of_pairs=calculate_support(frq_pairs,df)
print(support_of_pairs)


threshold_filtered_pairs=[]
for i in range(len(pairs)):
	if(support_of_pairs[i]>=support_thresh):
		threshold_filtered_pairs.append(pairs[i])

print('threshold_filtered_pairs')
print(threshold_filtered_pairs)


########################################################

pairs_3digit=element_paring(threshold_filtered_pairs)
print(pairs_3digit)
frequency=calculate_frequency_of_pairs(pairs_3digit)
print(frequency)


support_of_3pairs=calculate_support(frequency,df)
print(support_of_3pairs)
print(df)




threshold_filtered_3pairs=[]
for i in range(len(pairs_3digit)):
	if(support_of_3pairs[i]>=support_thresh):
		threshold_filtered_3pairs.append(pairs_3digit[i])

print('threshold_filtered_pairs')
print(threshold_filtered_3pairs)



'''
liste=['1','2','3','4','5','6','7']

retList, supportData=scanD(df, liste, 0.5)

print(supportData)
print(retList)




'''





'''
support__ = pd.Series(support_)

print(support__)

support_column_position=len(df.columns)
print(support_column_position)

df.insert(support_column_position, "support", support__) 


print(df)


'''






