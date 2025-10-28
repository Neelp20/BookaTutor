## Functional Testing

**Authentication**

Description:

Ensure a user can sign up to the website

Steps:

1. Navigate to [Book a Tutor](https://book-a-tutor-e586c5d4d680.herokuapp.com/) and click Register
2. Enter email, username and password 
3. Click Sign up

Expected:

Registration is successful, no need for approve from admin.no link is sent to confirm

Actual: 

Registration is successful, no link is received to confirm

<hr>

Description:

Ensure a user can log in once signed up

Steps:
1. Navigate to [The Wooden Spoon](https://the-wooden-spoon-cfb803cde318.herokuapp.com/)
2. Enter login detailscreated in previous test case
3. Click login

Expected:

User is successfully logged in and redirected to the home page

Actual:

User is successfully logged in and redirected to the home page

<hr>

Description:

Ensure a user can sign out

Steps:

1. Login to the website
2. Click the logout button
3. Click confirm on the confirm logout page

Expected:

User is logged out

Actual:

User is logged out

**Booking Forms**

Description:

Ensure a new booking can be created.

Steps:

1. Navigate to [page](https://book-a-tutor-e586c5d4d680.herokuapp.com/) - Login is required first.
2. Enter the following:
    - username: test@student
    - Your password: 
3. Click sign in
4. Bookings page:
    - Create bookings
    - Select tutor from dropdown
    - Enter subject
    - Any message
    - Book now

Expected:

Form successfully submits and alert is shown to the user of successful booking.

Actual:

Form successfully submits and a alert is shown to the user of successful booking.