# GetNextFacePair Method (IMidSurface)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface~GetNextFacePair`

Obsolete. Superseded by IMidSurface2::GetNextFacePair.
Obsolete. Superseded by [IMidSurface2::GetNextFacePair](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextFacePair.md).

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

Dim instance As IMidSurface
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

*PartnerFaceDisp*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface.md)  
[IMidSurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface_members.md)
