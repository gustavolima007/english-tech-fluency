import os
import re

def count_words(file_path):
    if not os.path.exists(file_path):
        return f"Error: File not found at {file_path}. Please check the path and permissions."
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Extract English words (sequences of letters, allowing hyphens)
        words = re.findall(r'\b[a-zA-Z]+(?:-[a-zA-Z]+)*\b', content)
        
        # Filter unique words and remove irrelevant headers or connectors
        unique_words = set(word.lower() for word in words if word.lower() not in ['english', 'vocabulary', 'categories', 'for', 'travel', 'and', 'work', 'basic', 'activities', 'needs', 'food', 'drink', 'housing', 'health', 'social', 'relations', 'communication', 'family', 'relationships', 'greetings', 'interactions'])
        
        return len(unique_words)
    except PermissionError:
        return f"Error: Permission denied to read the file {file_path}."
    except Exception as e:
        return f"Error reading the file: {str(e)}"

def get_cefr_level(word_count):
    if word_count <= 1000:
        return "A1 (Beginner)"
    elif word_count <= 2000:
        return "A2 (Elementary)"
    elif word_count <= 4000:
        return "B1 (Intermediate)"
    elif word_count <= 6000:
        return "B2 (Upper-Intermediate)"
    elif word_count <= 10000:
        return "C1 (Advanced)"
    else:
        return "C2 (Proficient)"

def main():
    file_path = "vocabulary/words.md"
    print(f"Attempting to access the file: {file_path}")
    word_count = count_words(file_path)
    
    if isinstance(word_count, int):
        level = get_cefr_level(word_count)
        print(f"You know {word_count} English words! Estimated level: {level}")
    else:
        print(word_count)

if __name__ == "__main__":
    main()