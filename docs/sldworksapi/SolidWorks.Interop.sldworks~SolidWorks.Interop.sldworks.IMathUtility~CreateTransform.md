# CreateTransform Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateTransform`

Creates a new math transform.
Creates a new math transform.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateTransform( _
   ByVal ArrayDataIn As System.Object _
) As System.Object
```

```

Dim instance As IMathUtility
Dim ArrayDataIn As System.Object
Dim value As System.Object
 
value = instance.CreateTransform(ArrayDataIn)
```

```

System.object CreateTransform( 
   System.object ArrayDataIn
)
```

```

System.Object^ CreateTransform( 
   System.Object^ ArrayDataIn
) 
```

#### Parameters

*ArrayDataIn*
:   Sixteen (16) components of the transform (see **Remarks**)

#### Return Value

Newly created [math transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md) or nothing or null if the operation fails

Remarks

Transformation matrix data:

     |a b c . n |

      |d e f . o |

      |g h i . p |

      |j k l . m |

The SOLIDWORKS transformation matrix is stored as a homogeneous matrix of 16 elements, ordered as shown. The first 9 elements (a to i) are elements of a 3x3 rotational sub-matrix, the next 3 elements (j,k,l) define a translation vector, and the next 1 element (m) is a scaling factor. The last 3 elements (n,o,p) are unused in this context.

The 3x3 rotational sub-matrix represents 3 axis sets:

- row 1 for x-axis components of rotation
- row 2 for y-axis components of rotation
- row 3 for z-axis components of rotation

The 3 axes are constrained to be orthogonal and unified so that they produce a pure rotational transformation. Reflections can also be added to these axes by setting the components to negative. The rotation sub-matrix coupled with the lower-left translation vector and the lower-right corner scaling factor creates an affine transformation, which is a transformation that preserves lines and parallelism; i.e., maps parallel lines to parallel lines.

If the 3 axis sets of the 3x3 rotational sub-matrix are not orthogonal or unified, then they are automatically corrected according to the following rules:

- If any axis is 0, or any two axes are parallel, or all axes are coplanar, then an identity matrix replaces the rotational sub-matrix.
- All axes are corrected to be of unit length.
- The axes are built to be orthogonal to each other in the prioritized order of Z, X, Y (X is orthogonal to Z, Y is orthogonal to Z and X).

Example

[Align Assembly Component to Assembly Origin and Planes (VBA)](Align_Assembly_Component_to_Assembly_Origin_and_Planes_Example_VB.htm)  
[Use Presentation Transforms to Move Component (VBA)](Use_Presentation_Transforms_to_Move_Component_Example_VB.htm)  
[Display Temporary Body (C#)](Display_Temporary_Body_Example_CSharp.htm)  
[Display Temporary Body (VB.NET)](Display_Temporary_Body_Example_VBNET.htm)  
[Display Temporary Body (VBA)](Display_Temporary_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility.md)  
[IMathUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility_members.md)  
[IMathUtility::ICreateTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateTransform.md)  
[IMathUtility::ComposeTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ComposeTransform.md)  
[IMathUtility::CreateTransformRotateAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateTransformRotateAxis.md)  
[IMathUtility::ICreateTransformRotateAxis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateTransformRotateAxis.md)
