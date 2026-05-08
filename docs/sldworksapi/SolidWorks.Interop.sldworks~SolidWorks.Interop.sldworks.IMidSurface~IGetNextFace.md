# IGetNextFace Method (IMidSurface)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface~IGetNextFace`

Obsolete. Superseded by IMidSurface2::IGetNextFace.
Obsolete. Superseded by [IMidSurface2::IGetNextFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextFace.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetNextFace( _
   ByRef FromFace1Disp As Face, _
   ByRef FromFace2Disp As Face, _
   ByRef Thickness As System.Double _
) As Face
```

```

Dim instance As IMidSurface
Dim FromFace1Disp As Face
Dim FromFace2Disp As Face
Dim Thickness As System.Double
Dim value As Face
 
value = instance.IGetNextFace(FromFace1Disp, FromFace2Disp, Thickness)
```

```

Face IGetNextFace( 
   out Face FromFace1Disp,
   out Face FromFace2Disp,
   out System.double Thickness
)
```

```

Face^ IGetNextFace( 
   [Out] Face^ FromFace1Disp,
   [Out] Face^ FromFace2Disp,
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
