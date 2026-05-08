# Contours Property (ISplitLineFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~Contours`

Gets or sets the contours for this split line feature.
Gets or sets the contours for this split line feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Contours As System.Object
```

```

Dim instance As ISplitLineFeatureData
Dim value As System.Object
 
instance.Contours = value
 
value = instance.Contours
```

```

System.object Contours {get; set;}
```

```

property System.Object^ Contours {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of contours of one of the following types:

- [Sketch contour](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.md)
- [Sketch region](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.md)  
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.md)  
[ISplitLineFeatureData::GetContoursCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetContoursCount.md)  
[ISplitLineFeatureData::IGetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~IGetContours.md)  
[ISplitLineFeatureData::ISetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetContours.md)
