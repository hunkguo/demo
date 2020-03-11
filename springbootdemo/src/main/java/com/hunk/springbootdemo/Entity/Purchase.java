package com.hunk.springbootdemo.Entity;

import lombok.Data;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.validation.constraints.NotNull;

@Entity
@Data
public class Purchase {
    @Id
    @GeneratedValue
    private Integer id;
    //private Product product;
    private Integer quantity;
    private Number price;
    private String contact;
}
