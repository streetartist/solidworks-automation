# TickFrequency Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~TickFrequency`

Gets or sets the frequency of tick marks on a slider.
Gets or sets the frequency of tick marks on a slider.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TickFrequency As System.Integer
```

```

Dim instance As IPropertyManagerPageSlider
Dim value As System.Integer
 
instance.TickFrequency = value
 
value = instance.TickFrequency
```

```

System.int TickFrequency {get; set;}
```

```

property System.int TickFrequency {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Frequency of tick marks on slider

Remarks

If you set the frequency to 1, then a tick mark appears on every increment in the [range](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~SetRange.md). A value of 10 means that a tick mark appears every 10 increments in the range. If you do not set a frequency, then the frequency of tick marks default to 1.

[IPropertyManagerPageSlider::Style](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~Style.md) must be set to swPropMgrPageSliderStyle\_AutoTicks to set IPropertyManagerPageSlider::TickFrequency.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSlider Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider.md)  
[IPropertyManagerPageSlider Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider_members.md)
