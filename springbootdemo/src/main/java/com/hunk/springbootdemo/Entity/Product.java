package com.hunk.springbootdemo.Entity;

import lombok.Data;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

@Entity
@Data
public class Product {

    @Id
    @GeneratedValue
    private int id;
    @Column(nullable = false, unique = true)
    private String sku;
    @Column(nullable = false, unique = true)
    private String name;
    private String specification;
    private String feature;
    private String description;

}


