package com.hunk.springbootdemo.Dao;

import org.apache.ibatis.annotations.*;

import java.util.List;

@Mapper
public interface CustomerMapper  {
    @Select("SELECT * FROM customers WHERE 1=1")
    List<Customer> findAll();


    @Select("SELECT * FROM customers WHERE id=#{id}")
    Customer findById(@Param("id") int id);


    @Insert("INSERT INTO customers(name, phone) VALUES(#{name}, #{phone})")
    int insert(@Param("name") String name, @Param("phone") String phone);


    @Update("UPDATE customers SET name=#{name}, phone=#{phone} WHERE id=#{id}")
    int update(@Param("id") int id,@Param("name") String name, @Param("phone") String phone);

}
