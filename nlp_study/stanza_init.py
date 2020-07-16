# Install; note that the prefix "!" is not needed if you are running in a terminal
#!pip install stanza

# Import the package
import stanza

# Download an English model into the default directory
print("Downloading English model...")
stanza.download('en')

# Similarly, download a (simplified) Chinese model
# Note that you can use verbose=False to turn off all printed messages
print("Downloading Chinese model...")
stanza.download('zh', verbose=False)