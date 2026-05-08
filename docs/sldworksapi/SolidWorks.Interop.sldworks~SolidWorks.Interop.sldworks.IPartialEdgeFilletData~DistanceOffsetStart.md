# DistanceOffsetStart Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~DistanceOffsetStart`

Gets the offset distance from the start point for this partial edge fillet.
Gets the offset distance from the start point for this partial edge fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property DistanceOffsetStart As System.Double
```

```

Dim instance As IPartialEdgeFilletData
Dim value As System.Double
 
value = instance.DistanceOffsetStart
```

```

System.double DistanceOffsetStart {get;}
```

```

property System.double DistanceOffsetStart {
   System.double get();
}
```

#### Property Value

Distance offset from the start point

Remarks

This property is valid only if [IPartialEdgeFilletData::StartCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~StartCondition.md) is set to swSimpleFilletPartialEdgeCondition\_e.PartialEdgeDistanceOffset.

To modify the start distance offset of the fillet after creation, you must call [IPartialEdgeFilletData::SetPartialFilletParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~SetPartialFilletParameters.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.md)  
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.md)  
[IPartialEdgeFilletData::DistanceOffsetEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~DistanceOffsetEnd.md)
