# GapForOtherGroups Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~GapForOtherGroups`

Gets and sets the gap between segments in different structural-member groups.
Gets and sets the gap between segments in different structural-member groups.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GapForOtherGroups As System.Double
```

```

Dim instance As IStructuralMemberGroup
Dim value As System.Double
 
instance.GapForOtherGroups = value
 
value = instance.GapForOtherGroups
```

```

System.double GapForOtherGroups {get; set;}
```

```

property System.double GapForOtherGroups {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Gap in meters between segments in different groups

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
[IStructuralMemberGroup::GapWithinGroup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~GapWithinGroup.md)
