Pegasus NDC Biletleme RT
=====================

DOM - (1 ADT + 1 CH + 1 INF) - RT - EKO - GARANTI
-----------------------------------------------------------------------------
tags: 1-NDCBiletlemeRTDom1Adt1Ch1InfEkoGaranti
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RTCokYolcu" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "ADA" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "ADA" "replaceAirportCodefourth" yerine "SAW" ve "replaceDatesecond" olarak "10" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
// doOrderCreate_RTCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping cok yolcu servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir (Is Bankasi)
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

INT - (1 ADT) - RT - EKO - İŞ BANKASI
-----------------------------------------------------------------------------
tags: 2-NDCBiletlemeRTInt1AdtEkoIsBankasi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RT1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "AMS" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "AMS" "replaceAirportCodefourth" yerine "SAW" ve "replaceDatesecond" olarak "10" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
// doOrderCreate_RTCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


INT - (1 ADT + 1 CH + 1 INF) - RT - EKO - MCO ile ödeme
-----------------------------------------------------------------------------
tags: 3-NDCBiletlemeRTInt1Adt1Ch1InfEkoMco
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RTCokYolcu" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "AMS" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "AMS" "replaceAirportCodefourth" yerine "SAW" ve "replaceDatesecond" olarak "10" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
// doOrderCreate_RTCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping cok yolcu servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir MCO
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

CP - (1 ADT) - RT - EKO - İŞ BANKASI
-----------------------------------------------------------------------------
tags: 4-NDCBiletlemeRTCp1AdtEkoIsBankasi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RT1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "ECN" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "ECN" "replaceAirportCodefourth" yerine "SAW" ve "replaceDatesecond" olarak "10" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
// doOrderCreate_RTCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

CP - (2 ADT + 1 CH + 1 INF) - RT - SEKO - İŞ BANKASI
-----------------------------------------------------------------------------
tags: 5-NDCBiletlemeRTCp2Adt1Ch1InfSekoIsBankasi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RT4Yolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT4Yolcu" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "ECN" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "ECN" "replaceAirportCodefourth" yerine "SAW" ve "replaceDatesecond" olarak "11" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
// doOrderCreate_RTCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping 4 yolcu servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* 4 Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir (Is Bankasi)
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

MC - (1 ADT + 1 CH) - RT - EKO - İŞ BANKASI
-----------------------------------------------------------------------------
tags: 6-NDCBiletlemeRTMc1Adt1Ch1EkoIsBankasi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RT2Yolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT2Yolcu" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "JED" ve "replaceDatefirst" olarak "4" gün ileri tarih, "replaceAirportCodethird" yerine "JED" "replaceAirportCodefourth" yerine "SAW" ve "replaceDatesecond" olarak "15" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
// doOrderCreate_RTCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping 2 yolcu servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* 2 Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir (Is Bankasi)
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at bypasserror

INT + INT - (1 ADT) - RT - EKO - GARANTI
-----------------------------------------------------------------------------
tags: 7-NDCBiletlemeRTIntInt1AdtEkoIsBankasi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT1ADT" requestine "replaceAirportCodefirst" yerine "AMS" "replaceAirportCodesecond" yerine "ATH" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "ATH" "replaceAirportCodefourth" yerine "AMS" ve "replaceDatesecond" olarak "15" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
// doOrderCreate_RTCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
//* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir (Is Bankasi)
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

DOM + INT - (1 ADT) - RT - EKO - İŞ BANKASI
-----------------------------------------------------------------------------
tags: 8-NDCBiletlemeRTDomInt1AdtEkoIsBankasi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RT1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT1ADT" requestine "replaceAirportCodefirst" yerine "TZX" "replaceAirportCodesecond" yerine "ATH" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "ATH" "replaceAirportCodefourth" yerine "TZX" ve "replaceDatesecond" olarak "10" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
// doOrderCreate_RTCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
//* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir (Is Bankasi)
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

INT - (1 ADT) - RT - gidiş(CATERING + XBAG + SEAT) - dönüş(CATERING + XBAG + SEAT) - MCO ile ödeme
-----------------------------------------------------------------------------
tags: 9-NDCBiletlemeRTInt1AdtCateringXbagSeatMco
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "AMS" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "AMS" "replaceAirportCodefourth" yerine "SAW" ve "replaceDatesecond" olarak "10" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
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
* MCO icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
//* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir (Is Bankasi)
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


