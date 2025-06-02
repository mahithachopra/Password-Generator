import random
import string
import streamlit as st
import pyperclip

# Function to generate password
def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Ensure at least one character from each selected set is used
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Fill the remaining length
    password += random.choices(characters, k=length - len(password))

    # Shuffle the password to prevent predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Function to copy password to clipboard
def copy_to_clipboard(password):
    pyperclip.copy(password)
    st.success("✅ Password copied to clipboard!")

# Streamlit Web App
def main():
    # App title and description with emoji
    st.title("🔐 Secure Password Generator")
    st.write("""
    Generate secure, random passwords to protect your online accounts and data.
    Customize the length and character types to create strong passwords.
    """)

    # Add sidebar with extra information
    st.sidebar.title("🛠️ How to Use")
    st.sidebar.write("""
    - Select the password length.
    - Choose the character types (uppercase, numbers, symbols).
    - Generate the password and copy it to your clipboard!
    """)

    # Password length input with description
    st.subheader("Password Criteria")
    length = st.slider("Select Password Length", 8, 32, 12, help="Drag the slider to select the length of the password.")

    # Password criteria checkboxes with icons
    use_uppercase = st.checkbox("🔤 Include Uppercase Letters")
    use_numbers = st.checkbox("🔢 Include Numbers")
    use_symbols = st.checkbox("🔣 Include Symbols")

    # Button to generate the password
    if st.button("🚀 Generate Password"):
        # Ensure that at least one option is selected
        if not any([use_uppercase, use_numbers, use_symbols]):
            st.warning("⚠️ Please select at least one character type for password generation!")
        else:
            # Generate the password
            password = generate_password(length, use_uppercase, use_numbers, use_symbols)
            st.success("🎉 Your secure password has been generated!")
            
            # Display the generated password in a styled box
            st.code(password, language='')

            # Copy to clipboard button
            if st.button("📋 Copy to Clipboard"):
                copy_to_clipboard(password)

    # Add a footer
    st.markdown("""
    ---
    **Pro Tip**: Use this tool to generate a different password for each account. Keep them secure by storing them in a password manager.
    """)

if __name__ == "__main__":
    main()
