from bs4 import BeautifulSoup
import pprint
# url = ''
HTMLFileToBeOpened = open("udemy course.html", "r")
contents = HTMLFileToBeOpened.read()
beautifulSoupText = BeautifulSoup(contents, 'lxml')


followers= []
# beautifulSoupText.find('')

# print(beautifulSoupText.body.prettify())
#
# for span in beautifulSoupText.select(span):
#     print(span.text)

# for a_tag in beautifulSoupText.find_all("a", class_="_ap3a _aaco _aacw _aacx _aad7 _aade"):
#     if a_tag !=0:
#         list1.append(a_tag)
#     return list1

# for a_tag in beautifulSoupText.find_all('a'):
#     # Extract the text inside the anchor tag, which is likely the username
#     if a_tag and len(a_tag)> 0:
#         list1.append(a_tag)

for span in beautifulSoupText.find_all("span"):
    # Check if the anchor tag has a nested div or span with the username
    followers_username = span.get_text(strip=True)

    # If username is not empty and doesn't contain unwanted characters, add it to the list
    if followers_username and len(followers_username) > 0:  # Adjust this condition as needed
        followers.append(followers_username)

for index, followers_username in enumerate(followers, start=1):
    print(f"{index}. {followers_username}")

# print(usernames)


# followers = beautifulSoupText.text.prettify()

# print(followers)




