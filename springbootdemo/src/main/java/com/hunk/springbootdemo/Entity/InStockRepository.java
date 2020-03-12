package com.hunk.springbootdemo.Entity;

import org.springframework.data.jpa.repository.JpaRepository;

public interface InStockRepository extends JpaRepository<InStock, Integer> {
}
