package com.hunk.projectmanage.controller;

import com.hunk.projectmanage.entity.CompanyInfo;
import com.hunk.projectmanage.entity.CompanyInfoRepository;
import com.hunk.projectmanage.entity.ProjectInfo;
import com.hunk.projectmanage.entity.ProjectInfoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.transaction.Transactional;

@RestController
@RequestMapping("/")
public class HomeController {
    @Autowired
    private CompanyInfoRepository companyInfoRepository;
    @Autowired
    private ProjectInfoRepository projectInfoRepository;

    @Transactional
    @RequestMapping("")
    public String index(){
        CompanyInfo companyInfo=new CompanyInfo();
        companyInfo.setName("测试公司名称");

        ProjectInfo projectInfo=new ProjectInfo();
        projectInfo.setName("测试项目名称");

        projectInfo.getCompanyInfos().add(companyInfo);

        companyInfoRepository.save(companyInfo);
        projectInfoRepository.save(projectInfo);
        return "home";
    }
}
