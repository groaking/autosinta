# This Python script is the XHR API to perform the SINTA synchronization requests
# REFERENCES:
# [1] Clearing the cookies of Python requests' session
#   -> https://stackoverflow.com/a/23816320
# [2] Downloading files using Python requests
#   -> https://www.geeksforgeeks.org/downloading-files-web-using-python

from lxml import html
import datetime
import openpyxl as xl
import requests
import tempfile as temp
import time

class SintaAPI(object):
    
    URL_EXPORT_AUTHOR = 'https://sinta.kemdikbud.go.id/authorverification/affiliations/exportauthors'
    URL_LOGIN = 'https://sinta.kemdikbud.go.id/authorverification'
    URL_SYNC = 'https://sinta.kemdikbud.go.id/authorverification/author/syncData'
    
    HANDLER_LOGIN = 'https://sinta.kemdikbud.go.id/authorverification/login/do_login'
    
    def __init__(self):
        # Initializing the class
        # Abstracting important and versatile variables
        self.author_list = { 'id': [], 'sid': [], 'name': [], 'url': [] }
        self.sync_list = { 'id': [], 'sid': [], 'name': [], 'url': [] }
        self.username = ''
        self.password = ''
        
        # Creating the Python requests object
        self.s = requests.Session()
    
    def connect(self):
        ''' Returns "True" if login was successful, "False" if otherwise. '''
        
        # Clearing the cookie
        self.s.cookies.clear()
        
        # Loading the login page
        self.s.get(self.URL_LOGIN)
        
        # Preparing the login data payload
        d = { 'username': self.username, 'password': self.password }
        
        # Connecting with the AV login page
        r = self.s.post(self.HANDLER_LOGIN, data=d)
        
        # Checking if an element which is only available in the dashboard
        # upon successful login is present in the HTML response
        try:
            h = html.fromstring(r.text)
            l = h.xpath('//span[@class="text-uppercase page-subtitle"]/text()')
            # If the element list of 'l' is not empty, then the dashboard is loaded
            if l == []:
                return False
            # The element must be entitled as "Dashboard" if the login was successful
            elif l[0] == 'Dashboard':
                return True
            else:
                return False
        except:
            return False
    
    def get_author_list(self):
        ''' Downloads the 'export_author.xlsx' file from SINTA and read the list of authors that can be synced '''
        
        try:
            # Downloading the excel file
            r = self.s.get(self.URL_EXPORT_AUTHOR)
            
            # Creating a temporary folder to save the downloaded excel file
            t = temp.mkdtemp()
            
            # Downloading and saving the excel file
            f = t + '/export_author.xlsx'
            with open(f, 'wb') as buffer:
                buffer.write(r.content)
            
            # Reading the excel file's sheet
            export_author = xl.open(f)['Export Authors']
            
            # Obtaining the required data columns
            # 'sid' stands for SINTA ID
            return_data = {
                'id': [],
                'sid': [l.value for l in export_author.__getitem__('B')[5:]],
                'name': [l.value for l in export_author.__getitem__('D')[5:]],
                'url': [],
            }
            
            # Filling the 'id' data (assuming every list has the same dimension)
            for l in return_data['sid']:
                return_data['id'].append( return_data['sid'].index(l) )
            
            # Creating the control URL data
            for l in return_data['sid']:
                return_data['url'].append('https://sinta.kemdikbud.go.id/authorverification/author/profile/' + str(l))
            
            # Saving the return data in this API's class object
            self.author_list = return_data
            
            # Return the data
            return return_data
        
        # Any arbitrary sort of errors will be caught here
        # We don't need to know what caused the error
        except:
            return False
    
    def reset_sync_list(self):
        ''' Resetting the list of authors to synchronize '''
        self.sync_list = { 'id': [], 'sid': [], 'name': [], 'url': [] }
    
    def set_credentials(self, user_, pass_):
        # Altering the SINTA author verificator login credential
        self.username = user_
        self.password = pass_
    
    def set_publications(self, scopus=False, wos=False, garuda=False, gs=False):
        ''' Determines which publication types of the authors to sync '''
        
        self.publications = {
            's' : scopus,
            'w' : wos,
            'g' : garuda,
            'gs': gs,
        }
    
    def sync(self, o, p):
        '''
        This object executes the synchronization process
        Requires three objects as arguments:
        - The main GUI's message output writer (o)
        - The main GUI's progress bar changer method (p)
        
        The list of authors and publication types to sync need to be
        pre-configured by modifying the class' internal variables.
        
        Returns:
        - True if the sync was successful
        - False if an error (any error) was returned
        '''
            
        # Reset the previous progress bar value
        p(0)
        
        # Iterating through every author enlisted to be synced
        # Assumes every sublist in "sync_list" has identical dimension (length "x")
        x = len(self.sync_list['id'])
        for i in range(x):
            # Truncating the lenghty variable name
            sync_list = self.sync_list
            
            # Preamble logging (front-end)
            o(f'Syncing { str(sync_list["name"][i]) } in progress ...')
            
            # Preamble logging (back-end)
            print(f'CONTROL_URL: { str(sync_list["url"][i]) }')
            
            # Begin syncronizing: Scopus
            if self.publications['s']:
                try:
                    # Syncing the publication
                    self.s.get(f'{self.URL_SYNC}/{str(sync_list["sid"][i])}?redirect={self.URL_LOGIN}&act=scopusSync')
                    # Redundantly wait for a tenth second to avoid conflicts
                    # This assumes the internet connection speed is fairly slow
                    time.sleep(0.05)
                    # Reporting
                    o('+ Scopus synchronization successful!')
                except:
                    # Some error was detected (usually connection reset) and the sync process was disturbed
                    o('Some unknown error was detected! Please check your internet connection.')
                    return False
            
            # Begin syncronizing: WOS
            if self.publications['w']:
                try:
                    # Syncing the publication
                    self.s.get(f'{self.URL_SYNC}/{str(sync_list["sid"][i])}?redirect={self.URL_LOGIN}&act=wosSync')
                    # Redundantly wait for a tenth second to avoid conflicts
                    # This assumes the internet connection speed is fairly slow
                    time.sleep(0.05)
                    # Reporting
                    o('+ Web of Science (WOS) synchronization successful!')
                except:
                    # Some error was detected (usually connection reset) and the sync process was disturbed
                    o('Some unknown error was detected! Please check your internet connection.')
                    return False
            
            # Begin syncronizing: Garuda
            if self.publications['g']:
                try:
                    # Syncing the publication
                    self.s.get(f'{self.URL_SYNC}/{str(sync_list["sid"][i])}?redirect={self.URL_LOGIN}&act=garudaSync')
                    # Redundantly wait for a tenth second to avoid conflicts
                    # This assumes the internet connection speed is fairly slow
                    time.sleep(0.05)
                    # Reporting
                    o('+ Garuda synchronization successful!')
                except:
                    # Some error was detected (usually connection reset) and the sync process was disturbed
                    o('Some unknown error was detected! Please check your internet connection.')
                    return False
            
            # Begin syncronizing: Google Scholar
            if self.publications['gs']:
                try:
                    # Syncing the publication
                    self.s.get(f'{self.URL_SYNC}/{str(sync_list["sid"][i])}?redirect={self.URL_LOGIN}&act=googleSync')
                    # Redundantly wait for a tenth second to avoid conflicts
                    # This assumes the internet connection speed is fairly slow
                    time.sleep(0.05)
                    # Reporting
                    o('+ Google Scholar synchronization successful!')
                except:
                    # Some error was detected (usually connection reset) and the sync process was disturbed
                    o('Some unknown error was detected! Please check your internet connection.')
                    return False
            
            # Deal with the progress bar progression
            current_percentage = round( ( (i+1)/x) * 100 )
            p(current_percentage)
            
        return True
