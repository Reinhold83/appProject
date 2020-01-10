from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired, Email

class Form(FlaskForm):
    """Please lets portrait the real picture together."""
    Email = StringField('Enter your email address', [
        Email(message='Not a valid email address.'),
        DataRequired()])

    sex = SelectField('Sex', [DataRequired()],
                    choices=[(None, ''),
                            ('Male', 'Male'),
                            ('Female', 'Female'),
                            ('No Answer', 'Prefer not to answer')
                            ])

    age = SelectField('Age', [DataRequired()],
                    choices=[(None, ''),
                            ('Under 14', 'Under 14'),
                            ('Between 15 - 19', 'Between 15 - 19'),
                            ('Between 20 - 24', 'Between 20 - 24'),
                            ('Between 25 - 29', 'Between 25 - 29'),
                            ('Between 30 - 34', 'Between 30 - 34'),
                            ('Between 35 - 39', 'Between 35 - 39'),
                            ('Between 40 - 44', 'Between 40 - 44'),
                            ('Between 45 - 49', 'Between 45 - 49'),
                            ('Between 50 - 54', 'Between 50 - 54'),
                            ('Between 55 - 59', 'Between 55 - 59'),
                            ('Between 60 - 64', 'Between 60 - 64'),
                            ('Between 65 - 69', 'Between 65 - 69'),
                            ('Between 70 - 74', 'Between 70 - 74'),
                            ('Between 75 - 79', 'Between 75 - 79'),
                            ('Between 80 - 84', 'Between 80 - 84'),
                            ('Between 85 - over', 'Between 85 - over')
                            ])

    Marital = SelectField('Marital Status', [DataRequired()],
                    choices=[(None, ''),
                            ('Single', 'Single'),
                            ('Married', 'Married'),
                            ('Divorced', 'Divorced'),
                            ('Widow','Widow')
                            ])

    county = SelectField('County', [DataRequired()],
                        choices=[(None, ''),
                                ('CARLOW', 'Carlow'),
                                ('CAVAN', 'Cavan'),
                                ('CLARE', 'Clare'),
                                ('CORK', 'Cork'),
                                ('DONEGAL', 'Donegal'),
                                ('DUBLIN', 'Dublin'),
                                ('GALWAY', 'Galway'),
                                ('KERRY', 'Kerry'),
                                ('KILDARE', 'Kildare'),
                                ('KILKENNY', 'Kilkenny'),
                                ('LAOIS', 'Laois'),
                                ('LEITRIM', 'Letrim'),
                                ('LIMERICK', 'Limeric'),
                                ('LONGFORD', 'Longford'),
                                ('LOUTH', 'Louth'),
                                ('MAYO','Mayo'),
                                ('MEATH', 'Meath'),
                                ('MONAGHAN', 'Monaghan'),
                                ('OFFALY', 'Offaly'),
                                ('ROSCOMMON', 'Roscommon'),
                                ('SLIGO', 'Sligo'),
                                ('TIPPERARY', 'Tipperary'),
                                ('WATERFORD', 'Wateford'),
                                ('WESTMEATH', 'Westmeath'),
                                ('WEXFORD', 'Wexford'),
                                ('WICKLOW', 'Wicklow')
                               ])

    Property = SelectField('Type of property', [DataRequired()],
                        choices=[(None, ''),
                                ('Apartment', 'Apartment'),
                                ('House', 'House'),
                                ('Studio', 'Studio'),
                                ('Rural', 'Rural')
                                 ])

    PropertyStatus = SelectField('Property status', [DataRequired()],
                        choices=[(None, ''),
                                ('Owner','Owner'),
                                ('Owner with mortgage','Owner with mortgage'),
                                ('Family Property', 'Family Property'),
                                ('Rental','Rental'),
                                ('HouseShared', 'House/Apt rental shared'),
                                ('RoomShared', 'Room rental shared'),
                                ('Social House','Social House'),
                                ('HAP/RAS','HAP/RAS'),
                                ('Others', 'Others')
                                ])
    AmountPaid = IntegerField('Value rent/mortgage in €')
    
    Rooms = SelectField('Number of rooms', [DataRequired()],
                        choices=[(None, ''),
                                ('Studio', 'Studio'),
                                ('one room', 'one room'),
                                ('two rooms', 'two rooms'),
                                ('three rooms', 'three rooms'),
                                ('four rooms', 'four rooms'),
                                ('five rooms or more', 'five rooms or more')
                                 ])
    People = IntegerField('Number per household')  #coerce=int if it doesnt work withintergerField than use SelectField and add the coerce
    
    submit = SubmitField('Submit')