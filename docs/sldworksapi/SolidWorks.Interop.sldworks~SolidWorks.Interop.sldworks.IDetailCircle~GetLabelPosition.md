# GetLabelPosition Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetLabelPosition`

Gets the position of the label of this detail circle.
Gets the position of the label of this detail circle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetLabelPosition( _
   ByRef XPosition As System.Double, _
   ByRef YPosition As System.Double _
) 
```

```

Dim instance As IDetailCircle
Dim XPosition As System.Double
Dim YPosition As System.Double
 
instance.GetLabelPosition(XPosition, YPosition)
```

```

void GetLabelPosition( 
   out System.double XPosition,
   out System.double YPosition
)
```

```

void GetLabelPosition( 
   [Out] System.double XPosition,
   [Out] System.double YPosition
) 
```

#### Parameters

*XPosition*
:   x coordinate of the label

*YPosition*
:   y coordinate of the label

Example

[Create Detail Circle and Detail View (VBA)](Create_Detail_Circle_and_Detail_View_Example_VB.htm)  
[Create Detail Circle and Detail View (VB.NET)](Create_Detail_Circle_and_Detail_View_Example_VBNET.htm)  
[Create Detail Circle and Detail View (C#)](Create_Detail_Circle_and_Detail_View_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)  
[IDetailCircle::SetLabelPosition Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetLabelPosition.md)  
[IDetailCircle::GetLabel Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetLabel.md)
