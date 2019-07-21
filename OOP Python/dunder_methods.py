class book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"


    def __len__(self):
        return self.pages


b = book("40 rules of love", "Elif shafak", 345)

print(b,"<--") ##will print the address of where the object of the class is located

print(str(b),"<----")
print(len(b),"<<</.")