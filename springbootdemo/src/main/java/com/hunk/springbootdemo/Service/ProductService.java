package com.hunk.springbootdemo.Service;

import com.hunk.springbootdemo.Dao.Product;

import java.util.List;

public interface ProductService {
    List<Product> getList();
    Product findProductById(int id);
    int addProduct(Product p);
    int updateProduct(Product p);
    int removeProduct(Product p);
}
