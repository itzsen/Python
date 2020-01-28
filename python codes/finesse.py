import sys
import time

# Using Python external "requests" module to call REST APIs
import requests 
from requests.auth import HTTPBasicAuth
from xml.etree import ElementTree

# Using SleekXMPP to connect to the Finesse Notification Service
# There are other python libraries here: http://xmpp.org/software/libraries.html
from sleekxmpp import ClientXMPP
from sleekxmpp import Message
from sleekxmpp.xmlstream import ElementBase
from sleekxmpp.xmlstream import register_stanza_plugin
from sleekxmpp.xmlstream.handler import Callback
from sleekxmpp.xmlstream.matcher import StanzaPath
import logging
# logging.basicConfig(level=logging.DEBUG) # Uncomment this if you want logging for sleekxmpp

"""
    This Finesse python script demonstrates how to use Finesse REST
    APIs in python and how to establish a XMPP connection to the
    Finesse Notification Service and receive Finesse events using a
    third party XMPP library.

    This is a simple script that logs in, changes state, and logs
    out. The script does not integrate the Finesse events back
    into the User object. This work would need to be done to
    enhance the script for production usage.

    This python script requires the following libraries:
        - requests (http://docs.python-requests.org/)
        - SleekXMPP (http://sleekxmpp.com/)

    This is only a sample and is NOT intended to be production
    quality and will not be supported as such.  It is NOT guaranteed
    to be bug free. It is merely provided as a guide for a programmer
    to see how to use the Finesse REST APIs and receive Finesse
    notifications in python.
"""

def printRESTAPIResponse(prefix='printRESTAPIResponse()', response=''):
    """
        Print the REST API response with the HTTP Request status code
        and the Response body text
    """
    print (prefix + " - Status: ", response.status_code) # This is the http request status
    print (prefix + " - Text: ", response.text)
    print ("\n")

def GET(url, username, password, params=''):
    """
        Call the GET HTTP Request using HTTP Basic Auth authentication
        
        Parameters:
            url (str): The URL to make the REST request
            username (str): The username of the user making the HTTP request
            password (str): The password of the user making the HTTP request
            params(dictionary, optional): Dictionary or bytes to be sent in the query string for the Request.
                                          (e.g. {"category" : "NOT_READY"})

        Returns: Response object (http://docs.python-requests.org/en/master/api/#requests.Response) - The HTTP Response as a result of the HTTP Request
    """
    print ("Executing GET '%s'" % url)
    try:
        response = requests.get(url=url, auth=HTTPBasicAuth(username, password), params=params)
        printRESTAPIResponse("GET()", response)
        return(response)
    except:
       print ("An error occured in the GET request to %s" % url)
       print (sys.exc_info());
       sys.exit()

def PUT(url, username, password, params='', data=''):
    """
        Call the PUT HTTP Request using HTTP Basic Auth authentication
        
        Parameters:
            url (str): The URL to make the REST request
            username (str): The username of the user making the HTTP request
            password (str): The password of the user making the HTTP request
            params(dictionary, optional): Dictionary or bytes to be sent in the query string for the Request.
                                          (e.g. {"category" : "NOT_READY"})
            data(str, optional): The HTTP request body as a string

        Returns: Response object (http://docs.python-requests.org/en/master/api/#requests.Response) - The HTTP Response as a result of the HTTP Request
    """
    print ("Executing PUT '%s'\n" % url)
    try:
        headers = {'Content-Type': 'application/xml'}
        print ("PUT() data: %s\n" % data)
        response = requests.put(url=url, auth=HTTPBasicAuth(username, password), headers=headers, params=params, data=data)
        printRESTAPIResponse("PUT()", response)
        return(response)
    except:
       print ("An error occured in the PUT request to %s" % url)
       print (sys.exc_info());
       sys.exit()

def POST(url, username, password, params='', data=''):
    """
        Call the POST HTTP Request using HTTP Basic Auth authentication
        
        Parameters:
            url (str): The URL to make the REST request
            username (str): The username of the user making the HTTP request
            password (str): The password of the user making the HTTP request
            params(dictionary, optional): Dictionary or bytes to be sent in the query string for the Request.
                                          (e.g. {"category" : "NOT_READY"})
            data(str, optional): The HTTP request body as a string

        Returns: Response object (http://docs.python-requests.org/en/master/api/#requests.Response) - The HTTP Response as a result of the HTTP Request
    """
    print ("Executing POST '%s'\n" % url)
    try:
        headers = {'Content-Type': 'application/xml'}
        print ("POST() data: %s\n" % data)
        response = requests.post(url=url, auth=HTTPBasicAuth(username, password), headers=headers, params=params, data=data)
        printRESTAPIResponse("POST()", response)
        return(response)
    except:
       print ("An error occured in the POST request to %s" % url)
       print (sys.exc_info());
       sys.exit()

