# Define copy function
def copy(source_file, destination_file):

    # Open the source file in read mode and destination file in write mode
    with open('story.txt', 'r') as src:
        content = src.read()  # Read the content of the source file

    # Open the destination file in write mode and write the content from story.txt 
    # to the destination file called story_copy.txt
    with open('story_copy.txt', 'w') as dest:
        dest.write(content)  # Write the content to the destination file 

# Call Function
copy('story.txt', 'story_copy.txt')