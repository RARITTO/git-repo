import re

pattern = re.compile(r'\b\w+@\w+\.\w+\b')  # Example pattern for matching email addresses
text = "Contact me at john.doe@example.com or jane.smith@example.org"
matches = pattern.findall(text)
print(matches)
