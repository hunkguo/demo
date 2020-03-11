package com.hunk.springbootdemo.Service;

import com.hunk.springbootdemo.Dao.Purchase;
import com.hunk.springbootdemo.Dao.PurchaseMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PurchaseServiceImpl implements PurchaseService{

    @Autowired
    private PurchaseMapper purchaseMapper;

    @Override
    public List<Purchase> getList() {
        return purchaseMapper.findAll();
    }

    @Override
    public int addPurchase(Purchase p){
        try
        {
            purchaseMapper.insert(p.getProduct_id(), p.getQuantity(),p.getPrice(),p.getContact());
            return 1;
        }
        catch(Exception e)
        {
            return 0;
        }

    }

    @Override
    public Purchase findPurchaseById(int id){
        Purchase p = purchaseMapper.findById(id);
        return p;
    }

    @Override
    public int updatePurchase(Purchase p){
        try{
            purchaseMapper.update(p.getId(),p.getProduct_id(), p.getQuantity(),p.getPrice(),p.getContact());
            return 1;
        }
        catch(Exception e)
        {
            return 0;
        }
    }

    @Override
    public int removePurchase(Purchase p){
        return 1;
    }
}
