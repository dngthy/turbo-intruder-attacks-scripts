# Pre-setting Macro:
# Go to /Project options/, open /Sessions/ tab, in /Session Handling Rules/ press /Add/ button to add new Rule.
# Tab to /Scope/, select all fields in /Tools Scope/, select /Include all URLs/ in /URL Scope/
# Add /Ok/
# In /Rule Actions/, press /Add/ and select /Run a macro/, select macro you wanna use, don't select request that
# you try intrudering. Test macro before press /Ok/

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           engine=Engine.BURP
                           )

    for word in open('path/to/wordlist','r'):
        engine.queue(target.req, word.strip())


def handleResponse(req, interesting):
    if req.status != 404:
        table.add(req)