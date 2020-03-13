package com.hunk.supplychainmanagement.Entity;

import lombok.Data;

import javax.persistence.*;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotNull;

@Entity
@Data
public class Purchase {
    @Id
    @GeneratedValue
    private Integer id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "product_id")
    @NotNull(message = "请选择产品！")
    private Product product;
    @Min(value=1,message = "采购数量不能为空！")
    private int quantity;
    @Min(value=1,message = "采购单价不能为空！")
    private float price;
    private String contact;
}
