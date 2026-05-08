# GetRange Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~GetRange`

Gets the range of the slider.
Gets the range of the slider.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetRange( _
   ByRef Min As System.Integer, _
   ByRef Max As System.Integer _
) 
```

```

Dim instance As IPropertyManagerPageSlider
Dim Min As System.Integer
Dim Max As System.Integer
 
instance.GetRange(Min, Max)
```

```

void GetRange( 
   out System.int Min,
   out System.int Max
)
```

```

void GetRange( 
   [Out] System.int Min,
   [Out] System.int Max
) 
```

#### Parameters

*Min*
:   Minimum range of slider

*Max*
:   Maximum range of slider

Remarks

Use [IPropertyManagerPageSlider::SetRange](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider~SetRange.md) to set the range of the slider.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSlider Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider.md)  
[IPropertyManagerPageSlider Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider_members.md)
