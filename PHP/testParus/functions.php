<?php

function getURL($url, $page){

    $pageNum = $page;

    $fields = [
        'ctl00$ctl00$BodyScripts$BodyScripts$scripts' => 'ctl00$ctl00$MainContent$ContentPlaceHolderMiddle$UpdatePanel2|ctl00$ctl00$MainContent$ContentPlaceHolderMiddle$PurchasesSearchResult$ctl01$ctl' . $pageNum,
        'ctl00$ctl00$LeftContentLogin$ctl00$Login1$UserName' => '',
        'ctl00$ctl00$LeftContentLogin$ctl00$Login1$Password' => '',
        'ctl00$ctl00$LeftContentSideMenu$mSideMenu$extAccordionMenu_AccordionExtender_ClientState' => '0',
        'ctl00$ctl00$MainExpandableArea$phExpandCollapse$PurchasesSearchCriteria$vPurchaseLot_lotNumber_лота' => '',
        'ctl00$ctl00$MainExpandableArea$phExpandCollapse$PurchasesSearchCriteria$vPurchaseLot_purchaseNumber_торга' => '',
        'ctl00$ctl00$MainExpandableArea$phExpandCollapse$PurchasesSearchCriteria$vPurchaseLot_lotTitle_Наименованиелота' => '',
        'ctl00$ctl00$MainExpandableArea$phExpandCollapse$PurchasesSearchCriteria$vPurchaseLot_fullTitle_Наименованиеторга' => '',
        'ctl00$ctl00$MainExpandableArea$phExpandCollapse$PurchasesSearchCriteria$Party_contactName_AliasFullOrganizerTitle' => '',
        'ctl00$ctl00$MainExpandableArea$phExpandCollapse$PurchasesSearchCriteria$vPurchaseLot_InitialPrice_Начальнаяценаотруб' => '',
        'ctl00$ctl00$MainExpandableArea$phExpandCollapse$PurchasesSearchCriteria$Party_inn_ИННорганизатора' => '',
        'ctl00$ctl00$MainExpandableArea$phExpandCollapse$PurchasesSearchCriteria$vPurchaseLot_bargainTypeID_Типторгов$ddlBargainType' => '10,11,12,111,13',
        'ctl00$ctl00$MainExpandableArea$phExpandCollapse$PurchasesSearchCriteria$Party_kpp_КППорганизатора' => '',
        'ctl00$ctl00$MainExpandableArea$phExpandCollapse$PurchasesSearchCriteria$BargainType_PriceForm_Формапредставленияпредложенийоцене' => '',
        'ctl00$ctl00$MainExpandableArea$phExpandCollapse$PurchasesSearchCriteria$Party_registeredAddress_Адресрегистрацииорганизатора' => '',
        'ctl00$ctl00$MainExpandableArea$phExpandCollapse$PurchasesSearchCriteria$vPurchaseLot_purchaseStatusID_Статус' => '',
        'ctl00$ctl00$MainExpandableArea$phExpandCollapse$PurchasesSearchCriteria$vPurchaseLot_BankruptName_Должник' => '',
        'ctl00$ctl00$MainExpandableArea$phExpandCollapse$PurchasesSearchCriteria$vPurchaseLot_BankruptINN_ИННдолжника' => '',
        '__EVENTTARGET'      => 'ctl00$ctl00$MainContent$ContentPlaceHolderMiddle$PurchasesSearchResult$ctl01$ctl' . $pageNum,
        '__EVENTARGUMENT' => '',
        '__VIEWSTATE' => '',
        '__SCROLLPOSITIONX' => '0',
        '__SCROLLPOSITIONY' => '0',
        '__EVENTVALIDATION' => '/wEdAC6vVXD1oYELeveMr0vHCmYPlMMwQdi9JE76XlDpiyGaGiK96Mh9z4MIAfI7yfbJUJsPO+W3lSX2/DWdCcCk3rJcyrcU+tH5HkUc0Yvcf5zJEfusfBu+8729k/lgDp402W3yZda1D3HpWSYwxVupBiDzqZcHwbjqlDITs67gXqoxNfGKJSyCDYUib6o0oO8HtPHXJt2lfoMywfGSYlr349hf1wsLz3uVDitIdW1lZLNUmyYlrA4KHjyQob8WN+OdgrOZQAlyEt7Ac1iMlWMve+MqqCrsOUlQmNy2NVlpKLTT57KnTrdrpaAhfRt5qtVLlLcHcNdJhcYI2VcxDA8VD3Ir+jo7rW34WQv2uKzvBI7h4wBshHV0UIxpVFC1vlt3IMv8FrmcMA/yYnzif9kvRnCBD+RzX2l6mETVSBYx/UgUBHyHS5ZYjtauxgBEt62NdpIcqqY4BfzDM3lEX3obQti9WxfXD8eq6AxVt+kZUqFymAx2CH+fmzFtIq6i3fRDE/CuQ9QkBrLRMoFzjNDPxTpy8t2eeMu4k5kMRztz2F6QpYlLhuk8SCesJY2cTWDGlKRR3qZjAUm5VohdIZTxgFtOwsthPrTfRJ1uz+Nuez56w2YpZWYcCxx3FNqgnWJck90R09dKJkUOzVGXvOctQ1XW1mgMvxtEvWPOp8+H5hp2uEqdpRZYka0e9HAecvAqjHHHGctzL2A0QUlkveF1yD+xs3VEL+tyDD2I2qKykC/B4RoSiaxRjewt3vKD8rA0rdjWgnn3CFbkRmaUb7S0y6wn/5xKIctnAx3op92ZwSyib8TBr0toBdLCJQzJ7bsV7REiaW64Grk4DXQTXa1aiMAyCjeHuz2YkgjgoXS1Znq2SswbSzaLLvEl5rMHIacrVnClK99uVWJkVmsOAAKMmpYegqyXE+ftg4U+17fn5qnGQmsoO3JUsyYElzrSDhh9iLPcSV/bqObCqsFGwbQg+Wt3pEusXKgPCCPNeNJtAvZOcB6wlut9wTtFGbWqbY+MRpM=',
        '__CVIEWSTATE' => '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',
        '__ASYNCPOST' => true
    
    ];

$fields_string = http_build_query($fields);

$ch = curl_init();

curl_setopt($ch,CURLOPT_URL, $url);
curl_setopt($ch,CURLOPT_POST, true);
curl_setopt($ch,CURLOPT_RETURNTRANSFER, true); 
curl_setopt($ch, CURLOPT_HEADER, 0);
curl_setopt($ch,CURLOPT_POSTFIELDS, $fields_string);

$html = curl_exec($ch);
file_put_contents('1.html', $html);
}

