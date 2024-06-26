# Fungi Fantasy

![responsive](docs/mockup_responsive.jpg)

Fungi Fantasy is a comprehensive e-commerce platform offering enchanting garden decor. Users can explore and purchase a variety of decorative mushrooms, while also creating personal accounts to track orders and preferences. Administrators have full control to manage products, handling inquiries, and curate an immersive experience for garden enthusiasts.


You can view the live site at **[Fungi Fantasy](https://fungi-fantasy-4819ad1964c1.herokuapp.com/).**


For testing purposes, you can utilize the following Stripe Dummy Card details:
- Success Card Number: 4242 4242 4242 4242
- Expiration Date: Enter any future date using the format MM/YY
- CVV: Enter any 3-digit number
- Postal Code: Enter any 5 numerical digits

Please note that payments made using valid debit/credit cards will not be processed, and the card will not be charged. Additionally, no orders placed will be fulfilled.


## Table of contents

  * [UX](#ux-user-experience)
    * [Overview](#overview)
    * [Customer objectives](#customer-objectives)
    * [Site goals](#site-goals)
    * [Epics and User Stories](#epics-and-user-stories)
    * [Wireframes](#wireframes)
    * [Color pallette](#color-pallete)

  * [Features](#features)
    * [Viewing Options](#viewing-options---visitorsregistered)
    * [CRUD](#crud-create-read-update-and-delete)
    * [Features HTML](#features-used-in-every-html-template)
    * [Entity Relationship Diagram](#entity-relationship-diagram)

  * [Marketing](#marketing-and-seo)
    * [Marketing](#marketing)
    * [SEO](#seo-search-engine-optimization)

  * [Manual Testing](#manual-testing)

  * [Validation](#validation)
    * [HTML](#html)
    * [CSS](#css)
    * [JavaScript](#javascript)
    * [Python](#python)
    * [Lighthouse](#lighthouse)

  * [Bug](#bug)  
  * [Deployment](#deployment)
    * [ElephantSQL Database](#elephantsql-database)
    * [Amazon AWS](#amazon-aws)
    * [Stripe API](#stripe-api)
    * [Gmail API](#gmail-api)
    * [Heroku](#heroku)
    * [Cloning Project](#cloning-project)
    * [Forking Project](#forking-project)

  * [Tecnologies used](#tecnologies-used)
    * [Languages](#languages) 
    * [Frameworks and Libraries](#frameworks-and-libraries)
    * [Developmen and Deploy](#development-and-deploy)

  * [Credits](#credits)

  * [Acknowledgements](#acknowledgements)  

## UX User Experience

### Overview

The purpose of the Fungi Fantasy website is to provide a user-friendly online shop where visitors can explore a variety of products sorted into categories. In addition to browsing product details, users can also view comments and ratings left by other customers to make informed decisions about their purchases.

### Customer objectives

At Fungi Fantasy, customers enjoy a seamless and intuitive shopping journey, where they're inspired to discover extraordinary products to turn their garden into a whimsical fairy tale. Registering an account with Fungi Fantasy grants access to various user features, such as rating or commenting on purchased products. Plus, subscribers receive a monthly newsletter with updates on new arrivals, trends, and coupons.

### Site goals

- Provide users with the convenience of online shopping from the comfort of their homes at Fungi Fantasy.
- Allow users to peruse comments from other shoppers regarding products.
- Enable users to add items to their Wishlist for future consideration.
- Empower users to view comprehensive details of each item in the shop, including price, and description.
- Admin Dashboard for business owners. It helps you manage your products, you can quickly make any changes you need.

### Epics and User Stories

In planning our strategy at Fungi Fantasy, we developed 5 main goals, called EPICS, to guide our project. You can find the detailed list of these epics and their links in our project's [Kanban Board](https://github.com/users/Bruna-Andelieri/projects/3). From these epics, we broke down into smaller tasks, called user stories, to make sure we cover everything we need.

List of the EPICS and user stories

**EPIC: VIEW WEBSITE AND USER ACCOUNT**
- As a customer, I can view the site's home page so that I can comprehend the site's objectives and purpose
- As a customer, I have visibility and functionality of the navigation bar to navigate across the site.
- As a customer, I can input text into the search bar to locate a specific item.
- As a visitor, I can register to the website and create an account so that I can save my details and become a customer
- As a customer logged in, I can update my details within my account to ensure they remain current
- As a customer, I can save my username and password so that I can easily access my details.
- As a visitor, I can click on the external links so that I can view relevant information.
- As a visitor, I can enter my email into the newsletter field so that I can receive relevant news about the website.
- 

**EPIC: PRODUCTS AND SHOPPING CART CHECK OUT**
- As a customer, I can click on "All products" so that I can explore all items available on the website.
- As a customer, I can click on a navbar to select a specific method for searching for an item.
- As a customer, I can select an individual product so that I can view its description, price, etc.
- As a customer, I can click on 'Add to Cart' in my product views so that I can add the product to my cart.
- As a customer, I can increase/decrease/remove quantities of a product in my cart so that I can have control over what I wish to purchase.
- As a customer, I can securely check out my products to finalize my purchase.
- As a customer, I can receive an email post-purchase to confirm my order and maintain a record of my purchase.
- As a customer logged in I can see my order history so that I can track my spending and details of purchase

**EPIC: ADMIN MANAGEMENT**
- As an admin, I can log in to the admin panel so that I can manage/see the panel.
- As an admin, I can add edit, or delete products so that I can update the website's products page.
- As an admin, I want to view an order so that I can review what customers are purchasing.

**EPIC CUSTOM MODELS**
- As an admin, I can view the inquiries submitted via the contact form to respond to customer queries.
- As a visitor, I can enter my details on the Contact form so that I can send a message to the company.
- As a user logged in after the purchase I can write a review about the product.
- As a user logged in after the purchase I can rate the product purchased.
- As a logged-in user, I can click the 'Add to Wishlist' button to save my favourite items for future reference.
- As a logged-in user, I can click the 'Remove' icon next to an item on my Wishlist to delete that product.

**EPIC: TESTING AND DOCUMENTATION**
- As a developer, I conduct comprehensive testing across all aspects of my project to ensure users have a seamless experience devoid of errors.
- As a developer, I document all project information in my README.md to provide comprehensive documentation for myself and others.

[Back to the top](#fungi-fantasy)

### Wireframes


I've drafted wireframes for the primary pages of the website using [Balsamiq](https://balsamiq.com/). Below are the wireframes for the main pages:

- Landing Page - Header and Footer
  - Consistent Header and Footer: Each page incorporates a consistent header at the top and a footer positioned at the bottom. This ensures that the header remains visible without obstructing any content, while the footer is always accessible.
  The landing page serves to provide users with a clear overview of the page's purpose as contact, useful links...
 
    ![landing](docs/landing-page.jpg)

 - Products page:
   - The products page offers users a comprehensive selection of all available products. Users can easily identify item names and prices.
    ![products](docs/product-page.jpg)

- Prdoucts detail:
  - Users can easily identify item names, prices, comment counts and ratings.
  ![products-details](docs/product-detail.jpg)

- Wishlist
  - This feature enables users to save items to their Wishlist for future purchase or trend monitoring. Accessible exclusively to logged-in users.
  ![wishlist](docs/wishlits.jpg)

- Shopping Cart
  - This page acts as the final review before checkout. Users can adjust the quantity of items previously added to their cart, remove specific items, or clear the entire cart altogether.
  ![shopping-cart](docs/shopping-cart.jpg)

- Checkout
  - Users are prompted to input delivery details, which are pre-filled if the user is logged in and details are saved, and  complete payment using the credit card details field.
  ![checkout](docs/checkout.jpg)

- My Profile
  - Empowers users to modify their details and preferences conveniently. The form comes pre-populated with their current information for ease of adjustment.
  ![profile](docs/my-profile.jpg)

### Color pallete

The color palette chosen for the ecommerce platform is inspired by the enchanting world of mushrooms and fungi, creating a whimsical and immersive shopping experience with a dash of vintage and modern colors.
  ![colors](docs/color-pallette.jpg)

[Back to the top](#fungi-fantasy)
## Features

### Viewing Options - Visitors/Registered

| Feature   | Visitor           | Registered, Account Holder |
|-----------|-------------------|----------------------------|
| Home Page | Visible           | Visible                    |
| Account   | Not Visible - 'Account' option only appears for registered logged-in users                 | Visible and full feature interaction available |
| All Products  | Visable - items can be viewed and added to Cart | Visible and full feature interaction available |
| Wishlist  | Not visible       | Visible and full feature interaction available|
| Review   | Visible, not interaction(del/edit)| Visible and full feature interaction available|
| Read   | Visible | Visible |
| Search  | Visible | Visible |
| Contact Us/Newsletter | Visible | Visible |
| Admin Dashboard | Not Visible | Only visible to Admin |

### CRUD (Create, Read, Update, and Delete)

| Feature | Create | Read | Update | Delete |
|---------|--------|------|--------|--------|
| Account | On registration | Yes, delivery details and order history | Yes, update address | No, users are unable to delete their accounts, this is restricted to Admin |
| Cart | Yes, customers may add to their cart | Yes | Yes, items can be added/removed | Yes |
| Products | Yes, Admin only | Yes, all users | Yes, Admin only | Yes, Admin only |
| Review | Yes, customers can add a comment and rating after purchasing the product  | Yes, all users | Yes, the customer who wrote the review |  Yes, the customer who wrote the review |


[Back to the top](#fungi-fantasy)

### Features used in every HTML template

- **Header**:
  The header consists of a Logo section, which also serves as a link to the Home page . The center of the header features a Search Bar, while the Menu section, along with Cart and Wishlist options, is located in the top easy navigation across all pages.
  ![header](docs/feat-header.jpg) 
  
- **Logged in**
  When logged in, the wishlist appears in a distinct color and is clickable.
  ![header-logged](docs/feat-header-logged.jpg)

- **Footer**
  The footer is a valuable resource for users to connect and engage further. Featuring prominently in the footer is a direct link to our Facebook page, providing a convenient avenue for users to stay updated with our latest news and offerings. Additionally, we provide essential contact details, a link to a contact form is also included, enabling users to submit queries directly through our website and a newsletter for future news.
  ![footer](docs/feat-footer.jpg)

### Landing Page
  The landing page features a captivating image designed to immediately capture visitors' attention. Additionally, the shop button is prominently displayed and easily accessible, ensuring users can quickly find and browse through all available products.
  ![landing](docs/feat-landing-page.jpg)

### About us
  The About Us page includes a dedicated section that provides detailed information about our company.
  ![about](docs/feat-about.jpg)

### Contact Form
  The contact form on our website serves as a convenient and efficient way for visitors to get in touch with us. With user-friendly fields for name, email and message, it's easy for individuals to reach out with questions, feedback, or inquiries.
  ![contact](docs/feat-contact.jpg)

### Products
  - The product page displays simplicity, showcasing only the image, price, and name of the item.
  ![products](docs/feat-products.jpg)

  - **Product page as Admin**
    - If you're an admin or staff member, you'll have access to buttons to edit or delete products.
    ![admin-edit](docs/feat-managment.jpg)

  - **Product details:**
    Clicking on a specific product allows you to access its details and reviews.
    ![product-detail](docs/feat-product-detail.jpg)

  - **Product details as a logged in customer**
    
    - When logged in, you'll find the button to add a review visible on the page.
    ![add-review-button](docs/feat-add-review-button.jpg)

    - And when clicked, you will be directed to a page where you can read and submit reviews. After that, if you're not satisfied with the review, you can edit it and submit the updated version.
    ![add-review](docs/feat-add-review.jpg)
    
    - When you click on a specific product, you can view its details. If you've previously purchased this product , you can add a review and rate. Attempting to add a review without purchasing it will result in an error message.
    ![product-detail-logged](docs/feat-error-review.jpg)

    - **Product detais page as Admin**
     - As an administrator, you have the ability to edit existing products or add new ones.
     ![product-edit](docs/feat-edit-product.jpg)
     ![product-add](docs/feat-add-product.jpg)

  ### Wishlist

  - The Wishlist feature is exclusively accessible to logged-in users. Users have the capability to review all items they've ever added to their Wishlist. Users have the option to remove individual items from their Wishlist. Additionally, they can click on a button to add more mushrooms, which redirects them to the products page, where they can explore and add additional items to their Wishlist.
 ![add-wishlist](docs/feat-add-wishlist.jpg)
 ![wishlist](docs/feat-wishlist.jpg)

 ### Cart
 
 - The cart feature empowers users to review their orders before proceeding to the checkout page. Users can conveniently adjust the quantity of items in their cart, remove specific items, or clear the Vault entirely. These functionalities are accessible to both logged-in and guest users. Once satisfied with the Vault contents, users can seamlessly proceed to checkout.
 ![add-cart](docs/feat-add-to-cart.jpg)
 ![cart](docs/feat-cart.jpg)
 
  - **Checkout**

    Once you've filled in all the required details and completed the payment, you will receive an order confirmation via email or you can also review your order in your profile.
 ![checkout](docs/feat-checkout.jpg)
 ![order](docs/feat-order-details.jpg)
 ![order-email](docs/feat-order-email.jpg)

### Account

Django AllAuth offers Fungi Fantasy a robust and customizable authentication system, ensuring the security of user data. When a customer wishes to register an account, they can input their username, email, and password (entered twice for accuracy). After submitting the form, the user will receive an email to verify their email address and then proceed to sign in to Fungi Fantasy. 

![account](docs/feat-register.jpg)

  - Once registered, you can simply use your username and password to log in to the website.
![account-sign-in](docs/feat-signin.jpg)
![account-success](docs/feat-success-sigin.jpg)

[Back to the top](#fungi-fantasy)

### Entity Relationship Diagram
The Entity Relationship Diagram (ERD) was generated using Database Designer (for Android), providing a visual representation of the database structure. It illustrates the tables, their respective columns, and the relationships between them. The following is the ERD derived from my planning:
![Entity](docs/Entity-relationship-diagram.jpg)


[Back to the top](#fungi-fantasy)

## Marketing and SEO

### Marketing

- The Fungi Fantasy website also features a Facebook business page, enabling us to share content with customers and interact with them through comments and messages. You can [click here](https://www.facebook.com/profile.php?id=61558190435969) to visit the Fungi Fantasy Facebook Business Page.

![Facebbok-page](docs/facebook-page.jpg)


- The website also features a Mailchimp newsletter signup form, allowing us to gather email addresses for marketing purposes. You can find the newsletter form below:
![Newsletter](docs/newsletter.jpg)

### SEO (Search Engine Optimization)


Keywords relevant to Fungi Fantasy's business scope were meticulously researched, along with description tags. Wordtracker was employed to ensure the inclusion of both short-tail and long-tail keywords. Furthermore, product names and descriptions were carefully crafted to enhance visibility on search engines like Google. See below some of the words:

- Mushrooms
- Fairytale
- Magical
- Mistic
- Decorative mushrooms
- Garden decor
- Outdoor accessories
- Fairy garden decorations
- Enchanted garden ornaments
- Magical mushroom 

To enhance the site's visibility, it have been created two essential files: sitemap.xml and robots.txt. These files play a crucial role in SEO (Search Engine Optimization). The sitemap.xml, generated with XML Sitemap, is located in the root folder, while the robots.txt guides search engine crawlers on accessing and crawling our site's pages.

[Back to the top](#fungi-fantasy)

## Manual Testing


I conducted manual testing based on my user stories. For a test to pass, it must meet the acceptance criteria. I performed the tests on Google Chrome and Mozilla Firefox.

| User story - As a user, I can...                                                                                             | Notes  | Chrome | Firefox | 
| ---------------------------------------------------------------------------------------------------------------------------- | ------ | :----: | :-----: | 
| **click on "All products"** to **explore all items available on the website.**                                               | Passed |   ✅   |   ✅    |
  **create an account** to **access personalised features and save my preferences**.                                           | Passed |   ✅   |   ✅    |  
| **click on a navbar** to **select a specific method for searching for an item**                                              | Passed |   ✅   |   ✅    |
| **Log into my account** to **access my settings and history, or prefill my details at checkout**.                            | Passed |   ✅   |   ✅    |   
| **Log out of my account** to **ensure my account is secure when I'm not using it**.                                          | Passed |   ✅   |   ✅    |   
| **update my account/profile** to **keep my personal information up to date for checking out**.                               | Passed |   ✅   |   ✅    |   
| **delete my account** to **remove my personal data from the platform**.                                                      | Passed |   ✅   |   ✅    |   
| **Access and view my user profile** to **see my personal information, order history, and manage my account settings**.       | Passed |   ✅   |   ✅    |   
| **view a summary of my orders** to **keep track of my purchases** (as a **registered customer**).                            | Passed |   ✅   |   ✅    |   
| **add products to a wishlist** to **save them for future consideration or purchase**.                                        | Passed |   ✅   |   ✅    |  
| **create new products** to **offer more choices to customers** (as a **admin**).                                             | Passed |   ✅   |   ✅    |   
| **update product details** to **ensure all information about the products is current and accurate** (as a **admin**).        | Passed |   ✅   |   ✅    |   
| **delete products** to **remove items that are no longer available or relevant** (as a **admin**).                           | Passed |   ✅   |   ✅    |   
| **add products to my cart** to **purchase them** (as a **customer**).                                                        | Passed |   ✅   |   ✅    |   
| **remove products from my cart** to **manage items before finalizing my purchase** (as a **customer**).                      | Passed |   ✅   |   ✅    |   
| **see an order summary in the cart** to **review my order before completing the purchase** (as a **customer**).              | Passed |   ✅   |   ✅    |   
| **complete the checkout process and pay** to **finalise my order** (as a **customer**).                                      | Passed |   ✅   |   ✅    |   
| **create reviews for products** to **share my experience with others** (as a **logged-in customer**).                        | Passed |   ✅   |   ✅    |   
| **update my reviews** to **modify my feedback if my opinion changes** (as a **logged-in customer**).                         | Passed |   ✅   |   ✅    |   
| **delete my reviews** to **remove my feedback if I no longer wish it to be displayed** (as a **logged-in**).                 | Passed |   ✅   |   ✅    |   
| **Enter my details on the Contact form** to **send a message to the company**.                                               | Passed |   ✅   |   ✅    |                                

[Back to the top](#fungi-fantasy)

## Validation

#### HTML
- I use the [W3C Markup Validation Service](https://validator.w3.org/) to validate my HTML code.
![html-validator](docs/html-validator.jpg)

#### CSS
- I use the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate my CSS code.
![css-validator](docs/css-validator.jpg)

#### JavaScript
- I used [JSHint](https://jshint.com/) to validate my JavaScript code.
![js-validator](docs/js-validator.jpg)


### Python
- I validated the Python files I created or edited using [CI Python Linter](https://pep8ci.herokuapp.com/#).
![python-validator](docs/python-validator.jpg)

- Due to the amount of python files in my project, I've installed [black](https://pypi.org/project/black/) in my terminal for Python and Django testing purposes.

  ![black](docs/black-validator.jpg)

### Lighthouse
- I conducted Lighthouse testing in Incognito mode to obtain optimal results.
![lighthouse](docs/lighthouse.jpg)

[Back to the top](#fungi-fantasy)

## Bug

Throughout the development process, the following bug was identified:
  - User not able to Update the cart, the click event was working but it did not display the expected results.
  
  My code:
  ```
  $('.update-link').click(function(e) {
        var form = $(this).prev('.update-form');
        form.submit();
  }
  ```
  I changed to this and worked it.

  ```
  $('.update-link').on('click', function () {
            var form = $(this).closest('tr').find('.update-form');
            form.submit();
  }
  ```

## Deployment

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To create your Postgres Database, simply sign up with your GitHub account and follow these steps:

- Click on Create New Instance to initiate a new database.
Specify a name for your database (typically the project name, such as "Fungi-Fantasy").
- Choose the Tiny Turtle (Free) plan.
- You can opt to leave the Tags field empty.
- Select the nearest Region and Data Center.
- After creation, access your database by clicking on its name, where you'll find the database URL and Password.

### Amazon AWS
This project utilizes  [AWS](https://aws.amazon.com) for storing media and static files online, as Heroku does not retain this data type.

After creating an AWS account and logging in, navigate to the AWS Management Console page and follow these steps to connect your project.

#### S3 Bucket
- Find and select S3.
- Create a new bucket, providing a name typically matching your Heroku app name, and select the region closest to you.
- Disable "Block all public access" and acknowledge that the bucket will be public, as it's required for Heroku operation.
- Ensure ACLs are enabled and select "Bucket owner preferred" under Object Ownership.
- Navigate to the Properties tab, enable static website hosting, and input "index.html" and "error.html" in their respective fields. Save your changes.
- Move to the Permissions tab and paste the following CORS configuration:
```
[
 {
  "AllowedHeaders": [
   "Authorization"
  ],
  "AllowedMethods": [
   "GET"
  ],
  "AllowedOrigins": [
   "*"
  ],
  "ExposeHeaders": []
 }
]
```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:

- Policy Type: **S3 Bucket Policy**
  - Effect: **Allow**
  - Principal: `*`
  - Actions: **GetObject**
  - Amazon Resource Name (ARN): **paste-your-ARN-here**
  - Click **Add Statement**
  - Click **Generate Policy**
  - Copy the entire Policy, and paste it into the **Bucket Policy Editor**

```
{
 "Id": "Policy1234567890",
 "Version": "2012-10-17",
 "Statement": [
  {
   "Sid": "Stmt1234567890",
   "Action": [
    "s3:GetObject"
   ],
   "Effect": "Allow",
   "Resource": "arn:aws:s3:::your-bucket-name/*"
   "Principal": "*",
  }
 ]
}
```
Before you click "Save", add /* to the end of the Resource key in the Bucket Policy Editor (as shown above).
- Click Save.
#### IAM

- Navigate to IAM by searching for it on the AWS Services Menu. Once on the IAM page, proceed with the following steps:

- Under User Groups, click on Create New Group.
- Suggested Name: group-fungi-fantasy (the group name combined with the project name)
- Tags are optional but must be clicked to access the review policy page.
- Select the newly created group from User Groups and move to the Permissions tab.
- Click on the Add Permissions dropdown and select Attach Policies.
- Choose the desired policy and click Add Permissions at the bottom to finish.
- Under the JSON tab, select the Import Managed Policy link.
```
{
 "Version": "2012-10-17",
 "Statement": [
  {
   "Effect": "Allow",
   "Action": "s3:*",
   "Resource": [
    "arn:aws:s3:::your-bucket-name",
    "arn:aws:s3:::your-bucket-name/*"
   ]
  }
 ]
}
```
- Click on Review Policy.
  - Suggested Name: policy-fungi-fantasy (policy combined with the project name)
   - Provide a description: "Access to S3 Bucket for fungi-fantasy static files."
   - Click Create Policy.
- Under User Groups, select your "group-fungi-fantasy".
- Click Attach Policy.
- Search for the policy you've just created ("policy-fungi-fantasy"), select it, then Attach Policy.
- Under User Groups, click Add User.
- Suggested Name: user-fungi-fantasy (user combined with the project name)
  - For "Select AWS Access Type," choose Programmatic Access.
  - Select the group to add your new user to: group-fungi-fantasy.
  - Tags are optional, but click it to access the review user page.
  - Click Create User once done.
- You should see a button to Download .csv, so click it to save a copy on your system.
***IMPORTANT: Once you pass this page, you cannot come back to download it again, so do it immediately!***
- This contains the user's Access key ID and Secret access key.
  - AWS_ACCESS_KEY_ID = Access key ID
  - AWS_SECRET_ACCESS_KEY = Secret access key.

#### Set up AWS

- If DISABLE_COLLECTSTATIC is still present in Heroku Config Vars, it can now be removed to allow AWS to handle static files.
- In the S3 dashboard, create a new folder named: media.
- Choose existing media images for your project to prepare them for upload into the new folder.
- Under Manage Public Permissions, select Grant public read access to this object(s)
- No further settings are required, so click Upload.

### Stripe API

This project utilizes [Stripe](https://stripe.com) to handle the ecommerce payments.
To integrate your project with Stripe, follow these steps:

- Navigate to your Stripe dashboard and expand "Get your test API keys".
Here you'll find two keys:
   - STRIPE_PUBLIC_KEY = Publishable Key (starts with pk)
  - STRIPE_SECRET_KEY = Secret Key (starts with sk)
As a backup in case users close the purchase-order page during payment, Stripe Webhooks can be included.

- In your Stripe dashboard, go to Developers, then select Webhooks.
- Click Add Endpoint.
- Use the endpoint: https://fungi-fantasy-4819ad1964c1.herokuapp.com/checkout/wh/
- Select receive all events.
- Click Add Endpoint to complete the process.
- You'll receive a new key:
   -STRIPE_WH_SECRET = Signing Secret (Webhook) Key (starts with wh)

### Gmail API
This project utilizes [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.
To integrate your project with Gmail, follow these steps:

- Click on the Account Settings (cog icon) in the top-right corner of Gmail.
Go to the Accounts and Import tab.
- Under "Change account settings", select Other Google Account settings.
- On the new page, choose Security from the left sidebar.
- Turn on 2-Step Verification. (verify your password and account)
- After verification, turn on 2FA.
- Return to the Security page and find App passwords.
- Confirm your password and account again if prompted.
- Select Mail for the app type.
- Choose Other (Custom name) for the device type.
- Use any custom name, like "Django" or "fungifantasy"
- You'll receive a 16-character password (API key).
- Save this securely, as it can't be accessed later!
  - EMAIL_HOST_PASS = user's 16-character API key
  - EMAIL_HOST_USER = user's personal Gmail email address

### Heroku


This project utilizes [Heroku](https://www.heroku.com), a platform as a service (PaaS) that empowers developers to build, run, and manage applications entirely in the cloud.
Follow these deployment steps after setting up your account:

- Navigate to your Heroku Dashboard and click New in the top-right corner, then select Create new app.
- Choose a unique app name, select a region (EU or USA), and click Create App.
- In the app's Settings, click Reveal Config Vars, and set the following environment variables:

| Key                     | Value                                                                |
| ----------------------- | -------------------------------------------------------------------- |
| **AWS_ACCESS_KEY_ID**     | user's own value                                                     |
| **AWS_SECRET_ACCESS_KEY** | user's own value                                                     |
| **DATABASE_URL**          | user's own value                                                     |
| **DISABLE_COLLECTSTATIC** | 1 (_this is temporary, and can be removed for the final deployment_) |
| **EMAIL_HOST_PASS**       | user's own value                                                     |
| **EMAIL_HOST_USER**       | user's own value                                                     |
| **SECRET_KEY**            | user's own value                                                     |
| **STRIPE_PUBLIC_KEY**     | user's own value                                                     |
| **STRIPE_SECRET_KEY**     | user's own value                                                     |
| **STRIPE_WH_SECRET**      | user's own value                                                     |
| **USE_AWS**               | True                                                                 |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- pip3 install -r requirements.txt

If you have your own packages that have been installed, then the requirements file needs updated using:

- pip3 freeze --local > requirements.txt

The **Procfile** can be created with the following command:

- echo web: gunicorn app_name.wsgi > Procfile
- _replace **app_name** with the name of your primary Django app name; the folder where settings.py is located_

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: heroku login -i
- Set the remote for Heroku: heroku git:remote -a app_name (replace _app_name_ with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
  - git push heroku main

Your project is now successfully connected and deployed on Heroku!

### Cloning Project

A local clone of this repository can be made on GitHub. Please follow the below steps:

- Navigate to GitHub and log in.
- The [Fungi Fantasy Repository](https://github.com/Bruna-Andelieri/FungiFantasy) can be found at this location.
- Above the repository file section, locate the 'Code' button.
- Click on this button and choose your clone method from HTTPS, SSH, or GitHub CLI, copy the URL to your clipboard by clicking the 'Copy' button.
- Open your Git Bash Terminal.
- Change the current working directory to the location you want the cloned directory to be made.
- Type git clone and paste in the copied URL from the step above.
- Press 'Enter' for the local clone to be created.
- Use the **pip3 install -r requirements.txt** command to install the dependencies and libraries needed for Fungi Fantasy.
- Set up your env.py file and gather the PostgreSQL URL from ElephantSQL, if applicable, and add your SECRET_KEY and STRIPE/AWS keys if using these services.
- Ensure that your env.py file is placed in your .gitignore file and follow the remaining steps in the Django Project Setup section before pushing your code to GitHub.

### Forking Project

You can create a copy of the original repository on GitHub by following these steps:

- Log in to GitHub.
- Visit the [Fungi Fantasy Repository](https://github.com/Bruna-Andelieri/FungiFantasy).
- Click the 'Fork' button at the top right of the repository page to make a copy in your own GitHub account.

You will now have a forked version of the repository in your GitHub account. 

[Back to the top](#fungi-fantasy)

## Tecnologies Used
#### Languages

- HTML
- CSS
- JavaScript
- Python 

#### Frameworks and Libraries

- Django
- Bootstrap
- jQuery
- Stripe

#### Development and Deploy

- Heroku
- Git
- GitHub
- VsCode

## Credits

- [**Google Fonts**](https://fonts.google.com/)  - utilized for selecting the perfect typography
- [**AWS**](https://aws.amazon.com/) - employed as a storage solution for static and media files
- [**FavIcon.io**](https://favicon.io/favicon-converter/)  - utilized for compressing favicons
- [**FreePik**](https://www.freepik.com/)  - serves as a database for images
- [**Google Fonts**](https://fonts.google.com/)  - employed for selecting the best typography
-  [**W3Schools**](https://www.w3schools.com/) - provides useful information and cheat sheets
- [**Code Institute**](https://github.com/Code-Institute-Org>) Boutique Ado  walkthroughs
- [**XML-Sitemaps.com**](https://www.xml-sitemaps.com/)  - utilized for generating XML sitemaps
- [**Coolors**]((https://coolors.co/)) for color palette


## Acknowledgements


Completing this final project brings me immense joy...
Code Institute has been an invaluable source of support and guidance throughout the development journey, from my mentor Rohit Sharma to the helpful Slack community, my cohort and colleagues.

I owe a debt of gratitude to my partner, Ivan, whose coding expertise and unwavering belief in me have been instrumental in my journey into software development. His support has been crucial to the success and completion of this project, and I am truly thankful for his contributions.

[Back to the top](#fungi-fantasy)