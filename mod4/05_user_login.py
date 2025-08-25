# Constants.
USERNAME_PROMPT: str = "Enter username: "
PASSWORD_PROMPT: str = "Enter password: "
USERNAME: str = "python"
PASSWORD: str = "rules"
MAX_TRIES: int = 5
INVALID_CREDS_MSG: str = "Incorrect username or password. Please try again."
ACCESS_DENIED_MSG: str = "Access denied"
WELCOME_MSG: str = "Welcome"

# Variable for try count.
try_count: int = 1

# Loop while try count is less than or equal to max tries count.
while try_count <= MAX_TRIES:
    input_username = input(USERNAME_PROMPT)
    input_password = input(PASSWORD_PROMPT)

    # Break loop early if username and password match the constants.
    if input_username == USERNAME and input_password == PASSWORD:
        # Print welcome message and break early.
        print(WELCOME_MSG)
        break

    # If try count less than max tries:
    # -> print invalid credentials message.
    if try_count < MAX_TRIES:
        print(INVALID_CREDS_MSG)
    else:
        # Else print access denied on failed last try
        # and break early.
        print(ACCESS_DENIED_MSG)
        break

    # Increment try count.
    try_count += 1
