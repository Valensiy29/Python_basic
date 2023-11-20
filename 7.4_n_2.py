server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for i_data,i_incom in server_data.items():
    print(i_data,':','\n')
    for name,con in i_incom.items():
        print(con,'\n')