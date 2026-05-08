# SetLeader Method (IGtol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetLeader`

Sets the characteristics of the leader for this symbol.
Sets the characteristics of the leader for this symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetLeader( _
   ByVal Leader As System.Boolean, _
   ByVal LeaderSide As System.Integer, _
   ByVal BentLeader As System.Boolean, _
   ByVal AllAround As System.Boolean _
) 
```

```

Dim instance As IGtol
Dim Leader As System.Boolean
Dim LeaderSide As System.Integer
Dim BentLeader As System.Boolean
Dim AllAround As System.Boolean
 
instance.SetLeader(Leader, LeaderSide, BentLeader, AllAround)
```

```

void SetLeader( 
   System.bool Leader,
   System.int LeaderSide,
   System.bool BentLeader,
   System.bool AllAround
)
```

```

void SetLeader( 
   System.bool Leader,
   System.int LeaderSide,
   System.bool BentLeader,
   System.bool AllAround
) 
```

#### Parameters

*Leader*
:   True enables a leader on this symbol, false disables it

*LeaderSide*
:   Leader attachment information as defined in [swLeaderSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderSide_e.html)

*BentLeader*
:   True enables a bent leader on this symbol, false disables it

*AllAround*
:   True enables the all around symbol on the leader, false disables it

Remarks

This method ignores:

- LeaderSide, BentLeader, and AllAround values if the leader value is false. Use [IGtol::IsAttached](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IsAttached.md) to determine if this symbol is currently using a leader.
- AllAround value if the BentLeader value is false. Use [IGtol::HasExtraLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~HasExtraLeader.md) to determine if this symbol is using a bent leader.

Use:

- [IGtol::GetLeaderSide](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderSide.md) to determine where the leader is attached to the symbol
- [IGtol::GetAllAround](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetAllAround.md) to determine if this leader is using the all around symbol

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetLeaderAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderAtIndex2.md)  
[IGtol::GetLeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderCount.md)  
[IGtol::GetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLeaderInfo.md)  
[IGtol::IGetLeaderAtIndex2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderAtIndex2.md)  
[IGtol::IGetLeaderInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLeaderInfo.md)
