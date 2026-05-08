# CavitySurfaces Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~CavitySurfaces`

Gets or sets the cavity surface bodies for this tooling split feature.
Gets or sets the cavity surface bodies for this tooling split feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CavitySurfaces As System.Object
```

```

Dim instance As IToolingSplitFeatureData
Dim value As System.Object
 
instance.CavitySurfaces = value
 
value = instance.CavitySurfaces
```

```

System.object CavitySurfaces {get; set;}
```

```

property System.Object^ CavitySurfaces {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of cavity surface [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [IToolingSplitFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.md)  
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.md)  
[IToolingSplitFeatureData::GetCavitySurfacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~GetCavitySurfacesCount.md)  
[IToolingSplitFeatureData::IGetCavitySurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~IGetCavitySurfaces.md)  
[IToolingSplitFeatureData::ISetCavitySurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~ISetCavitySurfaces.md)
