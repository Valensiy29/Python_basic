def check_permission(permission='user'):
    def checker_dec(func):
        def wrapped_check(*args,**kwargs):
            if permission.lower() == 'admin':
                res = func(*args,**kwargs)
                return res
            else:
                raise 'PermissionError: у пользователя недостаточно прав, чтобы выполнить функцию'
        return wrapped_check
    return checker_dec



user_permissions = ['admin']

@check_permission()
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')

delete_site()
add_comment()