DOM + DOM - (1 ADT + 1 CH + 1 INF) - RT - gidiş(SEAT+ CATERING + XBAG ) - dönüş(SEAT+CATERING + XBAG ) - İŞ BANKASI
-----------------------------------------------------------------------------
tags: 10-NDCBiletlemeRTDomDom1Adt1Ch1InfCateringXbagSeatIsBankasi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RTCokYolcu" requestine "replaceAirportCodefirst" yerine "ADA" "replaceAirportCodesecond" yerine "SZF" ve "replaceDatefirst" olarak "6" gün ileri tarih, "replaceAirportCodethird" yerine "SZF" "replaceAirportCodefourth" yerine "ADA" ve "replaceDatesecond" olarak "11" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
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
//* MCO icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir (Is Bankasi)
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


INT + CP - (1 ADT + 1 CH + 1 INF) - RT - gidiş(CATERING + XBAG + SEAT) - dönüş(XBAG+CATERING + SEAT) - GARANTI
-----------------------------------------------------------------------------
tags: 11-NDCBiletlemeRTIntCp1Adt1Ch1InfCateringXbagSeatGaranti
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RTCokYolcu" requestine "replaceAirportCodefirst" yerine "ATH" "replaceAirportCodesecond" yerine "ECN" ve "replaceDatefirst" olarak "6" gün ileri tarih, "replaceAirportCodethird" yerine "ECN" "replaceAirportCodefourth" yerine "ATH" ve "replaceDatesecond" olarak "11" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
// doOrderCreate_OW1ADT
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
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak icin AddCatering servisindeki ilgili alana girilir
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


CP + INT - RT - (1ADT+1CHD+1INF) - Gidiş (ESNEK) + Dönüş (ESNEK) - YAPIKREDİ
-----------------------------------------------------------------------------
tags: 12-NDCBiletlemeRTCpInt1Adt1Ch1InfCateringXbagSeatGaranti
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RTCokYolcu" requestine "replaceAirportCodefirst" yerine "ECN" "replaceAirportCodesecond" yerine "BER" ve "replaceDatefirst" olarak "6" gün ileri tarih, "replaceAirportCodethird" yerine "BER" "replaceAirportCodefourth" yerine "ECN" ve "replaceDatesecond" olarak "11" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir FLEX
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

CP - 2ADT+1CHD+1INF - RT - ESNEK Paket - Gidiş(BAGAJ+CATERING) - ESNEK Paket - Dönüş(BAGAJ+CATERING) - MCO ile ödeme
-----------------------------------------------------------------------------
tags: 13-NDCBiletlemeRTCp2Adt1Ch1InfEsnekCateringXbagSeatMco
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RT4Yolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT4Yolcu" requestine "replaceAirportCodefirst" yerine "ECN" "replaceAirportCodesecond" yerine "SAW" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "SAW" "replaceAirportCodefourth" yerine "ECN" ve "replaceDatesecond" olarak "10" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir FLEX
// doOrderCreate_OW1ADT
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping 4 yolcu servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir


//CateringAvailabilityPnr
* "SOAPAction" key "cranendc/doCateringAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(2. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 3.yolcu icin AddCatering servisindeki ilgili alana girilir
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
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir 2.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddXbag servisindeki ilgili alana girilir 3.yolcu
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddXbag servisindeki ilgili alana girilir 3.yolcu
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
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


