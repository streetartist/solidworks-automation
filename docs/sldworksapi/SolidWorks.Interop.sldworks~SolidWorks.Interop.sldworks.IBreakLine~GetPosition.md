# GetPosition Method (IBreakLine)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~GetPosition`

Gets the location of this break line in the drawing view.
Gets the location of this break line in the drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPosition( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As IBreakLine
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.GetPosition(Index)
```

```

System.double GetPosition( 
   System.int Index
)
```

```

System.double GetPosition( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Break line to work with (0 or 1)

#### Return Value

Location of the break line (see **Remarks**)

Remarks

A drawing view break consists of a pair of lines. This method gets the break line at the location indicated by the Index argument.

|  |  |
| --- | --- |
| **If the orientation of the break is...** | **Then the return value is...** |
| Horizontal | Y value relative to the drawing view origin (center) that indicates where the break is along the Y axis |
| Vertical | X value relative to the drawing view origin (center) that indicates where the break is along the X axis |

To determine the orientation of the break line, use [IBreakLine::Orientation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~Orientation.md) .

Example

[Create Break View (C#)](Create_Broken_View_Example_CSharp.htm)  
[Create Break View (VB.NET)](Create_Broken_View_Example_VBNET.htm)  
[Create Break View (VBA)](Create_Broken_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBreakLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.md)  
[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.md)  
[IBreakline::SetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~SetPosition.md)
