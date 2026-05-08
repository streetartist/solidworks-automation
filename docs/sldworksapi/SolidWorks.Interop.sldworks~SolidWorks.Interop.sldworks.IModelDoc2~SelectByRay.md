# SelectByRay Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectByRay`

Obsolete. Superseded by IModelDocExtension::SelectByRay.
Obsolete. Superseded by [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SelectByRay( _
   ByVal DoubleInfoIn As System.Object, _
   ByVal TypeWanted As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim DoubleInfoIn As System.Object
Dim TypeWanted As System.Integer
Dim value As System.Boolean
 
value = instance.SelectByRay(DoubleInfoIn, TypeWanted)
```

```

System.bool SelectByRay( 
   System.object DoubleInfoIn,
   System.int TypeWanted
)
```

```

System.bool SelectByRay( 
   System.Object^ DoubleInfoIn,
   System.int TypeWanted
) 
```

#### Parameters

*DoubleInfoIn*
:   Array of 7 doubles: 3 for the start point of the ray, 3 for the direction of the ray, and 1 for the radius

*TypeWanted*
:   Type of objects to select as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

#### Return Value

True if a selection is made, false if not

Remarks

This method:

- Defines a cylindrical region of infinite length that begins at pointIn, runs parallel to VectorIn, and has a radius of RadiusIn. If you specified edge or vertex entities, then the first edge or vertex found within the selection cylinder is selected.
- Only selects entity objects, which include faces, edges, vertices, and so on. You cannot select sketch objects using this method.
- Does not support the selection of silhouette edges.

Only a single entity is selected within the distance radius regardless of multiple entities existing within that radius. For selecting face entities, RadiusIn is ignored and a cylinder of infinitely small radius is used.

Use model space view to determine the selection vector in a drawing.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetRayIntersectionsPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetRayIntersectionsPoints.md)  
[IModelDoc2::GetRayIntersectionsTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetRayIntersectionsTopology.md)  
[IModelDoc2::IGetRayIntersectionsPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetRayIntersectionsPoints.md)  
[IModelDoc2::IGetRayIntersectionsTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetRayIntersectionsTopology.md)  
[IModelDoc2::IMultiSelectByRay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IMultiSelectByRay.md)  
[IModelDoc2::IRayIntersections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IRayIntersections.md)  
[IModelDoc2::ISelectByRay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISelectByRay.md)  
[IModelDoc2::MultiSelectByRay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MultiSelectByRay.md)  
[IModelDoc2::RayIntersections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~RayIntersections.md)
