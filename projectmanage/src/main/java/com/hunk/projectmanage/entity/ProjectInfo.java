package com.hunk.projectmanage.entity;

import lombok.Data;
import lombok.Generated;
import org.hibernate.annotations.Cascade;

import javax.persistence.*;
import javax.validation.constraints.NotEmpty;
import java.math.BigDecimal;
import java.util.Date;
import java.util.HashSet;
import java.util.Set;

@Data
@Entity
public class ProjectInfo {

    @Id
    @GeneratedValue
    private int id;
    /**
     * 项目名称
     */
    @NotEmpty(message="工程项目名称不能为空")
    private String name;

    /**
     * 项目简介
     */
    private String introduction;

    /**
     * 建筑面积
     */
    private String area;

    @ManyToMany(targetEntity=CompanyInfo.class, cascade=CascadeType.PERSIST)
    @JoinTable(
            joinColumns={@JoinColumn(name="project_id")},
            inverseJoinColumns = {@JoinColumn(name="company_id")})
    private Set<CompanyInfo> companyInfos =new HashSet<CompanyInfo>();
    /**
     * 第三方审计价格 Third-party audit prices
     */
    private BigDecimal thirdPartyAuditPrices;

    /**
     * 审计局价格 Audit Office Audit Price
     */
    private BigDecimal auditOfficeAuditPrice;

    /**
     * 招标情况   公共资源交易中心
     */

    /**
     * 招标项目编号
     */
    private String tenderNo;

    /**
     * 招标项目立项日期
     */
    private Date tenderCreateDate;
    /**
     * 开标日期
     */
    private Date tenderOpeningDate;
    /**
     * 开标价格
     */
    private BigDecimal tenderOpeningPrices;
    /**
     * 开标结果
     */
    private String tenderOpeningResult;

    /**
     * 项目证件办理情况
     */

    /**
     * 发改委立项
     */
    private String pcCreateProject;
    /**
     * 发改委备案
     */
    private String pcRecord;
    /**
     * 发改委项目建议书
     */
    private String pcProposal;

    /**
     * 选址意见书 permission notes for location
     */
    private String pcPermissionNotesForLocation;
    /**
     * 建设用地规划许可证 land use permit
     */
    private String pcLandUsePermit;
    /**
     * 建设工程规划许可证 building permit
     */
    private String pcBuildingPermit;
    /**
     * 国有土地使用证 State-owned Land Use Certificate
     */
    private String pcStateOwnedLandUseCertificate;
    /**
     * 建设项目施工许可证 Construction Permits for Construction Projects
     */
    private String pcConstructionPermitsforConstructionProjects;
    /**
     * 不动产所有权证 Real Property Ownership Certificate
     */
    private String pcRealPropertyOwnershipCertificate;



}
