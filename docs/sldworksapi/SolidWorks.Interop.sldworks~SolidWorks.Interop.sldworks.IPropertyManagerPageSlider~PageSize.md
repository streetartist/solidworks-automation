# PageSize Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~PageSize`

Gets or sets how much the slider moves when the Page Up or Page Down keys are used to move the slider.
Gets or sets how much the slider moves when the Page Up or Page Down keys are used to move the slider.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PageSize As System.Integer
```

```

Dim instance As IPropertyManagerPageSlider
Dim value As System.Integer
 
instance.PageSize = value
 
value = instance.PageSize
```

```

System.int PageSize {get; set;}
```

```

property System.int PageSize {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

How much the slider moves when the Page Up or Page Down keys are used to move the slider

Remarks

If this property is not used to specified how the slider moves when the Page Up or Page Down keys are used to move the slider, the value defaults to 2.

Example

[Set Up PropertyManager Page Slider Control (C++)](Set_Up_PropertyManager_Page_Slider_Control_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSlider Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider.md)  
[IPropertyManagerPageSlider Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider_members.md)
