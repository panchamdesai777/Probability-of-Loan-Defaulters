# Probability-of-Loan-Defaulters
For this project, we will be exploring the publicly available data from LendingClub.com. Lending Club connects people who need money (borrowers) with people who have money (investors). As an investor one would want to invest in people who showed a profile of having a high probability of paying the amount back.

![Alt txt](http://fairbetquery.com/wp-content/uploads/2017/06/Probability-Betting.png)

## Problem Statement :
What is the probability that the borrower paid back their loan in full?

## About the dataset: <br/>
The dataset consists of information about the customer like : <br/>
* ID of the customer <br/>
* If the customer meets the credit underwriting criteria of LendingClub.com or not <br/> 
* The purpose of the loan(takes values :"creditcard", "debtconsolidation", "educational", "majorpurchase", "smallbusiness", and "all_other"). <br/>
* The interest rate of the loan
* The monthly installments owed by the borrower if the loan is funded
* The natural log of the self-reported annual income of the borrower
* The debt-to-income ratio of the borrower (amount of debt divided by annual income)
* The FICO credit score of the borrower
* The number of days the borrower has had a credit line.
* The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle)
* The borrower's revolving line utilization rate (the amount of the credit line used relative to total credit available)
* The borrower's number of derogatory public records (bankruptcy filings, tax liens, or judgments)
* The borrower's number of inquiries by creditors in the last 6 months
* The number of times the borrower had been 30+ days past due on a payment in the past 2 years
* Whether the user has paid back loan

## Things done in project:
* To calculate the joint probability it's very important that conditions are idependent from each other.check whether the condition fico credit score is greater than 700 and purpose == 'debt_consolidation' are independent from each other.<br/>
* Calculating conditional probabilty is the very important step. Let's calculate the bayes theorem for the probability of credit policy is yes and the person is given the loan.
*  visualization of Purpose vs paid back loan
*  plot the histogram for visualization of the continuous variable. So that you will get the basic idea about how the distribution of continuous variables looks like.

## Learnings from this project:
After completing this project, we will have a better understanding of probability. In this project, you will apply the following concepts.
* Independency check
* Bayes theorem
* Visualizing discrete variable
* Visualizing continuous variable
