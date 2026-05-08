# SetRange Method (IPropertyManagerPageSlider)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~SetRange`

Sets the range of a slider.
Sets the range of a slider.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetRange( _
   ByVal Min As System.Integer, _
   ByVal Max As System.Integer _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPageSlider
Dim Min As System.Integer
Dim Max As System.Integer
Dim value As System.Boolean
 
value = instance.SetRange(Min, Max)
```

```

System.bool SetRange( 
   System.int Min,
   System.int Max
)
```

```

System.bool SetRange( 
   System.int Min,
   System.int Max
) 
```

#### Parameters

*Min*
:   Minimum range of slider

*Max*
:   Maximum range of slider

#### Return Value

True if range is set, false if not

Remarks

If you do not use this method to specify the range, it will default to a range of 0 to 10. Use [IPropertyManagerPageStyle::GetRange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~GetRange.md) to get the current range of the slider.

Example

[Set Up PropertyManager Page Slider Control (C++)](Set_Up_PropertyManager_Page_Slider_Control_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSlider Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider.md)  
[IPropertyManagerPageSlider Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider_members.md)
