package com.hunk.projectmanage.entity;

import lombok.Data;
import lombok.Generated;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.ManyToMany;
import javax.validation.constraints.NotEmpty;
import java.util.HashSet;
import java.util.Set;

@Data
@Entity
public class CompanyInfo {
    @Id
    @GeneratedValue
    private int id;
    /**
     *企业名称
     */
    @NotEmpty(message="公司名称不能为空")
    private String name;
    /**
     *社会信用代码
     */
    private String unifiedSocialCreditIdentifier;
    /**
     * 地址
     */
    private String address;
    /**
     * 联系人
     */
    private String contactPeople;
    /**
     * 联系电话
     */
    private String contactPhone;

    @ManyToMany(mappedBy = "companyInfos")  //配置多表关系
    private Set<ProjectInfo> projectInfos = new HashSet<ProjectInfo>();

}
