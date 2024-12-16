from flask import Flask,render_template,request
from src.get_menu import Menu
from src.get_weather import Weather
from src.get_timings import Timings
import numpy as np

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def menu():
    menu_obj=Menu()
    weather_obj=Weather()
    timings_obj=Timings()
    timings_obj.fetch_timings_data()
    weather_obj.fetch_weather_details()
    item_category, menu_list=menu_obj.get_menu_items()
    iteration=menu_list.shape[0]
    return render_template('menu.html', item_category=item_category, menu_list=menu_list,iteration=iteration)

@app.route('/selected_card')
def selected_card():
    menu_obj=Menu()
    weather_obj=Weather()
    timings_obj=Timings()

    selected_value = request.args.get('value', 'No value selected')
    # Getting similar Items for recommendation
    smi,df, predicted_price=menu_obj.get_similar_results(selected_value)


    # Getting weather and temperature Status of Restaurant region
    weather, temperature=weather_obj.get_weather_data()
    opened, weekdays_opening=timings_obj.weekday_timings()
    
    if timings_obj.busy_timings()=="Busy":
        if predicted_price[0]==np.min(predicted_price):
            predicted_price[0]=predicted_price[1]+(0.01*np.min(predicted_price))
        predicted_price=np.round(predicted_price,2)
    elif weather=="Rain" or weather=="Snow":
        if predicted_price[0]==np.min(predicted_price):
            predicted_price[0]=predicted_price[1]+(0.01*np.min(predicted_price))
        predicted_price=np.round(predicted_price,2)
    elif int(temperature)<45:
        if predicted_price[0]==np.min(predicted_price):
            predicted_price[0]=predicted_price[1]+(0.01*np.min(predicted_price))
        predicted_price=np.round(predicted_price,2)
    else:
        # Getting Predicted Price Values
        if predicted_price[0]!=np.min(predicted_price):
            predicted_price[0]=np.min(predicted_price)-(0.03*np.min(predicted_price))
        predicted_price=np.round(predicted_price,2)


    return render_template('results.html',similar_item_index=smi,df=df,
    selected_value=int(selected_value),price=predicted_price, weather=weather, 
    temperature=temperature, open=opened, weekdays_opening=weekdays_opening)

if __name__=="__main__":
    app.run(debug=True)