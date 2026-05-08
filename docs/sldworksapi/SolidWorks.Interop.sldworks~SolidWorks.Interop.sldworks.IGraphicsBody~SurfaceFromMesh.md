# SurfaceFromMesh Method (IGraphicsBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGraphicsBody~SurfaceFromMesh`

Creates a surface from the selected facets in this graphics body.
Creates a surface from the selected facets in this graphics body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SurfaceFromMesh( _
   ByVal SurfaceType As System.Integer, _
   ByVal FacetTolerance As System.Double, _
   ByVal ExtendSurfaceSize As System.Double, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

```

Dim instance As IGraphicsBody
Dim SurfaceType As System.Integer
Dim FacetTolerance As System.Double
Dim ExtendSurfaceSize As System.Double
Dim ErrorCode As System.Integer
Dim value As System.Object
 
value = instance.SurfaceFromMesh(SurfaceType, FacetTolerance, ExtendSurfaceSize, ErrorCode)
```

```

System.object SurfaceFromMesh( 
   System.int SurfaceType,
   System.double FacetTolerance,
   System.double ExtendSurfaceSize,
   out System.int ErrorCode
)
```

```

System.Object^ SurfaceFromMesh( 
   System.int SurfaceType,
   System.double FacetTolerance,
   System.double ExtendSurfaceSize,
   [Out] System.int ErrorCode
) 
```

#### Parameters

*SurfaceType*
:   Type of surface to create as defined by [swSurfaceTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSurfaceTypes_e.html) (see **Remarks**)

*FacetTolerance*
:   0.0 (High tolerance) <= Percent facet selection <= 100.0 (Low tolerance)

*ExtendSurfaceSize*
:   Extension in meters of the surface body to fit the selected facets and geometric shape

*ErrorCode*
:   0 if successful, -1 if not

#### Return Value

[IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

This method:

- is analogous to the **Insert menu > Mesh > Surface From Mesh** functionality in the user interface.
- creates a **Surface-From-Mesh***X* feature in the FeatureManager design tree.

Before calling this method, select as many facets in the graphics body as are needed to create the surface type.

SurfaceType can be one of only swSurfaceTypes\_e.:

- PLANE\_TYPE
- SPHERE\_TYPE
- CYLINDER\_TYPE
- CONE\_TYPE

For more information, see the **SOLIDWORKS user-interface help > Parts and Features > Graphics Mesh and Mesh BREP Bodies > Creating a Surface from Mesh Featur**e topic.

Example

See the [IBody2::ConvertToMeshBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ConvertToMeshBody.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGraphicsBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGraphicsBody.md)  
[IGraphicsBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGraphicsBody_members.md)
