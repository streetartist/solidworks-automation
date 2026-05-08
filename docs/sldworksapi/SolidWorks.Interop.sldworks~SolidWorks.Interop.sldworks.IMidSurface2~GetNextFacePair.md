# GetNextFacePair Method (IMidSurface2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextFacePair`

Obsolete. Superseded by IMidSurface3::GetNextFacePair.
Obsolete. Superseded by [IMidSurface3::GetNextFacePair](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNextFacePair.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNextFacePair( _
   ByRef Thickness As System.Double, _
   ByRef PartnerFaceDisp As System.Object _
) As System.Object
```

```

Dim instance As IMidSurface2
Dim Thickness As System.Double
Dim PartnerFaceDisp As System.Object
Dim value As System.Object
 
value = instance.GetNextFacePair(Thickness, PartnerFaceDisp)
```

```

System.object GetNextFacePair( 
   out System.double Thickness,
   out System.object PartnerFaceDisp
)
```

```

System.Object^ GetNextFacePair( 
   [Out] System.double Thickness,
   [Out] System.Object^ PartnerFaceDisp
) 
```

#### Parameters

*Thickness*
:   Distance between theses two parallel faces

*PartnerFaceDisp*
:   [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) on the original part body used in generating the neutral face

#### Return Value

[Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) on the original part body used in generating the neutral face

Remarks

The two faces returned are the two parallel faces from the original part body that were used to generate the neutral face in this midsurface feature.

Call [IMidSurface2::GetFirstFacePair](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFirstFacePair.md) to get the first pair of faces used in this midsurface feature.

This method is similar to [IMidSurface2::GetNextFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextFace.md), except this method does not return the neutral face.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.md)  
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.md)  
[IMidSurface2::IGetNextFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextFacePair.md)  
[IMidSurface2::GetFacePairCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFacePairCount.md)  
[IMidSurface2::IGetFirstFacePair Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstFacePair.md)
