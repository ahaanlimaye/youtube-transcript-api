import os
import re

def update_imports(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Update imports
                updated_content = re.sub(
                    r'from youtube_transcript_api\.',
                    'from youtube_transcript_api_sentences.',
                    content
                )
                updated_content = re.sub(
                    r'import youtube_transcript_api\.',
                    'import youtube_transcript_api_sentences.',
                    updated_content
                )
                
                if content != updated_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f"Updated imports in {file_path}")

if __name__ == '__main__':
    update_imports('youtube_transcript_api_sentences') 