package com.hunk.springbootdemo.Dao;

import lombok.Data;

import javax.validation.constraints.NotNull;

@Data
public class Product {

    private int id;

    @NotNull
    private String sku;
    @NotNull
    private String name;

    private String specification;

    private String feature;

    private String description;

    public Product(String sku,String name,String specification, String feature,String description,Boolean isremove){
        this.id=id;
        this.sku=sku;
        this.name=name;
        this.specification=specification;
        this.feature=feature;
        this.description=description;
    }
}