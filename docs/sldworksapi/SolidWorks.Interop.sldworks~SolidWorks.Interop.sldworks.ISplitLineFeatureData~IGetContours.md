# IGetContours Method (ISplitLineFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~IGetContours`

Gets the selected contours for this split line feature.
Gets the selected contours for this split line feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetContours( _
   ByVal Count As System.Integer _
) As System.Object
```

```

Dim instance As ISplitLineFeatureData
Dim Count As System.Integer
Dim value As System.Object
 
value = instance.IGetContours(Count)
```

```

System.object IGetContours( 
   System.int Count
)
```

```

System.Object^ IGetContours( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of selected contours

#### Return Value

- in-process, unmanaged C++: Pointer to an array of contours of these types:
- - [Sketch contour](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.md)
  - [Sketch region](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ISplitLineFeatureData::GetContoursCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetContoursCount.md) before calling this method to determine the size of the array for this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.md)  
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.md)  
[ISplitLineFeatureData::ISetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetContours.md)  
[ISplitLineFeatureData::Contours Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~Contours.md)
