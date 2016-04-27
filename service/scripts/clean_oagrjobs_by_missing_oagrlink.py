from octopus.modules.oag.dao import JobsDAO
from service import models

oagrjobs_raw = JobsDAO.query('*', size=100000)
if oagrjobs_raw['hits']['total'] > 0:
    oagrjobs = [JobsDAO(o['_source']) for o in oagrjobs_raw['hits']['hits']]
    for oagrjob in oagrjobs:
        oagrlink = models.OAGRLink.by_oagr_id(oagrjob.id)
        if not oagrlink:
            print 'Deleting oagrjob {0}, no matching oagrlink records'.format(oagrjob.id)
            oagrjob.delete()
else:
    print 'No oagrjobs found in index, stopping.'
