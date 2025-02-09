import scrapy

class FilmsSpider(scrapy.Spider):
    name = "films"
    i = 0
    def start_requests(self):
        url = "https://ru.wikipedia.org/wiki/Категория:Фильмы_по_алфавиту"
        yield scrapy.Request(url=url, callback=self.response_parser)

    def response_parser(self, response):
        for film in response.css("div#mw-pages ul li a"):
            title = film.css("::text").get()
            film_url = film.css("::attr(href)").get()
            if film_url:
                print("ССЫЛКА для фильма", film_url)
                yield response.follow(film_url, callback=self.parse_film_details, meta={"title": title})  

        # Второй вариант: next_page_link = response.xpath('//div[@class="mw-category-generated"]//a[contains(text(), "Следующая страница")]/@href').get()
        next_page_link = response.css('div.mw-category-generated a:contains("Следующая страница")::attr(href)').get()
        if next_page_link:
            yield response.follow(next_page_link, callback=self.response_parser)
    
    def parse_film_details(self, response):
        title = response.meta["title"]

        genre = response.xpath('//th[contains(., "Жанр") or contains(., "Жанры")]/following-sibling::td')
        if genre:
            genre = genre.xpath('string()').get().strip()

        director = response.xpath('//th[contains(., "Режиссёр")]/following-sibling::td')
        if director:
            director = director.xpath('string()').get().strip()

        country = response.xpath('//th[contains(., "Страна") or contains(., "Страны")]/following-sibling::td')
        if country:
            country = country.xpath('string()').get().strip()

        year = response.xpath('//th[contains(., "Год") or contains(., "Дата выхода")]/following-sibling::td')
        if year:
            year = year.xpath('string()').get().strip()

        yield {
            "title": title,
            "genre": genre if genre else None,
            "director": director if director else None,
            "country": country if country else None,
            "year": year if year else None, 
            
        }
   