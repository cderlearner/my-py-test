sku_data = {"sku_data":
    [

    {
        "sku_id" : "932014047096762368",
        "quantity": 1
    },
    {
        "sku_id" : "111111",
        "quantity": 2
    }

 ],

}

data1 = sku_data["sku_data"]

for k in data1:
    print k["sku_id"]

if sku_data.get("sss") is None:
    print "haha"

SALES_SKU_ID_LIMITER = {
    "1" : 1,
    "2" : 1
}


if SALES_SKU_ID_LIMITER.get("2"):
    print "bbbb"





