# datadog-googlepagespeed
**Datadog custom check for collecting Google PageSpeed Insights score.**

This custom check allows you to retrieve Google PageSpeed Insights score from the PageSpeed Insights API and send it as a regular metric to Datadog.

- Support for multiple urls
- Allows for custom tagging for each url

## Installation
In order for the integration to work you must get a Server API key and enable PageSpeed Insights API. 
If you are ready with this, go directly to Step 3: Installing the check.

### Step 1 : Get a service account and API key
1. Create a project
  1. Go to [https://console.developers.google.com](https://console.developers.google.com)
  2. Upper right > Select a project
  3. Create a project or select an existing one
2. PageSpeed Insights API
  1. In the left menu "API Manager", go to Overview
  2. In the search box type "pagespeed"
  3. Click on PageSpeed Insights API
  4. Enable
3. Create Access Credentials
  1. In the left menu "API Manager", go to Credentials
  2. Create credential > API key
  3. Select "Server key"
  5. When done, **take note of the key**

### Step 3: Install the check (Finally!)
> This steps are based on Ubuntu Linux.

1. Clone or download from [https://github.com/aleksandrpanteleymonov/datadog-googlepagespeed](https://github.com/aleksandrpanteleymonov/datadog-googlepagespeed)
2. Install the check:
  1. Copy pagespeed.yaml to `/etc/dd-agent/conf.d/`
  2. Copy pagespeed.py to /`etc/dd-agent/checks.d/`
  3. Put the Google Api server key to `pagespeed.yaml`
3. Configure by adding urls to check
<pre>
init_config:
  min_collection_interval: 3600 # once an hour
  google_api_key: XXXXXXXXXXXXX-YYYYYYYYYYYYYYY

instances:
  - url: http://example.com/
    tags:
      - env:production
      - page:home
  - url: https://example.com/product_X/
    tags:
      - env:production
      - page:product
</pre>

## Done!

> Check that everything went right: `/etc/init.d/datadog-agent check pagespeed`.

* Restart the agent: `/etc/init.d/datadog-agent restart`.


##References
- [PageSpeed API: Pagespeedapi: runpagespeed](https://developers.google.com/speed/docs/insights/v2/reference/pagespeedapi/runpagespeed)
- [Datadog - Writing an Agent Check](http://docs.datadoghq.com/guides/agent_checks/)


##Licence
The code is licensed under the MIT License.
