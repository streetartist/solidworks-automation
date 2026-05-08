# GetNextFace Method (IMidSurface)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface~GetNextFace`

Obsolete. Superseded by IMidSurface2::GetNextFace.
Obsolete. Superseded by [IMidSurface2::GetNextFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextFace.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNextFace( _
   ByRef FromFace1Disp As System.Object, _
   ByRef FromFace2Disp As System.Object, _
   ByRef Thickness As System.Double _
) As System.Object
```

```

Dim instance As IMidSurface
Dim FromFace1Disp As System.Object
Dim FromFace2Disp As System.Object
Dim Thickness As System.Double
Dim value As System.Object
 
value = instance.GetNextFace(FromFace1Disp, FromFace2Disp, Thickness)
```

```

System.object GetNextFace( 
   out System.object FromFace1Disp,
   out System.object FromFace2Disp,
   out System.double Thickness
)
```

```

System.Object^ GetNextFace( 
   [Out] System.Object^ FromFace1Disp,
   [Out] System.Object^ FromFace2Disp,
   [Out] System.double Thickness
) 
```

#### Parameters

*FromFace1Disp*

*FromFace2Disp*

*Thickness*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface.md)  
[IMidSurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface_members.md)
