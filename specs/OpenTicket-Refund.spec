Pegasus NDC
=====================
Created by testinium on 7.09.2022



INT - RT - 2 ADT - EKO PAKET ( Gidiş bacağı open )
-----------------------------------------------------------------------------
tags: 1-NDCOpenTicketIntRtEkoGidis
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RT2ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT2ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "AMS" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "AMS" "replaceAirportCodefourth" yerine "SAW" ve "replaceDatesecond" olarak "10" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
// doOrderCreate_RT2ADT
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping 2 ADT servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir

//doAirDocIssue
* 2 ADT icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue_OpenTicket" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "AMS" "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
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

DOM+DOM - OW - 1 ADT - ESNEK PAKET ( Tüm uçuş open )
-----------------------------------------------------------------------------
tags: 2-NDCOpenTicketOwDomDomEsnekTumUcus
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

// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue_OpenTicket" requestine "replaceNewPort1" yerine "ADA" "replaceNewPort2" yerine "SAW" "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
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
// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue_OpenTicket" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "SZF" "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef2" degerlerini ekle
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

CP+INT - RT - 1 ADT 1 CHD - AVANTAJ PAKET ( Dönüş uçuşu open )
-----------------------------------------------------------------------------
tags: 3-NDCOpenTicketRtCpIntAdvDonus
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RTCokYolcu" requestine "replaceAirportCodefirst" yerine "ECN" "replaceAirportCodesecond" yerine "AMS" ve "replaceDatefirst" olarak "16" gün ileri tarih, "replaceAirportCodethird" yerine "AMS" "replaceAirportCodefourth" yerine "ECN" ve "replaceDatesecond" olarak "21" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir ADV
// doOrderCreate_RT3
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping cok yolcu servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir


