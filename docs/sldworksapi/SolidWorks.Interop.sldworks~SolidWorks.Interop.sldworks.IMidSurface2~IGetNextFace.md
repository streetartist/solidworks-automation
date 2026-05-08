# IGetNextFace Method (IMidSurface2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextFace`

Obsolete. Superseded by IMidSurface3::IGetNextFace.
Obsolete. Superseded by [IMidSurface3::IGetNextFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetNextFace.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetNextFace( _
   ByRef FromFace1Disp As Face2, _
   ByRef FromFace2Disp As Face2, _
   ByRef Thickness As System.Double _
) As Face2
```

```

Dim instance As IMidSurface2
Dim FromFace1Disp As Face2
Dim FromFace2Disp As Face2
Dim Thickness As System.Double
Dim value As Face2
 
value = instance.IGetNextFace(FromFace1Disp, FromFace2Disp, Thickness)
```

```

Face2 IGetNextFace( 
   out Face2 FromFace1Disp,
   out Face2 FromFace2Disp,
   out System.double Thickness
)
```

```

Face2^ IGetNextFace( 
   [Out] Face2^ FromFace1Disp,
   [Out] Face2^ FromFace2Disp,
   [Out] System.double Thickness
) 
```

#### Parameters

*FromFace1Disp*
:   [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) on the original part body used in generating the neutral face

*FromFace2Disp*
:   [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) on the original part body used in generating the neutral face

*Thickness*
:   Distance between the two parallel faces, FromFace1Disp and FromFace2Disp

#### Return Value

[Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) in this midsurface feature

Remarks

Call [IMidSurface2::IGetFirstFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstFace.md) before calling this method to get the first neutral face.

This method returns the next neutral face in this midsurface feature along with three other items.

- The first two return values are the two faces from the original part body that were used to generate this neutral midsurface face.
- The next return value is the thickness (in meters) between the two parallel faces from the original part body.
- The last return value is the neutral face in this midsurface feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.md)  
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.md)  
[IMidSurface2::GetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFirstFace.md)  
[IMidSurface2::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFaceCount.md)  
[IMidSurface2::GetNextFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextFace.md)
