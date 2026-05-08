# MergeArcSegmentBodies Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~MergeArcSegmentBodies`

Gets or sets whether to merge arc segment bodies with adjacent bodies in this structural-member group.
Gets or sets whether to merge arc segment bodies with adjacent bodies in this structural-member group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MergeArcSegmentBodies As System.Boolean
```

```

Dim instance As IStructuralMemberGroup
Dim value As System.Boolean
 
instance.MergeArcSegmentBodies = value
 
value = instance.MergeArcSegmentBodies
```

```

System.bool MergeArcSegmentBodies {get; set;}
```

```

property System.bool MergeArcSegmentBodies {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to merge arc segment bodies with adjacent bodies, false to not

Remarks

This property is valid for curved entities only. The arc segment and adjacent bodies must be tangent to merge.

Example

[Merge Arc Segment Bodies With Adjacent Bodies (C#)](Merge_Arc_Segment_Bodies_With_Adjacent_Bodies_Example_CSharp.htm)  
[Merge Arc Segment Bodies With Adjacent Bodies (VB.NET)](Merge_Arc_Segment_Bodies_With_Adjacent_Bodies_Example_VBNET.htm)  
[Merge Arc Segment Bodies With Adjacent Bodies (VBA)](Merge_Arc_Segment_Bodies_With_Adjacent_Bodies_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)  
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.md)
