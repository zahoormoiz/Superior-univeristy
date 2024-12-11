import time
import random

class TypingSpeedTest:
    def __init__(self):
        self.text_samples = [
            "The quick brown fox jumps over the lazy dog.",
            "A journey of a thousand miles begins with a single step.",
            "To be or not to be, that is the question.",
            "All that glitters is not gold.",
            "Practice makes perfect."
        ]
        self.selected_text = ""
        self.start_time = 0
        self.end_time = 0

    def select_text(self):
        self.selected_text = random.choice(self.text_samples)

    def start_test(self):
        self.select_text()
        print("\nTyping Speed Test\n")
        print("Type the following text:")
        print(f"\n{self.selected_text}\n")
        input("Press Enter when you are ready to start...")
        self.start_time = time.time()

    def end_test(self):
        self.end_time = time.time()

    def calculate_results(self, user_input):
        elapsed_time = self.end_time - self.start_time
        words = len(user_input.split())
        speed = words / (elapsed_time / 60)  # Words per minute

        # Calculate accuracy
        correct_chars = sum(1 for i, c in enumerate(user_input) if i < len(self.selected_text) and c == self.selected_text[i])
        accuracy = (correct_chars / len(self.selected_text)) * 100

        return speed, accuracy, elapsed_time

    def run(self):
        self.start_test()
        user_input = input("Start typing: ")
        self.end_test()

        speed, accuracy, elapsed_time = self.calculate_results(user_input)
        print("\nTest Results:")
        print(f"Time Taken: {elapsed_time:.2f} seconds")
        print(f"Typing Speed: {speed:.2f} words per minute")
        print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    typing_test = TypingSpeedTest()
    typing_test.run()
