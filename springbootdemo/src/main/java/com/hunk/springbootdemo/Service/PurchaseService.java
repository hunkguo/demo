package com.hunk.springbootdemo.Service;

import com.hunk.springbootdemo.Dao.Purchase;

import java.util.List;

public interface PurchaseService {
    List<Purchase> getList();
    Purchase findPurchaseById(int id);
    int addPurchase(Purchase p);
    int updatePurchase(Purchase p);
    int removePurchase(Purchase p);
}
