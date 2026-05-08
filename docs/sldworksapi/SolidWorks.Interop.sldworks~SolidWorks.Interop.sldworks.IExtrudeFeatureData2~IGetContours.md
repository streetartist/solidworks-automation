# IGetContours Method (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IGetContours`

Gets the selected contours for this extrude feature.
Gets the selected contours for this extrude feature.

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

Dim instance As IExtrudeFeatureData2
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

- in-process, unmanaged C++: Pointer to an array of contours ([sketch contours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.md) and [sketch regions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.md)) of size count

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IExtrudeFeatureData2::GetContoursCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetContoursCount.md) before calling this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::ISetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetContours.md)  
[IExtrudeFeatureData2::Contours Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~Contours.md)
