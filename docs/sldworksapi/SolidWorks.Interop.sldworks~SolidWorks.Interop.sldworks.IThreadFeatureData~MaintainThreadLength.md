# MaintainThreadLength Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MaintainThreadLength`

Gets or sets whether to keep the thread a constant length from the starting surface in this thread feature.
Gets or sets whether to keep the thread a constant length from the starting surface in this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MaintainThreadLength As System.Boolean
```

```

Dim instance As IThreadFeatureData
Dim value As System.Boolean
 
instance.MaintainThreadLength = value
 
value = instance.MaintainThreadLength
```

```

System.bool MaintainThreadLength {get; set;}
```

```

property System.bool MaintainThreadLength {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to maintain a constant thread length, false to not (default)

Remarks

This property is valid only if:

- [IThreadFeatureData::Offset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Offset.md) is set to true.
- [IThreadFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndCondition.md) is set to [swThreadEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swThreadEndCondition_e.html):

> - swThreadEndCondition\_Blind
>
>     - or -
>
> - swThreadEndCondition\_Revolutions

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)
