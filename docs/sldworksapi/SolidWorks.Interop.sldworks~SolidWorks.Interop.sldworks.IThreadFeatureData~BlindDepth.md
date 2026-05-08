# BlindDepth Property (IThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~BlindDepth`

Gets or sets the distance from the blind end condition reference of this thread feature, taking into account any offset.
Gets or sets the distance from the blind end condition reference of this thread feature, taking into account any offset.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BlindDepth As System.Double
```

```

Dim instance As IThreadFeatureData
Dim value As System.Double
 
instance.BlindDepth = value
 
value = instance.BlindDepth
```

```

System.double BlindDepth {get; set;}
```

```

property System.double BlindDepth {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.0 < Distance from the blind end condition reference; default is 0.01 m

Remarks

This property is valid only if [IThreadFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~EndCondition.md) is set to [swThreadEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swThreadEndCondition_e.html).swThreadEndCondition\_Blind.

Specify either a value or an equation that starts with an equal sign (=).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)
