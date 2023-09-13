def main():
    print("Welcome to the email slicer")
    print("")

    email_input=input("Input your email address:")

    (username,domain)=email_input.split("@")
    (domain,extention)=domain.split(".")

    print("Username:",username)
    print("Domain:",domain)
    print("Extention:",extention)

while True:
    main()    