# EvaluateAtPoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~EvaluateAtPoint`

Evaluates a surface at the specified XYZ point.
Evaluates a surface at the specified XYZ point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EvaluateAtPoint( _
   ByVal PositionX As System.Double, _
   ByVal PositionY As System.Double, _
   ByVal PositionZ As System.Double _
) As System.Object
```

```

Dim instance As ISurface
Dim PositionX As System.Double
Dim PositionY As System.Double
Dim PositionZ As System.Double
Dim value As System.Object
 
value = instance.EvaluateAtPoint(PositionX, PositionY, PositionZ)
```

```

System.object EvaluateAtPoint( 
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ
)
```

```

System.Object^ EvaluateAtPoint( 
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ
) 
```

#### Parameters

*PositionX*
:   X position

*PositionY*
:   Y position

*PositionZ*
:   Z position

#### Return Value

Array of doubles (see **Remarks**)

Remarks

This method calculates the normal, the principal directions, and the principal curvatures, of the surface at the specified point.

Use [IFace2::FaceInSurfaceSense](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~FaceInSurfaceSense.md) to check the directions of the face normal and surface normal. IFace2::FaceInSurfaceSense returns true when the face normal and surface normal point in opposite directions, and false when they point in the same direction.

The return value is the following array of eleven doubles:

[surfNorm[i, j, k], principalDir1[i, j, k], principalDir2[I, j, k], principalCurvature1, principalCurvature2 ]

where:

surfNorm[i, j, k] = normalized vector describing the surface normal

principalDir1[i, j, k] = normalized vector describing the first principal direction

principalDir2[i, j, k] = normalized vector describing the second principal direction

principalCurvature1 = first principal curvature

principalCurvature2 = second principal curvature

Principal Curvature 1 is the minimum normal curvature at the point (largest radius). Principal Curvature 2 is the maximum normal curvature at the point.

The tangent direction producing Principal Curvature 1 is called the first principal direction, and the tangent direction producing Principal Curvature 2 is called the second principal direction.

It is a property of differentiable surfaces that principalDir1 and principalDir2 are orthogonal.

A positive curvature by convention implies a centre of curvature on the side pointed away from by the surface normal (convex).

See "Faux and Pratt Computational Geometry for Design and Manufacture" for more information.

Example

[Determine Type of Face (VBA)](Determine_Type_of_Face_Example_VB.htm)  
[Evaluate Points on Surface (VBA)](Evaluate_Points_on_Surface_Example_VB.htm)  
[Select Tangent Faces (VBA)](Select_Tangent_Faces_Example_VB.htm)  
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)  
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)  
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)  
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.md)  
[ISurface::IEvaluateAtPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IEvaluateAtPoint.md)  
[ISurface::IEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IEvaluate.md)  
[ISurface::Evaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Evaluate.md)  
[ISurface::IParameterization Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IParameterization.md)  
[ISurface::IReverseEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IReverseEvaluate.md)  
[ISurface::Parameterization Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Parameterization.md)  
[ISurface::ReverseEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ReverseEvaluate.md)
