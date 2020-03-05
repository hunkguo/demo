package com.hunk.springbootdemo.Dao;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface CustomerMapper  {
    @Select("SELECT * FROM customers WHERE 1=1")
    List<Customer> findAll();


    @Select("SELECT * FROM customers WHERE name=#{name}")
    Customer findByName(@Param("name") String name);


    @Insert("INSERT INTO customers(name, phone) VALUES(#{name}, #{phone})")
    int insert(@Param("name") String name, @Param("phone") String phone);
}
