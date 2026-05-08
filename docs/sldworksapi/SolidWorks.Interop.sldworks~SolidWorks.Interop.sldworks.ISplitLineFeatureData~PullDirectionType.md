# PullDirectionType Property (ISplitLineFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~PullDirectionType`

Gets the type of entity indicating the direction of pull for this split line feature.
Gets the type of entity indicating the direction of pull for this split line feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property PullDirectionType As System.Integer
```

```

Dim instance As ISplitLineFeatureData
Dim value As System.Integer
 
value = instance.PullDirectionType
```

```

System.int PullDirectionType {get;}
```

```

property System.int PullDirectionType {
   System.int get();
}
```

#### Property Value

Type of entity as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

- swSelDATUMAXES
- swSelEDGES
- swSelFACES
- swSelDATUMPLANES
- swSelDATUMPOINT
- swSelVERTICES

Remarks

Before calling this property, call [ISplitLineFeatureData::PullDirectionBase](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~PullDirectionBase.md) to get the entity that indicates the pull direction.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.md)  
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.md)  
[ISplitLineFeatureData::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ReverseDirection.md)  
[ISplitLineFeatureData::SingleDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SingleDirection.md)
