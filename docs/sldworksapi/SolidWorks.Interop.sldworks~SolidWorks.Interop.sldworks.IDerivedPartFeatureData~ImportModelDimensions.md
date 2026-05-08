# ImportModelDimensions Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportModelDimensions`

Gets or sets whether to import model dimensions with the derived part feature.
Gets or sets whether to import model dimensions with the derived part feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ImportModelDimensions As System.Boolean
```

```

Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean
 
instance.ImportModelDimensions = value
 
value = instance.ImportModelDimensions
```

```

System.bool ImportModelDimensions {get; set;}
```

```

property System.bool ImportModelDimensions {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to import its model dimensions, false to not

Remarks

This property is valid onlty if [IDerivedPartFeatureData::ImportSolidBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportSolidBodies.md) is true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.md)  
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.md)
