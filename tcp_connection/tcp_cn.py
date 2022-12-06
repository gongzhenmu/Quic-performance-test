from urllib.request import urlopen 
import json
import time
import datetime
import argparse
import ssl

def main(args):

    targets = [
    'www.google.com',
    'www.facebook.com',
    'www.yahoo.com',
    'www.wikipedia.org',
    'www.amazon.com',
    'www.bing.com',
    'www.twitter.com',
    'www.reddit.com',
    'www.linkedin.com',
    'www.ebay.com',
    'www.instagram.com',
    'www.craigslist.org',
    'www.tumblr.com',
    'www.paypal.com',
    'www.cnn.com',
    'www.nytimes.com',
    'www.imbd.com',
    'www.espn.com',
    'www.office.com',
    'www.dropbox.com',
    'www.purdue.edu',]

    urls =[ "http://" + args.addr+f"/data/{args.task[0]}/{target}/index.html" for target in targets]
    print(urls)
    time_dict = {}
    for target in targets:
        time_dict[target] = []
        for i in range(args.iteration):
            start_time = time.time()
            url = "http://" + args.addr+f"/data/{args.task[0]}/{target}/index.html"
            html = urlopen(url)
            a= html.read()
            duration = time.time() - start_time
            time_dict[target].append(duration)
            # print(f"{args.task} iterations:{i} {target} duration:{duration:.2f}")
    with open(args.path, 'w') as f:
        for target, durations in time_dict.items():
            f.write('$'+target)
            f.write("\n")
            for duration in durations:
                f.write(str(duration))
                f.write("\n")

            


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tcp connection test')
    parser.add_argument('--addr',type=str, default='0.0.0.0:8888', help='target ip')
    parser.add_argument('--task','-t',choices=['html','video'], nargs=1, default='html', help='task type: [html, video]')
    parser.add_argument('--iteration','-i',type=int, default=10, help='how many times the experiment will be repeated')
    parser.add_argument('--verbose','-v',action='store_true', help='verbose mode')
    parser.add_argument('--path',type=str, default='./tcp_output.txt', help='path to save the results')
    args = parser.parse_args()
    main(args)
  
