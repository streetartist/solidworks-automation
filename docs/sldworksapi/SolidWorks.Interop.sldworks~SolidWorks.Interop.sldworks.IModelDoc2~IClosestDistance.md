# IClosestDistance Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IClosestDistance`

Calculates the distance and closest points between two geometric objects.
Calculates the distance and closest points between two geometric objects.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IClosestDistance( _
   ByVal Object1 As System.Object, _
   ByVal Object2 As System.Object, _
   ByRef Point1 As System.Double, _
   ByRef Point2 As System.Double _
) As System.Double
```

```

Dim instance As IModelDoc2
Dim Object1 As System.Object
Dim Object2 As System.Object
Dim Point1 As System.Double
Dim Point2 As System.Double
Dim value As System.Double
 
value = instance.IClosestDistance(Object1, Object2, Point1, Point2)
```

```

System.double IClosestDistance( 
   System.object Object1,
   System.object Object2,
   out System.double Point1,
   out System.double Point2
)
```

```

System.double IClosestDistance( 
   System.Object^ Object1,
   System.Object^ Object2,
   [Out] System.double Point1,
   [Out] System.double Point2
) 
```

#### Parameters

*Object1*
:   Pointer to first object

*Object2*
:   Pointer to second object

*Point1*
:   Array of x, y, z coordinates for the first point

*Point2*
:   Array of x, y, z coordinates for the second point

#### Return Value

Minimum distance; -1.0 if no solution

Remarks

Supported input object types include:

- swSelFACES (face)
- swSelEDGES (edge)
- swSelVERTICES (vertex)
- swSelSKETCHSEGS (sketch segments)
- swSelDATUMPLANES (reference plane)
- swSelEXTSKETCHPOINTS (point on origin)
- swSelDATUMAXES  (reference axis)
- swSelCOMPONENTS (component)
- swSelREFCURVES (reference curves)

This method includes these restrictions for drawings:

- Cannot measure between a sketch entity and a model entity
- Measured sketch entities have to belong to the same sheet
- Model entity measurements are based on the model origin
- Measured object cannot be a temporary geometric entity

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
