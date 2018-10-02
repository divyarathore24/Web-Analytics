Instructions:

1. This folder contains rotten.txt file and finalProjectWeb.py 
2. Run the finalProjectWeb.py 
3. Expected outcome is: 

{'Linear Regression': 12.982060700555296, 'Grid Search': 18.561197340396163, 
'Random Forest': 14.248375390558063, 'SVM': 13.245602736505626, 'Decision Tree': 16.31835158127573}


Steps we followed:
==================

1. The function 'encode' is used to encode genre, ratings & top 10 studios.
2. We used actor_link to scrape data for each actor and calculate their total cast score for respective movies.
   The score was calculated as follows:	
   Certified Fresh Value is 2
   Fresh Value is 1
   Rotten Value is -1	
   Using actor scores, we calculated total cast score. 
   Since, scraping data for total movies would take too much time, we have commented it out.
3. We ran PCA for dimension reduction and then ran regression on 15 components
   Since there was no significant improvement in accuracy, we decided to go ahead with the original variables.
4. We used K-fold cross validation techniques to split the data into training and test data.
5. We used 5 prediction models to compare predicted results. 
   The models used are:
   Linear, Random Forest, SVM, Decision Trees and Grid Search (KNN, Decision Tree, Logistic Regression)
6. The output is a summary of all the models run and their corresponding error rates.
   For the data provided, SVM and LR are giving the best results.
