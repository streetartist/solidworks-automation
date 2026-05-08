# SetPosition Method (IBreakLine)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~SetPosition`

Sets the locations of the break lines in the drawing view.
Sets the locations of the break lines in the drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetPosition( _
   ByVal Position1 As System.Double, _
   ByVal Position2 As System.Double _
) As System.Boolean
```

```

Dim instance As IBreakLine
Dim Position1 As System.Double
Dim Position2 As System.Double
Dim value As System.Boolean
 
value = instance.SetPosition(Position1, Position2)
```

```

System.bool SetPosition( 
   System.double Position1,
   System.double Position2
)
```

```

System.bool SetPosition( 
   System.double Position1,
   System.double Position2
) 
```

#### Parameters

*Position1*
:   Location of the first break line

*Position2*
:   Location of the second break line

#### Return Value

True if the break lines are positioned, false if not

Remarks

Call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) after calling this method.

Example

[Create Break View (VBA)](Create_Broken_View_Example_VB.htm)  
[Create Break View (VB.NET)](Create_Broken_View_Example_VBNET.htm)  
[Create Break View (C#)](Create_Broken_View_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBreakLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.md)  
[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.md)  
[IBreakline::GetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~GetPosition.md)
