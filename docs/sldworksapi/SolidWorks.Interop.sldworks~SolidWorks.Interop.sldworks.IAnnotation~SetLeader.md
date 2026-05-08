# SetLeader Method (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader`

Obsolete. Superseded by IAnnotation::SetLeader3.
Obsolete. Superseded by [IAnnotation::SetLeader3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetLeader( _
   ByVal Leader As System.Boolean, _
   ByVal LeaderSide As System.Integer, _
   ByVal SmartArrowHeadStyle As System.Boolean, _
   ByVal BentLeader As System.Boolean _
) As System.Integer
```

```

Dim instance As IAnnotation
Dim Leader As System.Boolean
Dim LeaderSide As System.Integer
Dim SmartArrowHeadStyle As System.Boolean
Dim BentLeader As System.Boolean
Dim value As System.Integer
 
value = instance.SetLeader(Leader, LeaderSide, SmartArrowHeadStyle, BentLeader)
```

```

System.int SetLeader( 
   System.bool Leader,
   System.int LeaderSide,
   System.bool SmartArrowHeadStyle,
   System.bool BentLeader
)
```

```

System.int SetLeader( 
   System.bool Leader,
   System.int LeaderSide,
   System.bool SmartArrowHeadStyle,
   System.bool BentLeader
) 
```

#### Parameters

*Leader*

*LeaderSide*

*SmartArrowHeadStyle*

*BentLeader*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)
