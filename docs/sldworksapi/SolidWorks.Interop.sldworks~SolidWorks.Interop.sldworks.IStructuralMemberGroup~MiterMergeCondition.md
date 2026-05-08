# MiterMergeCondition Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~MiterMergeCondition`

Get or set whether to merge miter trimmed bodies in this structural-member group.
Get or set whether to merge miter trimmed bodies in this structural-member group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MiterMergeCondition As System.Boolean
```

```

Dim instance As IStructuralMemberGroup
Dim value As System.Boolean
 
instance.MiterMergeCondition = value
 
value = instance.MiterMergeCondition
```

```

System.bool MiterMergeCondition {get; set;}
```

```

property System.bool MiterMergeCondition {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to merge miter trimmed bodies, false to not

Remarks

This property is only available when [IStructuralMemberGroup::CornerTreatmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~CornerTreatmentType.md) is [swSolidworksWeldmentEndCondOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSolidworksWeldmentEndCondOptions_e.html).swEndConditionMiter.

Example

[Merge Miter Trimmed Bodies (C#)](Merge_Miter_Trimmed_Bodies_Example_CSharp.htm)  
[Merge Miter Trimmed Bodies (VB.NET)](Merge_Miter_Trimmed_Bodies_Example_VBNET.htm)  
[Merge Miter Trimmed Bodies (VBA)](Merge_Miter_Trimmed_Bodies_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)  
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.md)  
[IStructuralMemberGroup::ApplyCornerTreatment Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~ApplyCornerTreatment.md)
