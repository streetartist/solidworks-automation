# EdgeFilletRadius Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~EdgeFilletRadius`

Gets or sets the fillet radius of edges in this flat-back gusset.
Gets or sets the fillet radius of edges in this flat-back gusset.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EdgeFilletRadius As System.Double
```

```

Dim instance As ISMGussetFeatureData
Dim value As System.Double
 
instance.EdgeFilletRadius = value
 
value = instance.EdgeFilletRadius
```

```

System.double EdgeFilletRadius {get; set;}
```

```

property System.double EdgeFilletRadius {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Gusset edge fillet radius

Remarks

This property is valid only if [ISMGussetFeatureData::FilletGussetEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FilletGussetEdges.md) is true and [ISMGussetFeatureData::GussetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~GussetType.md) is set to 1.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md)  
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.md)
