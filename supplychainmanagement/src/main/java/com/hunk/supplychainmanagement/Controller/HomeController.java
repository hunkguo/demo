package com.hunk.supplychainmanagement.Controller;

import antlr.StringUtils;
import org.springframework.security.web.WebAttributes;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.ui.Model;
import javax.servlet.http.HttpSession;


@Controller
@RequestMapping("/")
public class HomeController {

    private static final String FIELD_ERROR_MSG = "errorMsg";
    private static final String FIELD_ENABLE_CAPTCHA = "enableCaptcha";

    @RequestMapping("")
    public String index(){
        return "home";
    }

    @RequestMapping("/login")
    public String login(){
        return "login";
    }
}
