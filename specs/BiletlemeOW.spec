Pegasus NDC Biletleme OW
=====================
Created by testinium on 7.09.2022

DOM - (1 ADT + 1 CH + 1 INF) - OW - EKO - GARANTI
-----------------------------------------------------------------------------
tags: 1-NDCBiletlemeOwDom3AdtEkoGaranti
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OWCokYolcu" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "TZX" ve "replaceDate" olarak "4" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doOrderCreate_OWCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping cok yolcu sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID Ucret ve pnr kismi kayit edilir
//doAirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


DOM - (1 ADT) - OW - MCO ile ödeme
-----------------------------------------------------------------------------
tags: 2-NDCBiletlemeOwDom1AdtMCO
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "ADA" ve "replaceDate" olarak "5" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doOrderCreate_OW1ADT
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID Ucret ve pnr kismi kayit edilir
//doAirDocIssue_MCO1ADT
* MCO icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

INT - (1 ADT + 1CH + 1INF) - OW - SEKO Finans
-----------------------------------------------------------------------------
tags: 3-NDCBiletlemeOwInt3AdtSekoFinans
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OWCokYolcu" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "AMS" ve "replaceDate" olarak "3" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doOrderCreate_OWCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping cok yolcu sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID Ucret ve pnr kismi kayit edilir
//doAirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


INT - (1 ADT) - OW - SEKO İsBankasi
-----------------------------------------------------------------------------
tags: 4-NDCBiletlemeOwInt1AdtSekoIsBankasi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "AMS" ve "replaceDate" olarak "3" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doOrderCreate_OW1ADT
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID ve Ucret kismi kayit edilir
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

CP - (1 ADT) - OW - gidis - (CATERING + XBAG + SEAT) - GARANTI
-----------------------------------------------------------------------------
tags: 5-NDCBiletlemeOwCp1AdtCatingXbagSeatGaranti
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "ECN" ve "replaceDate" olarak "8" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir

//OrderCreate
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef ve Ucret kısmı kayıt edilir

//CateringAvailabilityPnr
* "SOAPAction" key "cranendc/doCateringAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(1. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//XbagAvailabilityPnr
* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
//AddSsr_AddXbag
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2

//AddSsr_Addseat
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//AirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

CP - (1 ADT + 1 CH + 1 INF) - OW - (CATERING + XBAG + SEAT) - Is Bankasi
-----------------------------------------------------------------------------
tags: 6-NDCBiletlemeOwCp3AdtCatingXbagSeatIsBankasi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OWCokYolcu" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "ECN" ve "replaceDate" olarak "7" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir

//OrderCreate
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping cok yolcu sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir

//CateringAvailabilityPnr
* "SOAPAction" key "cranendc/doCateringAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(1. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Cok Yolcu icin Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Cok Yolcu icin Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Cok Yolcu icin Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir 2.yolcu
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at



//XbagAvailabilityPnr
* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
//AddSsr_AddXbag
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2

//AddSsr_Addseat
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2

* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//AirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

DOM + DOM - (1 ADT) - OW - gidiş(CATERING + XBAG + SEAT) - Is Bankasi
-----------------------------------------------------------------------------
tags: 7-NDCBiletlemeOwCp1AdtDomDomCateringXbagSeatIsBankasi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "TZX" "replaceAirportCodesecond" yerine "BJV" ve "replaceDate" olarak "10" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir

//OrderCreate
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir

//CateringAvailabilityPnr
* "SOAPAction" key "cranendc/doCateringAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(2. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//XbagAvailabilityPnr
* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doXbagAvailability servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(2. bacak icin) degeri kaydedilir

//AddSsr_AddXbag
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2

//AddSsr_Addseat
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//AirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

DOM + INT - (2 ADT + 1 CH + 1 INF) - OW - gidiş(CATERING + XBAG + SEAT) - MCO ile Odeme
-----------------------------------------------------------------------------
tags: 8-NDCBiletlemeOwCp4AdtDomIntCateringXbagSeatMCO
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OWCokYolcu" requestine "replaceAirportCodefirst" yerine "TZX" "replaceAirportCodesecond" yerine "AMS" ve "replaceDate" olarak "3" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir

//OrderCreate
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping cok yolcu sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir

//CateringAvailabilityPnr
* "SOAPAction" key "cranendc/doCateringAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(2. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//XbagAvailabilityPnr
* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doXbagAvailability servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(2. bacak icin) degeri kaydedilir

//AddSsr_AddXbag
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2

//AddSsr_Addseat
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2

* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle


//AirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir MCO
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

INT + INT - (1 ADT + 1 CH + 1 INF) - OW - gidiş(CATERING + XBAG + SEAT) - Garanti
-----------------------------------------------------------------------------
tags: 9-NDCBiletlemeOwIntInt3AdtCateringXbagSeatGaranti
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OWCokYolcu" requestine "replaceAirportCodefirst" yerine "AMS" "replaceAirportCodesecond" yerine "ATH" ve "replaceDate" olarak "10" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir

//OrderCreate
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping cok yolcu sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir

