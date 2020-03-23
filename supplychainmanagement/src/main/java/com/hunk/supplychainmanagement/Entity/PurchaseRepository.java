package com.hunk.supplychainmanagement.Entity;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface PurchaseRepository extends JpaRepository<Purchase, Integer> {

    public List<Purchase> findByProduct(Product product);
}
