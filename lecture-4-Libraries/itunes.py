# Example 1
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(response.json())

# $ python itunes.py blackpink
# {'resultCount': 1, 'results': [{'wrapperType': 'track', 'kind': 'song', 'artistId': 1141774019, 'collectionId': 1263315668, 'trackId': 1263315989, 'artistName': 'BLACKPINK', 'collectionName': 'BLACKPINK - EP', 'trackName': "As If It's Your Last (Japanese Version)", 'collectionCensoredName': 'BLACKPINK - EP', 'trackCensoredName': "As If It's Your Last (Japanese Version)", 'artistViewUrl': 'https://music.apple.com/us/artist/blackpink/1141774019?uo=4', 'collectionViewUrl': 'https://music.apple.com/us/album/as-if-its-your-last-japanese-version/1263315668?i=1263315989&uo=4', 'trackViewUrl': 'https://music.apple.com/us/album/as-if-its-your-last-japanese-version/1263315668?i=1263315989&uo=4', 'previewUrl': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview125/v4/27/39/18/27391889-acec-5c7d-feae-10b77f420ee6/mzaf_7325735014632280538.plus.aac.p.m4a', 'artworkUrl30': 'https://is1-ssl.mzstatic.com/image/thumb/Music118/v4/1b/4b/9f/1b4b9f6a-fabd-c2e1-cfea-3d967db0c358/AVCY-58498.jpg/30x30bb.jpg', 'artworkUrl60': 'https://is1-ssl.mzstatic.com/image/thumb/Music118/v4/1b/4b/9f/1b4b9f6a-fabd-c2e1-cfea-3d967db0c358/AVCY-58498.jpg/60x60bb.jpg', 'artworkUrl100': 'https://is1-ssl.mzstatic.com/image/thumb/Music118/v4/1b/4b/9f/1b4b9f6a-fabd-c2e1-cfea-3d967db0c358/AVCY-58498.jpg/100x100bb.jpg', 'collectionPrice': 7.74, 'trackPrice': 1.29, 'releaseDate': '2017-08-29T12:00:00Z', 'collectionExplicitness': 'notExplicit', 'trackExplicitness': 'notExplicit', 'discCount': 1, 'discNumber': 1, 'trackCount': 6, 'trackNumber': 5, 'trackTimeMillis': 212773, 'country': 'USA', 'currency': 'USD', 'primaryGenreName': 'J-Pop', 'isStreamable': True}]}

# Example 2
# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))
# {
#   "resultCount": 1,
#   "results": [
#     {
#       "wrapperType": "track",
#       "kind": "song",
#       "artistId": 1141774019,
#       "collectionId": 1263315668,
#       "trackId": 1263315989,
#       "artistName": "BLACKPINK",
#       "collectionName": "BLACKPINK - EP",
#       "trackName": "As If It's Your Last (Japanese Version)",
#       "collectionCensoredName": "BLACKPINK - EP",
#       "trackCensoredName": "As If It's Your Last (Japanese Version)",
#       "artistViewUrl": "https://music.apple.com/us/artist/blackpink/1141774019?uo=4",
#       "collectionViewUrl": "https://music.apple.com/us/album/as-if-its-your-last-japanese-version/1263315668?i=1263315989&uo=4",
#       "trackViewUrl": "https://music.apple.com/us/album/as-if-its-your-last-japanese-version/1263315668?i=1263315989&uo=4",
#       "previewUrl": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview125/v4/27/39/18/27391889-acec-5c7d-feae-10b77f420ee6/mzaf_7325735014632280538.plus.aac.p.m4a",
#       "artworkUrl30": "https://is1-ssl.mzstatic.com/image/thumb/Music118/v4/1b/4b/9f/1b4b9f6a-fabd-c2e1-cfea-3d967db0c358/AVCY-58498.jpg/30x30bb.jpg",
#       "artworkUrl60": "https://is1-ssl.mzstatic.com/image/thumb/Music118/v4/1b/4b/9f/1b4b9f6a-fabd-c2e1-cfea-3d967db0c358/AVCY-58498.jpg/60x60bb.jpg",
#       "artworkUrl100": "https://is1-ssl.mzstatic.com/image/thumb/Music118/v4/1b/4b/9f/1b4b9f6a-fabd-c2e1-cfea-3d967db0c358/AVCY-58498.jpg/100x100bb.jpg",
#       "collectionPrice": 7.74,
#       "trackPrice": 1.29,
#       "releaseDate": "2017-08-29T12:00:00Z",
#       "collectionExplicitness": "notExplicit",
#       "trackExplicitness": "notExplicit",
#       "discCount": 1,
#       "discNumber": 1,
#       "trackCount": 6,
#       "trackNumber": 5,
#       "trackTimeMillis": 212773,
#       "country": "USA",
#       "currency": "USD",
#       "primaryGenreName": "J-Pop",
#       "isStreamable": true
#     }
#   ]
# }

# Example 3
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
data = response.json()
for result in data["results"]:
    print(result["trackName"])

# As If It's Your Last (Japanese Version)
# CS50P/lecture-4-Libraries/ $ python itunes.py blackpink
# As If It's Your Last (Japanese Version)
# Playing With Fire (Japanese Version)
# Stay (Japanese Version)
# Whistle (Japanese Version)
# Boombayah (Japanese Version)
# Whistle (Acoustic Ver.) [Japanese Version]
# Blackpink
# Blackpink
# Sour Candy
# DDU-DU DDU-DU -JP Ver.-
# STAY -JP Ver.-
# SO HOT -THEBLACKLABEL REMIX- (BLACKPINK ARENA TOUR 2018 "SPECIAL FINAL IN KYOCERA DOME OSAKA")
# As If It's Your Last
# Shoong! (feat. LISA of BLACKPINK)
# How You Like That
# Blackpink
# Ice Cream
# Boombayah (Japanese Version)
# As If It's Your Last (Japanese Version)
# PLAYING WITH FIRE -JP Ver.-
# WHISTLE -JP Ver.-
# Blackpink
# REALLY -JP Ver.-
# Whistle (Japanese Version)
# FOREVER YOUNG -JP Ver.-
# AS IF IT'S YOUR LAST -JP Ver.-
# Kiss and Make Up
# BOOMBAYAH -JP Ver.-
# SEE U LATER -JP Ver.-
# BOOMBAYAH
# Stay (Japanese Version)
# Playing With Fire (Japanese Version)
# Whistle (Acoustic Ver.) [Japanese Version]
# Lovesick Girls
# Black Pink
# How You Like That
# SOLO
# Pretty Savage
# How You Like That
# PLAYING WITH FIRE
# Ice Cream
# Blackpink
# Blackpink!
# SOLO
# Kill This Love
# WHISTLE
# Bet You Wanna (feat. Cardi B)
# Gone
# BOOMBAYAH
# Crazy Over You