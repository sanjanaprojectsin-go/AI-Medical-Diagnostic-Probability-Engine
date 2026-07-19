from disease_data import diseases


def predict_disease(selected_symptoms):


    probabilities = {}



    for disease, data in diseases.items():


        probability = data["prior"]



        for symptom in selected_symptoms:


            if symptom in data["symptoms"]:


                probability *= data["symptoms"][symptom]


            else:

                # Additional user entered symptoms
                # handled safely

                probability *= 0.1



        probabilities[disease] = probability





    total = sum(probabilities.values())



    if total > 0:


        for disease in probabilities:


            probabilities[disease] = round(
                (probabilities[disease] / total) * 100,
                2
            )




    predicted_disease = max(
        probabilities,
        key=probabilities.get
    )



    return predicted_disease, probabilities