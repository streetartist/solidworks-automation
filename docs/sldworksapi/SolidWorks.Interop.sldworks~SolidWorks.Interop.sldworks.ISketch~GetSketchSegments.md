# GetSketchSegments Method (ISketch)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchSegments`

Gets the sketch segments in this sketch, which include line, arc, spline, parabola, and ellipse entities.
Gets the sketch segments in this sketch, which include line, arc, spline, parabola, and ellipse entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchSegments() As System.Object
```

```

Dim instance As ISketch
Dim value As System.Object
 
value = instance.GetSketchSegments()
```

```

System.object GetSketchSegments()
```

```

System.Object^ GetSketchSegments(); 
```

#### Return Value

Array of [sketch segments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md), which include line, arc, spline, parabola, and ellipse entities, in this sketch (see **Remarks**)

Remarks

If the sketch has errors, this method does not return all of the sketch segments.

Example

[Delete All Constraints in Selected Sketch (VBA)](Delete_All_Constraints_in_Selected_Sketch_Example_VB.htm)  
[Find Total Length of Sketch Segments in Sketch (VBA)](Find_Total_Length_of_Sketch_Segments_in_Sketch_Example_VB.htm)  
[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)  
[Get All Sketch Segments in Drawing Template (VBA)](Get_All_Sketch_Segments_in_Drawing_Template_Example_VB.htm)  
[Get Sketch Constraints (VBA)](Get_Sketch_Constraints_Example_VB.htm)  
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)  
[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)  
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)  
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)  
[Rotate and Copy 3D Sketch About Coordinates (C#)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_CSharp.htm)  
[Rotate and Copy 3D Sketch About Coordinates (VB.NET)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_VBNET.htm)  
[Rotate and Copy 3D Sketch About Coordinates (VBA)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::IEnumSketchSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchSegments.md)  
[ISketch::GetSketchTextSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchTextSegments.md)  
[ISketch::IEnumSketchTextSegments Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchTextSegments.md)
