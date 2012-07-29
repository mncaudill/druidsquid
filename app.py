from flask import Flask, Response
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return """
<h1>Druid-Squid-GUID Generator</h1>

<h2>This program does three things:</h2>
    <ol>
        <li>Prints out an ASCII art representation of a <a href="/druid">druid</a>.</li>
        <li>Prints out an ASCII art representation of a <a href="/squid">squid</a>.</li>
        <li>Prints out a version 4 <a href="/uuid">UUID</a> in hex form.</li>
    </ol>

<h2>Why?</h2>
<p>I'm not quite sure how to pronounce 'GUID'.</p>

<h2>Who?</h2>
<p><a href="http://nolancaudill.com">Nolan Caudill</a>

<h2>How?</h2>
<p>With <a href="http://github.com/mncaudill/druidsquid">code</a>. The squid came from <a href="http://www.retrojunkie.com/asciiart/animals/squid.htm">here</a>
and the druid came from <a href="http://ascii.co.uk/art/druid">here</a>.</p>
</p>

"""

@app.route('/uuid')
def uu_id():
    return Response(uuid.uuid4().hex, mimetype="text/plain") 

@app.route('/druid')
def druid():
    return Response("""
\n         __       \n,--.   \(  ` _     _      Kra-a!  \n   \\__ J\  / `   ("r  -'                                      ,--.  \n __/\_ \ .--.__  / )                                          (    ) \n  \  /\ | /""-.`/7(_                                           `--' \n    '\ \ \/`\_ \_.`)\   .__ \n \ __   ( L / `- )   ___/_ \ \n/.'  ^\_| |,-' /____/'""  ) ` \n) . /  L\  \.-'_.-,`\_.                         __ \n ,_|_ _( \  .-' \_, ' __                       /_ \ \n. /__\ |_  --'""==-._/ _\_              _     /,##/  .--.  \n='    /  )  /'"\\--) \                 /  \  (  ` \  \   \ \n/ `>-'_    (  -(/ /| '\                \  (  \ \_/ )  \/  .  \n  /.-' |c  |   .--.                    /  `. |`._)/    )  |                \n /  \  |   /   (   \                  )    ) |    |   / / | \n \  '  >   \    `)  .  _____________  \    / )  \ |   \/  >  ___________ \n       | . |     )  |                 /    | Y___\)    |  | \n       )   |    <_/ |                 |    |a888P^    /   (-.  \n       |    .--'|`  >                 /    (YPP      8a___.-' \n     aPa`|.'    |   |                a._..a-'       88888P \n  a:f88P-x-'    \   (.             a88888P         8888P \na8888P   )    `8(___.'           a8888P         888888         \n88P     (    888888P            8888P          8888P            \n           a8888P             8888P            888 \n         a888P               888 \n      a8888P \n      88P 

    """, mimetype="text/plain")

@app.route('/squid')
def squid():
    return Response("""
\n            ^ \n          /   \ \n          \   / \n          |   | \n          |   | \n          | 0 | \n         // ||\\ \n        (( // || \n         \\))  \\ \n       //||    )) \n       ( ))   // \n        //   ((
    """, mimetype="text/plain")

if __name__ == "__main__":
    app.run()
