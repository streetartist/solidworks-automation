# IGetBoundaries Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~IGetBoundaries`

Gets the boundaries for this OLE object.
Gets the boundaries for this OLE object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetBoundaries( _
   ByRef Boundary As System.Double _
) 
```

```

Dim instance As ISwOLEObject
Dim Boundary As System.Double
 
instance.IGetBoundaries(Boundary)
```

```

void IGetBoundaries( 
   out System.double Boundary
)
```

```

void IGetBoundaries( 
   [Out] System.double Boundary
) 
```

#### Parameters

*Boundary*
:   - in-process, unmanaged C++: Pointer to an array of doubles of these coordinates:

      - Drawings: sheet coordinates
      - Parts or assemblies: screen pixel coordinates
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwOLEObject Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md)  
[ISwOLEObject Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.md)  
[ISwOLEObject::ISetBoundaries Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~ISetBoundaries.md)  
[ISwOLEObject::Boundaries Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject~Boundaries.md)
