import peewee

db = peewee.SqliteDatabase('/Users/santiteeragul/PycharmProjects/Flask101/coffeeshop.db')


class Menu(peewee.Model):
    coffee_name = peewee.CharField()
    price = peewee.IntegerField()

    class Meta:
        database = db
        db_table = 'menus'


Menu.create_table()

# menu1 = Menu.create(coffee_name='Esspresso', price=50)
# menu1.save()
#
# menu2 = Menu.create(coffee_name='Americano', price=40)
# menu2.save()
#
# menu3 = Menu.create(coffee_name='Latte', price=60)
# menu3.save()
