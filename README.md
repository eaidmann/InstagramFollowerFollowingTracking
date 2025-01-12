# Instagram Follower/Following Tracking
This tool allows the user to track their current followers or following list on their Instagram account by comparing it with the previous follower/following list.

The tool uses downloaded Instagram information from the owner's account without requiring any login credentials inside the code.

The user needs to have the previous follower/following list data before keeping track of the current follower/following list for any unfollowed or new Instagram users.

NOTE : PLEASE USE THIS AT YOUR OWN RISK.

## Table of Contents
- [Pre-Requisites](#pre-requisites)
- [Information Data File](#Information-Data-File)
- [Tutorial Video](#Tutorial-Video)
- [How to Use ?](#How-to-Use-?)
- [Output File](#Output-File)


## Pre-Requisites
The user of this tool needs to download their Instagram follower/following list beforehand from their own Instagram account. The following example is based on the Android Instagram application:

1. Open your Instagram account.
2. Go to Settings and then Activity.
3. Click Your Activity.
4. In Your Activity, under Information you’ve shared with Instagram, click on Download Your Information.
5. Choose the Instagram account from which you want to download the information.
6. Click Download or Transfer Information.
7. Under Where do you want to get information from?, select your Instagram account and click Next.
8. Under How much information do you want?, choose Some of your information for a quick download.
9. Under What information do you want for this profile?, scroll down until you find Followers and Following under the Connections section.
10. Check it, then click Next.
11. Choose Download to Device.
12. Select the date range for the information you wish to download, then click Create Files.
13. Wait for the process to finish, then return to the page and click Download to get the data.

Note:
- It is better to download all-time data for better tracking.
- The first downloaded follower/following list data can be used as the original data for subsequent use.

## Information Data File
After you have downloaded the compressed information data file, you need to extract it.

Inside the information data file, you can find the follower HTML file in the directory "connections\followers_and_following\followers_1.html".

For the following HTML file data, look for "connections\followers_and_following\following.html".

## Tutorial Video
1. How to download Instagram Information Data File.
- Youtube Link : https://www.youtube.com/watch?v=8xTpM4jpCNk
- All credits go to the video owner.
- The video explains how to retrieve DM data, but you can modify the steps to download follower/following data instead.
- The other steps are the same.

2. Tutorial on how to use the tool.
- Youtube Link : https://youtu.be/GuYz_9dYnpk

## How to Use ?
1. Go to "dist" folder and run the "main.exe" file to open the application.
2. After the application is opened. First, click the "Import" button to import your Original Follower Data Path.
3. Once imported, the "Retrieve" button will be available. Click on "Retrieve" to convert it to CSV format.
4. Do the same for the second "Import" button for the Updated Follower Data Path.
5. Once both files have been successfully imported and retrieved, click on "Compare".
6. The output file will be generated in the "Output" folder once the comparison is successful. Click the "Open" button to open the generated output file.

## Output File
Inside this output file, you will see the Link, Username, Date Joined, and Status of the Instagram users who have unfollowed or followed you.

- Link: The Instagram link of the follower/following user.
- Username: The Instagram username of the follower/following user.
- Date Joined: The date the follower/following user joined Instagram.
- Status: Unfollowed: User who unfollowed your Instagram account. ; New: User who was not previously following you.
