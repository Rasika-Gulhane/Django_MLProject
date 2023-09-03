from django.shortcuts import render


from joblib import load
model = load('./savedModels/model.joblib')


# Create your views here.

def predictor(request):
    if request.method == 'POST':
        sepal_length = request.POST['sepallength']
        sepal_width = request.POST['sepalwidth']
        petal_length = request.POST['petallength']
        petal_width = request.POST['petalwidth']

        y_pred = model.predict([[sepal_length,sepal_width, petal_length, petal_width]])

        if y_pred[0] == 0:
            result = 'setosa' 
        elif y_pred[0] == 1:
            result = 'versicolor'
        else:
            result = 'verginica'

        return render(request, 'iris.html', {'result' : result})
    return render(request, 'iris.html')


     
 