//CateringAvailabilityPnr
* "SOAPAction" key "cranendc/doCateringAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(2. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//XbagAvailabilityPnr
* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doXbagAvailability servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(2. bacak icin) degeri kaydedilir

//AddSsr_AddXbag
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2

//AddSsr_Addseat
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2

* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//AirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

DOM + CP - (1 ADT + 1 CH + 1 INF) - OW - gidiş(CATERING + XBAG + SEAT) - MCO ile odeme
-----------------------------------------------------------------------------
tags: 10-NDCBiletlemeOw3AdtDomCpCateringXbagSeatMCO
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OWCokYolcu" requestine "replaceAirportCodefirst" yerine "TZX" "replaceAirportCodesecond" yerine "ECN" ve "replaceDate" olarak "5" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir

//OrderCreate
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping cok yolcu sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir

//CateringAvailabilityPnr
* "SOAPAction" key "cranendc/doCateringAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(2. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//XbagAvailabilityPnr
* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doXbagAvailability servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(2. bacak icin) degeri kaydedilir

//AddSsr_AddXbag
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2

//AddSsr_Addseat
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2

* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//AirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir MCO
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

MC - (1 ADT + 1 CH ) - OW - EKO - Is Bankasi
-----------------------------------------------------------------------------
tags: 11-NDCBiletlemeOwMc2AdtIsBankasi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1Adt1Ch" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1Adt1Ch" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "JED" ve "replaceDate" olarak "9" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doOrderCreate_OWCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping 2 yolcu sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID Ucret ve pnr kismi kayit edilir
//doAirDocIssue
* 2 Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir (Is Bankasi)
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


INT + INT - ( 1 ADT) - OW - gidiş(CATERING + XBAG + SEAT) - İŞ BANKASI
-----------------------------------------------------------------------------
tags: 12-NDCBiletlemeOwIntInt1AdtCateringXbagSeatIsBankasi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "AMS" "replaceAirportCodesecond" yerine "ATH" ve "replaceDate" olarak "5" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir

//OrderCreate
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir

//CateringAvailabilityPnr
* "SOAPAction" key "cranendc/doCateringAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(1. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//XbagAvailabilityPnr
* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir

//AddSsr_AddXbag
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2

//AddSsr_Addseat
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//AirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

INT + CP - (1 ADT) - OW - gidiş(CATERING + XBAG + SEAT) - MCO Ödeme
-----------------------------------------------------------------------------
tags: 13-NDCBiletlemeOw1AdtIntCpCateringXbagSeatMCO
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "AMS" "replaceAirportCodesecond" yerine "ECN" ve "replaceDate" olarak "5" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir

//OrderCreate
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir

//CateringAvailabilityPnr
* "SOAPAction" key "cranendc/doCateringAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(2. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//XbagAvailabilityPnr
* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doXbagAvailability servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(2. bacak icin) degeri kaydedilir

//AddSsr_AddXbag
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2

//AddSsr_Addseat
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//AirDocIssue
* MCO icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

INT - OW - (1 ADT) - Gidiş (AVANTAJ) - İŞ BANKASI
-----------------------------------------------------------------------------
tags: 14-NDCBiletlemeOw1AdtAvantajIsBankasi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "ATH" ve "replaceDate" olarak "4" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir ADV
// doOrderCreate_OW1ADT
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir

//CateringAvailabilityPnr
* "SOAPAction" key "cranendc/doCateringAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(1. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2

//AddSsr_Addseat
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

DOM + INT - OW - (1ADT+1CHD+1INF) - Gidiş (ESNEK) - GARANTI
-----------------------------------------------------------------------------
tags: 15-NDCBiletlemeOw1Adt1Chd1InfEsnekGaranti
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OWCokYolcu" requestine "replaceAirportCodefirst" yerine "TZX" "replaceAirportCodesecond" yerine "AMS" ve "replaceDate" olarak "7" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir FLEX
// doOrderCreate_OW1ADT
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping cok yolcu sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir

//CateringAvailabilityPnr
* "SOAPAction" key "cranendc/doCateringAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(2. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2

//AddSsr_Addseat
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2

* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2

* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2


* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

DOM+DOM - 1ADT - OW - ESNEK Paket - Dönüş(BAGAJ+CATERING) - YAPIKREDI
-----------------------------------------------------------------------------
tags: 16-NDCBiletlemeOw1AdtDomDomEsnekYapiKredi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "ADA" "replaceAirportCodesecond" yerine "SZF" ve "replaceDate" olarak "5" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir FLEX

//OrderCreate
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir

//CateringAvailabilityPnr
* "SOAPAction" key "cranendc/doCateringAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(2. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//XbagAvailabilityPnr
* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doXbagAvailability servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(2. bacak icin) degeri kaydedilir

//AddSsr_AddXbag
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2

//AddSsr_Addseat
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//AirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

