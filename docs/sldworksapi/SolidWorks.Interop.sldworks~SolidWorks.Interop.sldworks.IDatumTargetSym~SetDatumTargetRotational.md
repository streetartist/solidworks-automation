# SetDatumTargetRotational Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDatumTargetRotational`

Sets this datum target to moveable rotational.
Sets this datum target to moveable rotational.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDatumTargetRotational( _
   ByVal MoveableDatumDirection As System.Integer, _
   ByVal LockLeader As System.Boolean, _
   ByVal LockLeaderAngle As System.Double, _
   ByVal GeometryRef As System.Boolean, _
   ByRef RefGeometryError As System.Integer _
) As System.Boolean
```

```

Dim instance As IDatumTargetSym
Dim MoveableDatumDirection As System.Integer
Dim LockLeader As System.Boolean
Dim LockLeaderAngle As System.Double
Dim GeometryRef As System.Boolean
Dim RefGeometryError As System.Integer
Dim value As System.Boolean
 
value = instance.SetDatumTargetRotational(MoveableDatumDirection, LockLeader, LockLeaderAngle, GeometryRef, RefGeometryError)
```

```

System.bool SetDatumTargetRotational( 
   System.int MoveableDatumDirection,
   System.bool LockLeader,
   System.double LockLeaderAngle,
   System.bool GeometryRef,
   out System.int RefGeometryError
)
```

```

System.bool SetDatumTargetRotational( 
   System.int MoveableDatumDirection,
   System.bool LockLeader,
   System.double LockLeaderAngle,
   System.bool GeometryRef,
   [Out] System.int RefGeometryError
) 
```

#### Parameters

*MoveableDatumDirection*
:   Moveable datum direction as defined in [swMoveableDatumDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMoveableDatumDirection_e.html)

*LockLeader*
:   True to lock the leader, false to not

*LockLeaderAngle*
:   Angle of locked leader; valid only if LockLeader is set to true

*GeometryRef*
:   True to use a geometry reference, false to not; true is valid only if MoveableDatumDirection is set to swMoveableDatumDirection\_e.swMoveableDatumDirectionBySelection

*RefGeometryError*
:   Reference geometry error as defined in [swRefGeometryError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRefGeometryError_e.html)

#### Return Value

True if datum target successfully set, false if errors

Remarks

If GeometryRef is set to true, then select a geometry reference before calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md)  
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.md)  
[IDatumTargetSym::SetDatumTargetNotMoveable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDatumTargetNotMoveable.md)  
[IDatumTargetSym::SetDatumTargetHorizontal Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~SetDatumTargetHorizontal.md)
