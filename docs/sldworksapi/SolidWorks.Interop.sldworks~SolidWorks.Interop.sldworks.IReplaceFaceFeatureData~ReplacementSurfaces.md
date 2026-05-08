# ReplacementSurfaces Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ReplacementSurfaces`

Gets or sets the replacement surfaces for this feature.
Gets or sets the replacement surfaces for this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReplacementSurfaces As System.Object
```

```

Dim instance As IReplaceFaceFeatureData
Dim value As System.Object
 
instance.ReplacementSurfaces = value
 
value = instance.ReplacementSurfaces
```

```

System.object ReplacementSurfaces {get; set;}
```

```

property System.Object^ ReplacementSurfaces {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of replacement surfaces

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IReplaceFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData.md)  
[IReplaceFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData_members.md)  
[IReplaceFaceFeatureData::GetReplacementSurfacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~GetReplacementSurfacesCount.md)  
[IReplaceFaceFeatureData::IGetReplacementSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~IGetReplacementSurfaces.md)  
[IReplaceFaceFeatureData::ISetReplacementSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData~ISetReplacementSurfaces.md)
