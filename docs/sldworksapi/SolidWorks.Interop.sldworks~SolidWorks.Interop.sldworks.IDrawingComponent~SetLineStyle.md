# SetLineStyle Method (IDrawingComponent)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~SetLineStyle`

Sets the line style for the drawing component.
Sets the line style for the drawing component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetLineStyle( _
   ByVal LineFontOption As System.Integer, _
   ByVal Style As System.Integer _
) 
```

```

Dim instance As IDrawingComponent
Dim LineFontOption As System.Integer
Dim Style As System.Integer
 
instance.SetLineStyle(LineFontOption, Style)
```

```

void SetLineStyle( 
   System.int LineFontOption,
   System.int Style
)
```

```

void SetLineStyle( 
   System.int LineFontOption,
   System.int Style
) 
```

#### Parameters

*LineFontOption*
:   Line font style of the component as defined in [swDrawingComponentLineFontOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingComponentLineFontOption_e.html)

*Style*
:   Line style as defined in [swLineStyles\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html)

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
[IDrawingComponent::GetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetLineStyle.md)  
[IDrawingComponent::GetLineThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetLineThickness.md)  
[IDrawingComponent::SetLineThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~SetLineThickness.md)  
[IDrawingComponent::UseDocumentDefaults Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~UseDocumentDefaults.md)
