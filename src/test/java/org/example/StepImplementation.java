package org.example;

import com.thoughtworks.gauge.Step;
import io.restassured.path.xml.XmlPath;
import io.restassured.specification.RequestSpecification;

import okhttp3.*;
import org.apache.commons.io.FileUtils;
import org.junit.jupiter.api.Assertions;
import org.junit.platform.engine.support.hierarchical.Node;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.w3c.dom.NodeList;
import org.w3c.dom.Element;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.time.LocalDate;
import java.util.*;
import java.util.concurrent.TimeUnit;

import static io.restassured.RestAssured.given;
//import static org.openqa.selenium.logging.LogEntry.DATE_FORMAT;


public class StepImplementation {

    StringBuilder sb=null;
    Response response;
    Request request=null;
    RequestSpecification httpRequest= given();
    OkHttpClient client=null;
    HashMap<String, Object> hashMap = new HashMap<String, Object>();
    HashMap<String, String> headers = new HashMap<>();

    private Logger logger = LoggerFactory.getLogger(getClass());


    @Step("xml olustur")
    public void xml(){
        sb=new StringBuilder();
    }

    @Step("<element> elementini xml'e ekle")
    public void xmlAddElement(String element){
        sb.append(element);
        System.out.println(element+" elementi xml'e eklendi");
    }

    @Step("<element> elementini <param> parametresiyle xml'e ekle")
    public void xmlAddElementParam(String element,String param){
        sb.append("<" + element + ">" + param + "</" + element + ">" );
        System.out.println(element+" elementi "+param+" parametresi ile xml'e eklendi");
    }

    @Step("<element> elementini hashmap'deki <param> key ile xml'e ekle")
    public void xmlAddElementHashmapToXml(String element,String param){
        sb.append("<" + element + ">" + hashMap.get(param).toString() + "</" + element + ">");
        System.out.println(element+" elementi "+param+" hashmapden xml'e eklendi");
    }

    @Step("<key> keyli <value> degeri hashmap'e ekle")
    public void addHashmapManuel(String key, String value)
    {
        hashMap.put(key, value);
        System.out.println(key + " keyli " + value + " degeri manuel olarak hashmap'e eklendi");
    }

    @Step("<url> servisine istek at bypasserror")
    public void sendRequestBypassError(String url) throws Exception {
        int maxRetries = 3;
        int retryCount = 0;
        boolean success = false;
        boolean hasError = false; // New variable to track if there's an error in the response
        String errorPart = null;

        while (!success && retryCount < maxRetries) {
            try {
                client = new OkHttpClient().newBuilder()
                        .connectTimeout(30, TimeUnit.SECONDS)
                        .readTimeout(100, TimeUnit.SECONDS)
                        .build();
                MediaType mediaType = MediaType.parse("text/xml;charset=UTF-8;");
                RequestBody body = RequestBody.create(mediaType, hashMap.get("data").toString());
                request = new Request.Builder()
                        .url(url)
                        .method("POST", body)
                        .headers(Headers.of(headers))
                        .build();
                response = client.newCall(request).execute();
                String responseBody = response.peekBody(Long.MAX_VALUE).string();

                // Print request body, response, and status code
                System.out.println("RequestBody: " + hashMap.get("data").toString());
                System.out.println("Response: " + response.peekBody(Long.MAX_VALUE).string());
                System.out.println("Status Code: " + response.code());

                System.out.println("-------------------------------------------------------");
            } catch (IOException e) {
                System.out.println("Request failed. Retrying...");
                retryCount++;
            }
        }
    }
    @Step("<url> servisine istek at")
    public void sendRequest(String url) throws Exception {
        int maxRetries = 3;
        int retryCount = 0;
        boolean success = false;
        boolean hasError = false; // New variable to track if there's an error in the response
        String errorPart = null;
        long startTime = System.currentTimeMillis(); // Capture the start time before making the request


        while (!success && retryCount < maxRetries) {
            try {
                client = new OkHttpClient().newBuilder()
                        .connectTimeout(30, TimeUnit.SECONDS)
                        .readTimeout(100, TimeUnit.SECONDS)
                        .build();
                MediaType mediaType = MediaType.parse("text/xml;charset=UTF-8;");
                RequestBody body = RequestBody.create(mediaType, hashMap.get("data").toString());
                request = new Request.Builder()
                        .url(url)
                        .method("POST", body)
                        .headers(Headers.of(headers))
                        .build();
                response = client.newCall(request).execute();
                String responseBody = response.peekBody(Long.MAX_VALUE).string();

                // Print request body, response, and status code
                System.out.println("RequestBody: " + hashMap.get("data").toString());
                System.out.println("Response: " + response.peekBody(Long.MAX_VALUE).string());
                System.out.println("Status Code: " + response.code());

                System.out.println("-------------------------------------------------------");
                if (responseBody.toLowerCase().contains("error")) {
                    System.out.println("Error found in the response.");
                    hasError = true; // Set hasError to true if an error is found
                    int startIndex = responseBody.indexOf("<ns2:Errors>");
                    int endIndex = responseBody.indexOf("</ns2:Error>", startIndex) + "</ns2:Error>".length();
                    if (startIndex >= 0 && endIndex >= 0) {
                        errorPart = responseBody.substring(startIndex, endIndex);
                        System.out.println("Error Part: " + errorPart);
                    }
                    // Extract and print the error part

                    break; // Exit the loop immediately
                } else {
                    success = true; // Request succeeded, exit the loop
                }
            } catch (IOException e) {
                System.out.println("Request failed. Retrying...");
                retryCount++;
            }
        }
            long endTime = System.currentTimeMillis(); // Capture the end time after receiving the response
            double responseTimeInSeconds = (endTime - startTime) / 1000.0; // Calculate response time in seconds
            System.out.println("Response Time: " + responseTimeInSeconds + " seconds");

        // If there's an error in the response, don't proceed further
        if (hasError) {
            throw new Exception("Error found in the response: " + errorPart);

        }
    }

