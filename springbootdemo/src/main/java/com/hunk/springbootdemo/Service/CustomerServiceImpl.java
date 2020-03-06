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
}
