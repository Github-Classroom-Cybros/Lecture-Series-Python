#!/usr/bin/env python

import urllib2
import lxml.html
import argparse
import sys

def check_arg(args=None):
	parser = argparse.ArgumentParser(description='Script to get Price and Rating of a product on amazon.in . Run the script with \'-p <ASINid>\' to get the dealprice, saleprice and rating of a product. To know more about ASIN https://www.amazon.com/gp/help/customer/display.html?nodeId=200202190')
	parser.add_argument('-p', '--product', help='ASIN id of product', default='B00KGZZ824')
	results = parser.parse_args(args)
	return (results.product)


def get_data(html):
	tree = lxml.html.fromstring(html)
	XPATH_TITLE = '//*[@id="productTitle"]/text()'
	XPATH_PRICE = '//*[@id="priceblock_ourprice"]/text()'
	XPATH_DEALPRICE = '//*[@id="priceblock_dealprice"]/text()'
	XPATH_RATING = './/i[@data-hook="average-star-rating"]//text()'
	price = tree.xpath(XPATH_PRICE)
	dealprice = tree.xpath(XPATH_DEALPRICE)
	title = tree.xpath(XPATH_TITLE)
	rating  = tree.xpath(XPATH_RATING)
	product = {"title":title[0].strip(), "price": price[0].strip(), "rating":rating[0].strip()}
	if dealprice:
		product["dealprice"] = dealprice[0].strip()
	else:
		product["dealprice"] = "No deal"
	return product

def main():
	asin = check_arg(sys.argv[1:])
	url = 'http://www.amazon.in/dp/'
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	url = url + asin
	request = urllib2.Request(url, headers=headers)
	print "Downloading page: ", url
	try:
		html = urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print 'Error: ', e.reason
		html = None
		sys.exit(1)
	product = get_data(html)
	print "Title:", product['title']
	print "Price:", product['price']
	print "DealPrice:", product['dealprice']
	print "Rating:", product['rating']

if __name__ == '__main__':
	main()
