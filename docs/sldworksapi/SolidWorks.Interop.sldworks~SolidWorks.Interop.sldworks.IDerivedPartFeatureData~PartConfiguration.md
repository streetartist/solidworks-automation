# PartConfiguration Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~PartConfiguration`

Gets or sets the part configuration to use to create the derived part feature.
Gets or sets the part configuration to use to create the derived part feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PartConfiguration As System.String
```

```

Dim instance As IDerivedPartFeatureData
Dim value As System.String
 
instance.PartConfiguration = value
 
value = instance.PartConfiguration
```

```

System.string PartConfiguration {get; set;}
```

```

property System.String^ PartConfiguration {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of the part configuration to use; Nothing or null to use the Default configuration

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.md)  
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.md)
