package com.hunk.springbootdemo.Dao;

import lombok.Data;

import javax.validation.constraints.NotNull;

import static java.lang.Float.NaN;

@Data
public class Purchase {
    private Integer id;
    @NotNull
    private Integer product_id;

    @NotNull
    private Integer quantity;

    @NotNull
    private Number price;

    private String contact;

    public Purchase(Integer product_id,Integer quantity,Number price,String contact){
        this.product_id = product_id;
        this.quantity=quantity;
        this.price = price;
        this.contact=contact;

    }
}
