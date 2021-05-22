import scrapy
import dateparser as dt
from ..items import StockscraperItem


class BitcoinDailySpider(scrapy.Spider):
    name = "btcusd-daily"
    start_urls = ["https://uk.investing.com/crypto/bitcoin/historical-data"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pages = response.xpath(".//tbody/tr")
        for p in pages:
            info = p.xpath(".//td/text()").getall()
            date = info[0]
            date = dt.parse(date_string=date, settings={"DATE_ORDER": "DMY"}).strftime(
                "%Y-%m-%d"
            )
            current_price = (info[1]).replace(",", "")
            high_price = (info[3]).replace(",", "")
            low_price = (info[4]).replace(",", "")
            volume = (info[5]).replace(".", "")
            volume = volume.replace("K", "000")
            volume = volume.replace(",", "")

            item = StockscraperItem(
                low_price=float(low_price),
                high_price=float(high_price),
                date=date,
                volume=float(volume),
                current_price=float(current_price),
            )
            yield item
