class String:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return f"{self.string}"

    # custom method: lower()
    def lowercase(self):
        new_str = ""
        for char in self.string:
            new_str += char.lower()
        return new_str

def main():
    my_string = get_string()
    print(my_string.lowercase()) # hello world my friends

def get_string():
    prompt = input("Input: ")
    return String(prompt)

if __name__ == "__main__":
    main()