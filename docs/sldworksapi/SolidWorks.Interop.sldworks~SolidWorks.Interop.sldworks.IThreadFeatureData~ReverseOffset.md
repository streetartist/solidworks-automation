# ReverseOffset Property (IThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~ReverseOffset`

Gets or sets whether to flip the offset of the helix to the opposite side of the starting entity in this thread feature.
Gets or sets whether to flip the offset of the helix to the opposite side of the starting entity in this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReverseOffset As System.Boolean
```

```

Dim instance As IThreadFeatureData
Dim value As System.Boolean
 
instance.ReverseOffset = value
 
value = instance.ReverseOffset
```

```

System.bool ReverseOffset {get; set;}
```

```

property System.bool ReverseOffset {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flip the offset of the helix, false to not (default)

Remarks

This property is valid only if [IThreadFeatureData::Offset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Offset.md) is set to true.

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)
