from urllib.request import urlopen ,urlretrieve
import json
import time
import datetime
import argparse
import ssl

def main(args):

    htmls = [
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

    videos = [
        "test0.5.mp4",
        "test3.mp4",
        "test5.mp4",
        "test11.mp4",
        "test12.mp4",
        "test20.mp4",
        "test36.mp4",
        "test66.mp4",
    ]
    time_dict = {}
    if args.task[0] == 'html':
        targets = htmls
    else:
        targets = videos
    for target in targets:
        time_dict[target] = []
        for i in range(args.iteration):
            start_time = time.time()
            if args.task[0] == "html":
                url = "http://" + args.addr+f"/data/{args.task[0]}/{target}/index.html"
                html = urlopen(url)     
                h = html.read()
            else:
                url = "http://" + args.addr+f"/data/{args.task[0]}/{target}"
                v = urlretrieve(url, f'{target}') 

            duration = time.time() - start_time
            time_dict[target].append(duration)
            print(f"{args.task} iterations:{i} {target} duration:{duration:.4f}")
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
  
