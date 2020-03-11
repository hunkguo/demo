package com.hunk.springbootdemo.Entity;

import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepository extends JpaRepository<Product, Integer> {
    Product findProductById(int id);
}

