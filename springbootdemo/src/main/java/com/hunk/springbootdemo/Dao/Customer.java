package com.hunk.springbootdemo.Dao;

import lombok.Data;

import javax.validation.constraints.NotNull;

@Data

public class Customer {

    private int id;
    @NotNull
    private String name;
    @NotNull
    private String phone;

    public Customer(String name, String phone){
        this.id = id;
        this.name = name;
        this.phone = phone;
    }

}

