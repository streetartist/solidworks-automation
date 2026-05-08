# GussetType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~GussetType`

Gets or sets the type of this gusset.
Gets or sets the type of this gusset.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GussetType As System.Integer
```

```

Dim instance As ISMGussetFeatureData
Dim value As System.Integer
 
instance.GussetType = value
 
value = instance.GussetType
```

```

System.int GussetType {get; set;}
```

```

property System.int GussetType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of gusset as defined in [swSheetMetalRibGussetType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalRibGussetType_e.html)

Example

See the examples for [ISMGussetFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md)  
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.md)  
[ISMGussetFeatureData::EdgeFilletRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~EdgeFilletRadius.md)  
[ISMGussetFeatureData::FilletGussetEdges Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FilletGussetEdges.md)
