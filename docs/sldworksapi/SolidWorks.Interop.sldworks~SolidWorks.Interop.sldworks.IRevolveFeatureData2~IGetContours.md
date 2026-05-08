# IGetContours Method (IRevolveFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IGetContours`

Gets the selected contours for this revolve feature.
Gets the selected contours for this revolve feature.

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

Dim instance As IRevolveFeatureData2
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

- in-process, unmanaged C++: Pointer to an array of selected contours ([sketch contours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.md) and [sketch regions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.md)) of size Count

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IRevolveFeatureData2::GetContoursCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetContoursCount.md) before calling this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.md)  
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.md)  
[IRevolveFeatureData2::ISetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ISetContours.md)  
[IRevolveFeatureData2::Contours Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~Contours.md)
