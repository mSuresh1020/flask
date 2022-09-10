from first_flask_db import create_app
import os

config_name=os.getenv("FLASK_CONFIG","Development")
app1=create_app(config_name)

if __name__ == "__main__":
    app1.run(debug=True)

    
    
    

