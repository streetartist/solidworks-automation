# NumberofSplitInstances Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~NumberofSplitInstances`

Gets the number of instances in this dimension split member.
Gets the number of instances in this dimension split member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NumberofSplitInstances As System.Integer
```

```

Dim instance As IStructureSystemSplitMember
Dim value As System.Integer
 
instance.NumberofSplitInstances = value
 
value = instance.NumberofSplitInstances
```

```

System.int NumberofSplitInstances {get; set;}
```

```

property System.int NumberofSplitInstances {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number of instances

Remarks

This property is valid only for [IStructureSystemSplitMember::DimensionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~DimensionType.md) set to [swSplitMemberDimensionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSplitMemberDimensionType_e.html).swSplitMemberDimensionType\_Instance.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemSplitMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember.md)  
[IStructureSystemSplitMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember_members.md)
