from sys import maxsize


class Contact:
    def __init__(self, user_firstname=None, user_middlename=None, user_lastname=None, user_nickname=None, photo_path=None, user_title=None, company_name=None, address=None, home_address=None, mobile_phone=None,
                            work_phone=None, fax_phone=None, email_1=None, email_2=None, email_3=None, homepage=None, b_day=None, b_month=None, b_year=None, a_day=None,
                            a_month=None, a_year=None, address_2=None, phone_2=None, notes=None, id=None):
        self.user_firstname = user_firstname
        self.user_middlename = user_middlename
        self.user_lastname = user_lastname
        self.user_nickname = user_nickname
        self.photo_path = photo_path
        self.user_title = user_title
        self.company_name = company_name
        self.address = address
        self.home_address = home_address
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax_phone = fax_phone
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.b_day = b_day
        self.b_month = b_month
        self.b_year = b_year
        self.a_day = a_day
        self.a_month = a_month
        self.a_year = a_year
        self.address_2 = address_2
        self.phone_2 = phone_2
        self.notes = notes
        self.id = id

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               self.user_firstname == other.user_firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
