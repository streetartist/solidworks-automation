# GetContoursCount Method (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetContoursCount`

Gets the number of selected contours for this extrude feature.
Gets the number of selected contours for this extrude feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetContoursCount() As System.Integer
```

```

Dim instance As IExtrudeFeatureData2
Dim value As System.Integer
 
value = instance.GetContoursCount()
```

```

System.int GetContoursCount()
```

```

System.int GetContoursCount(); 
```

#### Return Value

Number of selected contours

Remarks

This method returns the total number of sketch contours and sketch regions used in the base sketch for this feature.

Call this method before calling [IExtrudeFeatureData2::IGetContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IGetContours.md).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

[Create Extrude Feature Using Sketch Contours (C#)](Create_Extrude_Feature_Using_Sketch_Contours_Example_CSharp.htm)  
[Create Extrude Feature Using Sketch Contours (VB.NET)](Create_Extrude_Feature_Using_Sketch_Contours_Example_VBNET.htm)  
[Create Extrude Feature Using Sketch Contours (VBA)](Create_Extrude_Feature_Using_Sketch_Contours_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::ISetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetContours.md)  
[IExtrudeFeatureData2::Contours Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~Contours.md)
