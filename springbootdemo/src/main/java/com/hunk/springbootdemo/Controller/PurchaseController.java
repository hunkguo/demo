package com.hunk.springbootdemo.Controller;

import com.hunk.springbootdemo.Dao.Product;
import com.hunk.springbootdemo.Dao.Purchase;
import com.hunk.springbootdemo.Service.ProductService;
import com.hunk.springbootdemo.Service.PurchaseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
@RequestMapping("/purchase")
public class PurchaseController {
    @Autowired
    private PurchaseService purchaseService;
    @Autowired
    private ProductService productService;

    @GetMapping("")
    public String getPurchaseList(Model model) {

        List<Purchase> purchase_list=purchaseService.getList();
        model.addAttribute("purchases",purchase_list);
        model.addAttribute("isPurchaseManage", true);
        return "purchase/index";
    }

    @GetMapping("/create")
    public String getCreate(@ModelAttribute("purchaseInfo")  Purchase purchaseInfo,Model model){
        List<Product> product_list=productService.getList();
        model.addAttribute("product_list",product_list);
        return "purchase/create";
    }

    @PostMapping("/create")
    public String postCreate(@ModelAttribute(value = "purchaseInfo") Purchase purchaseInfo){

        int result = purchaseService.addPurchase(purchaseInfo);

        if(result>0) {
            return "redirect:/purchase";
        }
        else
        {
            return "redirect:/purchase";
        }
    }



    @GetMapping("/intoUpdate")
    public String intoUpdate(@RequestParam("id") int id, Model model){
        Purchase purchaseInfo = purchaseService.findPurchaseById(id);
        model.addAttribute("purchaseInfo", purchaseInfo);
        return "purchase/update";
    }

    @PostMapping("/saveupdate")
    public String saveUpdate(@ModelAttribute(value = "purchaseInfo") Purchase purchaseInfo){
        int result = purchaseService.updatePurchase(purchaseInfo);
        if(result>0) {
            return "redirect:/purchase";
        }
        else
        {
            return "redirect:/purchase";
        }
    }
}
