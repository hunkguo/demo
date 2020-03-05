package com.hunk.springbootdemo.Controller;


import com.hunk.springbootdemo.Dao.Customer;
import com.hunk.springbootdemo.Dao.CustomerMapper;
import com.hunk.springbootdemo.Dao.User;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.*;

@RestController
@RequestMapping("/customers")
public class CustomerController {

    @Autowired
    private  CustomerMapper customerMapper;

    @GetMapping("")
    public List<Customer> getCustomerList() {

        customerMapper.insert("hunkguo", "1367435987346");

        List<Customer> r = customerMapper.findAll();
        return r;
    }

}
