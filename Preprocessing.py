
#Preprocessing.py
# function to preprocess the britannica.txt file
def preprocess_britannica_file(file_path):
    entries = []

    # Open the file and read its contents
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Initialize variables to store URL and content
    url = None
    content = None

    # Iterate through the lines in the file
    for line in lines:
        # Check if the line starts with "URL:"
        if line.startswith('URL:'):
            # If yes, extract the URL
            url = line.split('URL: ')[1].strip()
        # Check if the line starts with "Content:"
        elif line.startswith('Content:'):
            # If yes, extract the content
            content = line.split('Content: ')[1].strip()
        # If both URL and content are extracted, append them to the entries list
        if url and content:
            entries.append({'url': url, 'content': content})
            # Reset URL and content for the next entry
            url = None
            content = None

    return entries

# Preprocess the britannica.txt file
britannica_entries = preprocess_britannica_file('britannica.txt')

# Print the preprocessed entries
for entry in britannica_entries:
    print(entry)
