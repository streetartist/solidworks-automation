# GetExtents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~GetExtents`

Gets the coordinates on the drawing sheet format that define the extents of the title block.
Gets the coordinates on the drawing sheet format that define the extents of the title block.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetExtents( _
   ByRef XUpperLeft As System.Double, _
   ByRef YUpperLeft As System.Double, _
   ByRef XLowerRight As System.Double, _
   ByRef YLowerRight As System.Double _
) 
```

```

Dim instance As ITitleBlock
Dim XUpperLeft As System.Double
Dim YUpperLeft As System.Double
Dim XLowerRight As System.Double
Dim YLowerRight As System.Double
 
instance.GetExtents(XUpperLeft, YUpperLeft, XLowerRight, YLowerRight)
```

```

void GetExtents( 
   out System.double XUpperLeft,
   out System.double YUpperLeft,
   out System.double XLowerRight,
   out System.double YLowerRight
)
```

```

void GetExtents( 
   [Out] System.double XUpperLeft,
   [Out] System.double YUpperLeft,
   [Out] System.double XLowerRight,
   [Out] System.double YLowerRight
) 
```

#### Parameters

*XUpperLeft*
:   X upper-left coordinate

*YUpperLeft*
:   Y upper-left coordinate

*XLowerRight*
:   X lower-right coordinate

*YLowerRight*
:   Y lower-right coordinate

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITitleBlock Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock.md)  
[ITitleBlock Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock_members.md)  
[ITitleBlock::SetExtents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~SetExtents.md)
