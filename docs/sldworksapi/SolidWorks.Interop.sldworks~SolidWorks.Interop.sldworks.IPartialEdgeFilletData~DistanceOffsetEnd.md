# DistanceOffsetEnd Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~DistanceOffsetEnd`

Gets the offset distance from the end point for this partial edge fillet.
Gets the offset distance from the end point for this partial edge fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property DistanceOffsetEnd As System.Double
```

```

Dim instance As IPartialEdgeFilletData
Dim value As System.Double
 
value = instance.DistanceOffsetEnd
```

```

System.double DistanceOffsetEnd {get;}
```

```

property System.double DistanceOffsetEnd {
   System.double get();
}
```

#### Property Value

Distance offset from the end point

Remarks

This property is valid only if [IPartialEdgeFilletData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~EndCondition.md) is set to swSimpleFilletPartialEdgeCondition\_e.PartialEdgeDistanceOffset.

To modify the end distance offset of the fillet after creation, you must call [IPartialEdgeFilletData::SetPartialFilletParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~SetPartialFilletParameters.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.md)  
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.md)  
[IPartialEdgeFilletData::DistanceOffsetStart Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~DistanceOffsetStart.md)
