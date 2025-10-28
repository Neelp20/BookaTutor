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

**Edit Booking Forms**

Description:

Ensure a booking can be edited.

Steps:

1. Navigate to [Manage booking page](https://book-a-tutor-e586c5d4d680.herokuapp.com/) - Login is required first.
2. Enter the following:
    - username: test@student
    - Your password: 
3. Click sign in
4. Bookings page:
    - Manage bookings
    - Edit
    - user gets confirmation post edit/delete

Expected:

Form successfully submits and alert is shown to the user of successful editing/deleting.

Actual:

Form successfully submits and a alert is shown to the user of successful editing/deleting.

<hr>

**Tutor Page**

Description:

Search option by subjects on tutors page

Steps:

1. Navigate to [Tutors page](https://book-a-tutor-e586c5d4d680.herokuapp.com/) - Login is required first.
2. Enter the following details:
    - Select subject from the dropdown
    - It shows the tutors, whoch teaches that subject


Expected:

Page should show the tutors teaching that particular subject

Actual:

Page has shown the tutors teaching that subject

<hr>

**Navigation Links**

Testing was performed to ensure all navigation links on the respective pages, navigated to the correct pages as per design. This was done by clicking on the navigation links on each page.

* Home -> index.html - Visible to all
  * Bookings (Drop Down):
    * Create Booking -> bookings.html - Visible to logged in users
    * Upcoming BookingS -> manage_bookings.html - Visible to logged in users
    * Past BookingS -> past_bookings.html - Visible to logged in users
    * All Bookings(Admin) --> admin_manage_bookings.html - visible to admin only
  * Menus (Drop Down):
    * View Menus -> menu.html - Visible to all
    * Create Menu -> create_menu.html - Visible to staff
    * Create Menu Item -> create_menu_items.html - Visible to staff
    * Create Allergy Label -> create_allergy_label.html - Visible to staff
    * Manage Menu -> manage_menu.html - Visible to staff
  * Login -> login.html - Visible to logged out users
  * Register -> signup.html - Visible to logged out users
  * Logout -> logout.html - Visible to logged in users

All navigation links directed to the corect pages as expected.

<hr>

**Footer**

Testing was performed on the footer links by clicking the font awesome icons and ensuring that the facebook icon opened facebook in a new tab. These behaved as expected.

## Negative Testing

Tests were performed on the create booking to ensure that:

1. A userr cannot book a date in the past
2. A user cannot book for less than 24hrs.
3. Forms cannot be submitted when required fields are empty
