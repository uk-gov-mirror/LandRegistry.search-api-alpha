from flask.ext.restful import Resource, fields, marshal_with, reqparse, abort

from searchapi.server import app, es

def get_hits(raw_result):
    hits = raw_result.get('hits')
    return hits.get('hits')

def get_item(raw_result):
    return raw_result.get("_source")

class PublicTitleResource(Resource):

    # no marshaller, because the feeder already took out the sensitive fields.
    def get(self, title_number):
        app.logger.info("Search for title number %s" % title_number)
        raw_result = es.search(index="public_titles", body={
            "query": {
            "match": {"title_number": title_number}
            }
        })
        hits = get_hits(raw_result)
        if hits:
            title = get_item(hits[0])
            app.logger.info('Found title %s' % title)
            return title
        else:
            abort(404)


class AuthenticatedTitleResource(Resource):

    # no marshaller, because the feeder already gave us the data as we need it.
    def get(self, title_number):
        app.logger.info("Search for title number %s" % title_number)
        raw_result = es.search(index="authenticated_titles", body={
            "query": {
            "match": {"title_number": title_number}
            }
        })
        hits = get_hits(raw_result)
        if hits:
            title = get_item(hits[0])
            app.logger.info('Found title %s' % title)
            return title
        else:
            abort(404, message="Title number %s not found" % title_number )