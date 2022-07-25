"""grade"""
def main():
    """input grade"""
    grade_1 = float(input())
    if grade_1 < 1.00:
        print("I'm so sad.")
    elif grade_1 >= 1.00 and grade_1 < 2.00:
        grade_2 = 4.00 - grade_1
        print("%.2f"%grade_2)
    elif grade_1 >= 2.00:
        print("I'm so happy.")
main()
