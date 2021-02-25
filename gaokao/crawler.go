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
)



// 下载网页
func download(url string) {
	client := &http.Client{}
	req, _ := http.NewRequest("GET", url, nil)
	// 自定义Header
	req.Header.Set("User-Agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)")
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
	fmt.Println(string(body))
}



 
type Link struct {
	ID    string `bson:"_id"`
	Link string `bson:"link"`
	CheckAt  time.Time  `bson:"check_at"`
}



// 定义 mongodb 数据库连接 url 常量
const MONGODB_URL = "mongodb://localhost:27017"
func main() {
	fmt.Println("Hello, world")
	// url := "http://www.baidu.com/"
	// url := "https://static-data.eol.cn/www/2.0/schoolprovinceindex/detial/102/52/1/1.json"
	// download(url)

	//连接数据库
	// Set client options
	clientOptions := options.Client().ApplyURI("mongodb://localhost:27017")
	// Connect to MongoDB
	client, err := mongo.Connect(context.TODO(), clientOptions)
	if err != nil {
		log.Fatal(err)
	}
	// Check the connection
	err = client.Ping(context.TODO(), nil)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Connected to MongoDB!")




	// 查询数据
	collection := client.Database("db_gaokao").Collection("school_score_link_data")
	// Pass these options to the Find method
	findOptions := options.Find()
	findOptions.SetLimit(10)
	// Here's an array in which you can store the decoded documents
	var results []*Link
	// Passing bson.D{{}} as the filter matches all documents in the collection
	cur, err := collection.Find(context.TODO(), bson.D{{}}, findOptions)
	if err != nil {
		log.Fatal(err)
	}

	// Finding multiple documents returns a cursor
	// Iterating through the cursor allows us to decode documents one at a time
	for cur.Next(context.TODO()) {
		// create a value into which the single document can be decoded
		var elem Link
		err := cur.Decode(&elem)
		if err != nil {
			log.Fatal(err)
		}

		results = append(results, &elem)
	}

	if err := cur.Err(); err != nil {
		log.Fatal(err)
	}

	// Close the cursor once finished
	cur.Close(context.TODO())

	// fmt.Printf("Found multiple documents (array of pointers): %+v\n", results)

	for i :=0; i<=len(results)-1; i++ {
		fmt.Println(results[i].ID)
		fmt.Println(results[i].Link)
		fmt.Println(results[i].CheckAt)
	}


	// 关闭连接
	err = client.Disconnect(context.TODO())

	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Connection to MongoDB closed.")
	




}




