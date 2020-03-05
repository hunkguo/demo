package com.hunk.springbootdemo.Dao;
import lombok.Data;

import javax.validation.constraints.*;

@Data
public class User {
    private long id;

    @NotNull
    @Size(min=4, max=10)
    private String name;

    @NotNull
    private String phone;

    public User (String name,String phone) {
        this.name = name;
        this.phone = phone;
    }

}
