package main
import (
	"fmt"
	"io/ioutil"
	"net/http"
	"context"
	"log"
    "go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"go.mongodb.org/mongo-driver/bson"
	"time"
	// "runtime"
	"github.com/EDDYCJY/fake-useragent"
)

var ctx = context.Background() 		// create a new context
var SchoolScoreLinkColl *mongo.Collection 		// create a new collection

// connect database
func db_connect() {
	ctx, _ := context.WithTimeout(context.Background(), 10*time.Second)
	client, err := mongo.Connect(ctx, options.Client().ApplyURI("mongodb://localhost:27017"))  // change the URI when you need
	if err != nil {
		log.Fatal(err)
	}
	// check connection
	ctx, _ = context.WithTimeout(context.Background(), 2*time.Second)
	if err = client.Ping(ctx, nil); err != nil {
		log.Fatal(err)
	}
    	//example coll
	SchoolScoreLinkColl = client.Database("db_gaokao").Collection("school_score_link_data")
}




type EolLink struct {
	ID    string `bson:"_id"`
	Link string `bson:"link"`
	CheckAt  time.Time  `bson:"check_at"`
}

// models
func FindManyLinks(filter bson.M) ([]EolLink, error) {

	findOptions := options.Find()
	// findOptions.SetSort(bson.D{{"check_at", -1}})
	// findOptions.SetLimit(10000)

	cursor, err := SchoolScoreLinkColl.Find(ctx, filter, findOptions)
	if err != nil {
		return nil, err
	}
	// iterate through all documents
	var res []EolLink
	for cursor.Next(ctx) {
		// fmt.Println(cursor)
		var p EolLink
		// decode the document into given type
		if err := cursor.Decode(&p); err != nil {
			// fmt.Println(p.Link)
			return nil, err
		}
		// fmt.Println(p.Link)
		res = append(res, p)
	}
	return res, nil
}
func UpdateOneLink(filter bson.M, update bson.M) (*mongo.UpdateResult, error) {
	res, err := SchoolScoreLinkColl.UpdateOne(ctx, filter, update)
	// fmt.Println(update)
	return res, err
}




func schoolScoreLink(inChEolLink chan EolLink){
	
	

	filterFindMany := bson.M{}
	if res, err := FindManyLinks(filterFindMany); err != nil {
		fmt.Println(err)
	}else{
		for i :=0; i<=len(res)-1; i++ {
			// fmt.Println(res[i].ID)
			// fmt.Println(res[i].Link)
			// fmt.Println(res[i].CheckAt)

			elem := res[i]
			inChEolLink <-elem
			// fmt.Println(elem.Link) 
			
		}
	}
	
	
}



func schoolScoreFetch(inChEolLink chan EolLink){
	for {
		eolLink := <- inChEolLink
		url := eolLink.Link

		// fmt.Printf("fetch lind: %s\n", url)
		
		client := &http.Client{}
		req, _ := http.NewRequest("GET", url, nil)

		// 自定义Header
		req.Header.Set("User-Agent", browser.Random())
		resp, err := client.Do(req)
		if err != nil {
			fmt.Println("http get error", err)
			return
		}
		//函数结束后关闭相关链接
		defer resp.Body.Close()
		body, err := ioutil.ReadAll(resp.Body)
		if err != nil {
			fmt.Println("read error", err)
			return
		}
		fmt.Printf("fetch link: %s\n", url)
		responseData := string(body)


		


		if responseData == "\"\""{
			responseData = "none"
		} 

		// update one user
		now := time.Now()
		current_local, err_local := time.LoadLocation("Asia/Chongqing")//服务器设置的时区
		if err_local != nil {
			fmt.Println(err_local)
		}
	

		filter := bson.M{"link": url}
		update := bson.M{"$set": bson.M{"responseData": responseData, "check_at": now.In(current_local)},}


	
		if res, err := UpdateOneLink(filter, update); err != nil {
			fmt.Println(err)
			return
		}else {
			fmt.Printf("save data count: %d\n", res.ModifiedCount)
		}
	}


}





func schoolScore(){

	db_connect()

	// 初始化channels
	var inChEolLink = make(chan EolLink, 300)

	

	go schoolScoreFetch(inChEolLink)
	schoolScoreLink(inChEolLink)
	defer close(inChEolLink)
}


func main() {
	fmt.Println("Hello, world")
	// for {
	// 	schoolScore()
	// 	time.Sleep(time.Duration(2)*time.Second)
	// }

	schoolScore()


	

}




