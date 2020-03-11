package com.hunk.springbootdemo.Dao;


import org.apache.ibatis.annotations.*;

import java.util.List;

@Mapper
public interface PurchaseMapper {
    @Select("SELECT * FROM purchases INNER JOIN products ON products.id=purchases.product_id WHERE purchases.isremove=1")
    List<Purchase> findAll();


    @Select("SELECT * FROM purchases WHERE id=#{id}")
    Purchase findById(@Param("id") int id);


    @Insert("INSERT INTO purchases(product_id,quantity, price,contact) VALUES(#{product_id}, #{quantity}, #{price}, #{contact})")
    int insert(@Param("product_id") int product_id, @Param("quantity") int quantity, @Param("price") Number price, @Param("contact") String contact);


    @Update("UPDATE purchases SET product_id=#{product_id}, quantity=#{quantity}, price=#{price}, contact=#{contact} WHERE id=#{id}")
    int update(@Param("id") int id,@Param("product_id") int product_id, @Param("quantity") int quantity, @Param("price") Number price, @Param("contact") String contact);
}
