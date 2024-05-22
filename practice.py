#lista de usuarios con tres parametros
user = ["name", "phone", "age"]

#Crear un lista de usuarios
users = [
    {"name": "Alex", "phone":"654345333","age":32},
    {"name": "Maria", "phone":"65497663","age":30},
    {"name": "Tania", "phone":"676845331","age":26}
]

#con el loop for llamamos un parametro dentro de la lista users e imprime en consola el dato de "name"
for user in users:
    print(user["name"])

#imprimir de esta manera los datos de la lista: Alex | 32 | 654345333
#con el loop for llamamos cada user e imprimimos en format cada dato de usuario separado por |
for user in users:
    print(f"{user["name"]} | {user["age"]} | {user["phone"]}")

#pedimos por la funcion input() al usuario que introduzca sus datos 
name = input("name: ")
phone = input("phone: ")
age = input("age: ")

#los datos introducidos se añaden por la funcion append() a la lista users que ya teniamos
users.append({"name":name, "age":age, "phone":phone})

#volvemos a imprimir users con el nuevo usuario
for user in users:
    print(f"{user["name"]} | {user["age"]} | {user["phone"]}")

