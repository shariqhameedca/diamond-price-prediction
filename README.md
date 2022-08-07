# Diamond Price Prediction
In this project, I used Diamonds dataset from Kaggle. I performed analysis, visualization, cleaning and preprocessing of the data.
I created 3 models, Linear Regression, Polynomial Regression and Random Forest Regressor.
Finally, I created a simple flask server which takes dimensions of a diamond, let's you select a model for inference and then gives you the predicted price.


### Make sure you have the following installed:

1) Numpy, pandas, matplotlib, scikit-learn, seaborn
2) Flask

### To run the project:

1) Clone the repository
2) Run the Notebook using Jupyter
3) Run all cells, this will make the saved_models folder where models will be saved.
4) Run server.py (Make sure you have flask installed)

The main landing page looks like this:

![image](https://user-images.githubusercontent.com/57900267/183287597-477acfd7-ac71-4e9b-974e-ad48d5ccb21d.png)

Enter dimensions here for any diamond and select a model, it will give results like this:

![image](https://user-images.githubusercontent.com/57900267/183287665-b79de65e-0346-48c9-93ce-a42fdb14231d.png)
