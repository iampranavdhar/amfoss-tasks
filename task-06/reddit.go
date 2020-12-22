package main

import (
	"context"
	"fmt"
	"log"
	"github.com/vartanbeno/go-reddit/reddit"
)

var ctx = context.Background()

func main() {
	if err := run(); err != nil {
		log.Fatal(err)
	}
}

func run() (err error) {
	withCredentials := reddit.WithCredentials("ID", "Secret", "Username", "Password")
    client, _ := reddit.NewClient(withCredentials)
	if err != nil {
		return
	}

	sr, _, err := reddit.DefaultClient().Subreddit.Get(ctx, "memes")
	fmt.Printf("%s was created on %s and has %d subscribers.\n", sr.NamePrefixed, sr.Created.Local(), sr.Subscribers)
	posts, _, err := reddit.DefaultClient().Subreddit.TopPosts(ctx, "memes", &reddit.ListPostOptions{
		ListOptions: reddit.ListOptions{
			Limit: 100,
		},
		Time: "week",
	})
	if err != nil {
		return
	}

	for _, post := range posts {
		fmt.Println(post.Title)
		_, err := client.Post.Upvote(context.Background(), "t3_"+post.ID)
		if err != nil {
    		fmt.Println("Error in the process of upvoting")
		}
	}
	return
}