DOM MultiPort - (1 ADT + 1 CH + 1 INF) - OW - gidiş(CATERING + XBAG + SEAT) - MCO ödeme
-----------------------------------------------------------------------------
tags: 17-NDCBiletlemeOw1Adt1Ch1InfDomMultiportMco
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
//* "doAirShopping_OWCokYolcu" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "AYT" ve "replaceDate" olarak "8" gün ileri tarih yazilir
* DOM Multiport
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan Multiport ucuslarinin OfferID ve ResponseID alani kaydedilir

//OrderCreate
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping cok yolcu servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir


//CateringAvailabilityPnr
* "SOAPAction" key "cranendc/doCateringAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(2. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(3.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(3. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//XbagAvailabilityPnr
* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(2. bacak icin) degeri kaydedilir
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(3. bacak icin) degeri kaydedilir
//AddSsr_AddXbag
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(3.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(3. bacak icin) degeri kaydedilir2
//AddSsr_Addseat
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr 2.yolcu
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(3.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(3. bacak icin) degeri kaydedilir2

//AddSsr_Addseat 2.yolcu
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//AirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir MCO
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


INT MultiPort - (1 ADT + 1 CH + 1 INF) - OW - gidiş(CATERING + XBAG + SEAT) - MCO ödeme
-----------------------------------------------------------------------------
tags: 18-NDCBiletlemeOw1Adt1Ch1InfIntMultiportMco
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
//* "doAirShopping_OWCokYolcu" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "AYT" ve "replaceDate" olarak "8" gün ileri tarih yazilir
* INT Multiport
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan Multiport ucuslarinin OfferID ve ResponseID alani kaydedilir

//OrderCreate
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping cok yolcu servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir


//CateringAvailabilityPnr
* "SOAPAction" key "cranendc/doCateringAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(2. bacak icin) degeri kaydedilir
//* OrderCreate servisinden donen SegmentKey(3.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(3. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak icin AddCatering servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//XbagAvailabilityPnr
* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(2. bacak icin) degeri kaydedilir
//* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(3. bacak icin) degeri kaydedilir
//AddSsr_AddXbag
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak icin AddXbag servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2
//* OrderCreate servisinden donen SegmentKey(3.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(3. bacak icin) degeri kaydedilir2
//AddSsr_Addseat
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak icin AddSeat servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr 2.yolcu
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2
//* OrderCreate servisinden donen SegmentKey(3.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(3. bacak icin) degeri kaydedilir2

//AddSsr_Addseat 2.yolcu
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//AirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir MCO
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

INT MultiPort - (1 ADT + 1 CH + 1 INF) - OW - gidiş(CATERING + XBAG + SEAT) - MCO ödeme2
-----------------------------------------------------------------------------
tags: 18-NDCBiletlemeOw1Adt1Ch1InfIntMultiportMco2
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "ADA" ve "replaceDate" olarak "4" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir ADV
// doOrderCreate_OW1ADT
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir

//CateringAvailabilityPnr
* "SOAPAction" key "cranendc/doCateringAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(1. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//XbagAvailabilityPnr
* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir

//AddSsr_AddXbag
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2

//AddSsr_Addseat
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "TZX" ve "replaceDate" olarak "10" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef2" degerlerini ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doReissuePreview
* "doReissuePreview_ReissueTekSegment" requestine "replaceOrderID" yerine hashmapdeki "orderId" "replaceSegmentId" yerine "segmentRef2" ve "replaceNewOfferId" yerine "reshopOfferId" degerlerini ekle
* "SOAPAction" key "cranendc/doReissuePreview" value degerini headera ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* ReissuePreview servisindeki responseID alani kaydedilir

// doReissueCommit
* "SOAPAction" key "cranendc/doReissueCommit" value degerini headera ekle
* "doReissueCommit_ByPasOdemeReissueTekSegment" requestine "replaceOrderId" yerine hashmapdeki "orderId" "replaceNewPrice" yerine "newPrice" "replaceNewResponseId" yerine "newResponseId" "replaceReshopOfferId" yerine "reshopOfferId" "replaceSegmentId" yerine "segmentRef2" degerlerini ekle
//* ReissuePreview sorgusundan donen responceID ve newPrice alani reissueCommit servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue commit sorgusundan donen degerler kontrol edilir

// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue_OpenTicket" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "TZX" "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doReissuePreview
* "doReissuePreview_ReissueTekSegment" requestine "replaceOrderID" yerine hashmapdeki "orderId" "replaceSegmentId" yerine "segmentRef1" ve "replaceNewOfferId" yerine "reshopOfferId" degerlerini ekle
* "SOAPAction" key "cranendc/doReissuePreview" value degerini headera ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* ReissuePreview servisindeki responseID alani kaydedilir

// doReissueCommit
* "SOAPAction" key "cranendc/doReissueCommit" value degerini headera ekle
* "doReissueCommit_ByPasOdemeReissueTekSegment" requestine "replaceOrderId" yerine hashmapteki "orderId" "replaceNewPrice" yerine "newPrice" "replaceNewResponseId" yerine "newResponseId" "replaceReshopOfferId" yerine "reshopOfferId" "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
//* ReissuePreview sorgusundan donen responceID ve newPrice alani reissueCommit servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue commit sorgusundan donen degerler kontrol edilir open