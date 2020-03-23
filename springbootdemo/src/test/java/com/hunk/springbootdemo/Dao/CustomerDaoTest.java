package com.hunk.springbootdemo.Dao;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.annotation.Rollback;

public class CustomerDaoTest {

    //@Autowired
    //private  CustomerMapper customerMapper;

    @Test
    @Rollback
    public void test() throws Exception{

        //customerMapper.insert("hunkguo", "1367435987346");

        //list <Customer> c = customerMapper.findAll();

        //Customer c = customerMapper.findByName("hunkguo");

        //Assert.assertEquals("1367435987346", c.getPhone());

    }
}