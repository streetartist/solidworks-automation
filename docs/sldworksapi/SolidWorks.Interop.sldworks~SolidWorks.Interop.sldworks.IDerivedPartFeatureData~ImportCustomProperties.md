# ImportCustomProperties Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportCustomProperties`

Gets or sets which custom properties to import with the derived part feature.
Gets or sets which custom properties to import with the derived part feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ImportCustomProperties As System.Integer
```

```

Dim instance As IDerivedPartFeatureData
Dim value As System.Integer
 
instance.ImportCustomProperties = value
 
value = instance.ImportCustomProperties
```

```

System.int ImportCustomProperties {get; set;}
```

```

property System.int ImportCustomProperties {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Custom properties to import as defined in [swImportPartCustomPropertiesToOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swImportPartCustomPropertiesToOptions_e.html)

Remarks

This property is valid when:

- the derived part has custom properties,

    - and -

- [IDerivedPartFeatureData::ImportSolidBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportSolidBodies.md) is set to true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.md)  
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.md)
