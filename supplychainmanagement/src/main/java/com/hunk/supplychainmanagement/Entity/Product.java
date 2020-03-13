package com.hunk.supplychainmanagement.Entity;

import lombok.Data;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.validation.constraints.NotEmpty;

@Entity
@Data
public class Product {

    @Id
    @GeneratedValue
    private int id;
    @Column(nullable = false, unique = true)
    @NotEmpty(message = "SKU不能为空！")
    private String sku;
    @Column(nullable = false, unique = true)
    @NotEmpty(message = "产品名称不能为空！")
    private String name;
    private String specification;
    private String feature;
    private String description;

}


