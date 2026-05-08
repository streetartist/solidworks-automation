# ProfileLocation Property (IGussetFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~ProfileLocation`

Gets or sets where to locate the profile for this gusset feature.
Gets or sets where to locate the profile for this gusset feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProfileLocation As System.Integer
```

```

Dim instance As IGussetFeatureData
Dim value As System.Integer
 
instance.ProfileLocation = value
 
value = instance.ProfileLocation
```

```

System.int ProfileLocation {get; set;}
```

```

property System.int ProfileLocation {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Location of profile as defined by [swGussetProfileLocationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swGussetProfileLocationType_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.md)  
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.md)
