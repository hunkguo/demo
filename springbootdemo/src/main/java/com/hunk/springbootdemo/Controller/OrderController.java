package com.hunk.springbootdemo.Controller;

import com.hunk.springbootdemo.Entity.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@Controller
@RequestMapping("/order")
public class OrderController {
    @Autowired
    private CustomerRepository customerRepository;
    @Autowired
    private ProductRepository productRepository;
    @Autowired
    private OrderRepository orderRepository;

    @GetMapping("")
    public String getOrderList(Model model) {

        List<Order> list=orderRepository.findAll();
        model.addAttribute("order",list);
        model.addAttribute("isOrderManage", true);
        return "order/index";
    }
    
    @GetMapping("/create")
    public String getCreate(@ModelAttribute("orderInfo") Order orderInfo, Model model){
        List<Product> product_list=productRepository.findAll();
        List<Customer> customer_list=customerRepository.findAll();
        model.addAttribute("product_list",product_list);
        model.addAttribute("customer_list",customer_list);
        return "order/create";
    }
    @PostMapping("/save")
    public String postSave(@ModelAttribute(value = "orderInfo") @Valid Order orderInfo){
        orderRepository.save(orderInfo);
        return "redirect:/order";

    }
    @GetMapping("/edit/{id}")
    public String getEdit(@PathVariable("id") int id, Model model){
        Order orderInfo = orderRepository.getOne(id);
        List<Product> product_list=productRepository.findAll();
        List<Customer> customer_list=customerRepository.findAll();
        model.addAttribute("product_list",product_list);
        model.addAttribute("customer_list",customer_list);
        model.addAttribute("orderInfo", orderInfo);
        return "order/edit";
    }

    @PostMapping("/update")
    public String postUpdate(@ModelAttribute(value = "orderInfo") @Valid Order orderInfo){

        orderRepository.save(orderInfo);
        return "redirect:/order";
    }

    @GetMapping("/delete/{id}")
    public String getDelete(@PathVariable("id") int id, Model model){
        Order orderInfo = orderRepository.getOne(id);
        orderRepository.delete(orderInfo);
        return "redirect:/order";
    }
}
