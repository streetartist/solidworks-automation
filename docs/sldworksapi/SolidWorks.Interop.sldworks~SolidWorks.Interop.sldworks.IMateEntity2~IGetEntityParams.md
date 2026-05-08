# IGetEntityParams Method (IMateEntity2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~IGetEntityParams`

Gets the parameters of this mate entity.
Gets the parameters of this mate entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEntityParams( _
   ByVal NParamsSize As System.Integer _
) As System.Double
```

```

Dim instance As IMateEntity2
Dim NParamsSize As System.Integer
Dim value As System.Double
 
value = instance.IGetEntityParams(NParamsSize)
```

```

System.double IGetEntityParams( 
   System.int NParamsSize
)
```

```

System.double IGetEntityParams( 
   System.int NParamsSize
) 
```

#### Parameters

*NParamsSize*
:   Number of parameters for this mate entity

#### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles representing the parameters for this mate entity (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IMateEntity2::GetEntityParamsSize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~GetEntityParamsSize.md) to get the value for the size of the array.

The return value is the following array of doubles:

[ pointX, pointY, pointZ, vectorI, vectorJ, vectorK, radius1, radius2 ]

 where

- pointX is the X location of this mate entity in the assembly model space
- pointY is the Y location of this mate entity in the assembly model space
- pointZ is the Z location of this mate entity in the assembly model space
- vectorI is the i component of the assembly mate vector
- vectorJ is the j component of the assembly mate vector
- vectorK is the k component of the assembly mate vector
- radius1 is the value for the first radius
- radius2 is the value for the second radius

To define the mate entity, the following information is returned based on the mate type. All coordinate information is given in terms of the assembly coordinate system where the mate resides.

|  |  |
| --- | --- |
| **Mate Type** | **Returned** |
| swMatePoint | pointX, pointY, pointZ |
| swMateLine | pointX, pointY, pointZ, vectorI, vectorJ, vectorK where the point is a point on the line and the vector represents the line direction. |
| swMatePlane | pointX, pointY, pointZ, vectorI, vectorJ, vectorK where the point is a point on the plane and the vector represents the plane normal. |
| swMateCylinder | pointX, pointY, pointZ, vectorI, vectorJ, vectorK, radius1 where the point is a point on the cylinder axis and the vector represents the cylinder axis. |
| swMateCone | pointX, pointY, pointZ, vectorI, vectorJ, vectorK, radius1, radius2 where the point is a point on the cone axis and the vector represents the cone axis. |

To get the [IMateEntity2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2.md) interface, use [IMate2::MateEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MateEntity.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateEntity2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2.md)  
[IMateEntity2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2_members.md)  
[IMateEntity2::EntityParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~EntityParams.md)
