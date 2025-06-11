import requests
##<img src="https://tryhackme-badges.s3.amazonaws.com/tatsukikitamura.png" alt="Your Image Badge" />
##https://tryhackme.com/api/v2/badges/public-profile?userPublicId=4877687
api_url = "https://tryhackme-badges.s3.amazonaws.com/tatsukikitamura.png"
post_url = "https://tryhackme.com/api/v2/badges/public-profile/image"
data = {userPublicId: 4877687, username: "tatsukikitamura"}

preresponse = requests.post(post_url,params=data)
res = requests.get(api_url)


def save_image(filename, image):
    with open(filename, "wb") as fout:
        fout.write(image)

save_image("assets/thm_propic.png",res.content)
