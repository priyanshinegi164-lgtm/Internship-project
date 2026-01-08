import pickle
with open("svm.pickle","rb") as file:
    model=pickle.load(file)
    
print("model loaded successfully")
print(model)
    
sample=[[5.7,2.8,4.1,1.3]]

prediction=model.predict(sample)
print("prediction",prediction)