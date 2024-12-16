# Food Price Recommender System
    It is a machine learning algorithm app which shows similar suggestions of restaurants based on selected item from menu.
    This application shows the predicted price of restaurants based on trained data.
    Note:
    Prices of restaurants may vary based on weather conditions, temperature and busy schedule of restaurants.

## Frameworks used:
![alt text](/static/images/image.png)
    
    Flask is a python framework used to create web applications.

![alt text](/static/images/image-1.png)

    It is a python library used for machine learning to implement machine learning algorithms, metrics and other preprocessing techniques.

![alt text](/static/images/image-5.png)

    Hyper text markup language is a language to implement structural designing of webpages in frontend.

![alt text](/static/images/image-4.png)

    Cascade style sheet is a style sheet to implement positioning, coloring, and manipulating other structural tags of HTML for providing better visuals.

## Steps to setup applications:

- Create a virtual environment in any directory.

        virtualenv ./venv

- Change directory using following command

        cd ./venv/Scripts

- Activate virtualenv using following command

        activate

- Now get back to the previous directory.

        cd ../..

- Now pull all the files and directory from github repository or download them, in current folder.
       
        (if downloaded then please extract all files in current directory.)

- Now execute the following command in the virtual environment activated terminal, to install all the dependencies of project.

        pip install -r requirements.txt

- Now after downloading of all the dependencies simply type the command

        python app.py

- Now after successfully launch of application. Type the following url in the internet browser.

        localhost:5000


## Note:
This project also requires api_keys like openweathermap.org API KEY and Google Maps (Places API) key.
I'm requesting first of all, to create a .env file and place both keys in following format.
        
        API_KEY=abcd (openweather.org)
        GMAP_KEY=wxyz (Google maps API)

Please keep the ".env" inside the directory in which app.py file is present.