def DELETE(url, username, password):
    """
        Call the DELETE HTTP Request using HTTP Basic Auth authentication
        
        Parameters:
            url (str): The URL to make the REST request
            username (str): The username of the user making the HTTP request
            password (str): The password of the user making the HTTP request

        Returns: Response object (http://docs.python-requests.org/en/master/api/#requests.Response) - The HTTP Response as a result of the HTTP Request
    """
    print ("Executing DELETE '%s'\n" % url)
    try:
        response = requests.delete(url=url, auth=HTTPBasicAuth(username, password))
        printRESTAPIResponse("DELETE()", response)
        return(response)
    except:
       print ("An error occured in the DELETE request to %s" % url)
       print (sys.exc_info());
       sys.exit()


class User:
    """
        Represents a User object.

        Initializing the User will call a GET on the user and store the
        XML response. All subsequent getters (id, extension, role, etc)
        gets the value from the stored XML response. Explicitly calling
        the getUser() method will update the XML response by calling the
        GET on the user again.

        User sign in, change state and sign out REST APIs have also been
        added to this User object.

        The connection to the Finesse notification service also happens
        during the initialization of the User. The events that are received
        are NOT tied back into stored XML response. Further work will be
        needed to enhance this. 
    """

    def __init__(self, username, password, scheme, fqdn, port, domain):
        # Get the information from the config file
        self.scheme = scheme
        self.fqdn = fqdn
        self.port = port
        self.domain = domain

        self.username = username
        self.password = password

        # Call the GET user API (and store the XML response)
        self.getUser(id=self.username)

        # Establish a connection to the Finesse Notification Service
        self.xmppConnection = Jabber(self.username, password, self.domain)
        self.xmppConnection['feature_mechanisms'].unencrypted_plain = True
        print("Connecting to the Finesse Notification Service.")
        if self.xmppConnection.connect(address=(self.fqdn, 5222), use_tls=False, use_ssl=False):
            print("Waiting 2 seconds to establish a connection.")
            self.xmppConnection.process(block=False)

            # Need to wait a couple of seconds before calling a REST API
            self.waitForNotification()
            print("The XMPP connection is successful.")
        else:
            print("Failed to connect to XMPP.")
            sys.exit(0)

    def getElementFromTree(self, xmlTag):
        """
            From the stored GET User XML response, return
            the value of the given XML tag.

            Parameters:
                xmlTag (str): The XML tag to search for

            Returns: String - The value of the given XML tag or empty string if not found
        """
        if self.userTree:
            elementValue = self.userTree.find(xmlTag).text;
            if elementValue:
                return(elementValue)

        return ("")

    def getDialogsUri(self):
        """
            Get the value in the <dialogs> tag.

            Returns: String - The value of the <dialogs> tag or empty string if not found
        """
        return(self.getElementFromTree('dialogs'))

    def getExtension(self):
        """
            Get the value in the <extension> tag.

            Returns: String - The value of the <extension> tag or empty string if not found
        """
        return(self.getElementFromTree('extension'))

    def getFirstName(self):
        """
            Get the value in the <firstName> tag.

            Returns: String - The value of the <firstName> tag or empty string if not found
        """
        return(self.getElementFromTree('firstName'))

    def getLastName(self):
        """
            Get the value in the <lastName> tag.

            Returns: String - The value of the <lastName> tag or empty string if not found
        """
        return(self.getElementFromTree('lastName'))

    def getLoginId(self):
        """
            Get the value in the <loginId> tag.

            Returns: String - The value of the <loginId> tag or empty string if not found
        """
        return(self.getElementFromTree('loginId'))

    def getLoginName(self):
        """
            Get the value in the <loginName> tag.

            Returns: String - The value of the <loginName> tag or empty string if not found
        """
        return(self.getElementFromTree('loginName'))

    def getPendingState(self):
        """
            Get the value in the <pendingState> tag.

            Returns: String - The value of the <pendingState> tag or empty string if not found
        """
        return(self.getElementFromTree('pendingState'))

    def getReasonCodeId(self):
        """
            Get the value in the <reasonCodeId> tag.

            Returns: String - The value of the <reasonCodeId> tag or empty string if not found
        """
        return(self.getElementFromTree('reasonCodeId'))

    def getRoles(self):
        """
            Get a list of roles from the <roles> tag.

            Returns: List - A list of values from the <role> tag or empty list if not found
        """
        rolesList = []
        roles = self.userTree.find('roles')
        for role in roles.findall('role'):
            rolesList.append(role.text)
        return(rolesList)

    def getSettings(self):
        """
            Get the value in the <settings> tag.

            Returns: String - The value of the <settings> tag or empty string if not found
        """
        return(self.getElementFromTree('settings'))

    def getState(self):
        """
            Get the value in the <state> tag.

            Returns: String - The value of the <state> tag or empty string if not found
        """
        return(self.getElementFromTree('state'))

    def getStateChangeTime(self):
        """
            Get the value in the <stateChangeTime> tag.

            Returns: String - The value of the <stateChangeTime> tag or empty string if not found
        """
        return(self.getElementFromTree('stateChangeTime'))

    def getTeamId(self):
        """
            Get the value in the <teamId> tag.

            Returns: String - The value of the <teamId> tag or empty string if not found
        """
        return(self.getElementFromTree('teamId'))

    def getTeamName(self):
        """
            Get the value in the <teamName> tag.

            Returns: String - The value of the <teamName> tag or empty string if not found
        """
        return(self.getElementFromTree('teamName'))

    def getUri(self):
        """
            Get the value in the <uri> tag.

            Returns: String - The value of the <uri> tag or empty string if not found
        """
        return(self.getElementFromTree('uri'))

    def getURLPrefix(self, api):
        """
            Build the prefix URL for the Finesse REST APIs using the scheme,
            fqdn, port, and username (as id) from the config file.

            Parameters:
                api (str): API Type (e.g. User, Dialog, Queue, Team, etc.)

            Returns: String - The URL built with the scheme, FQDN, port, API type and id
        """
        url = self.scheme + "://" + self.fqdn + ":"+ self.port + "/finesse/api/" + api
        if self.username:
            url += "/" + self.username
        print ("REST API URL is: '%s'" % url)
        return(url)

    def getUser(self, id):
        """
            Get the User object. Call the GET User REST API and store the
            XML response in the User object.

            Parameters:
                id (str): The ID of the user

            Returns: User object - The User object representation of the user with the given id.
        """
        print("GET User - ID: " + id)
        url = self.getURLPrefix(api="User")
        response = GET(url=url, username=self.username, password=self.password)

        self.userTree = ElementTree.fromstring(response.text)
        return(self)

    def getDialogs(self):
        return()

    def waitForNotification(self):
        """
            Wait method to sleep for 2 seconds to receive the
            Finesse notification.
        """
        time.sleep(2) # Wait for the Finesse Notification

    def signIn(self, extension):
        """
            Call the 'User — Sign In to Finesse' REST API with
            the provided extension. The username and password
            comes from the config file.

            Wait for the Finesse notification to be received
            before proceeding.

            **Note** This code does not process the event
            that gets sent as a result of the sign in.

            Parameters:
                extension (str): The extension of the user
        """
        signInXml = """
        <User>
            <state>LOGIN</state>
            <extension>""" + extension + """</extension>
        </User>"""
        url = self.getURLPrefix(api="User")
        PUT(url=url, username=self.username, password=self.password, data=signInXml)
        self.waitForNotification()

    def changeStateWithReasonCode(self, state, reasonCodeId=''):
        """
            Call the 'User — Change Agent State' REST API with
            the provided state. If a reasonCodeId is provided,
            it will be sent with the change state request.

            Wait for the Finesse notification to be received
            before proceeding.

            **Note** This code does not process the event
            that gets sent as a result of the change state.

            Parameters:
                state (str): The state to change the agent to
                reasonCodeId (str, optional): The reason code id
        """
        changeStateXml = """
        <User>
            <state>""" + state + """</state>""";
        if reasonCodeId:
            changeStateXml += """
            <reasonCodeId>""" + reasonCodeId + """</reasonCodeId>"""
        changeStateXml += """
        </User>"""
        url = self.getURLPrefix(api="User")
        PUT(url=url, username=self.username, password=self.password, data=changeStateXml)
        self.waitForNotification()

    def changeState(self, state):
        """
            Call the 'User — Change Agent State' REST API with
            the provided state.

            Wait for the Finesse notification to be received
            before proceeding.

            **Note** This code does not process the event
            that gets sent as a result of the change state.

            Parameters:
                state (str): The state to change the agent to
        """
        self.changeStateWithReasonCode(state=state)

    def signOut(self):
        """
            Call the 'User — Change Agent State' REST API with
            the state as LOGOUT. This also disconnects the
            XMPP connection.

            Wait for the Finesse notification to be received
            before proceeding.

            **Note** This code does not process the event
            that gets sent as a result of the change state.
        """
        self.changeStateWithReasonCode(state='LOGOUT')
        self.xmppConnection.session_end()

