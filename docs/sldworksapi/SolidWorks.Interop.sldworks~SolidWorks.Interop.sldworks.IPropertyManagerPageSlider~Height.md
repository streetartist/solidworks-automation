# Height Property (IPropertyManagerPageSlider)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~Height`

Gets or sets the height of the slider control.
Gets or sets the height of the slider control.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Height As System.Short
```

```

Dim instance As IPropertyManagerPageSlider
Dim value As System.Short
 
instance.Height = value
 
value = instance.Height
```

```

System.short Height {get; set;}
```

```

property System.short Height {
   System.short get();
   void set (    System.short value);
}
```

#### Property Value

Height of slider control

Remarks

You can only set this property before the PropertyManager page is displayed.

Normally you should not use this property because SOLIDWORKS will size the slider appropriately based on its orientation and display properties. However, the complexity of the PropertyManager page's layout may make it necessary to use this property with [IPropertyManagerPageControl::Left](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~Left.md), [IPropertyManagerPageControl::Top](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~Top.md), and [IPropertyManagerPageControl::Width](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~Width.md) to get the desired look.

This property is also for creating a small slider by clearing the [IPropertyManagerPageSlider::Style](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~Style.md) swPropMgrPageSliderStyle\_AutoTicks bit and setting Height to a value less than the default. A horizontal slider without tick marks has a default height of 16. This height is in dialog-box units. You can convert this value to screen units (pixels) by using the Windows MapDialogRect function.

Example

[Set Up PropertyManager Page Slider Control (C++)](Set_Up_PropertyManager_Page_Slider_Control_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSlider Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider.md)  
[IPropertyManagerPageSlider Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider_members.md)
