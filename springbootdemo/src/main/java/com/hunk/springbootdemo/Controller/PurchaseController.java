package com.hunk.springbootdemo.Controller;

import com.hunk.springbootdemo.Entity.Product;
import com.hunk.springbootdemo.Entity.ProductRepository;
import com.hunk.springbootdemo.Entity.Purchase;
import com.hunk.springbootdemo.Entity.PurchaseRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
@RequestMapping("/purchase")
public class PurchaseController {
    @Autowired
    private PurchaseRepository purchaseRepository;
    @Autowired
    private ProductRepository productRepository;

    @GetMapping("")
    public String getPurchaseList(Model model) {

        List<Purchase> list=purchaseRepository.findAll();
        model.addAttribute("purchases",list);
        model.addAttribute("isPurchaseManage", true);
        return "purchase/index";
    }
    @GetMapping("/create")
    public String getCreate(@ModelAttribute("purchaseInfo") Purchase purchaseInfo,Model model){
        List<Product> list=productRepository.findAll();
        model.addAttribute("product_list",list);
        return "purchase/create";
    }

    @PostMapping("/save")
    public String postSave(@ModelAttribute(value = "purchaseInfo") Purchase purchaseInfo){
        purchaseRepository.save(purchaseInfo);
        return "redirect:/purchase";

    }
    @GetMapping("/edit/{id}")
    public String getEdit(@PathVariable("id") int id, Model model){
        Purchase purchaseInfo = purchaseRepository.getOne(id);
        List<Product> list=productRepository.findAll();
        model.addAttribute("product_list",list);
        model.addAttribute("purchaseInfo", purchaseInfo);
        return "purchase/edit";
    }

    @PostMapping("/update")
    public String postUpdate(@ModelAttribute(value = "purchaseInfo") Purchase purchaseInfo){

        purchaseRepository.save(purchaseInfo);
        return "redirect:/purchase";
    }

    @GetMapping("/delete/{id}")
    public String getDelete(@PathVariable("id") int id, Model model){
        Purchase purchaseInfo = purchaseRepository.getOne(id);
        purchaseRepository.delete(purchaseInfo);
        return "redirect:/purchase";
    }
}