    @Step("test <text>")
    public void test(String text) throws IOException {
        File textFile = new File("src/main/resources/" + text + ".text");
        String data = FileUtils.readFileToString(textFile);

        hashMap.put("data", data);
        System.out.println("data : " + data);


    }
    @Step("<url> servisine istek at reissue")
    public void sendRequestReissue(String url) throws Exception {
        client = new OkHttpClient().newBuilder()
                .connectTimeout(5, TimeUnit.SECONDS)
                .readTimeout(50, TimeUnit.SECONDS)
                .build();
        MediaType mediaType = MediaType.parse("text/xml;charset=UTF-8;");
        RequestBody body = RequestBody.create(mediaType, hashMap.get("data").toString());
        request = new Request.Builder()
                .url(url)
                .method("POST", body)
                .headers(Headers.of(headers))
                .build();
        response = client.newCall(request).execute();
        System.out.println("RequestBody: "+hashMap.get("data").toString());
        System.out.println("Response: "+response.peekBody(Long.MAX_VALUE).string());
        System.out.println("Status Code:" + response.code());

        System.out.println("-------------------------------------------------------");
    }
    @Step("log")
    public void log() throws Exception {
        System.out.println("_________________________________________________________________________" + "\r\n");
    }


    @Step("Hashmapin icindeki <hashmapKey> keyinin degeri <hashmapKey2> keyinin degeri ile <type> mı kontrol et")
    public void checkDifferenceHashmap(String hashmapKey, String hashmapKey1, String type)
    {
        if ("aynı".equals(type))
        {
            Assertions.assertEquals(hashMap.get(hashmapKey).toString(), hashMap.get(hashmapKey1).toString(), "hashmapteki degerler eslesiyor...");
            System.out.println(hashMap.get(hashmapKey).toString()+" , "+ hashMap.get(hashmapKey1).toString() + " ile " + type + "mi kontrol edildi");
        }
        else if ("farklı".equals(type))
        {
            Assertions.assertNotEquals(hashMap.get(hashmapKey).toString(), hashMap.get(hashmapKey1).toString(), "hashmapteki degerler eslesmiyor...");
            System.out.println(hashMap.get(hashmapKey).toString()+" , "+ hashMap.get(hashmapKey1).toString() + " ile " + type + " mi kontrol edildi");
        }
        else
        {
            Assertions.fail("Lütfen Gecerli bir tip giriniz");
        }
    }

    @Step("xml <yol> xpathinindeki elementi <element> keyiyle hashmape ekle")
    public void xpath(String yol,String element) throws IOException {
        ResponseBody responseBodyCopy = response.peekBody(Long.MAX_VALUE);
        XmlPath path = XmlPath.from(responseBodyCopy.string());
       // Bu olur çünkü .string()yalnızca bir kez çağrılabilir
        path.getList(yol).forEach(o-> hashMap.put(element,o.toString()));
        System.out.println(element + " hashmape eklendi : " +hashMap.get(element));
    }

    @Step("Seat status f olan ilk koltugun degerleri <element1> <element2> ve <element3> keyiyle hashmape ekle")
    public void addSeatStatusToHashMap(String element1, String element2, String element3) throws IOException {
        ResponseBody responseBodyCopy = response.peekBody(Long.MAX_VALUE);
        XmlPath path = XmlPath.from(responseBodyCopy.string());
        int i = 0;
        while (true) {

            // Xpath'i oluştur ve SeatStatus değerini al
            String xpath = "Envelope.Body.SeatAvailabilityRS.SeatMap.Cabin.Row["+i+"].Seat[0].SeatStatus";
            String seatStatus = path.get(xpath);

            if (seatStatus.equals("F")) {
                // Eğer SeatStatus F ise, istediğimiz koltuğu bulduk
                String element4 = path.get("Envelope.Body.SeatAvailabilityRS.SeatMap.Cabin.Row["+i+"].Number");
                String element5 = path.get("Envelope.Body.SeatAvailabilityRS.SeatMap.Cabin.Row["+i+"].Seat[0].Column");
                String element6 = path.get("Envelope.Body.SeatAvailabilityRS.SeatMap.Cabin.Row["+i+"].Seat[0].OfferItemRefs");
                hashMap.put(element1, element4);
                System.out.println(element1 + " hashmape eklendi :" + element4);
                hashMap.put(element2, element5);
                System.out.println(element2 + " hashmape eklendi :" + element5);
                hashMap.put(element3, element6);
                System.out.println(element3 + " hashmape eklendi :" + element6);
                break;
            } else {
                // Eğer SeatStatus F değilse, bir sonraki koltuğu kontrol etmek için number değerini artır
                i++;
            }
        }
    }


