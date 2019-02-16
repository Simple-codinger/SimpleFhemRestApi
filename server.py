from flask import render_template
import connexion

#create application instance
app = connexion.App(__name__, specification_dir='./')

#Endpoint configuration file
app.add_api('swagger.yml')

#Create a URL route in our application folder "/"
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)