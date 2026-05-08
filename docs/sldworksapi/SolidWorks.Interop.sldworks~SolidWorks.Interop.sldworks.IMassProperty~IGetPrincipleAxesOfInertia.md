# IGetPrincipleAxesOfInertia Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetPrincipleAxesOfInertia`

Gets the principal axes of inertia for this model.
Gets the principal axes of inertia for this model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetPrincipleAxesOfInertia( _
   ByVal Axis As System.Integer _
) As System.Double
```

```

Dim instance As IMassProperty
Dim Axis As System.Integer
Dim value As System.Double
 
value = instance.IGetPrincipleAxesOfInertia(Axis)
```

```

System.double IGetPrincipleAxesOfInertia( 
   System.int Axis
)
```

```

System.double IGetPrincipleAxesOfInertia( 
   System.int Axis
) 
```

#### Parameters

*Axis*
:   - 0 = X axis
    - 1 = Y axis
    - 2 = Z axis

#### Return Value

- in-process, unmanaged C++: Pointer to an array of size 3 (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

This method returns:

- a vector that represents the requested axis.
- metric units unless explicitly specified otherwise.

The return value is a 0-based array of doubles:

[ lx, ly, lz ]

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)  
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.md)  
[IMassProperty::GetMomentOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~GetMomentOfInertia.md)  
[IMassProperty::IGetMomentOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetMomentOfInertia.md)  
[IMassProperty::IGetPrincipleMomentsOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetPrincipleMomentsOfInertia.md)  
[IMassProperty::PrincipleAxesOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleAxesOfInertia.md)  
[IMassProperty::PrincipleMomentsOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleMomentsOfInertia.md)
