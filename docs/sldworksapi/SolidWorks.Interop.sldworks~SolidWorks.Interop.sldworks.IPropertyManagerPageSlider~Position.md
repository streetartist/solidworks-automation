# Position Property (IPropertyManagerPageSlider)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~Position`

Gets or sets the current position of the slider.
Gets or sets the current position of the slider.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Position As System.Integer
```

```

Dim instance As IPropertyManagerPageSlider
Dim value As System.Integer
 
instance.Position = value
 
value = instance.Position
```

```

System.int Position {get; set;}
```

```

property System.int Position {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Current position of slider

Remarks

Position must be a value within the specified range. To get the range, use [IPropertyManagerPageSlider::GetRange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~GetRange.md); to set the range, use [IPropertyManagerPageSlider::SetRange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~SetRange.md).

If you do not set the initial position of a slider, then the value defaults to a position of 5.

Example

[Set Up PropertyManager Page Slider Control (C++)](Set_Up_PropertyManager_Page_Slider_Control_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSlider Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider.md)  
[IPropertyManagerPageSlider Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider_members.md)
