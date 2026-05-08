# GetArcEndCondition Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetArcEndCondition`

Gets the end conditions for linear dimensions that end on an arc.
Gets the end conditions for linear dimensions that end on an arc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArcEndCondition( _
   ByVal Index As System.Integer _
) As System.Integer
```

```

Dim instance As IDimension
Dim Index As System.Integer
Dim value As System.Integer
 
value = instance.GetArcEndCondition(Index)
```

```

System.int GetArcEndCondition( 
   System.int Index
)
```

```

System.int GetArcEndCondition( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of the endpoint to get the end condition from; 1 is the first endpoint, 2 is the second endpoint

#### Return Value

End condition as defined in [swArcEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArcEndCondition_e.html)

Remarks

In a linear dimension, the distance measured is from one point to another. If one or both of those points are on an arc, you can change the point to be the center of the arc, the nearest point on the arc, or the furthest point on the arc. The arc end condition describes which point is used.

Use [IDimension::SetArcEndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetArcEndCondition.md) to set the arc end conditions.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)  
[IDimension::SetArcEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetArcEndCondition.md)
