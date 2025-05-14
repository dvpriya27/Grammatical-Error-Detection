
# main.py

from textblob import TextBlob
import language_tool_python

def check_textblob_errors(text):
    blob = TextBlob(text)
    print("Corrected (TextBlob):", blob.correct())

def check_languagetool_errors(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    print(f"Number of grammatical issues (LanguageTool): {len(matches)}")
    for match in matches[:5]:  # Show only first 5 issues
        print(f"- {match.ruleId}: {match.message} at position {match.offset}-{match.offset + match.errorLength}")

if __name__ == "__main__":
    input_text = input("Enter a sentence or paragraph with grammatical errors:\n")
    print("\n--- Using TextBlob ---")
    check_textblob_errors(input_text)

    print("\n--- Using LanguageTool ---")
    check_languagetool_errors(input_text)
