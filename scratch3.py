from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import numpy as np
import copy



def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1



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



def item_paring1(x):
	item_column_index=x.index
	list1=[]
	list2=[]
	list3=[]
	for i in range(len(item_column_index)):
		for j in range(i+1,len(item_column_index)):
			list1.append(item_column_index[i])
			list2.append(item_column_index[j])
	for i in range(len(list1)):
		list3.append([list1[i],list2[i]])
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



def item_paring2(sets):
	print(sets)
	number_set=len(sets)
	elements_in_set=len(sets[0])
	
	first_elements=[]
	for i in range(number_set):
		first_elements.append(sets[i][0])
		
		
	
	repeat=Repeat(first_elements)
	
	#print('ss')
	#print(repeat)
	Three_sets=[]
	for j in range(len(repeat)):
		Three_sets.append( [i for i, x in enumerate(first_elements) if x == repeat[j]])
	

	#print(Three_sets)
	
	all_=[]
	
	for i in range(len(Three_sets)):
		set_selected=Three_sets[i]
		set_length=len(set_selected)
		#print(set_length)
		#print('selected sets -'+str(set_selected))
	
		items_pairs=[]
		for j in range(len(set_selected)):
			items_pairs.append(sets[set_selected[j]])
		
		#print(items_pairs)
		initial=[]
		for j in range(len(set_selected)):
			initial=sets[set_selected[j]]
			#print('initial')
			#print(initial)
			#print(ll)
			
			for w in range(j+1,len(set_selected)):
				number_=[sets[set_selected[w]][1]]
				#print('instance'+str(w))
				#print(number_)
				final=initial
				final.extend(number_)
				#print(final)
				all_.append(list(final)) 
				#print(all_)
				final.pop()
				
				
	
	
	return(all_)




def calculate_frequency_of_pairs(sets):
	
	if(len(sets[0])>2):
		frq_pairs=[]
		for i in range(len(sets)):
			item_set=sets[i]
			a=df[ (df[df.columns[int(item_set[0])]] == 1) &(df[df.columns[int(item_set[1])]]==1) &(df[df.columns[int(item_set[2])]] == 1) ].sum()
			frq_pairs.append(a[int(item_set[0])])
	elif(len(sets[0])==2):	
		frq_pairs=[]
		for i in range(len(sets)):
			item_set=sets[i]
			a=df[ (df[df.columns[int(item_set[0])]] == 1) &(df[df.columns[int(item_set[1])]]==1) ].sum()
			frq_pairs.append(a[int(item_set[0])])
			
	return(frq_pairs)

def threshold_filtering(frq_pairs,pairs,df):
	support_of_pairs=calculate_support(frq_pairs,df)
	#print(support_of_pairs)


	threshold_filtered_pairs=[]
	for i in range(len(pairs)):
		if(support_of_pairs[i]>=support_thresh):
			threshold_filtered_pairs.append(pairs[i])


	return(threshold_filtered_pairs)

	
	

data= pd.read_excel('Online Retail.xlsx')

data['Description'] = data['Description'].str.strip()
data.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
data['InvoiceNo'] = data['InvoiceNo'].astype('str')
data = data[~data['InvoiceNo'].str.contains('C')]

basket = (data[data['Country'] =="France"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))


df = basket.applymap(encode_units)
df.drop('POSTAGE', inplace=True, axis=1)




support_thresh=0.09

df_with_initial_threshold=freq_initial(df,support_thresh)



print('Threshold filterd dataframe')

print(df_with_initial_threshold)
pairs=item_paring1(df_with_initial_threshold)
frq_pairs=calculate_frequency_of_pairs(pairs)		
threshold_filtered_pairs=threshold_filtering(frq_pairs,pairs,df)

########################################################

pairs_3d=item_paring2(threshold_filtered_pairs)
frq_3pairs=calculate_frequency_of_pairs(pairs_3d)
threshold_filtered_3pairs=threshold_filtering(frq_3pairs,pairs_3d,df)



		
if(len(threshold_filtered_pairs)>0):
	print(' 2 Items together ')
	for c in range(len(threshold_filtered_pairs)):
		for y in range(len(threshold_filtered_pairs[0])):
			print(df.columns[threshold_filtered_pairs[c][y]])
		print('\n')


if(len(threshold_filtered_3pairs)>0):
	print(' 3 Items together ')
	for c in range(len(threshold_filtered_3pairs)):
		for y in range(len(threshold_filtered_3pairs[0])):
			print(df.columns[threshold_filtered_3pairs[c][y]])
		print('\n')








