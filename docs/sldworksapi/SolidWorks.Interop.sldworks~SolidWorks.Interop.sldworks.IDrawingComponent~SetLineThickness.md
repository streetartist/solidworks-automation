# SetLineThickness Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~SetLineThickness`

Sets the line thickness for the drawing component.
Sets the line thickness for the drawing component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetLineThickness( _
   ByVal LineFontOption As System.Integer, _
   ByVal LineWeights As System.Integer, _
   ByVal Thickness As System.Double _
) 
```

```

Dim instance As IDrawingComponent
Dim LineFontOption As System.Integer
Dim LineWeights As System.Integer
Dim Thickness As System.Double
 
instance.SetLineThickness(LineFontOption, LineWeights, Thickness)
```

```

void SetLineThickness( 
   System.int LineFontOption,
   System.int LineWeights,
   System.double Thickness
)
```

```

void SetLineThickness( 
   System.int LineFontOption,
   System.int LineWeights,
   System.double Thickness
) 
```

#### Parameters

*LineFontOption*
:   Line font style of the component as defined in [swDrawingComponentLineFontOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingComponentLineFontOption_e.html)

*LineWeights*
:   Line weight style as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

*Thickness*
:   Thickness of line; only valid if LineWeights set to swLW\_CUSTOM

Example

[Get Components in Drawing View (C#)](Get_Components_in_Drawing_View_Example_CSharp.htm)  
[Get Components in Drawing View (VB.NET)](Get_Components_in_Drawing_View_Example_VBNET.htm)  
[Get Components in Drawing View (VBA)](Get_Components_in_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md)  
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.md)  
[IDrawingComponent::GetLineThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetLineThickness.md)  
[IDrawingComponent::GetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetLineStyle.md)  
[IDrawingComponent::SetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~SetLineStyle.md)  
[IDrawingComponent::UseDocumentDefaults Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~UseDocumentDefaults.md)
