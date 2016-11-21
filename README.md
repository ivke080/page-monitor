<h1>Page Monitor</h1>
<p>With this python project you can make a list of websites that you want to watch for recent changes. If some website has been
changed recently, script will notice that, update the list and open that url in the browser.</p>
<h2>Usage example</h2>
<p>This adds a url to the monitor list: python monitor.py --add http://www.example.com</p>
<p>You can list all the urls that that are being watched by the script: python monitor.py --list</p>
<p>To check for updates, you just type: python monitor.py --check</p>
<p>And ofc, you can chain all that options together python monitor.py --add http://www.example.com --list --remove www.example.com
 --check</p>