class Jabber(ClientXMPP):
    """
        The XMPP connection to the Finesse Notification Service.
        This class uses the SleekXMPP library (http://sleekxmpp.com/index.html)
    """

    def __init__(self, username, password, domain=''):
        """
            Initializes the Jabber object with the jid, username
            and password. Also, register the necessary handlers
            that is needed to receive the Finesse notifications
        """
        jid = "%s@%s" % (username, domain)
        ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.session_start, threaded=True)
        self.register_handler(
          Callback('Finesse Event',
            StanzaPath('{%s}message/{http://jabber.org/protocol/pubsub#event}event' % (self.default_ns)),
            self.receive_message))
        register_stanza_plugin(Message, Event)

    def session_start(self, event):
        """
            The XMPP connection is established so
            send the presence information.
        """
        self.send_presence()
        roster = self.get_roster()

    def receive_message(self, message):
        """
            The user received a message. Parse the
            <Update></Update> XML data out of the message
            and print it to the console.

            **Note** The XMPP connection/events is not tied into
            the User object so the events that are received does
            not update the stored XML response. This would be
            an enhancement to the script
        """
        print(message)
        if message['event']:
            event = message['event']

            try:
                event.getUserEvent()
            except:
                traceback.print_exc()

    def session_end(self):
        """
            Disconnect the XMPP connection
        """
        self.disconnect()


