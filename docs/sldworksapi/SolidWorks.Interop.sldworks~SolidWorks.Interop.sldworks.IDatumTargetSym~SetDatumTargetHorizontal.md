# SetDatumTargetHorizontal Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDatumTargetHorizontal`

Sets this datum target to moveable horizontal.
Sets this datum target to moveable horizontal.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDatumTargetHorizontal( _
   ByVal MoveableDatumDirection As System.Integer, _
   ByVal LockLeader As System.Boolean, _
   ByVal LockLeaderAngle As System.Double _
) As System.Boolean
```

```

Dim instance As IDatumTargetSym
Dim MoveableDatumDirection As System.Integer
Dim LockLeader As System.Boolean
Dim LockLeaderAngle As System.Double
Dim value As System.Boolean
 
value = instance.SetDatumTargetHorizontal(MoveableDatumDirection, LockLeader, LockLeaderAngle)
```

```

System.bool SetDatumTargetHorizontal( 
   System.int MoveableDatumDirection,
   System.bool LockLeader,
   System.double LockLeaderAngle
)
```

```

System.bool SetDatumTargetHorizontal( 
   System.int MoveableDatumDirection,
   System.bool LockLeader,
   System.double LockLeaderAngle
) 
```

#### Parameters

*MoveableDatumDirection*
:   Moveable datum direction as defined in [swMoveableDatumDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMoveableDatumDirection_e.html)

*LockLeader*
:   True to lock the leader, false to not

*LockLeaderAngle*
:   Angle of locked leader; valid only if LockLeader is set to true

#### Return Value

True if this datum target is successfully set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md)  
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.md)  
[IDatumTargetSym::SetDatumTargetNotMoveable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDatumTargetNotMoveable.md)  
[IDatumTargetSym::SetDatumTargetRotational Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDatumTargetRotational.md)
