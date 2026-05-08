# ArrayData Property (IMathPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~ArrayData`

Gets or sets the array of x,y,z coordinates that describe this math point.
Gets or sets the array of x,y,z coordinates that describe this math point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ArrayData As System.Object
```

```

Dim instance As IMathPoint
Dim value As System.Object
 
instance.ArrayData = value
 
value = instance.ArrayData
```

```

System.object ArrayData {get; set;}
```

```

property System.Object^ ArrayData {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of 3 doubles representing the x,y,z coordinates of the math point

Example

[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)  
[Get Names of Sketch Segments (VBA)](Get_Names_of_Sketch_Segments_Example_VB.htm)  
[Get Reference Point Data (VBA)](Get_Reference_Point_Data_Example_VB.htm)  
[Insert Reference Points (VBA)](Insert_Reference_Points_Example_VB.htm)  
[Transform Sketch to Model (VBA)](Transform_Sketch_to_Model_Example_VB.htm)  
[Get Points of Repeating Elements in Table-driven Pattern (C#)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_CSharp.htm)  
[Get Points of Repeating Elements in Table-driven Pattern (VB.NET)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VBNET.htm)  
[Get Points of Repeating Elements in Table-driven Pattern (VBA)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VB.htm)  
[Get Coordinates of the Plane's Bounding Box (C#)](Get_Coordinates_of_the_Plane's_Bounding_Box_Example_CSharp.htm)  
[Get Coordinates of the Plane's Bounding Box (VB.NET)](Get_Coordinates_of_the_Plane's_Bounding_Box_Example_VBNET.htm)  
[Get Coordinates of the Plane's Bounding Box (VBA)](Get_Coordinates_of_the_Plane's_Bounding_Box_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)  
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.md)  
[IMathPoint::IArrayData Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~IArrayData.md)
