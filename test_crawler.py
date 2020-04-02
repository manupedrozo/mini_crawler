from mini_crawler import MiniCrawler

OUTPUT_FOLDER = "../data/test"
TERMS = ["covid", "coronavirus", "covid-19", "#covid-19", "#coronavirus"]

def test_constructor():
    crawler = MiniCrawler(config_path="../config/config.json", output_folder=OUTPUT_FOLDER)
    print(crawler.output_folder)

def test_crawler():
    crawler = MiniCrawler(config_path="../config/config.json", output_folder=OUTPUT_FOLDER)
    result = crawler.search_by_terms(TERMS, 10, output_to_file=True)
    #print(result)
    n = 1
    for tweet in result:
        print("Tweet {} :".format(n))
        print(tweet["full_text"])
        print("\n")
        n += 1

def test_config():
    config_path = "../config/config.json"
    config = None
    with open(os.path.abspath(config_path), 'r') as config_f:
        config = json.load(config_f)
    apikeys = list(config['apikeys'].values()).pop()
    print(apikeys)

#test_config("../config/config.json")
test_crawler()
#test_constructor()
