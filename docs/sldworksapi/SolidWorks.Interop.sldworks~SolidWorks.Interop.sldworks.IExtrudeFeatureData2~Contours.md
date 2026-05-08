# Contours Property (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~Contours`

Gets and sets the selected contours in this extrude feature.
Gets and sets the selected contours in this extrude feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Contours As System.Object
```

```

Dim instance As IExtrudeFeatureData2
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

Array of contours (see **Remarks**)

Remarks

The array passed to or returned by this property can contain both [ISketchContour](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour.md) and [ISketchRegion](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion.md) objects. This method returns an emtpy array if sketch contours or sketch regions do not exist.

**NOTE:** An extrude feature has one, and only one, sketch. If the sketch does not contain sketch contours or sketch regions, then an empty array is returned. To get the sketch of an extrude feature that does not contain sketch contours or sketch regions, you can traverse the FeatureManager design tree to get the parent sketch of the extrude feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

[Determine If Sketch Contour or Sketch Region (VBA)](Determine_if_Sketch_Contour_or_Sketch_Region_Example_VB.htm)  
[Create Extrude Feature Using Sketch Contours (C#)](Create_Extrude_Feature_Using_Sketch_Contours_Example_CSharp.htm)  
[Create Extrude Feature Using Sketch Contours (VB.NET)](Create_Extrude_Feature_Using_Sketch_Contours_Example_VBNET.htm)  
[Create Extrude Feature Using Sketch Contours (VBA)](Create_Extrude_Feature_Using_Sketch_Contours_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::GetContoursCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetContoursCount.md)  
[IExtrudeFeatureData2::IGetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IGetContours.md)  
[IExtrudeFeatureData2::ISetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetContours.md)
