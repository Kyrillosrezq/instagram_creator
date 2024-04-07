Instagram Account Creator

This Python script automates the process of creating Instagram accounts using the Selenium library. It operates through the following stages:

Email Creation: The script navigates to outlook.com to generate an email address for receiving the OTP code.

Instagram Account Setup: After obtaining the email address, it proceeds to Instagram to fill in the required information and initiate the account creation process, awaiting verification.

OTP Retrieval: The script then navigates back to the Outlook inbox to locate and copy the OTP code sent by Instagram.

Account Verification: With the OTP code in hand, the script returns to Instagram to paste the code and finalize the account creation.

Logging Information: Upon successful account creation, login details (username, password, and associated email) are appended to a text file for future reference.

**** Human Interaction: The script only requires human intervention for solving captchas. ****

Requirements: This script necessitates the use of proxies for operation.



