# AutoSelect Property (ISurfaceCutFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~AutoSelect`

Gets or sets whether to automatically select all or only specific bodies for the surface-cut feature to affect in a multibody part.
Gets or sets whether to automatically select all or only specific bodies for the surface-cut feature to affect in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AutoSelect As System.Boolean
```

```

Dim instance As ISurfaceCutFeatureData
Dim value As System.Boolean
 
instance.AutoSelect = value
 
value = instance.AutoSelect
```

```

System.bool AutoSelect {get; set;}
```

```

property System.bool AutoSelect {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to automatically select all bodies, false to select specific bodies for [ISurfaceCutFeatureData::FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~FeatureScopeBodies.md) or [ISurfaceCutFeatureData::ISetFeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~ISetFeatureScopeBodies.md)

Remarks

To access this interface, you must declare it as SurfCutFeatureData or ISurfCutFeatureData.

This property is only available when [ISurfaceCutFeatureData::FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~FeatureScope.md) is true.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

[Insert Surface-cut Feature (C#)](Insert_Surface-cut_Feature_Example_CSharp.htm)  
[Insert Surface-cut Feature (VB.NET)](Insert_Surface-cut_Feature_Example_VBNET.htm)  
[Insert Surface-cut Feature (VBA)](Insert_Surface-cut_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.md)  
[ISurfaceCutFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData_members.md)  
[ISurfaceCutFeatureData::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~GetFeatureScopeBodiesCount.md)  
[ISurfaceCutFeatureData::IGetFeatureScopeBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~IGetFeatureScopeBodies.md)
