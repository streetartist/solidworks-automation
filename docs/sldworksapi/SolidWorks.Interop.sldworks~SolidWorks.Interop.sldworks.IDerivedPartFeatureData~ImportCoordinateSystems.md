# ImportCoordinateSystems Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportCoordinateSystems`

Gets or sets whether to import coordinate systems with the derived part feature.
Gets or sets whether to import coordinate systems with the derived part feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ImportCoordinateSystems As System.Boolean
```

```

Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean
 
instance.ImportCoordinateSystems = value
 
value = instance.ImportCoordinateSystems
```

```

System.bool ImportCoordinateSystems {get; set;}
```

```

property System.bool ImportCoordinateSystems {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to import its coordinate systems, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.md)  
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.md)
