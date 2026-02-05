from classes import Employee , Car , office    

car1 = Car(name="Fiat128", fuel_rate=100, velocity=80)
emp1 = Employee(
        emp_id=1,
        car=car1,
        email="samy@mail.com",
        salary=5000,
        distance_to_work=20,
        name="samy",
        money=3000)
emp1.sleep(7)
emp1.eat(3)
emp1.buy(2)
print("Money after buying:", emp1.money)
print("Mood:", emp1.mood)
print("Health rate:", emp1.healthrate)
emp1.work(8)
office1 = office("ITI")
office1.hire(emp1)
office1.reward_employee(1, 200)
print("Money after reward:", emp1.money)
office1.deduct_salary(1, 100)
print("Money after deduction:", emp1.money)
emp1.send_mail(
    to="manager@mail.com",
    subject="Daily Report",
    body="Work completed successfully."
)
