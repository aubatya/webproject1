import string
import random
import random_date
import datetime

def randomdb(quantity_object: int) -> list:
    lu = []
    lp = []
    lo = []
    alp = list(string.ascii_lowercase)
    foundation_date = "01.07.1988"
    now = datetime.datetime.now().strftime('%d.%m.%Y')
    with open("name_user.txt", "r") as f:
        lname = f.readlines()
    for k in range(quantity_object):
            quantity_in_stock = random.randint(1, 1000000)
            pname = ""
            uname = ""
            surname = ""
            email = ""
            telephone = "+7"
            for i in range(random.randint(5, 15)):
                pname+=random.choice(alp)
            surname, uname = map(lambda x: x, random.choice(lname).split()[:2])
            for i in range(random.randint(5, 9)):
                email+=random.choice(alp)
            for i in range(10):
                telephone+=str(random.randint(0, 9))
            description = ""
            for j in range(150):
                description+=random.choice(alp)
            address = ""
            for i in range(4):
                for j in range(random.randint(3, 7)):
                    address+=random.choice(alp)
                address+=" "
                if i == 3:
                    address+=f" {random.randint(1, 200)}"
            image = bin(random.randint(1, 100000000))
            price = random.uniform(1, 1000000)
            uname = uname.capitalize()
            surname = surname.capitalize()
            description = description.capitalize()
            pname = pname.capitalize()
            email+="@gmail.com"
            quantity = random.randint(1, 100000)
            product_id = random.randint(1, k+1)
            user_id = random.randint(1, k+1)
            usdate = random_date.random_date("01.01.2021", now, random.random())
            ubdate = random_date.random_date("01.01.1900", usdate, random.random())
            odate = random_date.random_date(usdate, now, random.random())
            pdate = random_date.random_date(foundation_date, odate, random.random())
            delivery_date= random_date.random_date(odate, "31.12.2021", random.random())
            delivered = 1 if int(delivery_date[3:5])<9 else 0 
            lp.append((quantity_in_stock, pname, description, image, price, pdate))
            lu.append((uname, surname, email, telephone, ubdate, usdate))
            lo.append((address, quantity, product_id, user_id, odate, delivered, delivery_date))
    return lp, lu, lo