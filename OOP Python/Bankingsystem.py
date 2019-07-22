import datetime


class MessageUser:
    user_details = []
    messages = []
    base_message = """
    
    run it down, let’s run the plane, no
    You know how to kill a vibe
    We in and out on the regular
    
    -Team SSEO
    """
    def add_user(self,name,amount,email = None):

        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" % (amount)
        detail = {
            "name": name[0].upper() + name[1:].lower(),
            "amount": amount,
        }

        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today= today)
        detail['date'] = date_text
        if email != None:
            detail["Email"] = email

        self.user_details.append(detail)


    def get_details(self):
        print (self.user_details)
        return self.user_details

    def make_messages(self):
        if len(self.user_details) > 0:
            for i in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail[date]
                message = self.base_message
                new_msg = unf_message.format(

                    name = name,
                    date = text,
                    total = new_amount
                )
                self.messages.append(new_msg)
                return self.messages

obj = MessageUser()
obj.add_user("Molly", 2345, "habe@123.com")
obj.add_user("Eman", 758)
obj.add_user("MM", 1900)
obj.add_user("NN", 400)
obj.get_details()
# print(obj.make_messages())