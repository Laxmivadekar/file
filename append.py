banks_list=['kotak','hdfc','rbl','sbi','andhra bank','bank of baroda']
for i in banks_list:
    f=open('ghi.txt','a')
    f.write(i)
    f.write('\n')
    f.close()