package com.hunk.springbootdemo;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.ui.ModelMap;

@Controller
public class HelloController {

    @RequestMapping("/")
    public String index(ModelMap map){
        map.addAttribute("host", "www.qq.com");
        return "index";
    }
}
