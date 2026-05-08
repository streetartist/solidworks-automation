# ProfileDistance4 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~ProfileDistance4`

Gets or sets the distance for the Profile Distance 4 parameter for this gusset feature.
Gets or sets the distance for the Profile Distance 4 parameter for this gusset feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProfileDistance4 As System.Double
```

```

Dim instance As IGussetFeatureData
Dim value As System.Double
 
instance.ProfileDistance4 = value
 
value = instance.ProfileDistance4
```

```

System.double ProfileDistance4 {get; set;}
```

```

property System.double ProfileDistance4 {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Distance

Remarks

[IGussetFeatureData::ProfileType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~ProfileType.md) must be set to swGussetProfilePolygon.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.md)  
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.md)
