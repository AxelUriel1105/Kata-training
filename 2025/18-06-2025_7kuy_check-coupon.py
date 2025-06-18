"""Story
Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

Task
Your mission:
Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".

Examples:
checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False
"""
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    current_date, expiration_date = current_date.replace(',','').split(), expiration_date.replace(',','').split()
    Months = {"January":1, "February":2, "March":3, "April":4,
              "May":5, "June":6, "July":7, "August":8, "September":9,
              "October":10, "November":11, "December":12}
    if (entered_code != correct_code or type(entered_code)!=type(correct_code)) or int(expiration_date[-1]) < int(current_date[-1]):
        return False
    elif int(expiration_date[-1]) == int(current_date[-1]):
        if Months.get(current_date[0]) > Months.get(expiration_date[0]):
            return False
        elif Months.get(current_date[0]) == Months.get(expiration_date[0]):
            return int(current_date[1]) <= int(expiration_date[1])
            
    return True