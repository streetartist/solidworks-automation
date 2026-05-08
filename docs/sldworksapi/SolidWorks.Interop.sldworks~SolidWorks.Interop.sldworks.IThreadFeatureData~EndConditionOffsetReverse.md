# EndConditionOffsetReverse Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndConditionOffsetReverse`

Gets or sets whether to flip the offset of the end condition to the opposite side of the end condition reference in this thread feature.
Gets or sets whether to flip the offset of the end condition to the opposite side of the end condition reference in this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EndConditionOffsetReverse As System.Boolean
```

```

Dim instance As IThreadFeatureData
Dim value As System.Boolean
 
instance.EndConditionOffsetReverse = value
 
value = instance.EndConditionOffsetReverse
```

```

System.bool EndConditionOffsetReverse {get; set;}
```

```

property System.bool EndConditionOffsetReverse {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flip the offset, false to not (default)

Remarks

This property is valid only if:

- [IThreadFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndCondition.md) is set to [swThreadEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swThreadEndCondition_e.html).swThreadEndCondition\_UpToSelection.

   - and -

- [IThreadFeatureData::EndConditionOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndConditionOffset.md) is set to true.

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)
