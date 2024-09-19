Pegasus NDC
=====================
Created by testinium on 7.09.2022



DOM - 2 ADT - RT - AVANTAJ PAKET ( Gidiş Dönüş uçuşuna reissue )
-----------------------------------------------------------------------------
tags: 1-NDCReissueDom2AdtRtAvantaj
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RT2ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT2ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "TZX" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "TZX" "replaceAirportCodefourth" yerine "SAW" ve "replaceDatesecond" olarak "10" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir ADV
// doOrderCreate_RT2ADT
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping 2 ADT servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
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
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.adt icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.adt icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

////XbagAvailabilityPnr
//* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
//* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
//* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(2. bacak icin) degeri kaydedilir
//
////AddSsr_AddXbag
//* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

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

//AddSsr_Addseat 2.yolcu
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.adt icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.adt icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle
//doAirDocIssue
* 2 ADT icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "ADA" ve "replaceDate" olarak "5" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doReissuePreview
* "doReissuePreview_ReissueTekSegment" requestine "replaceOrderID" yerine hashmapdeki "orderId" "replaceSegmentId" yerine "segmentRef1" ve "replaceNewOfferId" yerine "reshopOfferId" degerlerini ekle
* "SOAPAction" key "cranendc/doReissuePreview" value degerini headera ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* ReissuePreview servisindeki responseID alani kaydedilir
// doReissueCommit
* "SOAPAction" key "cranendc/doReissueCommit" value degerini headera ekle
* "doReissueCommit_ByPasOdemeReissueTekSegment" requestine "replaceOrderId" yerine hashmapdeki "orderId" "replaceNewPrice" yerine "newPrice" "replaceNewResponseId" yerine "newResponseId" "replaceReshopOfferId" yerine "reshopOfferId" "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
//* ReissuePreview sorgusundan donen responceID ve newPrice alani reissueCommit servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue commit sorgusundan donen degerler kontrol edilir
// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "ADA" "replaceNewPort2" yerine "SAW" ve "replaceDate" olarak "10" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef2" degerlerini ekle
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


INT - RT - 1 ADT - ESNEK PAKET - ( Gidiş Dönüş uçuşuna reissue )
-----------------------------------------------------------------------------
tags: 2-NDCReissueInt1AdtRtEsnek
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "AMS" ve "replaceDatefirst" olarak "6" gün ileri tarih, "replaceAirportCodethird" yerine "AMS" "replaceAirportCodefourth" yerine "SAW" ve "replaceDatesecond" olarak "11" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir FLEX
// doOrderCreate_RTCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
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

////XbagAvailabilityPnr
//* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
//* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
//* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(2. bacak icin) degeri kaydedilir
////AddSsr_AddXbag
//* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

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
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
//* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir (Is Bankasi)
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "ADA" ve "replaceDate" olarak "7" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
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
* Reissue commit sorgusundan donen degerler kontrol edilir
// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "ADA" "replaceNewPort2" yerine "SAW" ve "replaceDate" olarak "20" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef2" degerlerini ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doReissuePreview
* "doReissuePreview_ReissueTekSegment" requestine "replaceOrderID" yerine hashmapdeki "orderId" "replaceSegmentId" yerine "segmentRef2" ve "replaceNewOfferId" yerine "reshopOfferId" degerlerini ekle
* "SOAPAction" key "cranendc/doReissuePreview" value degerini headera ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* ReissuePreview servisindeki responseID alani kaydedilir

// doReissueCommit
* "SOAPAction" key "cranendc/doReissueCommit" value degerini headera ekle
* "doReissueCommit_ByPasOdemeReissueTekSegment" requestine "replaceOrderId" yerine hashmapteki "orderId" "replaceNewPrice" yerine "newPrice" "replaceNewResponseId" yerine "newResponseId" "replaceReshopOfferId" yerine "reshopOfferId" "replaceSegmentId" yerine "segmentRef2" degerlerini ekle
//* ReissuePreview sorgusundan donen responceID ve newPrice alani reissueCommit servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue commit sorgusundan donen degerler kontrol edilir


