import glob
import os
import copy 
  
header=["Threshold","Senstivity","Specificity","Accuracy","MCC","ROC_AUC","Kappa"]


def append_file_to_csv(fname,feature_name,dirname):
	f=open(dirname+"/"+feature_name+"_out.csv","a+")
	f.write(fname+"\n")
	f.write(header[0]+','+header[1]+','+header[2]+','+header[3]+','+header[4]+','+header[5]+','+header[6]+"\n")
	fread=open(dirname+"/"+fname)
	for x in fread:
		x=x.strip()
		arr=x.split(',')
		arr[0]=arr[0].split(':')[1].strip()
		arr[1]=arr[1].split(':')[1].strip()
		arr[2]=arr[2].split(':')[1].strip()
		arr[3]=arr[3].split(':')[1].strip()
		arr[4]=arr[4].split(':')[1].strip()
		arr[5]=arr[5].split(':')[1].strip()
		arr[6]=arr[6].split(':')[1].strip()
		f.write(arr[0] +  ',' + arr[1] + ','+ arr[2] + ',' + arr[3] +  ',' + arr[4] +  ','  + arr[5] +  ','  +  arr[6] + "\n")
	f.write('\n')
	f.close()




classifier_names=[
"extra_trees_",
"knn_",
"mlp_",
"rf_",
"ridge_",
"svm_"
]

nc_terminalx=[
"",
"_c5",
"_c10",
"_c15",
"_n5",
"_n10",
"_n15",
"_nc5",
"_nc10",
"_nc15"
]

# filenames_normal=[]
# filename_kfold=[]
directories=[x[0] for x in os.walk('.')]

print(directories)

for dirname in directories:
	files=glob.glob(dirname+'/*.txt')
	files.sort()
	if dirname == './train' or dirname== './validation' or dirname=='.':
		continue
	if dirname.strip()=='.':
		continue
	
	feature_name=files[0].rsplit('/', 1)[1][12:][:-4]
	
	if dirname[0:5]=='./aac' or dirname[0:5]=='./dpc': 
		nc_terminal=copy.deepcopy(nc_terminalx)
	else:
		nc_terminal=[""]
	print(dirname)
	print(nc_terminal)
	filenames_normal=[]
	filename_kfold=[]
	for i in range(len(classifier_names)-1):
		fname_normal=classifier_names[i]+feature_name+".txt"
		fname_kfold=classifier_names[i]+"kfold_"+feature_name+".txt"	
		filenames_normal+=[fname_normal]
		filename_kfold+=[fname_kfold]
	for i  in range(len(nc_terminal)):
		fname_normal=classifier_names[len(classifier_names)-1]+feature_name+nc_terminal[i]+".txt"
		fname_kfold=classifier_names[len(classifier_names)-1]+"kfold_"+feature_name+nc_terminal[i]+".txt"	
		filenames_normal+=[fname_normal]
		filename_kfold+=[fname_kfold]

	for i in range(len(filenames_normal)):
		append_file_to_csv(filenames_normal[i],feature_name,dirname)
		append_file_to_csv(filename_kfold[i],feature_name,dirname)





