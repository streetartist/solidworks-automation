# EndCondition Property (IThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndCondition`

Gets or sets the end condition for this thread feature.
Gets or sets the end condition for this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EndCondition As System.Integer
```

```

Dim instance As IThreadFeatureData
Dim value As System.Integer
 
instance.EndCondition = value
 
value = instance.EndCondition
```

```

System.int EndCondition {get; set;}
```

```

property System.int EndCondition {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Thread end condition as defined in [swThreadEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swThreadEndCondition_e.html); default is swThreadEndCondition\_e.swThreadEndCondition\_Blind

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)  
[IThreadFeatureData::GetEndConditionReference Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~GetEndConditionReference.md)  
[IThreadFeatureData::SetEndConditionReference Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~SetEndConditionReference.md)  
[IThreadFeatureData::BlindDepth Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~BlindDepth.md)  
[IThreadFeatureData::EndConditionOffset Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndConditionOffset.md)  
[IThreadFeatureData::EndConditionOffsetDistance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndConditionOffsetDistance.md)  
[IThreadFeatureData::EndConditionOffsetReverse Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndConditionOffsetReverse.md)  
[IThreadFeatureData::MaintainThreadLength Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MaintainThreadLength.md)  
[IThreadFeatureData::ReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~ReverseDirection.md)  
[IThreadFeatureData::Revolutions Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Revolutions.md)
