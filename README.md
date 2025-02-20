# QR Code Generator

The QR code generators available online are not free, or they have an expiry date to work, so I decided to make my own and avoid this problem in the future.

I created this while managing the website of an [academic event](https://europeanovaryworkshop.com/). I set their schedule on an [event application](https://eow2025.sched.com/) and [made de QR code available](https://www.canva.com/design/DAGey69uEgg/hyRrpLpBMN43S56q5pMJDA/edit?utm_content=DAGey69uEgg&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) for the attendees to download the app and check the program.

## How to Use

- Replace the URL by the link you want the code to point to:

``img = qrcode.make("http://your_url_here")``

- Run the program in the terminal:

``python qrcode_gen.py``