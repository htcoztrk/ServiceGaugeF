Pegasus NDC
=====================
Created by testinium on 7.09.2022

1 OW uçuşta değişiklik 1 ADT yolcu, OW DOM uçuşta tarih değişikliği yapılır.(tahsilat çıktı)
-----------------------------------------------------------------------------
tags: 1-NDCReissueEkOwDom1AdtTarih
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "ESB" ve "replaceDate" olarak "10" gün ileri tarih yazilir
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
* "doReshopForReissue" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "ESB" ve "replaceDate" olarak "11" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
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


1 ADT yolcu, OW uçuşta tarih değişikliği (bağlantılı uçuşa) yapılır.
-----------------------------------------------------------------------------
tags: 2-NDCReissueEkOw1AdtTarihDegisikligi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "ADA" "replaceAirportCodesecond" yerine "TZX" ve "replaceDate" olarak "4" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doOrderCreate_OWCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "TZX" ve "replaceDate" olarak "7" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef2" degerlerini ekle
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

1 ADT yolcu, OW DOM uçuş, SSR satın alınır ve tarih değişikliği yapılır.
-----------------------------------------------------------------------------
tags: 3-NDCReissueEkOwDom1AdtSsrAlinirTarihDegisikligi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "ESB" ve "replaceDate" olarak "10" gün ileri tarih yazilir
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

// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "ESB" ve "replaceDate" olarak "11" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
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

1 ADT yolcu, OW INT-DOM bağlantılı uçuşta tarih değişikliği (bağlantılı uçuşa) yapılır
-----------------------------------------------------------------------------
tags: 4-NDCReissueEkOwIntDom1AdtTarihDegisikligi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "AMS" "replaceAirportCodesecond" yerine "TZX" ve "replaceDate" olarak "11" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doOrderCreate_OW1yolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "TZX" ve "replaceDate" olarak "12" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef2" degerlerini ekle
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

