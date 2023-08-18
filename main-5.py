
from cat import cat

if __name__ == "__main__":
    cat1 = cat("luna", 5, True)
    cat1.display()
    cat1.sound()

    cat1.__isHappy = False