class Update(ElementBase):
    """
        The Update class is used for the Jabber class.
        This represents the <Update> XML in the XMPP
        message as part of the Finesse notification.
    """
    namespace = 'http://jabber.org/protocol/pubsub'
    name = 'Update'
    plugin_attrib = 'Update'

class Notification(ElementBase):
    """
        The Notification class is used for the Jabber class.
        This represents the <notification> XML in the XMPP
        message as part of the Finesse notification.
    """
    namespace = 'http://jabber.org/protocol/pubsub'
    name = 'notification'
    plugin_attrib = 'notification'
    interfaces = set(('Update'))
    subitem = (Update,)

class Item(ElementBase):
    """
        The Item class is used for the Jabber class.
        This represents the <item> XML in the XMPP
        message as part of the Finesse notification.
    """
    namespace = 'http://jabber.org/protocol/pubsub#event'
    name = 'item'
    plugin_attrib = 'item'
    interfaces = set(('id', 'notification'))
    subitem = (Notification,)

class Items(ElementBase):
    """
        The Items class is used for the Jabber class.
        This represents the <items> XML in the XMPP
        message as part of the Finesse notification.
    """
    namespace = 'http://jabber.org/protocol/pubsub#event'
    name = 'items'
    plugin_attrib = 'items'
    interfaces = set(('node', 'item'))
    subitem = (Item,)

class Event(ElementBase):
    """
        The Event class is used for the Jabber class.
        This represents the <event> XML in the XMPP
        message as part of the Finesse notification.
    """
    namespace = 'http://jabber.org/protocol/pubsub#event'
    name = 'event'
    plugin_attrib = 'event'
    interfaces = set(('items'))
    subitem = (Items,)

    def decodeNotification(self):
        """
            Decode the escaped characters (&lt; and &gt;)
            in order to convert it to an ElementTree
        """
        self.xml = self.__str__()
        self.xml = self.xml.replace("&lt;", "<")
        self.xml = self.xml.replace("&gt;", ">")
        print("Finesse Notification: " + self.xml)

    def getUserEvent(self):
        """
            Get the <user> notification from the XMPP
            event.
        """
        self.decodeNotification()
        root = ElementTree.fromstring(self.xml)
        updateElement = root.find((".//{%s}user") % (Update.namespace))


if __name__ == '__main__':

    #=========================================================================================
    # Step 1
    # Change Finesse FQDN and domain to the one you are using
    fqdn = "[FINESSE_FQDN]"
    domain = "[FINESSE_DOMAIN]"

    # Step 2
    # Change the Finesse REST API scheme (http or https) and the port (8080, 8082, 8443, 8445)
    scheme = "http"
    port = "8082"

    # Step 3
    # Change user1 & user2's Finesse user credentials
    user1_username = "[FINESSE_USER1_USERNAME]"
    user1_password = "[FINESSE_USER1_PASSWORD]"
    user1_extension = "[FINESSE_USER1_EXTENSION]"

    user2_username = "[FINESSE_USER2_USERNAME]"
    user2_password = "[FINESSE_USER2_PASSWORD]"
    user2_extension = "[FINESSE_USER2_EXTENSION]"
    #=========================================================================================

    # Instantiate user1 and user2
    user1 = User(username=user1_username, password=user1_password, scheme=scheme, fqdn=fqdn, port=port, domain=domain)
    user2 = User(username=user2_username, password=user2_password, scheme=scheme, fqdn=fqdn, port=port, domain=domain)

    # Sign both users in (establish XMPP connection)
    user1.signIn(extension=user1_extension)
    user2.signIn(extension=user2_extension)

    # Change user1's state to READY then back to NOT_READY
    user1.changeState(state='READY')
    user1.changeState(state='NOT_READY')

    # Sign both users out
    user2.signOut()
    user1.signOut()
