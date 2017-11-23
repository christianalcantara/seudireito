from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def is_company(user):
    """Check user is company"""
    try:
        user.company
    except:
        return False
    return True


def is_lawyer(user):
    """Check user is lawyer"""
    try:
        user.lawyer
    except:
        return False
    return True


def user_lawyer_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME,
                         login_url='login'):
    """
    Decorator for views that checks that the user is lawyer,
    redirecting to the login page if necessary.
    """
    try:
        actual_decorator = user_passes_test(
            lambda u: is_lawyer(u),
            login_url=login_url,
            redirect_field_name=redirect_field_name
        )
    except:
        return False
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


def user_company_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME,
                          login_url='login'):
    """
    Decorator for views that checks that the user is company,
    redirecting to the login page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: is_company(u),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator
