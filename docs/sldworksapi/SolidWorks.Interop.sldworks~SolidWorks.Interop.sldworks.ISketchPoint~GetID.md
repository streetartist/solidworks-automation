# GetID Method (ISketchPoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~GetID`

Gets the sketch point ID for this sketch point.
Gets the sketch point ID for this sketch point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetID() As System.Object
```

```

Dim instance As ISketchPoint
Dim value As System.Object
 
value = instance.GetID()
```

```

System.object GetID()
```

```

System.Object^ GetID(); 
```

#### Return Value

Array with two longs or two integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) identifying this sketch point ID

Remarks

The ID of the sketch point:

- is an ordered pair (i1, i2). For sketch points, the combination of these two numbers is always unique within a specific sketch.
- cannot be assigned by applications or users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm).

Each point within a specific sketch has a unique ID. However, a point and other sketch objects can have the same ID. Likewise, in a second sketch, you may find a different sketch element with the same ID. Therefore, your application must keep track of:

- sketch element type (that is, point, line, arc, spline, and so on)
- owning sketch name
- sketch element ID to uniquely identify a sketched item

Example

[Get Sketch Points and Sketch Point IDs (VBA)](Get_Sketch_Points_and_Their_Persistent_IDs_Example_VB.htm)  
[Get x,y,z Locations of Points in Sketch (VBA)](Get_x,y,z_Locations_of_Points_in_Sketch_Example_VB.htm)  
[Get Persistent Identifiers and Types for Sketch Points (VB.NET)](Get_Persistent_Identifiers_and_Types_for_Sketch_Points_Example_VBNET.htm)  
[Get Persistent Identifiers and Types for Sketch Points (C#)](Get_Persistent_Identifiers_and_Types_for_Sketch_Points_Example_CSharp.htm)  
[Get Sketch Relations (VBA)](Get_Sketch_Relations_Example_VB.htm)  
[Get Sketch Relations (VB.NET)](Get_Sketch_Relations_Example_VBNET.htm)  
[Get Sketch Relations (C#)](Get_Sketch_Relations_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)  
[ISketchPoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.md)  
[ISketchPoint::IGetID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint~IGetID.md)
