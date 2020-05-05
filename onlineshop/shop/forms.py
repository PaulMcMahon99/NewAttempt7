from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired



class AddTeaForm(FlaskForm):

# Working on this bit last, suppliers may be removed to make this work. The supplier
# Is prepped for deletion with the switch of the id to just a name. Whilst this may
# affect data redundancy, time considerations are pressing.

    tea_name = StringField('Tea Name', validators=[DataRequired()])
    description = TextAreaField('Tea Description', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    stock_level = IntegerField('Amount in Stock', validators=[DataRequired()])
    # supplier_id = IntegerField('Enter Supplier ID Number', validators=[DataRequired()])
    supplier_name = StringField('Enter Supplier Name', validators=[DataRequired()])
    submit = SubmitField('Register new Tea')

class UpdateTeaForm(FlaskForm):

    tea_name = StringField('Change Tea Name', validators=[DataRequired()])
    description = TextAreaField('Change Tea Description', validators=[DataRequired()])
    price = DecimalField('Change Price', validators=[DataRequired()])
    stock_level = IntegerField('Change Stock Amount', validators=[DataRequired()])
    supplier_name = StringField('Enter New Supplier Name', validators=[DataRequired()])
    tea_picture = FileField('Update Tea Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')


#  Suppliers mothballed until further notice.
# class AddSupplierForm(FlaskForm):
#
#     first_name = StringField('First Name',validators=[DataRequired()])
#     last_name = StringField('Last Name',validators=[DataRequired()])
#     company_name = StringField('Company Name',validators=[DataRequired()])
#     submit = SubmitField('Add Supplier')
#
# class UpdateSupplierForm(FlaskForm):
#
#     first_name = StringField('First Name',validators=[DataRequired()])
#     last_name = StringField('Last Name',validators=[DataRequired()])
#     company_name = StringField('Company Name',validators=[DataRequired()])
#     submit = SubmitField('Update Supplier')
