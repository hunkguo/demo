package com.hunk.springbootdemo.Entity;

import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;

@Entity
@Data
public class Customer {

    @Id
    @GeneratedValue
    private int id;

    @NotEmpty(message = "客户名称不能为空！")
    private String name;

    @NotEmpty(message = "客户联系方式不能为空")
    private String phone;
}
