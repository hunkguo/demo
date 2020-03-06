package com.hunk.springbootdemo.Controller;


import com.hunk.springbootdemo.Dao.Customer;
import com.hunk.springbootdemo.Dao.CustomerMapper;
import com.hunk.springbootdemo.Dao.User;
import com.hunk.springbootdemo.Service.CustomerService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.*;

@Controller
@RequestMapping("/customers")
public class CustomerController {
    @Autowired
    private CustomerService customerService;

    @GetMapping("")
    public String getCustomerList(Model model) {

        //customerMapper.insert("hunkguo", "1367435987346");


        List<Customer> list=customerService.getList();
        model.addAttribute("customers",list);
        return "customer/index";
    }

}
