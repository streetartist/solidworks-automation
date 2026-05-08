# DirectionReference Property (IPrimaryMemberPointLengthFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~DirectionReference`

Gets and sets the reference indicating the direction of this member.
Gets and sets the reference indicating the direction of this member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DirectionReference As System.Object
```

```

Dim instance As IPrimaryMemberPointLengthFeatureData
Dim value As System.Object
 
instance.DirectionReference = value
 
value = instance.DirectionReference
```

```

System.object DirectionReference {get; set;}
```

```

property System.Object^ DirectionReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) or [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)

Remarks

This property is:

- required for 3D sketches.
- valid only when [IPrimaryMemberPointLengthFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~EndCondition.md) is [swPrimaryMemberPointLengthEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPrimaryMemberPointLengthEndCondition_e.html):
  - swPrimaryMemberPointLengthEndCondition\_UpToPlane
  - swPrimaryMemberPointLengthEndCondition\_Length

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberPointLengthFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.md)  
[IPrimaryMemberPointLengthFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData_members.md)
