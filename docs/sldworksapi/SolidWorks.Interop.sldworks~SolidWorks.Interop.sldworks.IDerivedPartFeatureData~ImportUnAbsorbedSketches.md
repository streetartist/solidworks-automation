# ImportUnAbsorbedSketches Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportUnAbsorbedSketches`

Gets or sets whether to import unabsorbed sketches with the derived part feature.
Gets or sets whether to import unabsorbed sketches with the derived part feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ImportUnAbsorbedSketches As System.Boolean
```

```

Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean
 
instance.ImportUnAbsorbedSketches = value
 
value = instance.ImportUnAbsorbedSketches
```

```

System.bool ImportUnAbsorbedSketches {get; set;}
```

```

property System.bool ImportUnAbsorbedSketches {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to import unabsorbed sketches, false to not

Example

[Modify Derived Part (C#)](Modify_Derived_Part_Example_CSharp.htm)  
[Modify Derived Part (VB.NET)](Modify_Derived_Part_Example_VBNET.htm)  
[Modify Derived Part (VBA)](Modify_Derived_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.md)  
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.md)  
[IDerivedPartFeatureData::ImportAbsorbedSketches Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportAbsorbedSketches.md)
