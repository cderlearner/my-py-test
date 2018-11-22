"""
1 order_type = 'special_gift' if item.sku_kind == SKUKind.SKU_KIND_PACKAGE else 'gift'

2 "100" if config.fee_payer == "zhihu" else "0"

3 result = [val for val in DEMO_SKU_CONFIG if val.sku_id == str(sku_id)]
  return result[0] if result else None

4 sum([val.real_amount for val in items])

5      params = dict(
            event=event_type,
            callback_url=req.extend_params.callback_url,
            order_id=req.get_order_id(),
            data=data
        )
        if req.is_async:
            send_order_notify_v2.delay(**params)
        else:
            sync_send_order_notify_v2(**params)
  
  
  
  
"""
