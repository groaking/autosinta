# This file is executed first for the AutoSINTA GUI application
# REFERENCES:
#  [1] Viewing the UI script created using QtDesigner:
#    -> https://www.pythonguis.com/tutorials/first-steps-qt-creator/
#  [2] PyQt5 event listener:
#    -> https://www.techwithtim.net/tutorials/pyqt5-tutorial/buttons-and-events
#  [3] KActionSelector is cumbersome:
#    -> https://stackoverflow.com/questions/12591456
#  [4] You need to execute 'self.exec_()' to show a QDialog:
#    -> https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QDialog.html#code-examples
#  [5] QLineEdit API documentation:
#    -> https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QLineEdit.html
#  [6] QPlainTextEdit API documentation:
#    -> https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QPlainTextEdit.html
#  [7] GUI freezing? Use "QtCore.QCoreApplication.processEvents()":
#    -> https://www.xingyulei.com/post/qt-threading/index.html
#  [8] Pivotting a dict into a list
#    -> https://stackoverflow.com/a/37489445
#  [9] Sorting a list of dicts by a certain key
#    -> https://stackoverflow.com/a/73050
# [10] To move an item from a QListWidget, clone it!
#    -> https://stackoverflow.com/a/68229287
# [11] Listing the list of items in a QListWidget
#    -> https://stackoverflow.com/a/22572524

from datetime import datetime as dt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import QRunnable, Qt, QThreadPool
import sys
import time

# Importing the UI python scripts
from ui_exported import about_about
from ui_exported import about_changelog
from ui_exported import about_license
from ui_exported import credential_match
from ui_exported import credential_unmatch
from ui_exported import exportauthor_failed
from ui_exported import exportauthor_loaded
from ui_exported import help_howto
from ui_exported import help_troubleshooting
from ui_exported import main_gui
from ui_exported import sync_failed
from ui_exported import sync_selection
from ui_exported import sync_successful

# Importing the SINTA API
import api

