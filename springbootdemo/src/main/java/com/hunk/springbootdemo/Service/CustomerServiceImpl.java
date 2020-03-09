package com.hunk.springbootdemo.Service;

import com.hunk.springbootdemo.Dao.Customer;
import com.hunk.springbootdemo.Dao.CustomerMapper;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.List;

@Service
public class CustomerServiceImpl implements CustomerService{

    @Autowired
    private CustomerMapper customerMapper;

    @Override
    public List<Customer> getList() {
        return customerMapper.findAll();
    }

    @Override
    public int addCustomer(Customer c){
        try
        {
            customerMapper.insert(c.getName(), c.getPhone());
            return 1;
        }
        catch(Exception e)
        {
            return 0;
        }

    }

    @Override
    public Customer findCustomerById(int id){
        Customer c = customerMapper.findById(id);
        return c;
    }

    @Override
    public int updateCustomer(Customer c){
        try{
            customerMapper.update(c.getId(),c.getName(),c.getPhone());
            return 1;
        }
        catch(Exception e)
        {
            return 0;
        }
    }
}