CP - RT - 1 ADT 1 CHD 1 INF - EKO PAKET ( Gidiş uçuşuna reissue )
-----------------------------------------------------------------------------
tags: 3-NDCReissueCp1Adt1Chd1InfRtEko
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RTCokYolcu" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "ECN" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "ECN" "replaceAirportCodefourth" yerine "SAW" ve "replaceDatesecond" olarak "10" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
// doOrderCreate_RTCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping cok yolcu servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "TZX" ve "replaceDate" olarak "5" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
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
* Reissue commit sorgusundan donen degerler kontrol edilir
// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "TZX" "replaceNewPort2" yerine "SAW" ve "replaceDate" olarak "10" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef2" degerlerini ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doReissuePreview
* "doReissuePreview_ReissueTekSegment" requestine "replaceOrderID" yerine hashmapdeki "orderId" "replaceSegmentId" yerine "segmentRef2" ve "replaceNewOfferId" yerine "reshopOfferId" degerlerini ekle
* "SOAPAction" key "cranendc/doReissuePreview" value degerini headera ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* ReissuePreview servisindeki responseID alani kaydedilir

// doReissueCommit
* "SOAPAction" key "cranendc/doReissueCommit" value degerini headera ekle
* "doReissueCommit_ByPasOdemeReissueTekSegment" requestine "replaceOrderId" yerine hashmapteki "orderId" "replaceNewPrice" yerine "newPrice" "replaceNewResponseId" yerine "newResponseId" "replaceReshopOfferId" yerine "reshopOfferId" "replaceSegmentId" yerine "segmentRef2" degerlerini ekle
//* ReissuePreview sorgusundan donen responceID ve newPrice alani reissueCommit servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue commit sorgusundan donen degerler kontrol edilir

DOM+DOM - OW - 1 ADT - AVANTAJ PAKET ( Reissue )
-----------------------------------------------------------------------------
tags: 4-NDCReissueDomDom1AdtOwAvantaj
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "TZX" "replaceAirportCodesecond" yerine "ESB" ve "replaceDate" olarak "11" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir ADV

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

// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "DIY" "replaceNewPort2" yerine "ESB" ve "replaceDate" olarak "6" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doReissuePreview
* "doReissuePreview_ReissueCiftSegment" requestine "replaceOrderID" yerine hashmapdeki "orderId" "replaceSegmentId1" yerine "segmentRef1" ve "replaceSegmentId2" yerine "segmentRef2" ve "replaceNewOfferId" yerine "reshopOfferId" degerlerini ekle
* "SOAPAction" key "cranendc/doReissuePreview" value degerini headera ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* ReissuePreview servisindeki responseID alani kaydedilir
// doReissueCommit
* "SOAPAction" key "cranendc/doReissueCommit" value degerini headera ekle
* "doReissueCommit_ByPasOdemeReissueCiftSegment" requestine "replaceOrderId" yerine hashmapteki "orderId" "replaceNewPrice" yerine "newPrice" "replaceNewResponseId" yerine "newResponseId" "replaceReshopOfferId" yerine "reshopOfferId" "replaceSegmentId1" yerine "segmentRef1" ve "replaceSegmentId2" yerine "segmentRef2" degerlerini ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue commit sorgusundan donen degerler kontrol edilir

