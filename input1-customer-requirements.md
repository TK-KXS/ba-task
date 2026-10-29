# Meeting notes – SiamMart Returns project (kickoff)

date: 22 Oct 2026 (??) , room 3B + Teams
attendees: K.Somchai (Head of CS, SiamMart), K.Nok (Store Ops), K.Pim (Finance), K.Arthit (IT SiamMart – joined late), TK team: BA x2, SA x1
notes by: BA (rough, not cleaned yet)

---

## background (what they said)

- SiamMart = retail chain ~120 สาขา + online shop (website + Shopee/Lazada)
- ตอนนี้ลูกค้าคืนของ / ขอ refund วุ่นวายมาก
- ลูกค้าคืนที่หน้าร้าน -> พนักงานจดลงกระดาษ / บางสาขาใช้ Excel -> ถ่ายรูปส่ง LINE group "Return-HQ" -> CS ที่ HQ ดูแล้วอนุมัติใน LINE -> Finance ทำ refund manual ใน SAP ทุกวันศุกร์
- online return: ลูกค้าส่ง email มา returns@siammart.co.th หรือทัก chat -> CS copy ลง Excel กลาง (shared drive) "RETURN_MASTER_v7_final_FINAL.xlsx" 555
- refund ใช้เวลาเฉลี่ย 14 วัน (K.Pim said 10-21 วัน depends), คู่แข่ง 3 วัน
- complaint เรื่อง refund ช้า = #1 complaint บน social ไตรมาสที่แล้ว (~2,300 complaints?? need confirm number)
- ของคืนกองอยู่หลังร้าน ไม่รู้ว่าต้องส่งกลับ DC หรือทิ้ง หรือขายลดราคา

## what they want (raw)

- "อยากได้ระบบ return ที่ทุกอย่างอยู่ที่เดียว"
- ลูกค้าต้อง request return ได้เองผ่าน web / app (app ยังไม่มี?? K.Somchai said "LINE OA ก็ได้")
- staff หน้าร้านใช้ tablet scan barcode ใบเสร็จ แล้วระบบดึง order มาเลย
- ถ้าราคาต่ำกว่า 500 บาท auto approve ได้เลย (K.Somchai) / K.Pim: "ไม่ได้ ต้องผ่าน finance ทุกรายการ ตาม audit" -> CONFLICT, unresolved
- ถ้าเกิน 5,000 ต้องให้ manager approve
- refund กลับเข้าบัตรเครดิต / promptpay / store credit (store credit ได้ bonus 5%? marketing idea, not confirmed)
- ต้องเชื่อม SAP (finance) – K.Arthit: SAP ECC 6.0, มี RFC แต่ไม่อยากให้ใครแตะตรง ๆ
- ต้องเชื่อม POS (vendor = "RetailPro"? or in-house? K.Arthit not sure)
- ต้องเชื่อม Shopee/Lazada return ด้วย?? -> phase 2 maybe
- dashboard ให้ผู้บริหารดู: จำนวน return, เหตุผล, สาขาไหนคืนเยอะ, fraud?
- แจ้งเตือนลูกค้าทุก step (SMS? LINE? email?) "เหมือน Kerry tracking"
- ของคืน ต้องมี flow ว่าจะ restock / ส่งกลับ supplier / write-off
- fraud: ลูกค้าบางคนคืนของทุกอาทิตย์ อยากให้ระบบ flag
- "ต้องใช้ง่ายมาก พนักงานบางคนอายุเยอะ"
- ต้องรองรับ peak หลัง 11.11 / 12.12 (return พุ่ง 4-5 เท่า)
- รูปถ่ายสินค้า ต้องเก็บไว้ (เก็บกี่ปี? audit บอก 7 ปี? not sure)
- ข้อมูลลูกค้า -> PDPA!! (K.Arthit concern)
- ภาษา TH/EN

## constraints / commercial

- budget: "ไม่เกิน 8 ล้าน phase 1" (K.Somchai) – Finance หน้าตาไม่ค่อยเห็นด้วย
- go-live ก่อน 11.11 ปีหน้า (Nov 2027) "ต้องทัน"
- อยาก pilot 10 สาขาก่อน (Bangkok)
- IT SiamMart มีคนแค่ 4 คน -> อยากให้ TK host + support (MA?) 
- ไม่อยากซื้อ license แพง ๆ

## open / unclear (BA to follow up)

- policy คืนสินค้า: 7 วัน? 14 วัน? ต่างกันตาม category? (electronics 7 วัน, อื่น ๆ 30?) -> ask K.Nok for policy doc
- ใครคือ owner ของ process นี้? CS หรือ Store Ops?
- partial return (คืนบางชิ้นใน order) ได้ไหม -> probably yes
- exchange (เปลี่ยนของ) อยู่ใน scope ไหม??
- จำนวน return / เดือน: K.Nok ~18k, K.Somchai ~25k ???
- ระบบเดิม Excel ต้อง migrate ไหม -> "ย้อนหลัง 1 ปีพอ"
- SSO กับ AD ของ SiamMart?

## random notes

- K.Somchai showed screenshot of competitor app – liked the "return QR code" idea (ลูกค้าได้ QR ไปยื่นหน้าร้าน)
- K.Pim wants daily refund report export to Excel (lol)
- someone mentioned "AI ตรวจรูปสภาพสินค้า" – nice to have, ignore for now?
- next meeting: walk-through store process at สาขาบางนา, date TBC