1 ADT yolcu, OW paketli DOM-INT bağlantılı uçuş, direk uçuş olarak tarih değişikliği yapılır.
-----------------------------------------------------------------------------
tags: 5-NDCReissueEkOwDomIntTarihDegisikligi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "ADA" "replaceAirportCodesecond" yerine "DXB" ve "replaceDate" olarak "10" gün ileri tarih yazilir
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
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(2. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddCatering servisindeki ilgili alana girilir
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

//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "SAW" "replaceNewPort2" yerine "DXB" ve "replaceDate" olarak "11" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef2" degerlerini ekle
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

1 ADT yolcu, OW DOM-DOM bağlantılı uçuş, segmentlerden biri için SSR satın alınır ve bu segmentte rota değişikliği yapılır.
-----------------------------------------------------------------------------
tags: 6-NDCReissueEkOwDomDomSsrSatinAlRotaDegis
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "ADA" "replaceAirportCodesecond" yerine "SZF" ve "replaceDate" olarak "7" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
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
* "doReshopForReissue" requestine "replaceNewPort1" yerine "ESB" "replaceNewPort2" yerine "SAW" ve "replaceDate" olarak "7" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
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

1 ADT yolcu, OW INT-DOM paketli bağlantılı uçuş, master segmentte değişiklik yapılır.
-----------------------------------------------------------------------------
tags: 7-NDCReissueEkOwDomMasterSegment
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OW1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "BCN" "replaceAirportCodesecond" yerine "ADA" ve "replaceDate" olarak "9" gün ileri tarih yazilir
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
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "DUS" "replaceNewPort2" yerine "SAW" ve "replaceDate" olarak "10" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
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

1 ADT yolcu, OW DOM-INT bağlantılı uçuş, addon segment iptal edilir.
-----------------------------------------------------------------------------
tags: 8-NDCReissueEkOwDomIntAddonIptal
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "TZX" "replaceAirportCodesecond" yerine "DUS" ve "replaceDate" olarak "10" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doOrderCreate_OW1yolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
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

1 ADT yolcu, OW DOM-INT bağlantılı uçuş, master segment iptal edilir.
-----------------------------------------------------------------------------
tags: 9-NDCReissueEkOwDomIntAddonIptal
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "TZX" "replaceAirportCodesecond" yerine "DUS" ve "replaceDate" olarak "10" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doOrderCreate_OW1yolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
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

1 ADT yolcu, OW beyond bağlantılı uçuş, her iki segment beraber değişiklik yapılır.
-----------------------------------------------------------------------------
tags: 10-NDCReissueEkOwBeyondBaglantili2SegmentDegisiklik
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "BLQ" "replaceAirportCodesecond" yerine "DXB" ve "replaceDate" olarak "3" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doOrderCreate_OW1yolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue2" requestine "replaceNewPort1" yerine "TZX" "replaceNewPort2" yerine "AMS" ve "replaceDate" olarak "3" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" "replaceSegmentId1" yerine "segmentRef1" ve "replaceSegmentId2" yerine "segmentRef2" degerlerini ekle
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

1 ADT yolcu, OW beyond bağlantılı uçuş, segmentlerden birinde değişiklik yapılır.
-----------------------------------------------------------------------------
tags: 11-NDCReissueEkOwBeyondBaglantiliTekSegment
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "BLQ" "replaceAirportCodesecond" yerine "TLV" ve "replaceDate" olarak "3" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doOrderCreate_OW1yolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue2" requestine "replaceNewPort1" yerine "TZX" "replaceNewPort2" yerine "MUC" ve "replaceDate" olarak "3" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" "replaceSegmentId1" yerine "segmentRef1" ve "replaceSegmentId2" yerine "segmentRef2" degerlerini ekle
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



1 ADT yolcu, OW beyond bağlantılı uçuş, addon segmente sonradan SSR satın alınır ve segment iptal edilir.
-----------------------------------------------------------------------------
tags: 12-NDCReissueEkOwBeyondAddonSegmentSsrIptal
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "BLQ" "replaceAirportCodesecond" yerine "TLV" ve "replaceDate" olarak "4" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doOrderCreate_OW1yolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

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
* Toplam ssr ucreti odenir
* "SOAPAction" key "cranendc/doSellSsr" value degerini headera ekle
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


1 ADT yolcu, OW beyond bağlantılı uçuş, master segmente sonradan SSR satın alınır ve segment iptal edilir.
-----------------------------------------------------------------------------
tags: 13-NDCReissueEkOwBeyondMasterSegmentSsrIptal
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_OWCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_OW1ADT" requestine "replaceAirportCodefirst" yerine "BLQ" "replaceAirportCodesecond" yerine "TLV" ve "replaceDate" olarak "4" gün ileri tarih yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun OfferID ve ResponseID alani kaydedilir
// doOrderCreate_OW1yolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping sorgusundan donen OfferID ve ResponseID alani OrderCreate servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//CateringAvailabilityPnr
* "SOAPAction" key "cranendc/doCateringAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(2. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//XbagAvailabilityPnr
* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(2. bacak icin) degeri kaydedilir
//AddSsr_AddXbag
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
//SeatAvailabilityPnr
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2
//AddSsr_Addseat
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle
//doAirDocIssue
* Toplam ssr ucreti odenir
* "SOAPAction" key "cranendc/doSellSsr" value degerini headera ekle
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


2 ADT yolcu, INT RT uçuş, gidiş uçuşunda tarih değişikliği (bağlantılı uçuşa) yapılır
-----------------------------------------------------------------------------
tags: 14-NDCReissueEkIntRtBaglantiliUcusTarihDegisikligi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RT2Yolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT2Yolcu" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "AMS" ve "replaceDatefirst" olarak "4" gün ileri tarih, "replaceAirportCodethird" yerine "AMS" "replaceAirportCodefourth" yerine "SAW" ve "replaceDatesecond" olarak "15" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
// doOrderCreate_RTCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping 2 yolcu servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* 2 Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir (Is Bankasi)
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "DXB" "replaceNewPort2" yerine "AMS" ve "replaceDate" olarak "5" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef1" degerlerini ekle
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

1ADT yolcu, DOM RT uçuş, bundle olan dönüş uçuşunda tarih değişikliği yapılır. ADV
-----------------------------------------------------------------------------
tags: 15-NDCReissueEkDomRtBundleDonusTarihDegisikligiAdv
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "TZX" ve "replaceDatefirst" olarak "3" gün ileri tarih, "replaceAirportCodethird" yerine "TZX" "replaceAirportCodefourth" yerine "SAW" ve "replaceDatesecond" olarak "5" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir ADV
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
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "TZX" "replaceNewPort2" yerine "SAW" ve "replaceDate" olarak "11" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef2" degerlerini ekle
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





1ADT yolcu, DOM RT uçuş, bundle olan dönüş uçuşunda tarih değişikliği yapılır. CFLEX
-----------------------------------------------------------------------------
tags: 16-NDCReissueEkDomRtBundleDonusTarihDegisikligiFlex
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "TZX" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "TZX" "replaceAirportCodefourth" yerine "SAW" ve "replaceDatesecond" olarak "10" gün ileri tarih  yazilir
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
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

// doReshopforReissue
* "SOAPAction" key "cranendc/doReshopForReissue" value degerini headera ekle
* "doReshopForReissue" requestine "replaceNewPort1" yerine "TZX" "replaceNewPort2" yerine "SAW" ve "replaceDate" olarak "16" gün ileri tarih yazilir ve "replaceOrderID" yerine hashmapdeki "orderId" ve "replaceSegmentId" yerine "segmentRef2" degerlerini ekle
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



