package com.hunk.springbootdemo.Controller;


import com.hunk.springbootdemo.Dao.Customer;
import com.hunk.springbootdemo.Dao.CustomerMapper;
import com.hunk.springbootdemo.Dao.User;
import com.hunk.springbootdemo.Service.CustomerService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.*;

@Controller
@RequestMapping("/customer")
public class CustomerController {
    @Autowired
    private CustomerService customerService;

    @GetMapping("")
    public String getCustomerList(Model model) {

        //customerMapper.insert("hunkguo", "1367435987346");


        List<Customer> list=customerService.getList();
        model.addAttribute("customers",list);
        model.addAttribute("isCustomerManage", true);
        return "customer/index";
    }

    @GetMapping("/create")
    public String getCreate(@ModelAttribute("customerInfo")  Customer customerInfo){
        return "customer/create";
    }

    @PostMapping("/create")
    public String postCreate(@ModelAttribute(value = "customerInfo") Customer customerInfo){

        int result = customerService.addCustomer(customerInfo);

        if(result>0) {
            return "redirect:/customer";
        }
        else
        {
            return "redirect:/customer";
        }
    }



    @GetMapping("/intoUpdate")
    public String intoUpdate(@RequestParam("id") int id, Model model){
        Customer customerInfo = customerService.findCustomerById(id);
        model.addAttribute("customerInfo", customerInfo);
        return "customer/update";
    }

    @PostMapping("/saveupdate")
    public String saveUpdate(@ModelAttribute(value = "customerInfo") Customer customerInfo){

        int result = customerService.updateCustomer(customerInfo);

        if(result>0) {
            return "redirect:/customer";
        }
        else
        {
            return "redirect:/customer";
        }
    }
}


