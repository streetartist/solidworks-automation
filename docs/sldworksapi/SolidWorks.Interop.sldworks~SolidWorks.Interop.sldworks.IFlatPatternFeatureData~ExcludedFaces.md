# ExcludedFaces Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ExcludedFaces`

Gets and sets the faces to exclude from this Flat-Pattern feature.
Gets and sets the faces to exclude from this Flat-Pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ExcludedFaces As System.Object
```

```

Dim instance As IFlatPatternFeatureData
Dim value As System.Object
 
instance.ExcludedFaces = value
 
value = instance.ExcludedFaces
```

```

System.object ExcludedFaces {get; set;}
```

```

property System.Object^ ExcludedFaces {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [IFace2s](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

To get the size of the array returned by this method, call [IFlatPatternFeatureData::IGetExcludedFacesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~IGetExcludedFacesCount.md).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

[Exclude Faces Before Flattening (VBA)](Exclude_Faces_Before_Flattening_Example_VB.htm)  
[Exclude Faces Before Flattening (VB.NET)](Exclude_Faces_Before_Flattening_Example_VBNET.htm)  
[Exclude Faces Before Flattening (C#)](Exclude_Faces_Before_Flattening_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.md)  
[IFlatPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.md)  
[IFlatPatternFeatureData::IGetExcludedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~IGetExcludedFaces.md)  
[IFlatPatternFeatureData::ISetExcludedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData~ISetExcludedFaces.md)
