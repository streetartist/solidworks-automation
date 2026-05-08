# GetNextFaceArray Method (IMidSurface)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface~GetNextFaceArray`

Obsolete. Superseded by IMidSurface2::GetNextFaceArray.
Obsolete. Superseded by [IMidSurface2::GetNextFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextFaceArray.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNextFaceArray( _
   ByRef Thickness As System.Double _
) As System.Object
```

```

Dim instance As IMidSurface
Dim Thickness As System.Double
Dim value As System.Object
 
value = instance.GetNextFaceArray(Thickness)
```

```

System.object GetNextFaceArray( 
   out System.double Thickness
)
```

```

System.Object^ GetNextFaceArray( 
   [Out] System.double Thickness
) 
```

#### Parameters

*Thickness*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface.md)  
[IMidSurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface_members.md)
