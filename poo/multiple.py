class SMS:
    def send(self):
        print("It sends the message through SMS.")


class Saver:
    def save(self):
        print("It saves the data into the database.")
        
class Email:
    def send(self):
        print("It sends the message via email.")

class Sale(SMS, Saver, Email):
    pass

sale = Sale()
sale.send()
sale.save()
sale.send()