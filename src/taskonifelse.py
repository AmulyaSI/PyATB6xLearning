
"""Q - You receive an API response code from your test script.
Write an if-else block to check whether the response is successful (status code 200) or not.

I/P response = 404 , O/P ❌ Failed API Request
I/P response = 200 , O/P ✅ Passed API Request """

# logic building
int_res = int(input("Enter a nuber"))

if int_res == 200:
    print("✅ Passed API Request ✅")
elif int_res == 404:
    print("Failed API Request with 404")
elif int_res == 500:
    print("Failed API Request with 500")
elif int_res == 504:
    print("Failed API Request with 504")
else:
    print("⚠️enter a valid API Request⚠️")

print("*********************************************")

"""In automation, you often compare expected and actual outputs.
Write code to check if a test case passed or failed.

expected_title = "Dashboard"
actual_title = "Dashboard "

✅ Test Passed – Title matches
True - why >  Strip and convert them into the lowercase = both of them are equal"""

expected_title = input("Enter expected title").strip().lower() # strip removes extra spaces, lower converts the str to lower case
actual_title = input("Enter actual title").strip()

if expected_title == actual_title:
    print("✅ test case passed successfully ✅")
else:
    print("❌test case failed successfully❌")

print("***************************")