    @Step("hashmapteki <offerId> offerId ve <responseId> responseId elementlerini xml'e ekle")
    public void xmlAddElementHashmapToOffer(String offerId,String responseId){
        sb.append("<Offer OfferID="+ hashMap.get(offerId).toString() + "Owner=\"PC\" ResponseID=" +  hashMap.get(offerId).toString() + ">");
        System.out.println("OfferID: "+hashMap.get(offerId).toString()+" ve"+" ResponseID: "+ hashMap.get(responseId).toString()+" hashmapten xml'e eklendi");
    }


    @Step("<key> key <value> value degerini headera ekle")
    public void addHeader(String key, String value)
    {
        headers.put(key,value);
        System.out.println("Header'a " +key+ "," +value+ " degeri eklendi");
    }


    @Step("<text> requesti olustur")
    public void requestCreate(String text){
        try {
            File myObj = new File("src/main/resources/"+text+".text");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                hashMap.put("data",data);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    @Step("xml <yol> xpathinindeki elementi <value> degeriyle karsilastir")
    public void xpathResponseKarsilastir(String yol,String value) throws IOException {
        StringBuilder gelenEleman = new StringBuilder();
        ResponseBody responseBodyCopy = response.peekBody(Long.MAX_VALUE);
        XmlPath path = XmlPath.from(responseBodyCopy.string());
        // Bu olur çünkü .string()yalnızca bir kez çağrılabilir
        path.getList(yol).forEach(o-> gelenEleman.append(o.toString()));

        System.out.println("Gelen Eleman: "+gelenEleman);

        Assertions.assertEquals(value,gelenEleman.toString(),"Degerler eslesmiyor!..");
        System.out.println(value +" degeri " + gelenEleman.toString() + " ile ayni mi kontrol edildi....");
    }

    @Step("xml <yol> xpathinindeki elementi hashmapteki <key> keyli deger ile karsilastir")
    public void xmlHashmapKarsilastir(String yol,String key) throws IOException {
        StringBuilder gelenEleman = new StringBuilder();
        ResponseBody responseBodyCopy = response.peekBody(Long.MAX_VALUE);
        XmlPath path = XmlPath.from(responseBodyCopy.string());
        // Bu olur çünkü .string()yalnızca bir kez çağrılabilir
        path.getList(yol).forEach(o-> gelenEleman.append(o.toString()));

        System.out.println("Gelen Eleman: "+gelenEleman);

        Assertions.assertEquals(hashMap.get(key),gelenEleman.toString(),"Degerler eslesmiyor!..");
        System.out.println(hashMap.get(key) +" hashmapden gelen degeri " + gelenEleman + " ile ayni mi kontrol edildi....");
    }
    @Step("<text> xmlinde <yol> xpathinindeki elementi headerdaki <key> keyli deger ile karsilastir")
    public void xmlHeaderKarsilastir(String text, String yol, String key) throws IOException {
        StringBuilder xmlEleman = new StringBuilder();
        File textFile = new File("src/main/resources/"+text+".text");
        String data = FileUtils.readFileToString(textFile, StandardCharsets.UTF_8);

        XmlPath path =XmlPath.from(data);

        path.getList(yol).forEach(o-> xmlEleman.append(o.toString()));

        System.out.println("xml Eleman: " + xmlEleman);

        Assertions.assertEquals(headers.get(key),xmlEleman.toString(),"Degerler eslesmiyor!..");
        System.out.println(headers.get(key) +" headersdan gelen deger " + xmlEleman + " ile ayni mi kontrol edildi....");

    }

    private static final String DATE_FORMAT = "yyyy-MM-dd";
    private static final long THREE_DAY_MILLI_SECONDS = 72 * 60 * 60 * 1000;
    @Step("<text> requestine <tagfirst> yerine <datanewfirst> <tagsecond> yerine <datanewsecond> ve <date> olarak <nextday> gün ileri tarih yazilir")
    public void changesmth_one(String text,String tagfirst, String datanewfirst, String tagsecond, String datanewsecond,String date, String nextday) throws IOException {
        File textFile = new File("src/main/resources/"+text+".text");
        String data = FileUtils.readFileToString(textFile);
        //String data = hashMap.toString();

        LocalDate localDate = LocalDate.now();
        //System.out.println("Bugünün tarihi : " + localDate);

        localDate = localDate.plusDays(Long.parseLong(nextday));
        String nextdate = String.valueOf(localDate);
        //System.out.println(nextday + " gün eklendi : " + nextdate);
        hashMap.put("port1", datanewfirst);
        System.out.println("port1" + " hashmape eklendi :" + datanewfirst);
        hashMap.put("port2", datanewsecond);
        System.out.println("port2" + " hashmape eklendi :" + datanewsecond);

        data = data.replace(tagfirst,datanewfirst);
        hashMap.put("data", data);
        //System.out.println(data);
        data = data.replace(tagsecond,datanewsecond);
        hashMap.put("data", data);
       // System.out.println(data);
        data = data.replace(date, nextdate);
        hashMap.put("data", data);
        System.out.println(data);
    }
    @Step("<text> requestine <tagfirst> yerine <datanewfirst> <tagsecond> yerine <datanewsecond> ve <date> olarak <nextday> gün ileri tarih yazilir ve <oldData1> yerine hashmapdeki <data1> ve <oldData2> yerine <data2> degerlerini ekle")
    public void changesmth_one(String text,String tagfirst, String datanewfirst, String tagsecond, String datanewsecond,String date, String nextday, String oldData1, String data1,String oldData2, String data2) throws IOException {
        File textFile = new File("src/main/resources/"+text+".text");

        try {
            String data = FileUtils.readFileToString(textFile);
            //String data = hashMap.toString();

            LocalDate localDate = LocalDate.now();
            //System.out.println("Bugünün tarihi : " + localDate);

            localDate = localDate.plusDays(Long.parseLong(nextday));
            String nextdate = String.valueOf(localDate);


            //System.out.println(nextday + " gün eklendi : " + nextdate);
            data = data.replace(tagfirst,datanewfirst);
            hashMap.put("data", data);
            //System.out.println(data);
            data = data.replace(tagsecond,datanewsecond);
            hashMap.put("data", data);
            // System.out.println(data);
            data = data.replace(date, nextdate);
            hashMap.put("data", data);
            data = data.replace(oldData1,hashMap.get(data1).toString());
            data = data.replace(oldData2,hashMap.get(data2).toString());
            hashMap.put("data",data);
            System.out.println("data : " +data);
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }
    @Step("<text> requestine <tagfirst> yerine <datanewfirst> <tagsecond> yerine <datanewsecond> ve <date> olarak <nextday> gün ileri tarih yazilir ve <oldData1> yerine hashmapdeki <data1> <oldData2> yerine <data2> ve <oldData3> yerine <data3> degerlerini ekle")
    public void changesmth_one(String text,String tagfirst, String datanewfirst, String tagsecond, String datanewsecond,String date, String nextday, String oldData1, String data1,String oldData2, String data2, String oldData3, String data3) throws IOException {
        File textFile = new File("src/main/resources/"+text+".text");

        try {
            String data = FileUtils.readFileToString(textFile);
            //String data = hashMap.toString();

            LocalDate localDate = LocalDate.now();
            //System.out.println("Bugünün tarihi : " + localDate);

            localDate = localDate.plusDays(Long.parseLong(nextday));
            String nextdate = String.valueOf(localDate);


            //System.out.println(nextday + " gün eklendi : " + nextdate);
            data = data.replace(tagfirst,datanewfirst);
            hashMap.put("data", data);
            //System.out.println(data);
            data = data.replace(tagsecond,datanewsecond);
            hashMap.put("data", data);
            // System.out.println(data);
            data = data.replace(date, nextdate);
            hashMap.put("data", data);
            data = data.replace(oldData1,hashMap.get(data1).toString());
            data = data.replace(oldData2,hashMap.get(data2).toString());
            data = data.replace(oldData3,hashMap.get(data3).toString());
            hashMap.put("data",data);
            System.out.println("data : " +data);
        }
        catch (IOException e) {
            e.printStackTrace();
        }


    }
    @Step("<text> requestine <tagfirst> yerine <datanewfirst> <tagsecond> yerine <datanewsecond> <oldData1> yerine hashmapdeki <data1> ve <oldData2> yerine <data2> degerlerini ekle")
    public void changeForOpenTicket(String text,String tagfirst, String datanewfirst, String tagsecond, String datanewsecond, String oldData1, String data1,String oldData2, String data2) throws IOException {
        File textFile = new File("src/main/resources/"+text+".text");

        try {
            String data = FileUtils.readFileToString(textFile);



            //System.out.println(nextday + " gün eklendi : " + nextdate);
            data = data.replace(tagfirst,datanewfirst);
            hashMap.put("data", data);
            //System.out.println(data);
            data = data.replace(tagsecond,datanewsecond);
            hashMap.put("data", data);
            // System.out.println(data);
            data = data.replace(oldData1,hashMap.get(data1).toString());
            data = data.replace(oldData2,hashMap.get(data2).toString());
            hashMap.put("data",data);
            System.out.println("data : " +data);
        }
        catch (IOException e) {
            e.printStackTrace();
        }


    }
    @Step("<text> requestine <tagfirst> yerine <datanewfirst> <tagsecond> yerine <datanewsecond> <oldData1> yerine hashmapdeki <data1> <oldData2> yerine <data2> ve <oldData3> yerine <data3> degerlerini ekle")
    public void changeForOpenTicketCiftSegment(String text,String tagfirst, String datanewfirst, String tagsecond, String datanewsecond, String oldData1, String data1,String oldData2, String data2, String oldData3, String data3) throws IOException {
        File textFile = new File("src/main/resources/"+text+".text");

        try {
            String data = FileUtils.readFileToString(textFile);



            //System.out.println(nextday + " gün eklendi : " + nextdate);
            data = data.replace(tagfirst,datanewfirst);
            hashMap.put("data", data);
            //System.out.println(data);
            data = data.replace(tagsecond,datanewsecond);
            hashMap.put("data", data);
            // System.out.println(data);
            data = data.replace(oldData1,hashMap.get(data1).toString());
            data = data.replace(oldData2,hashMap.get(data2).toString());
            data = data.replace(oldData3,hashMap.get(data3).toString());

            hashMap.put("data",data);
            System.out.println("data : " +data);
        }
        catch (IOException e) {
            e.printStackTrace();
        }


    }
    @Step("<text> requestine <tagfirst> yerine <datanewfirst> <tagsecond> yerine <datanewsecond> ve <datefirst> olarak <nextdayfirst> gün ileri tarih, <tagthird> yerine <datanewthird> <tagfourth> yerine <datanewfourt> ve <datedecond> olarak <nextdaysecond> gün ileri tarih  yazilir")
    public void gidisdonus(String text,String tagfirst, String datanewfirst, String tagsecond, String datanewsecond, String datefirst, String nextdayfirst, String tagthird, String datanewthird, String tagfourth, String datanewfourt, String datedecond, String nextdaysecond) throws IOException {
        File textFile = new File("src/main/resources/"+text+".text");
        String data = FileUtils.readFileToString(textFile);
        //String data = hashMap.toString();

        LocalDate localDate = LocalDate.now();
        //System.out.println("Bugünün tarihi : " + localDate);

        localDate = localDate.plusDays(Long.parseLong(nextdayfirst));
        String nextdate = String.valueOf(localDate);
        //System.out.println(nextday + " gün eklendi : " + nextdate);

        localDate = localDate.plusDays(Long.parseLong(nextdaysecond));
        String nextdate_2 = String.valueOf(localDate);

        hashMap.put("port1", datanewfirst);
        System.out.println("port1" + " hashmape eklendi :" + datanewfirst);
        hashMap.put("port2", datanewsecond);
        System.out.println("port2" + " hashmape eklendi :" + datanewsecond);
        hashMap.put("port3", datanewthird);
        System.out.println("port3" + " hashmape eklendi :" + datanewthird);
        hashMap.put("port4", datanewfourt);
        System.out.println("port4" + " hashmape eklendi :" + datanewfourt);

        data = data.replace(tagfirst,datanewfirst);
        hashMap.put("data", data);
        //System.out.println(data);
        data = data.replace(tagsecond,datanewsecond);
        hashMap.put("data", data);
        data = data.replace(tagthird,datanewthird);
        hashMap.put("data", data);
        data = data.replace(tagfourth,datanewfourt);
        hashMap.put("data", data);

        // System.out.println(data);
        data = data.replace("replaceDatefirst", nextdate);
        hashMap.put("data", data);
        data = data.replace("replaceDatesecond", nextdate_2);
        hashMap.put("data", data);
        System.out.println(data);

    }

    @Step("<text> requestine <oldData1> yerine hashmapdeki <data1> ve <oldData2> yerine <data2> degerlerini ekle")
    public void ƒchangesmth(String text,String oldData1, String data1,String oldData2, String data2) {
        File textFile = new File("src/main/resources/"+text+".text");
        try {
            // String data = FileUtils.readFileToString(textFile);
            String data = FileUtils.readFileToString(textFile, StandardCharsets.UTF_8);
            data = data.replace(oldData1,hashMap.get(data1).toString());
            data = data.replace(oldData2,hashMap.get(data2).toString());
            hashMap.put("data",data);
            System.out.println(data);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    private static final String dateformat = "yyyy-MM-dd";
    @Step("tarih <nextday> gun ileri olarak degistirilir")
    public void datedeneme(String nextday) {


        LocalDate localDate = LocalDate.now();
        System.out.println("Bugünün tarihi : " + localDate);

        localDate = localDate.plusDays(Long.parseLong(nextday));
        String deneme = String.valueOf(localDate);
        System.out.println(nextday + " gün eklendi : " + deneme);

    }



    @Step("Servis bazli sorgu gonderilir")
    public void multiplerequest() throws IOException {

        String[] urls = {"https://172.17.18.71:443/CraneNDC/CraneNDCService", "https://172.17.18.89:443/CraneNDC/CraneNDCService", "https://172.17.18.105:443/CraneNDC/CraneNDCService"};
        int i;
        String x;

        for (i = 0; i < urls.length; i++) {

            // accessing each element of array
            x = urls[i];
            System.out.print(x + " ");

            client = new OkHttpClient().newBuilder()
                    .build();
            MediaType mediaType = MediaType.parse("text/xml;charset=UTF-8;");
            RequestBody body = RequestBody.create(mediaType, hashMap.get("data").toString());
            request = new Request.Builder()
                    .url(x)
                    .method("POST", body)
                    .headers(Headers.of(headers))
                    .build();
            response = client.newCall(request).execute();
            System.out.println("RequestBody: "+hashMap.get("data").toString());
            System.out.println("Response: "+response.peekBody(Long.MAX_VALUE).string());
            System.out.println("Status Code:" + response.code());
            System.out.println("-------------------------------------------------------");


        }

    }
    @Step("<text> requestine <oldData1> yerine hashmapdeki <data1> <oldData2> yerine <data2> <oldData3> yerine <data3> ve <oldData4> yerine <data4> <oldData5> yerine <data5> <oldData6> yerine <data6> degerlerini ekle")
    public void changesixdata(String text,String oldData1, String data1,String oldData2, String data2,String oldData3, String data3,String oldData4, String data4,String oldData5, String data5,String oldData6, String data6) {
        File textFile = new File("src/main/resources/"+text+".text");
        try {
            // String data = FileUtils.readFileToString(textFile);
            String data = FileUtils.readFileToString(textFile, StandardCharsets.UTF_8);
            data = data.replace(oldData1,hashMap.get(data1).toString());
            data = data.replace(oldData2,hashMap.get(data2).toString());
            data = data.replace(oldData3,hashMap.get(data3).toString());
            data = data.replace(oldData4,hashMap.get(data4).toString());
            data = data.replace(oldData5,hashMap.get(data5).toString());
            data = data.replace(oldData6,hashMap.get(data6).toString());
            hashMap.put("data",data);
            System.out.println(data);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    @Step("<text> requestine <oldData1> yerine hashmapdeki <data1> <oldData2> yerine <data2> <oldData3> yerine <data3> ve <oldData4> yerine <data4> <oldData5> yerine <data5> <oldData6> yerine <data6> ve <oldData7> yerine <data7> ve <oldData8> yerine <data8> degerlerini ekle")
    public void changeeightdata(String text,String oldData1, String data1,String oldData2, String data2,String oldData3, String data3,String oldData4, String data4,String oldData5, String data5,String oldData6, String data6,String oldData7, String data7, String oldData8,String data8) {
        File textFile = new File("src/main/resources/"+text+".text");
        try {
            // String data = FileUtils.readFileToString(textFile);
            String data = FileUtils.readFileToString(textFile, StandardCharsets.UTF_8);
            data = data.replace(oldData1,hashMap.get(data1).toString());
            data = data.replace(oldData2,hashMap.get(data2).toString());
            data = data.replace(oldData3,hashMap.get(data3).toString());
            data = data.replace(oldData4,hashMap.get(data4).toString());
            data = data.replace(oldData5,hashMap.get(data5).toString());
            data = data.replace(oldData6,hashMap.get(data6).toString());
            data = data.replace(oldData7,hashMap.get(data7).toString());
            data = data.replace(oldData8,hashMap.get(data8).toString());
            hashMap.put("data",data);
            System.out.println(data);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    @Step("<text> requestine <oldData1> yerine hashmapdeki <data1> <oldData2> yerine <data2> <oldData3> yerine <data3> ve <oldData4> yerine <data4> <oldData5> yerine <data5> <oldData6> yerine <data6> ve <oldData7> yerine <data7> degerlerini ekle")
    public void changesevendata(String text,String oldData1, String data1,String oldData2, String data2,String oldData3, String data3,String oldData4, String data4,String oldData5, String data5,String oldData6, String data6,String oldData7, String data7) {
        File textFile = new File("src/main/resources/"+text+".text");
        try {
            // String data = FileUtils.readFileToString(textFile);
            String data = FileUtils.readFileToString(textFile, StandardCharsets.UTF_8);
            data = data.replace(oldData1,hashMap.get(data1).toString());
            data = data.replace(oldData2,hashMap.get(data2).toString());
            data = data.replace(oldData3,hashMap.get(data3).toString());
            data = data.replace(oldData4,hashMap.get(data4).toString());
            data = data.replace(oldData5,hashMap.get(data5).toString());
            data = data.replace(oldData6,hashMap.get(data6).toString());
            data = data.replace(oldData7,hashMap.get(data7).toString());
            hashMap.put("data",data);
            System.out.println(data);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Step("<text> requestine <oldData1> yerine hashmapdeki <data1> <oldData2> yerine <data2> ve <oldData3> yerine <data3> ve <oldData4> yerine <data4> degerlerini ekle")
    public void changeFourData(String text,String oldData1, String data1,String oldData2, String data2,String oldData3, String data3,String oldData4, String data4) {
        File textFile = new File("src/main/resources/"+text+".text");
        try {
            // String data = FileUtils.readFileToString(textFile);
            String data = FileUtils.readFileToString(textFile, StandardCharsets.UTF_8);
            data = data.replace(oldData1,hashMap.get(data1).toString());
            data = data.replace(oldData2,hashMap.get(data2).toString());
            data = data.replace(oldData3,hashMap.get(data3).toString());
            data = data.replace(oldData4,hashMap.get(data4).toString());
            hashMap.put("data",data);
            System.out.println(data);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    @Step("<text> requestine <oldData1> yerine hashmapteki <data1> <oldData2> yerine <data2> <oldData3> yerine <data3> <oldData4> yerine <data4> <oldData5> yerine <data5> degerlerini ekle")
    public void changeFourIfExist(String text,String oldData1, String data1,String oldData2, String data2,String oldData3, String data3,String oldData4, String data4, String oldData5, String data5) {
        File textFile = new File("src/main/resources/"+text+".text");
        try {
            // String data = FileUtils.readFileToString(textFile);
            String data = FileUtils.readFileToString(textFile, StandardCharsets.UTF_8);
            data = data.replace(oldData1,hashMap.get(data1).toString());
            String newPrice = hashMap.get(data2).toString();
            if ("0".equals(newPrice) || newPrice == null || newPrice.isEmpty()) {
                System.out.println("ByPassenger degeri = 0");
                // Handle the case when newPrice is null or 0
                // Remove the content between <Payments> ... </Payments> tags
                int startIndex = data.indexOf("<Payments>");
                int endIndex = data.indexOf("</Payments>") + "</Payments>".length();
                if (startIndex >= 0 && endIndex >= 0) {
                    data = data.substring(0, startIndex) + data.substring(endIndex);
                }
            } else {
                data = data.replace(oldData2, newPrice);
            }
//            if (hashMap.get(data2).toString() == null) {
//                data2 = hashMap.get("newPrice2").toString();
//            }
//            data = data.replace(oldData2,hashMap.get(data2).toString());
            data = data.replace(oldData3,hashMap.get(data3).toString());
            data = data.replace(oldData4,hashMap.get(data4).toString());
            data = data.replace(oldData5,hashMap.get(data5).toString());
            hashMap.put("data",data);
            System.out.println(data);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    @Step("<text> requestine <oldData1> yerine hashmapteki <data1> <oldData2> yerine <data2> <oldData3> yerine <data3> <oldData4> yerine <data4> <oldData5> yerine <data5> ve <oldData6> yerine <data6> degerlerini ekle")
    public void changeSixData(String text,String oldData1, String data1,String oldData2, String data2,String oldData3, String data3,String oldData4, String data4, String oldData5, String data5, String oldData6, String data6) {
        File textFile = new File("src/main/resources/"+text+".text");
        try {
            // String data = FileUtils.readFileToString(textFile);
            String data = FileUtils.readFileToString(textFile, StandardCharsets.UTF_8);
            data = data.replace(oldData1,hashMap.get(data1).toString());
            String newPrice = hashMap.get(data2).toString();
            if ("0".equals(newPrice) || newPrice == null || newPrice.isEmpty()) {
                System.out.println("ByPassenger degeri = 0");
                // Handle the case when newPrice is null or 0
                // Remove the content between <Payments> ... </Payments> tags
                int startIndex = data.indexOf("<Payments>");
                int endIndex = data.indexOf("</Payments>") + "</Payments>".length();
                if (startIndex >= 0 && endIndex >= 0) {
                    data = data.substring(0, startIndex) + data.substring(endIndex);
                }
            } else {
                data = data.replace(oldData2, newPrice);
            }
            data = data.replace(oldData2,hashMap.get(data2).toString());
            data = data.replace(oldData3,hashMap.get(data3).toString());
            data = data.replace(oldData4,hashMap.get(data4).toString());
            data = data.replace(oldData5,hashMap.get(data5).toString());
            data = data.replace(oldData6,hashMap.get(data6).toString());
            hashMap.put("data",data);
            System.out.println(data);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    @Step("<text> requestine <oldData1> yerine hashmapdeki <data1> <oldData2> yerine <data2> <oldData3> yerine <data3> <oldData4> yerine <data4> <oldData5> yerine <data5> degerlerini ekle")
    public void changeFiveData(String text,String oldData1, String data1,String oldData2, String data2,String oldData3, String data3,String oldData4, String data4, String oldData5, String data5) {
        File textFile = new File("src/main/resources/"+text+".text");
        try {
            // String data = FileUtils.readFileToString(textFile);
            String data = FileUtils.readFileToString(textFile, StandardCharsets.UTF_8);
            data = data.replace(oldData1,hashMap.get(data1).toString());
            String newPrice = hashMap.get(data2).toString();
            if ("0".equals(newPrice) || newPrice == null || newPrice.isEmpty()) {
                System.out.println("ByPassenger degeri = 0");
                // Handle the case when newPrice is null or 0
                // Remove the content between <Payments> ... </Payments> tags
                int startIndex = data.indexOf("<Payments>");
                int endIndex = data.indexOf("</Payments>") + "</Payments>".length();
                if (startIndex >= 0 && endIndex >= 0) {
                    data = data.substring(0, startIndex) + data.substring(endIndex);
                }
            } else {
                data = data.replace(oldData2, newPrice);
            }
            data = data.replace(oldData2,hashMap.get(data2).toString());
            data = data.replace(oldData3,hashMap.get(data3).toString());
            data = data.replace(oldData4,hashMap.get(data4).toString());
            data = data.replace(oldData5,hashMap.get(data5).toString());
            hashMap.put("data",data);
            System.out.println(data);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    @Step("<text> requestine <oldData1> yerine hashmapdeki <data1> <oldData2> yerine <data2> ve <oldData3> yerine <data3> degerlerini ekle")
    public void changethreedata(String text,String oldData1, String data1,String oldData2, String data2,String oldData3, String data3) {
        File textFile = new File("src/main/resources/"+text+".text");
        try {
            // String data = FileUtils.readFileToString(textFile);
            String data = FileUtils.readFileToString(textFile, StandardCharsets.UTF_8);
            data = data.replace(oldData1,hashMap.get(data1).toString());
            data = data.replace(oldData2,hashMap.get(data2).toString());
            data = data.replace(oldData3,hashMap.get(data3).toString());
            hashMap.put("data",data);
            System.out.println(data);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Step("Paketi <text> olan ilk gidis ucusunun Offer ID sini al")
    public void findOfferId(String text) throws IOException {
        ResponseBody responseBodyCopy = response.peekBody(Long.MAX_VALUE);
        XmlPath path = XmlPath.from(responseBodyCopy.string());

        for (int i = 0; i < 25; i++) {
            String xpath_FlightRef = "Envelope.Body.AirShoppingRS.OffersGroup.AirlineOffers.Offer[" + i + "].FlightsOverview.FlightRef.text()";
            String xpath_ServiceDefinitionRef = "Envelope.Body.AirShoppingRS.OffersGroup.AirlineOffers.Offer[" + i + "].OfferItem.Service[1].ServiceDefinitionRef.text()";
            //System.out.println(xpath_FlightRef);
            //System.out.println(xpath_ServiceDefinitionRef);
            String FlightRef = path.getString(xpath_FlightRef);
            //System.out.println(FlightRef);
            String ServiceDefinitionRef = path.getString(xpath_ServiceDefinitionRef);
            //System.out.println(ServiceDefinitionRef);

            if (FlightRef.contains(hashMap.get("port1").toString()+hashMap.get("port2").toString()) && ServiceDefinitionRef.contains(text)) {
                String xpath_offergidis = "Envelope.Body.AirShoppingRS.OffersGroup.AirlineOffers.Offer[" + i + "].@OfferID.text()";
                //System.out.println(xpath_offergidis);
                String offeridgidis = path.getString(xpath_offergidis);
                hashMap.put("offerId_gidis", offeridgidis);
                System.out.println("offer id gidis hashmape eklendi : " + hashMap.get("offerId_gidis"));
                break;
            }
        }
    }

    @Step("Paketi <text> olan ilk donus ucusunun Offer ID sini al")
    public void findOfferIdReturn(String text) throws IOException {
        ResponseBody responseBodyCopy = response.peekBody(Long.MAX_VALUE);
        XmlPath path = XmlPath.from(responseBodyCopy.string());

        for (int i = 0; i < 300; i++) {
            String xpath_FlightRef = "Envelope.Body.AirShoppingRS.OffersGroup.AirlineOffers.Offer[" + i + "].FlightsOverview.FlightRef.text()";
            String xpath_ServiceDefinitionRef = "Envelope.Body.AirShoppingRS.OffersGroup.AirlineOffers.Offer[" + i + "].OfferItem.Service[1].ServiceDefinitionRef.text()";
            //System.out.println(xpath_FlightRef);
            //System.out.println(xpath_ServiceDefinitionRef);
            String FlightRef = path.getString(xpath_FlightRef);
            //System.out.println(FlightRef);
            String ServiceDefinitionRef = path.getString(xpath_ServiceDefinitionRef);
            //System.out.println(ServiceDefinitionRef);
            if (FlightRef.contains(hashMap.get("port2").toString()+hashMap.get("port1").toString()) && ServiceDefinitionRef.contains(text)) {
                String xpath_offerdonus = "Envelope.Body.AirShoppingRS.OffersGroup.AirlineOffers.Offer[" + i + "].@OfferID.text()";
                //System.out.println(xpath_offerdonus);
                String offeridonus = path.getString(xpath_offerdonus);
                hashMap.put("offerId_donus", offeridonus);
                System.out.println("offer id donus hashmape eklendi : " + hashMap.get("offerId_donus"));
                break;
            }
        }
    }

@Step("Paketi <text> olan ikinci gidis ucusunun Offer ID sini al")
    public void findOfferIdSecond(String text) throws IOException {
        ResponseBody responseBodyCopy = response.peekBody(Long.MAX_VALUE);
        XmlPath path = XmlPath.from(responseBodyCopy.string());

        for (int i = 0; i < 300; i++) {
            String xpath_FlightRef = "Envelope.Body.AirShoppingRS.OffersGroup.AirlineOffers.Offer[" + i + "].FlightsOverview.FlightRef.text()";
            String xpath_ServiceDefinitionRef = "Envelope.Body.AirShoppingRS.OffersGroup.AirlineOffers.Offer[" + i + "].OfferItem.Service[1].ServiceDefinitionRef.text()";
            //System.out.println(xpath_FlightRef);
            //System.out.println(xpath_ServiceDefinitionRef);
            String FlightRef = path.getString(xpath_FlightRef);
            //System.out.println(FlightRef);
            String ServiceDefinitionRef = path.getString(xpath_ServiceDefinitionRef);
            //System.out.println(ServiceDefinitionRef);
            if (FlightRef.contains(hashMap.get("port3").toString()+hashMap.get("port4").toString()) && ServiceDefinitionRef.contains(text)) {
                String xpath_offerdonus = "Envelope.Body.AirShoppingRS.OffersGroup.AirlineOffers.Offer[" + i + "].@OfferID.text()";
                //System.out.println(xpath_offerdonus);
                String offeridonus = path.getString(xpath_offerdonus);
                hashMap.put("offerId_donus", offeridonus);
                System.out.println("offer id donus hashmape eklendi : " + hashMap.get("offerId_donus"));
                break;
            }
        }
    }




}




