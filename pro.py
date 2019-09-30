import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

# probability of  fico score greater than 700

p_a = df[df['fico'].astype(float) >700].shape[0]/df.shape[0]
print(p_a)


# probability of purpose == debt_consolidation
p_b = df[df['purpose']== 'debt_consolidation'].shape[0]/df.shape[0]
print(p_b)

# Create new dataframe for condition ['purpose']== 'debt_consolidation' 
df1 = df[df['purpose']== 'debt_consolidation']

# Calculate the P(A|B)
p_a_b = df1[df1['fico'].astype(float) >700].shape[0]/df1.shape[0]
print(p_a_b)
# Check whether the P(A) and P(B) are independent from each other
result = (p_a == p_a_b)
print(result)

#Apply bayes Theorem
total= len(df)  
prob_lp = (df['paid.back.loan']=='Yes').sum()/total
print('probability of loan paid back P(A):',prob_lp) ##probability of A
prob_cs= (df['credit.policy']=='Yes').sum()/total
print('probability of credit policy P(B):',prob_cs) ## probability of B
new_df=df[df['paid.back.loan']=='Yes']
prob_pd_cs=new_df[new_df['credit.policy'] == 'Yes'].shape[0] / new_df.shape[0]  ##B given A
print('p(B|A):',prob_pd_cs)
bayes= (prob_pd_cs*prob_lp)/prob_cs ## applying bayes theorem
print('bayes value is:',bayes)


#bar plot for purpose
df['purpose'].value_counts(normalize=True).plot(kind='bar',figsize=[12,10])
plt.xlabel('"Number of Purpose"')
plt.ylabel("Probability")
plt.title("Probability Distribution of Purpose")
plt.show()

#plot the bar plot for 'purpose' where paid.back.loan == No 
df1= df[df['paid.back.loan']=='No']
df1.purpose.value_counts(normalize=True).plot(kind='Bar',figsize=[12,10])
plt.xlabel('"Number of Purpose"')
plt.ylabel("Probability")
plt.title("Probability Distribution of Purpose")
plt.show()


#visualization of continuous variable
inst_median = df['installment'].median()  ##median
print('median of installment:',inst_median)
inst_mean = df['installment'].mean() ###mean
print('mean of installment:',inst_mean)
df.installment.hist(figsize=[13,10]) ##histogram plotting
plt.axvline(x=inst_median,color='r') ##ploting median
plt.axvline(x=inst_mean,color='g') ####plotting mean
plt.xlabel('installment amount') 
plt.ylabel('frequency')
plt.title('Histogram  of installment')
plt.show()
df['log.annual.inc'].hist() ## plot histogram
plt.xlabel('annual income in logarithmic')
plt.ylabel('frequency')
plt.title('Histogram  of log annual income')
plt.show()
