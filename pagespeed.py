"""
Google PageSpeed Insights check

Author: Oleksandr Panteleimonov

2016-08-17
- URLs to check can be controlled via yaml file

"""
from checks import AgentCheck, CheckException
import httplib2
import time
import json


class GooglePageSpeedCheck(AgentCheck):
    def __init__(self, *args, **kwargs):
        AgentCheck.__init__(self, *args, **kwargs)
        self.google_api_key = self.init_config.get('google_api_key')

    def check(self, instance):
        url = instance.get('url')
        instance_tags = instance.get('tags')
        ts = time.time()
        h = httplib2.Http(timeout=10)

        for strategy in ['desktop', 'mobile']:
            tags = ["strategy:" + strategy] + instance_tags
            self.log.info('PageSpeed url: %s, tags: %s' % (url, tags))

            pagespeedurl = 'https://www.googleapis.com/pagespeedonline/v2/runPagespeed?url=%s&strategy=%s&key=%s' % (
                url, strategy, self.google_api_key
            )
            resp, content = h.request(pagespeedurl)
            obj = json.loads(content)
            score = obj['ruleGroups']['SPEED']['score']

            self.gauge("googlepagespeed.score",
                       score,
                       tags,
                       None,
                       None,
                       ts
                       )

            self.log.info("PageSpeed speed score for strategy '%s': %s" % (strategy, score))
