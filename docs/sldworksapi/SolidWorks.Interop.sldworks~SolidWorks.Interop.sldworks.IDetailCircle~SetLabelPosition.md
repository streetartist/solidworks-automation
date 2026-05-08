# SetLabelPosition Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetLabelPosition`

Sets the position of the label for this detail circle.
Sets the position of the label for this detail circle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetLabelPosition( _
   ByVal XPosition As System.Double, _
   ByVal YPosition As System.Double _
) 
```

```

Dim instance As IDetailCircle
Dim XPosition As System.Double
Dim YPosition As System.Double
 
instance.SetLabelPosition(XPosition, YPosition)
```

```

void SetLabelPosition( 
   System.double XPosition,
   System.double YPosition
)
```

```

void SetLabelPosition( 
   System.double XPosition,
   System.double YPosition
) 
```

#### Parameters

*XPosition*
:   x coordinate of the label

*YPosition*
:   y coordinate of the label

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)  
[IDetailCircle::GetLabelPosition Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetLabelPosition.md)  
[IDetailCircle::SetLabel Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetLabel.md)
