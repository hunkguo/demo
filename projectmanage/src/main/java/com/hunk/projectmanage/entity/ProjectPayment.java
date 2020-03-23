package com.hunk.projectmanage.entity;

import lombok.Data;
import lombok.Generated;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.validation.constraints.NotEmpty;

@Data
@Entity
public class ProjectPayment {
    @Id
    @Generated
    private int id;
    /**
     * 项目名称
     */
    @NotEmpty(message="名称不能为空")
    private String name;

/*
    收款金额
            支付日期

    付款金额
            付款日期

 */
}
