# SetArcEndCondition Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetArcEndCondition`

Sets the end conditions for linear dimensions that end on an arc.
Sets the end conditions for linear dimensions that end on an arc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetArcEndCondition( _
   ByVal Index As System.Integer, _
   ByVal Condition As System.Integer _
) As System.Integer
```

```

Dim instance As IDimension
Dim Index As System.Integer
Dim Condition As System.Integer
Dim value As System.Integer
 
value = instance.SetArcEndCondition(Index, Condition)
```

```

System.int SetArcEndCondition( 
   System.int Index,
   System.int Condition
)
```

```

System.int SetArcEndCondition( 
   System.int Index,
   System.int Condition
) 
```

#### Parameters

*Index*
:   Index of the endpoint on which to set the end condition; 1 is the first endpoint, 2 is the second endpoint

*Condition*
:   End condition as defined in [swArcEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArcEndCondition_e.html)

#### Return Value

Indicates the success or failure of this method:

|  |  |
| --- | --- |
| 0 | Command was successful; the arc end condition was set |
| -1 | Command failed for an unknown reason; the arc end condition was not set |
| -2 | Index parameter is invalid |
| -3 | Condition parameter is invalid |
| -4 | Endpoint 1 is not related to an arc |
| -5 | Endpoint 2 is not related to an arc |

Remarks

Linear dimensions measure the distance from one point to another. If one or both of those points is on an arc, the point can be changed to the center point of the arc, the nearest point on the arc, or the furthest point on the arc. The arc end condition describes which point to use.

Use [IDimension::GetArcEndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetArcEndCondition.md) to get the arc end conditions.

To see the effects of changing the arc endpoint conditions, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)  
[IDimension::GetArcEndCondition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetArcEndCondition.md)
