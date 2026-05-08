# MultiplyTransform Method (IMathPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~MultiplyTransform`

Multiplies a math point with a math transform; the point is rotated, scaled, and then translated.
Multiplies a math point with a math transform; the point is rotated, scaled, and then translated.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MultiplyTransform( _
   ByVal TransformObjIn As System.Object _
) As System.Object
```

```

Dim instance As IMathPoint
Dim TransformObjIn As System.Object
Dim value As System.Object
 
value = instance.MultiplyTransform(TransformObjIn)
```

```

System.object MultiplyTransform( 
   System.object TransformObjIn
)
```

```

System.Object^ MultiplyTransform( 
   System.Object^ TransformObjIn
) 
```

#### Parameters

*TransformObjIn*
:   Math transform by which to multiply this math point

#### Return Value

Newly created translated [math point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) or null if the operation fails

Example

[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)  
[Evaluate Curves Defined in Sketch Space (VBA)](Evaluate_Curves_Defined_in_Sketch_Space_Example_VB.htm)  
[Get Names of Sketch Segments (VBA)](Get_Names_of_Sketch_Segments_Example_VB.htm)  
[Transform Coordinates from Sketch to Model Space (VBA)](Transform_Coordinates_from_Sketch_to_Model_Space_Example_VB.htm)  
[Transform Sketch to Model (VBA)](Transform_Sketch_to_Model_Example_VB.htm)  
[Zoom to Region (VBA)](Zoom_to_Region_Example_VB.htm)  
[Get Points of Repeating Elements in Table-driven Pattern (C#)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_CSharp.htm)  
[Get Points of Repeating Elements in Table-driven Pattern (VB.NET)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VBNET.htm)  
[Get Points of Repeating Elements in Table-driven Pattern (VBA)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)  
[IMathPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.md)  
[IMathPoint::IMultiplyTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint~IMultiplyTransform.md)
