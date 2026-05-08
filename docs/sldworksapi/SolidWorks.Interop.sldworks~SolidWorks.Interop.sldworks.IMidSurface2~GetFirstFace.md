# GetFirstFace Method (IMidSurface2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFirstFace`

Obsolete. Superseded by IMidSurface3::GetFirstFace.
Obsolete. Superseded by [IMidSurface3::GetFirstFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstFace.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstFace( _
   ByRef FromFace1Disp As System.Object, _
   ByRef FromFace2Disp As System.Object, _
   ByRef Thickness As System.Double _
) As System.Object
```

```

Dim instance As IMidSurface2
Dim FromFace1Disp As System.Object
Dim FromFace2Disp As System.Object
Dim Thickness As System.Double
Dim value As System.Object
 
value = instance.GetFirstFace(FromFace1Disp, FromFace2Disp, Thickness)
```

```

System.object GetFirstFace( 
   out System.object FromFace1Disp,
   out System.object FromFace2Disp,
   out System.double Thickness
)
```

```

System.Object^ GetFirstFace( 
   [Out] System.Object^ FromFace1Disp,
   [Out] System.Object^ FromFace2Disp,
   [Out] System.double Thickness
) 
```

#### Parameters

*FromFace1Disp*
:   [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) on the original part body used in generating the neutral face

*FromFace2Disp*
:   Parallel [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to FromFace1Disp on the original part body used in generating the neutral face

*Thickness*
:   Distance between the two parallel faces, FromFace1Disp and FromFace2Disp

#### Return Value

First [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) in this midsurface feature

Remarks

- The first two return values are the two faces from the original part body that were used to generate this midsurface face.
- The next return value is the thickness (in meters) between the two parallel faces from the original part body.
- The last return value is the first face in this midsurface feature.

Use [IMidSurface2::GetNextFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextFace.md) to get the next neutral face in this midsurface feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.md)  
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.md)  
[IMidSurface2::IGetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstFace.md)  
[IMidSurface2::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFaceCount.md)  
[IMidSurface2::IGetNextFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextFace.md)
