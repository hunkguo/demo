package com.hunk.supplychainmanagement.Entity;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ProductImageRepository extends JpaRepository<ProductImage, Integer> {
    public List<ProductImage> findByProduct(Product product);
}
