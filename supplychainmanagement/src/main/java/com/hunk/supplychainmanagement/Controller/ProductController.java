package com.hunk.supplychainmanagement.Controller;

import com.hunk.supplychainmanagement.Entity.Customer;
import com.hunk.supplychainmanagement.Entity.Product;
import com.hunk.supplychainmanagement.Entity.ProductRepository;
import com.hunk.supplychainmanagement.Entity.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
@RequestMapping("/product")
public class ProductController {
    @Autowired
    private ProductRepository productRepository;

    @GetMapping("")
    public String getCustomerList(Model model) {

        List<Product> list=productRepository.findAll();
        model.addAttribute("products",list);
        model.addAttribute("isProductManage", true);
        return "product/index";
    }

    @GetMapping("/create")
    public String getCreate(@ModelAttribute("productInfo") Product productInfo){
        return "product/create";
    }

    @PostMapping("/save")
    public String postSave(@ModelAttribute(value = "productInfo") Product productInfo){
        productRepository.save(productInfo);
        return "redirect:/product";

    }

    @GetMapping("/edit/{id}")
    public String getEdit(@PathVariable("id") int id, Model model){
        Product productInfo = productRepository.getOne(id);
        model.addAttribute("productInfo", productInfo);
        return "product/edit";
    }

    @PostMapping("/update")
    public String postUpdate(@ModelAttribute(value = "productInfo") Product productInfo){

        productRepository.save(productInfo);
        return "redirect:/product";
    }

    @GetMapping("/delete/{id}")
    public String getDelete(@PathVariable("id") int id, Model model){
        Product productInfo = productRepository.getOne(id);
        productRepository.delete(productInfo);
        return "redirect:/product";
    }
}
