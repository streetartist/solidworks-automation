# ImportSolidBodies Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportSolidBodies`

Gets or sets whether to import solid bodies with the derived part feature.
Gets or sets whether to import solid bodies with the derived part feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ImportSolidBodies As System.Boolean
```

```

Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean
 
instance.ImportSolidBodies = value
 
value = instance.ImportSolidBodies
```

```

System.bool ImportSolidBodies {get; set;}
```

```

property System.bool ImportSolidBodies {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to import its solid bodies, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.md)  
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.md)  
[IDerivedPartFeatureData::ImportModelDimensions Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportModelDimensions.md)  
[IDerivedPartFeatureData::ImportHoleWizardData Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportHoleWizardData.md)  
[IDerivedPartFeatureData::ImportCustomProperties Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportCustomProperties.md)
