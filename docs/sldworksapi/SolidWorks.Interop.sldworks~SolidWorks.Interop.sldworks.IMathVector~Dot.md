# Dot Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~Dot`

Gets the value of the dot product between two math vectors.
Gets the value of the dot product between two math vectors.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Dot( _
   ByVal VectorObjIn As System.Object _
) As System.Double
```

```

Dim instance As IMathVector
Dim VectorObjIn As System.Object
Dim value As System.Double
 
value = instance.Dot(VectorObjIn)
```

```

System.double Dot( 
   System.object VectorObjIn
)
```

```

System.double Dot( 
   System.Object^ VectorObjIn
) 
```

#### Parameters

*VectorObjIn*
:   [Math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) to use to determine the dot value

#### Return Value

Value of the dot product

Example

[Get Angle of Hole Not Normal to Face (VBA)](Get_Angle_of_Hole_Not_Normal_to_a_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathVector Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)  
[IMathVector Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.md)  
[IMathVector::IDot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector~IDot.md)
