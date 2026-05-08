# SetArcLengthLeader Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetArcLengthLeader`

Sets the leader style of this arc-length dimension.
Sets the leader style of this arc-length dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetArcLengthLeader( _
   ByVal AutoLeader As System.Boolean, _
   ByVal LeaderType As System.Integer _
) As System.Integer
```

```

Dim instance As IDisplayDimension
Dim AutoLeader As System.Boolean
Dim LeaderType As System.Integer
Dim value As System.Integer
 
value = instance.SetArcLengthLeader(AutoLeader, LeaderType)
```

```

System.int SetArcLengthLeader( 
   System.bool AutoLeader,
   System.int LeaderType
)
```

```

System.int SetArcLengthLeader( 
   System.bool AutoLeader,
   System.int LeaderType
) 
```

#### Parameters

*AutoLeader*
:   True if the leader style is automatically selected, false if the leader style is  
    selected by the user

*LeaderType*
:   Leader style as defined in [swArcLengthLeaderType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArcLengthLeaderType_e.html) if autoLeader is false

#### Return Value

Return status:

|  |  |
| --- | --- |
| 0 | Command was successful, leader style values were set |
| -1 | Command failed for an unknown reason, no leader style values were set |
| -2 | Specified leader style value is not valid |

Remarks

The leader style of an arc length dimension is specific to each display dimension. The leader style can be parallel (the leaders are parallel to each other) or radial (the leaders are perpendicular to the extension line and would extend through the center of the arc). The style can be selected automatically by SOLIDWORKS, or specified by the user.

If the autoLeader value is passed in as True to automatically select the leader style, then SOLIDWORKS ignores the leaderStyle value.

This method applies only to arc length dimensions. It does not affect any other types of dimensions.

After using this method, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimensioin::GetArcLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetArcLengthLeader.md)
