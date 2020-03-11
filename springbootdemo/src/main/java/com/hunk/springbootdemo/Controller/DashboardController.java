package com.hunk.springbootdemo.Controller;

import com.hunk.springbootdemo.Entity.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.hunk.springbootdemo.entity.User;

@Controller
@RequestMapping("/")
public class DashboardController {
    @Autowired
    private UserRepository userRepository;

    @GetMapping("")
    public String index(ModelMap map){
        return "dashboard";
    }
}