class DialogAboutAbout(QtWidgets.QDialog, about_about.Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(DialogAboutAbout, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Must be executed last
        self.exec()

class DialogAboutChangelog(QtWidgets.QDialog, about_changelog.Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(DialogAboutChangelog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Must be executed last
        self.exec()

class DialogAboutLicense(QtWidgets.QDialog, about_license.Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(DialogAboutLicense, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Must be executed last
        self.exec()

class DialogExportAuthorFailed(QtWidgets.QDialog, exportauthor_failed.Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(DialogExportAuthorFailed, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Must be executed last
        self.exec()

class DialogExportAuthorLoaded(QtWidgets.QDialog, exportauthor_loaded.Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(DialogExportAuthorLoaded, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Must be executed last
        self.exec()

class DialogHelpHowto(QtWidgets.QDialog, help_howto.Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(DialogHelpHowto, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Must be executed last
        self.exec()

class DialogHelpTroubleshooting(QtWidgets.QDialog, help_troubleshooting.Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(DialogHelpTroubleshooting, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Must be executed last
        self.exec()

class DialogLoginMatch(QtWidgets.QDialog, credential_match.Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(DialogLoginMatch, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Must be executed last
        self.exec()

class DialogLoginUnmatch(QtWidgets.QDialog, credential_unmatch.Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(DialogLoginUnmatch, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Must be executed last
        self.exec()
        
class DialogSync(QtWidgets.QDialog, sync_selection.Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(DialogSync, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Set event listener
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_move_left.clicked.connect(self.btn_move_left_clicked)
        self.btn_move_right.clicked.connect(self.btn_move_right_clicked)
        self.btn_sync.clicked.connect(self.btn_sync_clicked)
        self.radio_sync_all.clicked.connect(self.radio_sync_all_clicked)
        self.radio_sync_some.clicked.connect(self.radio_sync_some_clicked)
    
    def btn_cancel_clicked(self):
        self.close()
    
    def btn_move_left_clicked(self):
        # Moving items selected from the right list to the left list
        for a in self.list_authors_right.selectedItems():
            # Clone the selected item, then move it to the other list
            b = a.clone()
            self.list_authors_left.addItem(b)
            
            # Get the index of the selected item, then remove the item from the list
            i = self.list_authors_right.indexFromItem(a).row()
            self.list_authors_right.takeItem(i)
        
        # Finally, sort the destination QListWidget
        self.list_authors_left.sortItems(Qt.AscendingOrder)
    
    def btn_move_right_clicked(self):
        # Moving items selected from the left list to the right list
        for a in self.list_authors_left.selectedItems():
            # Clone the selected item, then move it to the other list
            b = a.clone()
            self.list_authors_right.addItem(b)
            
            # Get the index of the selected item, then remove the item from the list
            i = self.list_authors_left.indexFromItem(a).row()
            self.list_authors_left.takeItem(i)
        
        # Finally, sort the destination QListWidget
        self.list_authors_right.sortItems(Qt.AscendingOrder)
    
    def btn_sync_clicked(self):
        # Referencing the list of authors
        a = self.api.author_list
        # Read the option the user selected
        o = self.radio_sync_all.isChecked()
        if o:
            # Sync all authors
            self.api.sync_list = a
        else:
            # Resetting the list of the sync data
            self.api.reset_sync_list()
            
            # Listing the list of items in the right QListWidget
            # SOURCE: https://stackoverflow.com/a/22572524
            items = []
            for x in range( self.list_authors_right.count() ):
                items.append( self.list_authors_right.item(x) )
            
            # Sync some authors per user's selection
            # First we read the user's selection from the right list widget
            for b in items:
                
                # Read the back-end information about the item's index
                i = int( b.toolTip().split('DATA INDEX:')[1] )
                
                # Listing of dict keys
                keys = [ c[0] for c in self.api.sync_list.items() ]
                
                # Construct the list of authors to sync
                for l in keys:
                    self.api.sync_list[l].append(a[l][i])
        
        # DEBUG
        # Please comment-out after use.
        # ---
        # print(self.api.sync_list)
        
        # Close the dialog
        self.close()
        
        # Perform the synchronization process
        sync_result = self.api.sync(self.o, self.p)
        
        # Checking the sync result
        if sync_result == True:
            self.o('Synchronization complete and successful.')
            DialogSyncSuccess().show()
        else:
            self.o('Cannot continue syncing. Please check your internet connection.')
            DialogSyncFail().show()
    
    def radio_sync_all_clicked(self):
        self.btn_move_left.setEnabled(False)
        self.btn_move_right.setEnabled(False)
        self.frame_authors.setEnabled(False)
        self.list_authors_left.setEnabled(False)
        self.list_authors_right.setEnabled(False)
    
    def radio_sync_some_clicked(self):
        self.btn_move_left.setEnabled(True)
        self.btn_move_right.setEnabled(True)
        self.frame_authors.setEnabled(True)
        self.list_authors_left.setEnabled(True)
        self.list_authors_right.setEnabled(True)
    
    def set_burden(self, api=object, o=object, p=object):
        '''
        Param. api --> the SINTA API object
        Param. o   --> the output QPlainTextEdit message element
        Param. p   --> the QProgressBar progress bar element
        '''
        
        # Make the QPlainTextEdit, QProgressBar, and the SINTA API
        # accessible to other functions in this class
        self.api = api
        self.o = o
        self.p = p
    
    def update_author_list(self):
        ''' If this function is called before set_burden(), it will err '''
        
        # Pivotting the author data dict
        # SOURCE: https://stackoverflow.com/a/37489445
        a = self.api.author_list
        b = [ dict( zip(a, col) ) for col in zip( *a.values() ) ]
        
        # Sorting the SINTA author data by the author name's alphabetical order
        # SOURCE: https://stackoverflow.com/a/73050
        b = sorted(b, key=lambda z: z['name'])
        
        # Enlisting the SINTA author data into the QListWidget element
        for c in b:
            # Creating a new list item of QListWidgetItem type
            item = QtWidgets.QListWidgetItem(c['name'])
            # Creating a tooltip text, carrying back-end information
            tooltip_text = f'SINTA ID: { str(c["sid"]) } - DATA INDEX: { str(c["id"]) }'
            item.setToolTip(tooltip_text)
            # Appending to the QListWidget element
            self.list_authors_left.addItem(item)

class DialogSyncFail(QtWidgets.QDialog, sync_failed.Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(DialogSyncFail, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Must be executed last
        self.exec()

class DialogSyncSuccess(QtWidgets.QDialog, sync_successful.Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(DialogSyncSuccess, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        # Must be executed last
        self.exec()

class WindowMain(QtWidgets.QMainWindow, main_gui.Ui_MainWindow):
    '''
    SINTA API is solely controlled and accessed in this class.
    This class controls the main GUI as well as the sync operations.
    '''
    
    def __init__(self, *args, obj=None, **kwargs):
        super(WindowMain, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.o('Loading graphical user interface ...')
        
        # Set event listener
        self.action_about.triggered.connect(self.action_about_clicked)
        self.action_changelog.triggered.connect(self.action_changelog_clicked)
        self.action_howto.triggered.connect(self.action_howto_clicked)
        self.action_license.triggered.connect(self.action_license_clicked)
        self.action_quit.triggered.connect(self.action_quit_clicked)
        self.action_troubleshooting.triggered.connect(self.action_troubleshooting_clicked)
        self.btn_exportauthor.clicked.connect(self.btn_exportauthor_clicked)
        self.btn_login.clicked.connect(self.btn_login_clicked)
        self.btn_sync.clicked.connect(self.btn_sync_clicked)
        
        # Initializing the API
        self.o('Initializing the SINTA API ...')
        self.api = api.SintaAPI()
    
    def action_about_clicked(self):
        DialogAboutAbout().show()
    
    def action_changelog_clicked(self):
        DialogAboutChangelog().show()
    
    def action_license_clicked(self):
        DialogAboutLicense().show()
    
    def action_howto_clicked(self):
        DialogHelpHowto().show()
    
    def action_troubleshooting_clicked(self):
        DialogHelpTroubleshooting().show()
    
    def action_quit_clicked(self):
        self.o('Closing the app ...')
        self.close()
    
    def btn_exportauthor_clicked(self):
        self.o('Downloading SINTA author data ...')
        r = self.api.get_author_list()
        
        if type(r) == dict:
            self.o('Author list has been updated successfully!')
            DialogExportAuthorLoaded().show()
        elif not r:
            self.o('Failed to retrieve author list.')
            DialogExportAuthorFailed().show()
        else:
            self.o('Failed to retrieve author list.')
            DialogExportAuthorFailed().show()
    
    def btn_login_clicked(self):
        # Obtaining and setting the login credentials
        u = self.input_avuser.text()
        p = self.input_avpass.text()
        self.api.set_credentials(u, p)
        
        # Attempting to do the login
        self.o(f'Attempting to login user [{u}] ...')
        r = self.api.connect()
        
        # Determining the responses
        if r == True:
            self.o(f'Login successful!')
            DialogLoginMatch().show()
        else:
            self.o(f'Login failed!')
            DialogLoginUnmatch().show()
    
    def btn_sync_clicked(self):
        # Pass the option of the kinds of publication to sync
        self.api.set_publications(
            scopus = self.select_scopus.isChecked(),
            wos = self.select_wos.isChecked(),
            garuda = self.select_garuda.isChecked(),
            gs = self.select_gs.isChecked(),
        )
        
        # Initialize the sync dialog object
        obj = DialogSync()
        
        # Load the "burden" of the synchronization processes
        obj.set_burden(
            api = self.api,
            o = self.o,
            p = self.p
        )
        
        # Load the list of authors
        obj.update_author_list()
        
        # Finally, show the sync dialog
        obj.exec()
    
    def o(self, str_: str):
        '''
        "o" stands for "output message logging"
        Any string passed to the parameter "str_" will be logged to both
        the terminal and the application's message TextArea
        '''
        
        # Do the message logging
        print('::: [' + str(dt.now()) + '] + ' + str_)
        self.area_message.appendPlainText(str_)
        
        # Prevent freezing
        QtCore.QCoreApplication.processEvents()
    
    def p(self, int_: int):
        '''
        "p" stands for "progress bar"
        This function controls the value of the app's main progress bar.
        Useful during during synchronization.
        '''
        
        # Filter the input values
        if int_ > 100:
            int_ = 100
        elif int_ < 0:
            int_ = 0
        int_ = int(int_)  # --- redundant, but nevermind.
        
        # Update the progress bar's value
        self.progress_sync.setProperty("value", int_)
        
        # Prevent freezing
        QtCore.QCoreApplication.processEvents()

app = QtWidgets.QApplication(sys.argv)

window = WindowMain()
window.show()
app.exec()