//SeatAvailabilityPnr 3.yolcu
* "SOAPAction" key "cranendc/doSeatAvailabilityPnr" value degerini headera ekle
* OrderCreate servisinden donen SegmentKey(1.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(1. bacak icin) degeri kaydedilir2
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doSeatAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doSeatAvailability servisinden donen sorgudan sececegimiz koltugun OfferItemıd(2. bacak icin) degeri kaydedilir2

//AddSsr_Addseat 3.yolcu
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 3.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 3.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle
//doAirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir MCO
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

DOM - RT - (1ADT+1CHD+1INF) - Gidiş (AVANTAJ) + Dönüş (AVANTAJ) - İŞ BANKASI
-----------------------------------------------------------------------------
tags: 14-NDCBiletlemeRTDom1Adt1Ch1InfAvatajCateringXbagSeatIsBankasi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RTCokYolcu" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "ADA" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "ADA" "replaceAirportCodefourth" yerine "SAW" ve "replaceDatesecond" olarak "10" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir ADV
// doOrderCreate_OW1ADT
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
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak 2.yolcu icin AddSeat servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle
//doAirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

INT + INT - RT - (1ADT - 1CHD - 1INF )- Gidiş (AVANTAJ) + Dönüş (AVANTAJ) - MCO ile ödeme
-----------------------------------------------------------------------------
tags: 15-NDCBiletlemeRTIntInt1Adt1Ch1InfAvatajCateringXbagSeatMCO
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RTCokYolcu" requestine "replaceAirportCodefirst" yerine "ATH" "replaceAirportCodesecond" yerine "AMS" ve "replaceDatefirst" olarak "11" gün ileri tarih, "replaceAirportCodethird" yerine "AMS" "replaceAirportCodefourth" yerine "ATH" ve "replaceDatesecond" olarak "13" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir ADV
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

//
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
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir MCO
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


DOM + DOM - (1 ADT) - RT - gidiş(CATERING + XBAG + SEAT) - dönüş(CATERING + XBAG + SEAT) - YAPIKREDİ
-----------------------------------------------------------------------------
tags: 16-NDCBiletlemeRTDomDom1AdtEsnekCateringXbagSeatYapiKredi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT1ADT" requestine "replaceAirportCodefirst" yerine "ADA" "replaceAirportCodesecond" yerine "SZF" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "SZF" "replaceAirportCodefourth" yerine "ADA" ve "replaceDatesecond" olarak "10" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
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
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//XbagAvailabilityPnr

* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doXbagAvailability servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(2. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(3.bacak icin) ve OrderId alanlari doXbagAvailability servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(3. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(4.bacak icin) ve OrderId alanlari doXbagAvailability servisindeki ilgili alana girilir
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
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir

* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


DOM + INT - (1 ADT) - RT - SEKO - İŞ BANKASI
-----------------------------------------------------------------------------
tags: 17-NDCBiletlemeRTDomInt1AdtSekoIsBankasi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RT1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT1ADT" requestine "replaceAirportCodefirst" yerine "TZX" "replaceAirportCodesecond" yerine "AMS" ve "replaceDatefirst" olarak "4" gün ileri tarih, "replaceAirportCodethird" yerine "AMS" "replaceAirportCodefourth" yerine "TZX" ve "replaceDatesecond" olarak "8" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
// doOrderCreate_RTCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


CP + INT - (1 ADT + 1 CH + 1 INF) - RT - SEKO - MCO ile ödeme
-----------------------------------------------------------------------------
tags: 18-NDCBiletlemeRTCpInt1Adt1Ch1InfSekoMco
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RTCokYolcu" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RTCokYolcu" requestine "replaceAirportCodefirst" yerine "ECN" "replaceAirportCodesecond" yerine "AMS" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "AMS" "replaceAirportCodefourth" yerine "ECN" ve "replaceDatesecond" olarak "10" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
// doOrderCreate_RTCokYolcu
* OrderCreate sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* AirShopping cok yolcu servisinden donen gidis ve donus icin OfferID degerleri ve ResponseID degeri OrderCreate servisindeki ilgili alana yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* OrderCreate sorgusundan donen OrderID PassengerID SegmentRef(4 adet) ve Ucret kısmı kayıt edilir
//doAirDocIssue
* Cok Yolcu icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir MCO
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


DOM - 1ADT - RT - ESNEK Paket - Gidiş(BAGAJ+CATERING) - ESNEK Paket - Dönüş(BAGAJ+CATERING) - İŞ BANKASI
-----------------------------------------------------------------------------
tags: 19-NDCBiletlemeRTDom1AdtEsnekIsBankasi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RT1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT1ADT" requestine "replaceAirportCodefirst" yerine "SAW" "replaceAirportCodesecond" yerine "ADA" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "ADA" "replaceAirportCodefourth" yerine "SAW" ve "replaceDatesecond" olarak "10" gün ileri tarih  yazilir
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


INT + INT - (1 ADT) - RT - gidiş(CATERING + XBAG + SEAT ) - dönüş(CATERING + XBAG + SEAT + ) - MCO ile ödeme
-----------------------------------------------------------------------------
tags: 20-NDCBiletlemeRTIntInt1AdtCateringXbagSeatMco
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RT1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT1ADT" requestine "replaceAirportCodefirst" yerine "ATH" "replaceAirportCodesecond" yerine "AMS" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "AMS" "replaceAirportCodefourth" yerine "ATH" ve "replaceDatesecond" olarak "15" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
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
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 3.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//XbagAvailabilityPnr

* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doXbagAvailability servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(2. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(3.bacak icin) ve OrderId alanlari doXbagAvailability servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(3. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(4.bacak icin) ve OrderId alanlari doXbagAvailability servisindeki ilgili alana girilir
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
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//doAirDocIssue
* MCO icin OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


DOM + CP - (1 ADT) - RT - gidiş(CATERING +SEAT+ XBAG ) - dönüş(SEAT +CATERING + XBAG) - İŞ BANKASI
-----------------------------------------------------------------------------
tags: 21-NDCBiletlemeRTDomCp1AdtCateringSeatXbagIsBankasi
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
* "doAirShopping_RT1ADT" sorgusu icin AgentUserID ile Username in ayni mi oldugu kontrol edilir
* "doAirShopping_RT1ADT" requestine "replaceAirportCodefirst" yerine "TZX" "replaceAirportCodesecond" yerine "ECN" ve "replaceDatefirst" olarak "5" gün ileri tarih, "replaceAirportCodethird" yerine "ECN" "replaceAirportCodefourth" yerine "TZX" ve "replaceDatesecond" olarak "10" gün ileri tarih  yazilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* AirShopping sorgusundan donen ilk ucusun gidis ve donus icin OfferID degerleri ve ResponseID degeri kaydedilir
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
* OrderCreate servisinden donen SegmentKey(4.bacak icin) ve OrderId alanlari CateringAvailabilityPnr servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* CateringAvailabilityPnr servisinden donen sorgudan sececegimiz yemegin OfferItemıd(4. bacak icin) degeri kaydedilir

//AddSsr_AddCatering
* "SOAPAction" key "cranendc/doAddSsr" value degerini headera ekle
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 1.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 4.bacak icin AddCatering servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at

//XbagAvailabilityPnr
* "SOAPAction" key "cranendc/doXbagAvailabilityPnr" value degerini headera ekle
* Kayitlarimizda bulunan SegmentKey, OrderId bilgileri XbagAvailabilityPnr servisinde ilgili alanlara girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(1. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(2.bacak icin) ve OrderId alanlari doXbagAvailability servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(2. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(3.bacak icin) ve OrderId alanlari doXbagAvailability servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* doXbagAvailabilityPnr servisinden donen sorgudan sececegimiz bagajın OfferItemıd(3. bacak icin) degeri kaydedilir
* OrderCreate servisinden donen SegmentKey(4.bacak icin) ve OrderId alanlari doXbagAvailability servisindeki ilgili alana girilir
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
//* Kayıtlarimizda bulunan OrderId, OfferItemId, PassengerRefs, PassengerId, SegmentId bilgileri 2.bacak icin AddSeat servisindeki ilgili alana girilir
//* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at
* xml "Envelope.Body.OrderViewRS.Response.Order.TotalOrderPrice.SimpleCurrencyPrice.text()" xpathinindeki elementi "currencyPrice" keyiyle hashmape ekle

//doAirDocIssue
* OrderCreate sorgusundan donen OrderID ve CurrencyPrice alani AirDocIssue servisindeki ilgili alana girilir
* "https://prepndc.flypgs.com/CraneNDC/CraneNDCService" servisine istek at


DOM MultiPort - (1 ADT + 1 CH + 1 INF) - RT - gidiş(SEAT+ CATERING + XBAG ) - dönüş(SEAT+CATERING + XBAG ) - MCO ile Ödeme
-----------------------------------------------------------------------------
tags: 22-NDCBiletlemeRTDomMultiport1Adt1Ch1InfMco
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir


INT MultiPort - (1 ADT + 1 CH + 1 INF) - RT - gidiş(SEAT+ CATERING + XBAG ) - dönüş(SEAT+CATERING + XBAG ) - MCO ile Ödeme
-----------------------------------------------------------------------------
tags: 23-NDCBiletlemeRTIntMultiport1Adt1Ch1InfMco
* Headers alanina gecerli kullanicinin Username ve Password bilgileri girilir
