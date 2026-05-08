# ClosestDistance Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClosestDistance`

Calculates the minimum distance between the specified geometric objects.
Calculates the minimum distance between the specified geometric objects.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ClosestDistance( _
   ByVal Object1 As System.Object, _
   ByVal Object2 As System.Object, _
   ByRef Point1 As System.Object, _
   ByRef Point2 As System.Object _
) As System.Double
```

```

Dim instance As IModelDoc2
Dim Object1 As System.Object
Dim Object2 As System.Object
Dim Point1 As System.Object
Dim Point2 As System.Object
Dim value As System.Double
 
value = instance.ClosestDistance(Object1, Object2, Point1, Point2)
```

```

System.double ClosestDistance( 
   System.object Object1,
   System.object Object2,
   out System.object Point1,
   out System.object Point2
)
```

```

System.double ClosestDistance( 
   System.Object^ Object1,
   System.Object^ Object2,
   [Out] System.Object^ Point1,
   [Out] System.Object^ Point2
) 
```

#### Parameters

*Object1*
:   Pointer to first object (see **Remarks**)

*Object2*
:   Pointer to second object (see **Remarks**)

*Point1*
:   Array of x, y, z coordinates for the point on Object1 that is nearest to Point2

*Point2*
:   Array of x, y, z coordinates for the point on Object2 that is nearest to Point1

#### Return Value

Distance in meters between Point1 and Point2; -1.0 if no solution

Remarks

Supported types of Object1 and Object2 include [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

- swSelFACES (face)
- swSelEDGES (edge)
- swSelVERTICES (vertex)
- swSelSKETCHSEGS (sketch segment)
- swSelDATUMPLANES (reference plane)
- swSelEXTSKETCHPOINTS (point on origin)
- swSelDATUMAXES (reference axis)
- swSelCOMPONENTS (component; multi-body part supported, but not multi-part sub-assembly)
- swSelREFCURVES (reference curve)
- swSelSOLIDBODIES (solid bodies only; surface bodies not supported)

This method has these restrictions for drawings:

- Cannot measure between a sketch entity and a model entity
- Measured sketch entities have to belong to the same sheet
- Model entity measurements are based on the model origin
- Measured object cannot be a temporary geometric entity

Example

[Calculate Closest Distance Between Faces (VBA)](Calculate_Closest_Distance_Between_Faces_Example_VB.htm)  
[Calculate Closest Distance Between Model Components (VBA)](Calculate_Closest_Distance_Between_Model_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
