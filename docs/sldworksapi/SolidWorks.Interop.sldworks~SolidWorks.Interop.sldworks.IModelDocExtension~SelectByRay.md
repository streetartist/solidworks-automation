# SelectByRay Method (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay`

Selects the first entity of the specified type that is intersected by a ray that starts at the specified point and runs parallel to the specified direction vector within the specified radius.
Selects the first entity of the specified type that is intersected by a ray that starts at the specified point and runs parallel to the specified direction vector within the specified radius.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SelectByRay( _
   ByVal WorldX As System.Double, _
   ByVal WorldY As System.Double, _
   ByVal WorldZ As System.Double, _
   ByVal RayVecX As System.Double, _
   ByVal RayVecY As System.Double, _
   ByVal RayVecZ As System.Double, _
   ByVal RayRadius As System.Double, _
   ByVal TypeWanted As System.Integer, _
   ByVal Append As System.Boolean, _
   ByVal Mark As System.Integer, _
   ByVal Option As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim WorldX As System.Double
Dim WorldY As System.Double
Dim WorldZ As System.Double
Dim RayVecX As System.Double
Dim RayVecY As System.Double
Dim RayVecZ As System.Double
Dim RayRadius As System.Double
Dim TypeWanted As System.Integer
Dim Append As System.Boolean
Dim Mark As System.Integer
Dim Option As System.Integer
Dim value As System.Boolean
 
value = instance.SelectByRay(WorldX, WorldY, WorldZ, RayVecX, RayVecY, RayVecZ, RayRadius, TypeWanted, Append, Mark, Option)
```

```

System.bool SelectByRay( 
   System.double WorldX,
   System.double WorldY,
   System.double WorldZ,
   System.double RayVecX,
   System.double RayVecY,
   System.double RayVecZ,
   System.double RayRadius,
   System.int TypeWanted,
   System.bool Append,
   System.int Mark,
   System.int Option
)
```

```

System.bool SelectByRay( 
   System.double WorldX,
   System.double WorldY,
   System.double WorldZ,
   System.double RayVecX,
   System.double RayVecY,
   System.double RayVecZ,
   System.double RayRadius,
   System.int TypeWanted,
   System.bool Append,
   System.int Mark,
   System.int Option
) 
```

#### Parameters

*WorldX*
:   x coordinate of ray start point

*WorldY*
:   y coordinate of ray start point

*WorldZ*
:   z coordinate of ray start point

*RayVecX*
:   x coordinate of ray direction vector

*RayVecY*
:   y coordinate of ray direction vector

*RayVecZ*
:   z coordinate of ray direction vector

*RayRadius*
:   Radius <= 2.9 m

*TypeWanted*
:   Type of entities to select as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

*Append*
:   | If... | And if entity is... | Then... |
    | --- | --- | --- |
    | True | Not already selected | Entity is appended to the current selection list |
    |  | Already selected | Entity is removed from the current selection list |
    | False | Not already selected | Current selection is cleared and then the entity is put on the list |
    |  | Already selected | Current selection list remains the same |

*Mark*
:   Value to use as a mark; this value is used by other functions that require ordered selection

*Option*
:   Selection option as defined in [swSelectOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectOption_e.html) (see **Remarks**)

#### Return Value

True if the entity is selected, false if not

Remarks

This method:

- Defines a cylindrical region of infinite length that starts at the specified point and runs parallel to the specified direction vector within the specified radius.
- Only selects these entities: faces, edges, and vertices.
- Does not support the selection of sketch entities, axes, center marks, center lines, section lines, etc.

Only a single entity is selected within the radius regardless if multiple entities existing within that radius. If selecting faces, then the RayRadius parameter is ignored and a cylinder of an infinitely small radius is used.

Use model space view to determine the selection vector in a drawing.

For the Option parameter, specify swSelectOption\_e.swSelectOptionDefault to indicate that the Shift key is not used during selection or swSelectOption\_e.swSelectOptionExtensive to indicate that the Shift key is used during selection.

**NOTES:**

- This method is recorded when [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) relies on the selection coordinates and prone to failure if the model view is altered.
- The difference between this method and the now obsolete [IModelDoc2::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectByRay.md) method is that if you call IModelDocExtension::SelectByRay in a macro or application to select an entity by an intersecting ray and then rerun that macro or application, the original entity is successfully selected regardless of the viewing transform.

Example

[Select Face Using Intersecting Ray (C#)](Select_Face_Using_Intersecting_Ray_Example_CSharp.htm)  
[Select Face Using Intersecting Ray (VB.NET)](Select_Face_Using_Intersecting_Ray_Example_VBNET.htm)  
[Select Face Using Intersecting Ray (VBA)](Select_Face_Using_Intersecting_Ray_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDoc2::GetRayIntersectionsPoints Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetRayIntersectionsPoints.md)  
[IModelDoc2::GetRayIntersectionsTopology Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetRayIntersectionsTopology.md)  
[IModelDoc2::MultiSelectByRay Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MultiSelectByRay.md)  
[IModelDoc2::RayIntersections Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~RayIntersections.md)
