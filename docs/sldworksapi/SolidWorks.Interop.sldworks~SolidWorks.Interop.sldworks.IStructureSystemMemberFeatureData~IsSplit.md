# IsSplit Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~IsSplit`

Gets and sets whether this structure system member is split.
Gets and sets whether this structure system member is split.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IsSplit As System.Boolean
```

```

Dim instance As IStructureSystemMemberFeatureData
Dim value As System.Boolean
 
instance.IsSplit = value
 
value = instance.IsSplit
```

```

System.bool IsSplit {get; set;}
```

```

property System.bool IsSplit {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if this structure system member is split, false if not

Remarks

If this property is true, then use [IStructureSystemMemberFeatureData::GetSplitMember](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData~GetSplitMember.md) to access the split member.

Example

See the [IPrimaryMemberPathSegmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.md)  
[IStructureSystemMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData_members.md)
