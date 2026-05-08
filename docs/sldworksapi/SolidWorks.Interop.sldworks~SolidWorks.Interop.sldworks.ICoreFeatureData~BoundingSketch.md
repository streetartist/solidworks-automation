# BoundingSketch Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~BoundingSketch`

Gets or sets the bounding sketch for this core feature.
Gets or sets the bounding sketch for this core feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BoundingSketch As Feature
```

```

Dim instance As ICoreFeatureData
Dim value As Feature
 
instance.BoundingSketch = value
 
value = instance.BoundingSketch
```

```

Feature BoundingSketch {get; set;}
```

```

property Feature^ BoundingSketch {
   Feature^ get();
   void set (    Feature^ value);
}
```

#### Property Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

[Get Core Feature Data (VBA)](Get_Core_Feature_Example_VB.htm)  
[Get Core Feature Data (C#)](Get_Core_Feature_Example_CSharp.htm)  
[Get Core Feature Data (VB.NET)](Get_Core_Feature_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.md)  
[ICoreFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.md)
