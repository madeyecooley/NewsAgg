def print_item(item):
    print "TITLE: %s" % item.get('Title')
    print "URLS: %s" % item.get('URL')
    print "SUMMARY: %s" % item.get('Summary')
    print "IMG URL: %s" % item.get('Photo')
    print "IMG CAPTION: %s" % item.get('Credit_Caption')
    print "ARTICLE SITE: %s" % item.get('Site')