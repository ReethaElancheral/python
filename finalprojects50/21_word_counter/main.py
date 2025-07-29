# 21. Word Counter (File Analysis) 
# Objective: Count words, lines, and characters in a text file. 
# Requirements: 
#  File Handling: Read .txt files. 
#  String Operations: Split text into words/lines. 
#  Dictionary: Store word frequencies ({"hello": 3}). 
#  Exception Handling: Handle missing files. 
#  Functions: count_words(), most_common_word(). 
#  Loops: Iterate through lines. 
#  Generator: Yield words one by one. 
#  Decorator: @time_execution to measure speed.


from analyzer import WordAnalyzer

def main():
    print("📘 Welcome to the Word Counter Tool")
    file_path = input("Enter the path to the text file: ")

    analyzer = WordAnalyzer(file_path)

    try:
        analyzer.analyze()
        analyzer.display_summary()
        print(f"\nMost common word: {analyzer.most_common_word()}")
        print("\nAll words (via generator):")
        for word in analyzer.word_generator():
            print(word, end=" ")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
