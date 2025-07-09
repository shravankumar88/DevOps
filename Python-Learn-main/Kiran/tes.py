def greet(name):
    def wish(n):
        return n.title()
    return f"Hello {wish(name)}"
print(greet("suresh"))