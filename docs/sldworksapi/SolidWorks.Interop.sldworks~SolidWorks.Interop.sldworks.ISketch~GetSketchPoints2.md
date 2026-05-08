# GetSketchPoints2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPoints2`

Gets the sketch points in this sketch.
Gets the sketch points in this sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchPoints2() As System.Object
```

```

Dim instance As ISketch
Dim value As System.Object
 
value = instance.GetSketchPoints2()
```

```

System.object GetSketchPoints2()
```

```

System.Object^ GetSketchPoints2(); 
```

#### Return Value

Array of [sketch points](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md) in this sketch

Remarks

The difference between this method and the now obsolete method [ISketch::GetSketchPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchPoints.md) is that this method does not return sketch points intended for internal SOLIDWORKS use only.

Example

[Delete All Constraints in Selected Sketch (VBA)](Delete_All_Constraints_in_Selected_Sketch_Example_VB.htm)  
[Get Sketch Points and Their Persistent IDs (VBA)](Get_Sketch_Points_and_Their_Persistent_IDs_Example_VB.htm)  
[Get Sketch Points (VBA)](Get_Sketch_Points_Example_VB.htm)  
[Get x,y,z Locations of Points in Sketch (VBA)](Get_x,y,z_Locations_of_Points_in_Sketch_Example_VB.htm)  
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)  
[Transform Sketch to Model (VBA)](Transform_Sketch_to_Model_Example_VB.htm)  
[Autodimension All Sketches (C#)](Autodimension_All_Sketches_Example_CSharp.htm)  
[Autodimension All Sketches (VB.NET)](Autodimension_All_Sketches_Example_VBNET.htm)  
[Autodimension All Sketches (VBA)](Autodimension_All_Sketches_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::IGetSketchPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSketchPoints2.md)  
[ISketch::IEnumSketchPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchPoints.md)  
[ISketch::GetUserPointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPointsCount.md)  
[ISketch::GetUserPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetUserPoints2.md)  
[ISketch::IGetUserPoints2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetUserPoints2.md)  
[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)  
[ISketch::MergePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~MergePoints.md)
