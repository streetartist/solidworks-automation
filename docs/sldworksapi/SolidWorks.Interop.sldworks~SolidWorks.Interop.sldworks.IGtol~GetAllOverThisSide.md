# GetAllOverThisSide Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetAllOverThisSide`

Gets whether this GTol uses an All Over This Side leader.
Gets whether this GTol uses an All Over This Side leader.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAllOverThisSide() As System.Boolean
```

```

Dim instance As IGtol
Dim value As System.Boolean
 
value = instance.GetAllOverThisSide()
```

```

System.bool GetAllOverThisSide()
```

```

System.bool GetAllOverThisSide(); 
```

#### Return Value

True if this GTol uses an All Over This Side leader, false if not

Remarks

This property is valid only for bent, perpendicular, and multi-jog leaders. Call [IGtol::GetLeaderAtIndex2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderAtIndex2.md) to determine which type of leader is set for this GTol.

Use:

- [IGtol::IsAttached](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IsAttached.md) to determine whether this symbol is currently using a leader.
- [IGtol::HasExtraLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~HasExtraLeader.md) to determine whether this symbol is using a bent leader.
- [IGtol::GetLeaderSide](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderSide.md) to determine where the leader is attached to the symbol.
- [IGtol::SetLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetLeader.md) to set the characteristics of the leader on this symbol.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::SetAllOverThisSide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetAllOverThisSide.md)  
[IGtol::GetAllAroundThisSide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetAllAroundThisSide.md)
