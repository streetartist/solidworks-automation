# SplitLengthRevDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~SplitLengthRevDirection`

Gets and sets whether to reverse the direction of the length of this dimension split member.
Gets and sets whether to reverse the direction of the length of this dimension split member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SplitLengthRevDirection As System.Boolean
```

```

Dim instance As IStructureSystemSplitMember
Dim value As System.Boolean
 
instance.SplitLengthRevDirection = value
 
value = instance.SplitLengthRevDirection
```

```

System.bool SplitLengthRevDirection {get; set;}
```

```

property System.bool SplitLengthRevDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse the direction of the length, false to not

Remarks

This property is valid only for [IStructureSystemSplitMember::DimensionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember~DimensionType.md) set to [swSplitMemberDimensionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSplitMemberDimensionType_e.html).swSplitMemberDimensionType\_SplitLength.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemSplitMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember.md)  
[IStructureSystemSplitMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemSplitMember_members.md)
