# Problem
Perform validation on a user inputted username and password.

Username validation includes:
   - At least one lowercase letter
   - At least one uppercase letter

Password validation includes:
   - At least one lowercase letter
   - At least one uppercase letter
   - At least one special character

# v1 attempt
Intend to solve the problem without consideration to design

# v2 attempt
Moves validators into separate module and methods see [Separation Of Concerns](https://softwareengineering.stackexchange.com/a/32614)

Therefore, making is easier to add and remove validators for username and password alongside any additional texts to validate against in the future.

Reduced code duplication.