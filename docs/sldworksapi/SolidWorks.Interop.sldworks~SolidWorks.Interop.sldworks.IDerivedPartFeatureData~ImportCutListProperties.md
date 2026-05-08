# ImportCutListProperties Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportCutListProperties`

Gets or sets whether to import cut list properties with the derived part feature.
Gets or sets whether to import cut list properties with the derived part feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ImportCutListProperties As System.Boolean
```

```

Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean
 
instance.ImportCutListProperties = value
 
value = instance.ImportCutListProperties
```

```

System.bool ImportCutListProperties {get; set;}
```

```

property System.bool ImportCutListProperties {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to import its cut list properties, false to not

Remarks

This property is valid only if:

- the derived part has cut list properties,

   - and -

- [IDerivedPartFeatureData::ImportSheetMetalInformation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportSheetMetalInformation.md) is not specified.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.md)  
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.md)
