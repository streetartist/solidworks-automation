# Select4 Method (ISketchPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~Select4`

Selects the sketch point and marks it.
Selects the sketch point and marks it.

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

Dim instance As ISketchPoint
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
:   True to append this selection to the selection list, false to replace the selection  
    list with this selection

*Data*
:   [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object

#### Return Value

True if the sketch point is selected, false if not

Example

[Create Plane Thru 3 Points In-context (VBA)](Create_Plane_Thru_3_Points_In-context_Example_VB.htm)  
[Get Reference Point Data (VBA)](Get_Reference_Point_Data_Example_VB.htm)  
[Get Sketch Points in Wizard Hole (VBA)](Get_Sketch_Points_in_Wizard_Hole_Example_VB.htm)  
[Insert Coordinate System at Center of Mass (VBA)](Insert_Coordinate_System_at_Center_of_Mass_Example_VB.htm)  
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)  
[Get Sketch Point's Selection Mark (C#)](Get_Sketch_Points_Selection_Mark_Example_CSharp.htm)  
[Get Sketch Point's Selection Mark (VB.NET)](Get_Sketch_Points_Selection_Mark_Example_VBNET.htm)  
[Get Sketch Point's Selection Mark (VBA)](Get_Sketch_Points_Selection_Mark_Example_VB.htm)  
[Get Sketch Relations (VBA)](Get_Sketch_Relations_Example_VB.htm)  
[Get Sketch Relations (VB.NET)](Get_Sketch_Relations_Example_VBNET.htm)  
[Get Sketch Relations (C#)](Get_Sketch_Relations_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)  
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.md)  
[ISketchPoint::DeSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~DeSelect.md)
