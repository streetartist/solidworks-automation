# Select4 Method (ISketchSegment)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~Select4`

Selects this sketch segment and marks it.
Selects this sketch segment and marks it.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select4( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

```

Dim instance As ISketchSegment
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean
 
value = instance.Select4(Append, Data)
```

```

System.bool Select4( 
   System.bool Append,
   SelectData Data
)
```

```

System.bool Select4( 
   System.bool Append,
   SelectData^ Data
) 
```

#### Parameters

*Append*
:   True to append this selection to the selection list, false to replace the selection list with this selection

*Data*
:   [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object

#### Return Value

True if the sketch segment is selected, false if not

Example

[Get All Sketch Segments in Drawing Template (VBA)](Get_All_Sketch_Segments_in_Drawing_Template_Example_VB.htm)  
[Get Axis of Revolve Feature (VBA)](Get_Axis_of_Revolve_Feature_Example_VB.htm)  
[Insert Coordinate System at Center of Mass (VBA)](Insert_Coordinate_System_at_Center_of_Mass_Example_VB.htm)  
[Create Sketch Path (C#)](Create_Sketch_Path_Example_CSharp.htm)  
[Create Sketch Path (VB.NET)](Create_Sketch_Path_Example_VBNET.htm)  
[Create Sketch Path (VBA)](Create_Sketch_Path_Example_VB.htm)  
[Rotate and Copy 3D Sketch About Coordinates (C#)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_CSharp.htm)  
[Rotate and Copy 3D Sketch About Coordinates (VB.NET)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_VBNET.htm)  
[Rotate and Copy 3D Sketch About Coordinates (VBA)](Rotate_and_Copy_3D_Sketch_About_Coordinates_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)
