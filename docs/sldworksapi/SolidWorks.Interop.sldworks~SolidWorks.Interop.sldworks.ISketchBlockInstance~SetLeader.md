# SetLeader Method (ISketchBlockInstance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~SetLeader`

Sets the leader style for this block instance.
Sets the leader style for this block instance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetLeader( _
   ByVal LeaderStyle As System.Integer, _
   ByVal ArrowHeadStyle As System.Integer _
) As System.Boolean
```

```

Dim instance As ISketchBlockInstance
Dim LeaderStyle As System.Integer
Dim ArrowHeadStyle As System.Integer
Dim value As System.Boolean
 
value = instance.SetLeader(LeaderStyle, ArrowHeadStyle)
```

```

System.bool SetLeader( 
   System.int LeaderStyle,
   System.int ArrowHeadStyle
)
```

```

System.bool SetLeader( 
   System.int LeaderStyle,
   System.int ArrowHeadStyle
) 
```

#### Parameters

*LeaderStyle*
:   Leader style as defined in [swLeaderStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderStyle_e.html)

*ArrowHeadStyle*
:   Arrowhead style as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

#### Return Value

True if the leader style is set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.md)  
[ISketchBlockInstance::GetArrowHeadStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetArrowHeadStyle.md)  
[ISketchBlockInstance::GetLeaderPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetLeaderPoints.md)  
[ISketchBlockInstance::GetLeaderStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetLeaderStyle.md)  
[ISketchBlockInstance::IGetLeaderPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IGetLeaderPoints.md)
