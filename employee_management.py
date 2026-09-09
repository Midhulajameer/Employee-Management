import mysql.connector


class db_connect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="123456789",
                database="company_db"
            )
            return self.connection
        except Exception as e:
            return None


class employee_manager(db_connect):
    def get(self):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
            query="select * from employee"
            self.cursor.execute(query)
            records= self.cursor.fetchall()
            print(records)
        except Exception as e:
            print(e)


    def post(self,**kwargs):
        self.connect= super().get_connection()
        self.cursor=self.connect.cursor()
        query="insert into employee(name,place,mobile,email,department,salary,joining_date)values(%s, %s, %s, %s, %s, %s, %s)"
        values = [v for v in kwargs.values()]
        self.cursor.execute(query,values)
        self.connect.commit()
        print("New employee added")


    def retrieve(self, id=None):
        self.connect= super().get_connection()
        self.cursor= self.connect.cursor()
        query= "select * FROM employee WHERE id = %s"
        values=(id,)
        self.cursor.execute(query,values)
        record=self.cursor.fetchone()
        print(record)


    def put(self):
        try:
            record=self.get_object(id=id)
            if record != None:
                self.cursor = self.connection.cursor()
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + "=%s,"
                placeholder = placeholder.rstrip(",")
                query=f"update employee SET {placeholder} WHERE id=%s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("employee details updated successfully")

            else:
                print("employee not found")

        except Exception as e:
            print(e)



connection_instance=db_connect()
print(connection_instance.get_connection())
employee_instance=employee_manager()
# employee_instance.post(name="Anu", place="Kakkanad", mobile="9866415765", email="Anu@gmail.com", department="Sales", salary=55000,joining_date="2026-09-02")
# employee_instance.post(name="Liya", place="Aluva", mobile="8136978459", email="Liya@gmail.com", department="Marketing", salary=60000,joining_date="2025-04-25")
employee_instance.get()
employee_instance.retrieve(2)
