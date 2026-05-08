# ImportSheetMetalInformation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportSheetMetalInformation`

Gets or sets how to import sheet metal information with the derived part feature.
Gets or sets how to import sheet metal information with the derived part feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ImportSheetMetalInformation As System.Integer
```

```

Dim instance As IDerivedPartFeatureData
Dim value As System.Integer
 
instance.ImportSheetMetalInformation = value
 
value = instance.ImportSheetMetalInformation
```

```

System.int ImportSheetMetalInformation {get; set;}
```

```

property System.int ImportSheetMetalInformation {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

How to import sheet metal information as defined in [swImportSheetMetalInformation\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swImportSheetMetalInformation_e.html)

Remarks

This property:

- is valid only if the part being inserted is a sheet metal part.
- is not valid if [IDerivedPartFeatureData::ImportCutListProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportCutListProperties.md) is set to true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.md)  
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.md)
