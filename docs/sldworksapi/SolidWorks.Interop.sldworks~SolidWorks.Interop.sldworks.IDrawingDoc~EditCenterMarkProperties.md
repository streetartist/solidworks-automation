# EditCenterMarkProperties Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditCenterMarkProperties`

Edits center mark properties.
Edits center mark properties.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub EditCenterMarkProperties( _
   ByVal Angle As System.Double, _
   ByVal Size As System.Double, _
   ByVal Lines As System.Boolean, _
   ByVal DocSettings As System.Boolean _
) 
```

```

Dim instance As IDrawingDoc
Dim Angle As System.Double
Dim Size As System.Double
Dim Lines As System.Boolean
Dim DocSettings As System.Boolean
 
instance.EditCenterMarkProperties(Angle, Size, Lines, DocSettings)
```

```

void EditCenterMarkProperties( 
   System.double Angle,
   System.double Size,
   System.bool Lines,
   System.bool DocSettings
)
```

```

void EditCenterMarkProperties( 
   System.double Angle,
   System.double Size,
   System.bool Lines,
   System.bool DocSettings
) 
```

#### Parameters

*Angle*
:   New angle of the center mark

*Size*
:   New size of the center mark

*Lines*
:   True displays the center mark lines, false displays the plus sign (+) at the circle  
    center

*DocSettings*
:   True uses the default settings for this document, false does not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md)
