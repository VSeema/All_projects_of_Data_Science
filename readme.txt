* Created Live chart using matplotlib FuncAnimation library
* Backend : 1. Used Postgresql database 
            2. Used psycopg2 libaray for establishing postgresql connection

* To run the code : 1. Create a database in postgresql Allsafe.
                    2. Create table report with id as serial(auto increment each time when we insert status code)
                    3. Create a virtual environment [ conda create -n (name of the env) ]
                    4. Run requirements.txt file [ pip install -r requirements.txt ] 
                    5. Run python command to execute the file [ python final_code.py ]
* output : Live chart which shows uptime(200) and dowtime(500) of the allsafe.in website.