DOM+INT - RT - 2 ADT - ESNEK PAKET - ( Dönüş uçuşuna reissue )
-----------------------------------------------------------------------------
tags: 5-NDCReissueDomInt2AdtRtEsnek
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RT2ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT2ADT" requestine "replaceAirportCodefirst" yerine "TZX" "replaceAirportCodesecond" yerine "AMS" ve "replaceDatefirst" olarak "6" gün ileri tarih, "replaceAirportCodethird" yerine "AMS" "replaceAirportCodefourth" yerine "TZX" ve "replaceDatesecond" olarak "9" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir FLEX
// doOrderCreate_RT2ADT
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping 2 ADT servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
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
* OrderCreate servisinden donen SegmentKey(4.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(4. bacak icin) degeri kaydedilir


//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.adt icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.adt icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak 2.adt icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak 2.adt icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

////XbagAvailabilityPnr
//* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
//* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
//* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(2. bacak icin) degeri kaydedilir
//
////AddSsr_AddXbag
//* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

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
* OrderCreate servisinden donen SegmentKey(4.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(4. bacak icin) degeri kaydedilir2

//AddSsr_Addseat
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


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
* OrderCreate servisinden donen SegmentKey(4.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(4. bacak icin) degeri kaydedilir2

//AddSsr_Addseat 2.yolcu
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.adt icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.adt icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak 2.adt icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak 2.adt icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle
//doAirDocIssue
* 2 ADT icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle

* "doReshopForReissue2" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "ATH" ve "replaceDate" olarak "5" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" "replaceSegmentId1" yerine "segmentRef3" ve "replaceSegmentId2" yerine "segmentRef4" degerlerini ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doReissuePreview
* "doReissuePreview_ReissueCiftSegment" requestine "replaceOrderID" yerine hashmapdeki "orderId" "replaceSegmentId1" yerine "segmentRef3" ve "replaceSegmentId2" yerine "segmentRef4" ve "replaceNewOfferId" yerine "reshopOfferId" degerlerini ekle
* "SOAPAction" key "cranendc/doReissuePreview" value degerini headera ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* ReissuePreview servisindeki responseID alani kaydedilir
// doReissueCommit
* "SOAPAction" key "cranendc/doReissueCommit" value degerini headera ekle
* "doReissueCommit_ByPasOdemeReissueCiftSegment" requestine "replaceOrderId" yerine hashmapteki "orderId" "replaceNewPrice" yerine "newPrice" "replaceNewResponseId" yerine "newResponseId" "replaceReshopOfferId" yerine "reshopOfferId" "replaceSegmentId1" yerine "segmentRef3" ve "replaceSegmentId2" yerine "segmentRef4" degerlerini ekle
//* ReissuePreview sorgusundan donen responceID ve newPrice alani reissueCommit servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue commit sorgusundan donen degerler kontrol edilir



2 ADT yolcu, OW INT uçuşu DOM uçuşa değişiklik yapılır. (iade çıktı)
-----------------------------------------------------------------------------
tags: 6-NDCReissue2AdtOwIntToDom
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW2ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW2ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "BCN" ve "replaceDate" olarak "5" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
// doOrderCreate_RT2ADT
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping 2 adt sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir

//doAirDocIssue
* 2 ADT icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "ESB" ve "replaceDate" olarak "5" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doReissuePreview
* "doReissuePreview_ReissueTekSegment" requestine "replaceOrderID" yerine hashmapdeki "orderId" "replaceSegmentId" yerine "segmentRef1" ve "replaceNewOfferId" yerine "reshopOfferId" degerlerini ekle
* "SOAPAction" key "cranendc/doReissuePreview" value degerini headera ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* ReissuePreview servisindeki responseID alani kaydedilir
// doReissueCommit
* "SOAPAction" key "cranendc/doReissueCommit" value degerini headera ekle
* "doReissueCommit_ByAirTekSegment" requestine "replaceOrderId" yerine hashmapdeki "orderId" "replaceNewResponseId" yerine "newResponseId" ve "replaceReshopOfferId" yerine "reshopOfferId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
//* ReissuePreview sorgusundan donen responceID ve newPrice alani reissueCommit servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue commit sorgusundan donen degerler kontrol edilir

1ADT yolcu, OW DOM uçuşta tarih değişikliği yapılır. (tahsilat-iade yok)
-----------------------------------------------------------------------------
tags: 7-NDCReissue1AdtOwDomTarih
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "AYT" ve "replaceDate" olarak "10" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doOrderCreate_OW1ADT
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue_1ADT
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "AYT" ve "replaceDate" olarak "11" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doReissuePreview
* "doReissuePreview_ReissueTekSegment" requestine "replaceOrderID" yerine hashmapdeki "orderId" "replaceSegmentId" yerine "segmentRef1" ve "replaceNewOfferId" yerine "reshopOfferId" degerlerini ekle
* "SOAPAction" key "cranendc/doReissuePreview" value degerini headera ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* ReissuePreview servisindeki responseID alani kaydedilir

// doReissueCommit
* "SOAPAction" key "cranendc/doReissueCommit" value degerini headera ekle
* "doReissueCommit_ByPasOdemeReissueTekSegment0" requestine "replaceOrderId" yerine hashmapdeki "orderId" "replaceNewResponseId" yerine "newResponseId" ve "replaceReshopOfferId" yerine "reshopOfferId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
//* ReissuePreview sorgusundan donen responceID ve newPrice alani reissueCommit servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue commit sorgusundan donen degerler kontrol edilir

1ADT, 1CHD, 1INF yolcu, OW DOM uçuşu açığa alma işlemi yapılır.
-----------------------------------------------------------------------------
tags: 8-NDCReissue1Adt1Ch1InfOwDomAcigaAlma
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OWCokYolcu" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "TZX" ve "replaceDate" olarak "4" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doOrderCreate_OWCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping cok yolcu sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
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
* Reissue commit sorgusundan donen degerler kontrol edilir


1 ADT yolcu, OW DOM uçuş, SSR satın alınır ve tarih değişikliği yapılır.
-----------------------------------------------------------------------------
tags: 9-NDCReissue1AdtOwDomSsrTarih
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "TZX" ve "replaceDate" olarak "5" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir

//OrderCreate
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir


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

// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "TZX" ve "replaceDate" olarak "7" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doReissuePreview
* "doReissuePreview_ReissueTekSegment" requestine "replaceOrderID" yerine hashmapdeki "orderId" "replaceSegmentId" yerine "segmentRef1" ve "replaceNewOfferId" yerine "reshopOfferId" degerlerini ekle
* "SOAPAction" key "cranendc/doReissuePreview" value degerini headera ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* ReissuePreview servisindeki responseID alani kaydedilir
// doReissueCommit
* "SOAPAction" key "cranendc/doReissueCommit" value degerini headera ekle
* "doReissueCommit_ByPasOdemeReissueTekSegment" requestine "replaceOrderId" yerine hashmapdeki "orderId" "replaceNewPrice" yerine "newPrice" "replaceNewResponseId" yerine "newResponseId" "replaceReshopOfferId" yerine "reshopOfferId" "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
//* ReissuePreview sorgusundan donen responceID ve newPrice alani reissueCommit servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue commit sorgusundan donen degerler kontrol edilir

// deletingDoReissue
* Reissue commit sorgusundan donen degerler kontrol edilir

1 ADT yolcu, DOM uçuşu INT uçuşa değişiklik yapılır. Çıkan tahsilat tutarı farklı bir currency ile ödenir.
-----------------------------------------------------------------------------
tags: 10-NDCReissue1AdtDomToInt
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "TZX" ve "replaceDate" olarak "6" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doOrderCreate_OW1ADT
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doOrderCreate_OW1ADT" requestine "replaceOffer" yerine hashmapdeki "offerId_gidis" ve "replaceResponse" yerine "responseId" degerlerini ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* "doAirDocIssue_KK1ADT" requestine "replaceOrder" yerine hashmapdeki "orderId" ve "replacePrice" yerine "currencyPrice" degerlerini ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue_currency" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "AMS" ve "replaceDate" olarak "8" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doReissuePreview
* "doReissuePreview_ReissueTekSegment_currency" requestine "replaceOrderID" yerine hashmapdeki "orderId" "replaceSegmentId" yerine "segmentRef1" ve "replaceNewOfferId" yerine "reshopOfferId" degerlerini ekle
* "SOAPAction" key "cranendc/doReissuePreview" value degerini headera ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* ReissuePreview servisindeki responseID alani kaydedilir
// doReissueCommit
* "SOAPAction" key "cranendc/doReissueCommit" value degerini headera ekle
* "doReissueCommit_ByPasOdemeReissueTekSegment_currency" requestine "replaceOrderId" yerine hashmapdeki "orderId" "replaceNewPrice" yerine "newPrice" "replaceNewResponseId" yerine "newResponseId" "replaceReshopOfferId" yerine "reshopOfferId" "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
//* ReissuePreview sorgusundan donen responceID ve newPrice alani reissueCommit servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue commit sorgusundan donen degerler kontrol edilir


1 ADT yolcu, OW INT uçuşta tarih değişikliği yapılır. Çıkan tahsilat MCO ile ödenir.
-----------------------------------------------------------------------------
tags: 11-NDCReissue1AdtIntTarihMco
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "AMS" ve "replaceDate" olarak "4" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doOrderCreate_OW1ADT
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue_MCO1ADT
* MCO icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "AMS" ve "replaceDate" olarak "5" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doReissuePreview
* "doReissuePreview_ReissueTekSegment" requestine "replaceOrderID" yerine hashmapdeki "orderId" "replaceSegmentId" yerine "segmentRef1" ve "replaceNewOfferId" yerine "reshopOfferId" degerlerini ekle
* "SOAPAction" key "cranendc/doReissuePreview" value degerini headera ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* ReissuePreview servisindeki responseID alani kaydedilir
// doReissueCommit
* "SOAPAction" key "cranendc/doReissueCommit" value degerini headera ekle
* "doReissueCommit_ByPasOdemeReissueTekSegment_mco" requestine "replaceOrderId" yerine hashmapdeki "orderId" "replaceNewPrice" yerine "newPrice" "replaceNewResponseId" yerine "newResponseId" "replaceReshopOfferId" yerine "reshopOfferId" "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
//* ReissuePreview sorgusundan donen responceID ve newPrice alani reissueCommit servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue commit sorgusundan donen degerler kontrol edilir
