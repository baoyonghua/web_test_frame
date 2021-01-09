
class LoginData():
    '''用户登陆数据'''
    # 登录成功的数据
    success_data = ("18684720553",'python')
    # 登录失败的数据，输入空的账号/密码/错误的手机号
    fail_form_data = [{"phone":"","pwd":"python","check":"请输入手机号"},
                    {"phone":"","pwd":"","check":"请输入手机号"},
                    {"phone":"18684720553","pwd":"","check":"请输入密码"},
                    {"phone":"1868472055","pwd":"python","check":"请输入正确的手机号"}
                    ]
    # 登录失败的数据，账号未注册/密码错误
    fail_layui_data = [
                        {"phone":"17816094179","pwd":"python","check":"此账号没有经过授权，请联系管理员!"},
                        {"phone":"18684720553","pwd":"pythonsas","check":"帐号或密码错误!"}
                        ]