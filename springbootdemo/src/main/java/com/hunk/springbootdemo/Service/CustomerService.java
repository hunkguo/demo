package com.hunk.springbootdemo.Service;

import com.hunk.springbootdemo.Dao.Customer;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public interface CustomerService {
    List<Customer> getList();
}