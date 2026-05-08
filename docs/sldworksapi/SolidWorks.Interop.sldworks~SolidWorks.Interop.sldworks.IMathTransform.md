# IMathTransform Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform`

Provides a simplified interface for manipulating transformation matrix data.
Provides a simplified interface for manipulating transformation matrix data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IMathTransform 
```

```

Dim instance As IMathTransform
```

```

public interface IMathTransform 
```

```

public interface class IMathTransform 
```

Remarks

Transformation matrix data:

   |a b c . n |

    |d e f . o |

    |g h i . p |

    |j k l . m |

The SOLIDWORKS transformation matrix is stored as a homogeneous matrix of 16 elements, ordered as shown. The first 9 elements (a to i) are elements of a 3x3 rotational sub-matrix, the next 3 elements (j,k,l) define a translation vector, and the next 1 element (m) is a scaling factor. The last 3 elements (n,o,p) are unused in this context.

The 3x3 rotational sub-matrix represents 3 axis sets:

- row 1 for x-axis components of rotation
- row 2 for y-axis components of rotation
- row 3 for z-axis components of rotation

The 3 axes are constrained to be orthogonal and unified so that they produce a pure rotational transformation. Reflections can also be added to these axes by setting the components to negative. The rotation sub-matrix coupled with the lower-left translation vector and the lower-right corner scaling factor creates an affine transformation, which is a transformation that preserves lines and parallelism; i.e., maps parallel lines to parallel lines.

If the 3 axis sets of the 3x3 rotational sub-matrix are not orthogonal or unified, then they are automatically corrected according to the following rules:

- If any axis is 0, or any two axes are parallel, or all axes are coplanar, then an identity matrix replaces the rotational sub-matrix.
- All axes are corrected to be of unit length.
- The axes are built to be orthogonal to each other in the prioritized order of Z, X, Y (X is orthogonal to Z, Y is orthogonal to Z and X).

Example

[Get Coordinate System Transform (VBA)](Get_Coordinate_System_Transform_Example_VB.htm)  
[Calculate Transformations in Part (C#)](Calculate_Transformations_in_Part_Example_CSharp.htm)  
[Calculate Transformations in Part (VB.NET)](Calculate_Transformations_in_Part_Example_VBNET.htm)  
[Calculate Transformations in Part (VBA)](Calculate_Transformations_in_Part_Example_VB.htm)  
[Get Patterned Cosmetic Thread Annotations Data (C#)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_CSharp.htm)  
[Get Patterned Cosmetic Thread Annotations Data (VB.NET)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VBNET.htm)  
[Get Patterned Cosmetic Thread Annotations Data (VBA)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IMathPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)  
[IMathUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility.md)  
[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)  
[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md)
