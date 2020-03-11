package com.hunk.springbootdemo.Controller;


import com.hunk.springbootdemo.Entity.Customer;
import com.hunk.springbootdemo.Entity.CustomerRepository;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.*;

@Controller
@RequestMapping("/customer")
public class CustomerController {
    @Autowired
    private CustomerRepository customerRepository;

    @GetMapping("")
    public String getCustomerList(Model model) {

        List<Customer> list=customerRepository.findAll();
        model.addAttribute("customers",list);
        model.addAttribute("isCustomerManage", true);
        return "customer/index";
    }


    @GetMapping("/create")
    public String getCreate(@ModelAttribute("customerInfo")  Customer customerInfo){
        return "customer/create";
    }

    @PostMapping("/save")
    public String postSave(@ModelAttribute(value = "customerInfo") Customer customerInfo){
        customerRepository.save(customerInfo);
        return "redirect:/customer";

    }



    @GetMapping("/edit")
    public String getEdit(@RequestParam("id") int id, Model model){
        Customer customerInfo = customerRepository.getOne(id);
        model.addAttribute("customerInfo", customerInfo);
        return "customer/edit";
    }

    @PostMapping("/update")
    public String postUpdate(@ModelAttribute(value = "customerInfo") Customer customerInfo){

        customerRepository.save(customerInfo);
        return "redirect:/customer";
    }

}


