import agnosticcode.Incrementors as a

print("Hello")

print("__name__ value: ", __name__)

inc = a.Incrementors().increment(1)

print(inc)

def main():
    print("python main function")


if __name__ == '__main__':
    main()