# python-extension-checker
Python script that checks for incorrect file extensions

<b>Description:</b>
This script will check the current directory in the terminal for files with bad filename extensions. If it comes to such a file, it will adjust the extension and then try to rename it. If the file already exists, it will loop, repeatedly creating a new time string to append to the filename, until it is ok to save (under normal circumstances, this should only be done once).

During execution, it will ask if you wish to continue, update you every 50 files, and then print the total number of files renamed and the total size of the directory.

<b>Why/Reasoning:</b>
Many desktop environments generate previews based on the file extension, so this should make sure the previews will work.

<b>Requires:</b>
<ul>
  <li><a href="https://github.com/ahupp/python-magic">python-magic</a></li>
</ul>

<b>Known Issues:</b>
<ul>
  <li>Will fail, if the filename gets too long for the operating system</li>
</ul>

<b>To Do:</b>
<ol>
  <li>Fix the filename length issue</li>
</ol>
