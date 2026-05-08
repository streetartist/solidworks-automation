# ReferenceOffsetStart Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetStart`

Gets the offset reference for the start condition for this partial edge fillet.
Gets the offset reference for the start condition for this partial edge fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ReferenceOffsetStart As System.Object
```

```

Dim instance As IPartialEdgeFilletData
Dim value As System.Object
 
value = instance.ReferenceOffsetStart
```

```

System.object ReferenceOffsetStart {get;}
```

```

property System.Object^ ReferenceOffsetStart {
   System.Object^ get();
}
```

#### Property Value

Offset reference (2D/3D sketch [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md), reference [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.md), planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md))

Remarks

This property is valid only if [IPartialEdgeFilletData::StartCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~StartCondition.md) is  swSimpleFilletPartialEdgeCondition\_e.PartialEdgeReferenceOffset.

Use [IPartialEdgeFilletData::ReferenceOffsetStartType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetStartType.md) to get the type of object returned by this property.

To modify reference offset for the start condition of the fillet after creation, you must call [IPartialEdgeFilletData::SetPartialFilletParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~SetPartialFilletParameters.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.md)  
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.md)