//CateringAvailabilityPnr
* "SOAPAction" key "cranendc/doCateringAvailabilityPnr" value degerini headera ekle
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
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//
////XbagAvailabilityPnr
//* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
//* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
//* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(2. bacak icin) degeri kaydedilir
//* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(3. bacak icin) degeri kaydedilir
//* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(4. bacak icin) degeri kaydedilir
////AddSsr_AddXbag
//* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak icin AddXbag servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak icin AddXbag servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(3. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
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
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(3. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(4. bacak icin) degeri kaydedilir2

//AddSsr_Addseat 2.yolcu
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//doAirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue_OpenTicketCiftSegment" requestine "replaceNewPort1" yerine "AMS" "replaceNewPort2" yerine "SAW" "replaceOrderID" yerine hashmapdeki "orderId" "replaceSegmentId1" yerine "segmentRef3" ve "replaceSegmentId2" yerine "segmentRef4" degerlerini ekle
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

INT+INT - OW - 1 ADT 1 INF - EKO PAKET ( Tüm uçuş open )
-----------------------------------------------------------------------------
tags: 4-NDCOpenTicketOwIntIntEko
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OWCokYolcu" requestine "replaceAirportCodefirst" yerine "AMS" "replaceAirportCodesecond" yerine "ATH" ve "replaceDate" olarak "4" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir

//OrderCreate
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping cok yolcu sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir

//AirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue_OpenTicketCiftSegment" requestine "replaceNewPort1" yerine "AMS" "replaceNewPort2" yerine "SAW" "replaceOrderID" yerine hashmapdeki "orderId" "replaceSegmentId1" yerine "segmentRef1" ve "replaceSegmentId2" yerine "segmentRef2" degerlerini ekle
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
//* ReissuePreview sorgusundan donen responceID ve newPrice alani reissueCommit servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue commit sorgusundan donen degerler kontrol edilir

INT + DOM - RT - 2 ADT -1 CHD - 1 INF - ESNEK PAKET ( Gidiş ve Dönüş Tüm uçuş )
-----------------------------------------------------------------------------
tags: 5-NDCRefundIntDomEsnekTumUcus
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RTCokYolcu" requestine "replaceAirportCodefirst" yerine "ATH" "replaceAirportCodesecond" yerine "TZX" ve "replaceDatefirst" olarak "28" gün ileri tarih, "replaceAirportCodethird" yerine "TZX" "replaceAirportCodefourth" yerine "ATH" ve "replaceDatesecond" olarak "5" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir FLEX
// doOrderCreate_RTCokYolcu
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
* OrderCreate servisinden donen SegmentKey(4.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(4. bacak icin) degeri kaydedilir

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
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
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
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(4. bacak icin) degeri kaydedilir
//AddSsr_AddXbag
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(3. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
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
* OrderCreate servisinden donen SegmentKey(4.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(4. bacak icin) degeri kaydedilir2

//AddSsr_Addseat 2.yolcu
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//doAirDocIssue
//* MCO icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir (Is Bankasi)
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

// CANCEL
* AirDocIssue sorgusundan donen Surname ve BookingReference kismi kayit edilir
* AirDocIssue sorgusundan donen Surname ve BookingReference alani doCancelCommit servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com:443/CraneNDC/CraneNDCService" servisine istek at

DOM+INT - OW- 1 ADT - 1 CHD - 1 INF - AVANTAJ PAKET ( İlk Bacak İptal )
-----------------------------------------------------------------------------
tags: 6-NDCRefundIntDomAvantajIlkBacak
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OWCokYolcu" requestine "replaceAirportCodefirst" yerine "TZX" "replaceAirportCodesecond" yerine "AMS" ve "replaceDate" olarak "5" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir ADV

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


// doReissuePreview
* "doReissuePreview_TekYonIptalTekSegment" requestine "replaceOrderId" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
* "SOAPAction" key "cranendc/doReissuePreview" value degerini headera ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* ReissuePreview servisindeki responseID alani kaydedilir
// doReissueCommit
* "SOAPAction" key "cranendc/doReissueCommit" value degerini headera ekle
* "doReissueCommit_TekYonIptalTekSegment" requestine "replaceOrderId" yerine hashmapdeki "orderId" "replaceNewResponseId" yerine "newResponseId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
//* ReissuePreview sorgusundan donen responceID ve newPrice alani reissueCommit servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue commit sorgusundan donen degerler kontrol edilir

INT - RT - 1 ADT - ESNEK PAKET - ( Dönüş uçuşu refund )
-----------------------------------------------------------------------------
tags: 7-NDCRefundIntEsnekDonus
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "ATH" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "ATH" "replaceAirportCodefourth" yerine "SAW" ve "replaceDatesecond" olarak "10" gün ileri tarih  yazilir
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

//XbagAvailabilityPnr
* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
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
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//doAirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir (Is Bankasi)
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

// doReissuePreview
* "doReissuePreview_TekYonIptalTekSegment" requestine "replaceOrderId" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef2" degerlerini ekle
* "SOAPAction" key "cranendc/doReissuePreview" value degerini headera ekle
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* ReissuePreview servisindeki responseID alani kaydedilir
// doReissueCommit
* "SOAPAction" key "cranendc/doReissueCommit" value degerini headera ekle
* "doReissueCommit_TekYonIptalTekSegment" requestine "replaceOrderId" yerine hashmapdeki "orderId" "replaceNewResponseId" yerine "newResponseId" ve "replaceSegmentId" yerine "segmentRef2" degerlerini ekle
//* ReissuePreview sorgusundan donen responceID ve newPrice alani reissueCommit servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Reissue commit sorgusundan donen degerler kontrol edilir

CP+INT - OW - 2 ADT 1 INF - EKO PAKET ( Tüm uçuş iptal )
-----------------------------------------------------------------------------
tags: 8-NDCRefundCpIntEkoTum
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OWCokYolcu" requestine "replaceAirportCodefirst" yerine "ECN" "replaceAirportCodesecond" yerine "ATH" ve "replaceDate" olarak "4" gün ileri tarih yazilir
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

// CANCEL
* AirDocIssue sorgusundan donen Surname ve BookingReference kismi kayit edilir
* AirDocIssue sorgusundan donen Surname ve BookingReference alani doCancelCommit servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com:443/CraneNDC/CraneNDCService" servisine istek at






