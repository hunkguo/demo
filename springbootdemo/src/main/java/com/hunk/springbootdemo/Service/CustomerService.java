package com.hunk.springbootdemo.Service;

import com.hunk.springbootdemo.Dao.Customer;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public interface CustomerService {
    List<Customer> getList();
    Customer findCustomerById(int id);
    int addCustomer(Customer c);
    int updateCustomer(Customer c);
}
