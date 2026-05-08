# SetScale Method (ISheet)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetScale`

Sets the scale for this drawing sheet.
Sets the scale for this drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetScale( _
   ByVal Numerator As System.Double, _
   ByVal Denominator As System.Double, _
   ByVal ScaleAnnoPosition As System.Boolean, _
   ByVal ScaleAnnoTextHeight As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISheet
Dim Numerator As System.Double
Dim Denominator As System.Double
Dim ScaleAnnoPosition As System.Boolean
Dim ScaleAnnoTextHeight As System.Boolean
Dim value As System.Boolean
 
value = instance.SetScale(Numerator, Denominator, ScaleAnnoPosition, ScaleAnnoTextHeight)
```

```

System.bool SetScale( 
   System.double Numerator,
   System.double Denominator,
   System.bool ScaleAnnoPosition,
   System.bool ScaleAnnoTextHeight
)
```

```

System.bool SetScale( 
   System.double Numerator,
   System.double Denominator,
   System.bool ScaleAnnoPosition,
   System.bool ScaleAnnoTextHeight
) 
```

#### Parameters

*Numerator*
:   First value in the scale ratio (n : n)

*Denominator*
:   Second value in the scale ratio (n : n)

*ScaleAnnoPosition*
:   True if the position of the annotations is scaled, false if not

*ScaleAnnoTextHeight*
:   True if the text height of the annotations is scaled, false if not

#### Return Value

True if the scale is set, false if not

Remarks

You can get the two scale values from the sheet by using [ISheet::GetProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetProperties.md) or [ISheet::IGetProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~IGetProperties.md).

You can also set the two scale values by using [IDrawingDoc::SetupSheet4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet4.md) or [ISheet::SetProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetProperties.md). However, you cannot specify the scaling of the position or text height of the annotations. Instead, both of these methods automatically scale the position of the annotations but do not scale the text height of the annotations when the drawing is changed.

Example

[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)  
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)  
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.md)  
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.md)  
[ISheet::GetSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetSize.md)
