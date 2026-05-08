# Style Property (IPropertyManagerPageSlider)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~Style`

Gets or sets the display properties of a slider control.
Gets or sets the display properties of a slider control.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Style As System.Integer
```

```

Dim instance As IPropertyManagerPageSlider
Dim value As System.Integer
 
instance.Style = value
 
value = instance.Style
```

```

System.int Style {get; set;}
```

```

property System.int Style {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Display properties of slider control as defined in [swPropMgrPageSliderStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropMgrPageSliderStyle_e.html)

Remarks

If you do not set the any display properties, then the value is set to 0, which means:

- Slider is horizontal.
- Slider has not ticks.
- Your application is only notified when the user is done dragging the slider to move it.

Example

[Set Up PropertyManager Page Slider Control (C++)](Set_Up_PropertyManager_Page_Slider_Control_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSlider Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider.md)  
[IPropertyManagerPageSlider Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider_members.md)
