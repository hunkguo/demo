package com.hunk.springbootdemo.Dao;

import org.apache.ibatis.annotations.*;

import java.util.List;

@Mapper
public interface ProductMapper {
    @Select("SELECT * FROM products WHERE isremove=1")
    List<Product> findAll();


    @Select("SELECT * FROM products WHERE id=#{id}")
    Product findById(@Param("id") int id);


    @Insert("INSERT INTO products(name, sku) VALUES(#{name}, #{sku})")
    int insert(@Param("name") String name, @Param("sku") String sku);


    @Update("UPDATE products SET name=#{name}, sku=#{sku} WHERE id=#{id}")
    int update(@Param("id") int id,@Param("name") String name, @Param("sku") String sku);
}


