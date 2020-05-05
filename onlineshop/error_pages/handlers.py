from flask import Blueprint,render_template

error_pages = Blueprint('error_pages',__name__)

# These errors return tuples for use elsewhere.
@error_pages.app_errorhandler(404)
def error_404(error):
    '''
    This is a 404 page not found handler
    '''
    return render_template('error_pages/404.html'), 404

@error_pages.app_errorhandler(403)
def error_403(error):
    '''
    The error here prevents unauthorised acess to another users account.
    You cannot edit other reviews or access the cart.
    '''
    return render_template('error_pages/403.html'), 403
