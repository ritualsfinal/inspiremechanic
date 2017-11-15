import pydblite

from pydblite import Base

_local_db = Base('inspire.pdl')  #The Local Entity Database
_local_db.create('name',mode='override')
#change .create() mode to 'open' after testing
# 'override' provides fresh dbs for testing

db = _local_db
