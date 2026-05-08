# EndConditionOffsetDistance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndConditionOffsetDistance`

Gets or sets the end condition offset distance of this thread feature.
Gets or sets the end condition offset distance of this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EndConditionOffsetDistance As System.Double
```

```

Dim instance As IThreadFeatureData
Dim value As System.Double
 
instance.EndConditionOffsetDistance = value
 
value = instance.EndConditionOffsetDistance
```

```

System.double EndConditionOffsetDistance {get; set;}
```

```

property System.double EndConditionOffsetDistance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.0 (default) < End condition offset distance

Remarks

This property is valid only if:

- [IThreadFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndCondition.md) is set to [swThreadEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swThreadEndCondition_e.html).swThreadEndCondition\_UpToSelection.

    - and -

- [IThreadFeatureData::EndConditionOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndConditionOffset.md) is set to true.

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)
