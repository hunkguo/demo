package com.hunk.springbootdemo.Service;

import com.hunk.springbootdemo.Dao.Product;
import com.hunk.springbootdemo.Dao.ProductMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ProductServiceImpl implements ProductService{

    @Autowired
    private ProductMapper productMapper;

    @Override
    public List<Product> getList() {
        return productMapper.findAll();
    }

    @Override
    public int addProduct(Product p){
        try
        {
            productMapper.insert(p.getName(), p.getSku());
            return 1;
        }
        catch(Exception e)
        {
            return 0;
        }

    }

    @Override
    public Product findProductById(int id){
        Product p = productMapper.findById(id);
        return p;
    }

    @Override
    public int updateProduct(Product p){
        try{
            productMapper.update(p.getId(),p.getName(),p.getSku());
            return 1;
        }
        catch(Exception e)
        {
            return 0;
        }
    }

    @Override
    public int removeProduct(Product p){
        return 1;
    }
}
