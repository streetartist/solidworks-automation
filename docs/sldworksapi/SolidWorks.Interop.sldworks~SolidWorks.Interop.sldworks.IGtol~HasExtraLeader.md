# HasExtraLeader Method (IGtol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~HasExtraLeader`

Gets whether the GTol has a bent leaderline or a straight leaderline.
Gets whether the GTol has a bent leaderline or a straight leaderline.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function HasExtraLeader() As System.Boolean
```

```

Dim instance As IGtol
Dim value As System.Boolean
 
value = instance.HasExtraLeader()
```

```

System.bool HasExtraLeader()
```

```

System.bool HasExtraLeader(); 
```

#### Return Value

True if extra leader line exists, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::IsAttached Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IsAttached.md)  
[IGtol::GetLeaderAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderAtIndex2.md)  
[IGtol::GetLeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderCount.md)  
[IGtol::GetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderInfo.md)  
[IGtol::GetLeaderSide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderSide.md)  
[IGtol::GetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLineAtIndex.md)  
[IGtol::IGetLeaderAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderAtIndex2.md)  
[IGtol::IGetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderInfo.md)  
[IGtol::IGetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLineAtIndex.md)  
[IGtol::SetLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetLeader.md)
