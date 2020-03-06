package com.hunk.springbootdemo.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/")
public class DashboardController {

    @GetMapping("")
    public String index(ModelMap map){
        map.addAttribute("title", "进销存管理系统");
        return "dashboard";
    }
}
