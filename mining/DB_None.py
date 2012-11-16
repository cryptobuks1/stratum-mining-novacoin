import stratum.logger
log = stratum.logger.get_logger('None')
                
class DB_None():
    def __init__(self):
	log.debug("Connecting to DB")

    def updateStats(self,averageOverTime):
	log.debug("Updating Stats")

    def import_shares(self,data):
	log.debug("Importing Shares")

    def found_block(self,data):
	log.debug("Found Block")

    def delete_user(self,username):
	log.debug("Deleting Username")

    def insert_user(self,username,password):
	log.debug("Adding Username/Password")

    def update_user(self,username,password):
	log.debug("Updating Username/Password")

    def check_password(self,username,password):
	log.debug("Checking Username/Password")
	return True

    def check_tables(self):
	log.debug("Checking Tables")
	
